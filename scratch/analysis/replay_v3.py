import json,glob,os,re,sys,ast
B,OUT=sys.argv[1],sys.argv[2]

def heredoc_bodies(cmd):
    out=[m.group(2) for m in re.finditer(r"<<\s*'?([A-Za-z_]\w*)'?\s*\n(.*?)\n\1(?:\s|$)", cmd, re.S)]
    return out or [cmd]

def pairs_from_py(src):
    """Ordered (old,new) replace pairs, resolving variables and string concatenation."""
    try: tree=ast.parse(src)
    except Exception: return []
    env={}
    def ev(n):
        if isinstance(n,ast.Constant): return n.value if isinstance(n.value,str) else None
        if isinstance(n,ast.Name): return env.get(n.id)
        if isinstance(n,ast.BinOp) and isinstance(n.op,ast.Add):
            l,r=ev(n.left),ev(n.right)
            return (l+r) if (isinstance(l,str) and isinstance(r,str)) else None
        if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and n.func.attr=='join':
            base=ev(n.func.value)
            if isinstance(base,str) and n.args and isinstance(n.args[0],(ast.List,ast.Tuple)):
                parts=[ev(x) for x in n.args[0].elts]
                if all(isinstance(x,str) for x in parts): return base.join(parts)
        return None
    lists={}; pairs=[]
    def pairlist(node):
        items=[]
        if isinstance(node,ast.Dict):
            for k,v in zip(node.keys,node.values):
                a,b=ev(k),ev(v)
                if isinstance(a,str) and isinstance(b,str): items.append((a,b,-1))
            return items
        for el in node.elts:
            if isinstance(el,(ast.Tuple,ast.List)) and len(el.elts)==2:
                a,b=ev(el.elts[0]),ev(el.elts[1])
                if isinstance(a,str) and isinstance(b,str): items.append((a,b,-1))
        return items
    def scan(body):
        for node in body:
            if isinstance(node,ast.Assign):
                if isinstance(node.value,(ast.List,ast.Tuple,ast.Dict)):
                    it=pairlist(node.value)
                    if it:
                        for t in node.targets:
                            if isinstance(t,ast.Name): lists[t.id]=it
                        continue
                v=ev(node.value)
                if isinstance(v,str):
                    for t in node.targets:
                        if isinstance(t,ast.Name): env[t.id]=v
            if isinstance(node,ast.For):
                it=node.iter
                if isinstance(it,ast.Call) and isinstance(it.func,ast.Attribute) and it.func.attr=='items' and isinstance(it.func.value,ast.Name) and it.func.value.id in lists:
                    pairs.extend(lists[it.func.value.id]); continue
                if isinstance(node.iter,ast.Name) and node.iter.id in lists:
                    pairs.extend(lists[node.iter.id]); continue
                if isinstance(node.iter,(ast.List,ast.Tuple,ast.Dict)):
                    it=pairlist(node.iter)
                    if it: pairs.extend(it); continue
            for sub in ast.walk(node):
                if isinstance(sub,ast.Call) and isinstance(sub.func,ast.Attribute) and sub.func.attr=='replace' and len(sub.args)>=2:
                    a,b=ev(sub.args[0]),ev(sub.args[1])
                    cnt=-1
                    if len(sub.args)>=3 and isinstance(sub.args[2],ast.Constant) and isinstance(sub.args[2].value,int): cnt=sub.args[2].value
                    if isinstance(a,str) and isinstance(b,str): pairs.append((a,b,cnt))
            if isinstance(node,(ast.If,ast.For,ast.While,ast.With,ast.Try)):
                scan(node.body)
    scan(tree.body)
    seen=set(); res=[]
    for a,b,c in pairs:
        if (a,b) in seen or not a: continue
        seen.add((a,b)); res.append((a,b,c))
    return res

for p in sorted(glob.glob(B+'/transcripts/*.json')):
    run=os.path.basename(p).replace('.json','')
    d=json.load(open(p)); data=d['contexts'][0]['conversation']['data']
    seq=[c for el in data for c in (el.get('contents') or []) if isinstance(c,dict) and c.get('type') in ('ToolUse','ToolResult')]
    steps=[]
    for i,c in enumerate(seq):
        if c.get('type')!='ToolUse': continue
        r=seq[i+1] if i+1<len(seq) and seq[i+1].get('type')=='ToolResult' else None
        out=''
        if r:
            for x in (r.get('content') or []):
                if isinstance(x,dict) and x.get('data'): out+=str(x.get('data'))
        steps.append((c.get('name'), c.get('parameters') or {}, out))
    mds=[prm['path'] for nm,prm,_ in steps if nm!='bash' and prm.get('command')=='create' and str(prm.get('path','')).endswith('.md')]
    if not mds:
        # Some runs generate the deliverable from a script instead of writing it
        # directly. Report and continue; handle those separately.
        print('%-22s NO DIRECT .md CREATE - deliverable is script-generated, handle separately' % run)
        continue
    target=mds[0]; base=os.path.basename(target)
    doc=None; applied=0; failed=0; aborted=0; log=[]
    for nm,prm,out in steps:
        if nm!='bash':
            if prm.get('path')!=target: continue
            c=prm.get('command')
            if 'rror' in out[:200] and c!='create':
                aborted+=1; log.append('edit-tool call errored, not applied'); continue
            if c=='create': doc=prm.get('file_text',''); applied+=1
            elif c=='str_replace' and doc is not None:
                o,n=prm.get('old_str',''),prm.get('new_str','')
                if o and o in doc: doc=doc.replace(o,n,1); applied+=1
                else: failed+=1; log.append('edit-tool unmatched: '+repr(o[:70]))
            elif c=='insert' and doc is not None:
                L=doc.split('\n'); L.insert(int(prm.get('insert_line',0)), prm.get('new_str','')); doc='\n'.join(L); applied+=1
            continue
        cmd=prm.get('command','')
        if doc is None or base not in cmd: continue
        if not re.search(r"write\(|\.replace\(|sed -i|>>",cmd): continue
        # only an assert (or a syntax error) in the writing block means nothing was written;
        # a traceback from a LATER command in the same bash call does not undo the write
        bodies=[b for b in heredoc_bodies(cmd) if base in b and 'write(' in b]
        guarded=any('assert' in b for b in bodies)
        if (guarded and 'AssertionError' in out) or 'SyntaxError' in out:
            aborted+=1; log.append('block raised -> no write: '+out.strip().split("\n")[-1][:70]); continue
        for body in heredoc_bodies(cmd):
            if base not in body: continue
            if 'write(' not in body: continue
            for a,b,c in pairs_from_py(body):
                if a and a in doc: doc=(doc.replace(a,b,c) if c>0 else doc.replace(a,b)); applied+=1
                else: failed+=1; log.append('py unmatched: '+repr(a[:70]))
        for m in re.finditer(r"sed -i\s+'s/((?:[^/\\]|\\.)+)/((?:[^/\\]|\\.)*)/g?'", cmd):
            a,b=m.group(1),m.group(2)
            if a in doc: doc=doc.replace(a,b); applied+=1
            else: failed+=1; log.append('sed unmatched: '+repr(a[:70]))
        for m in re.finditer(r">>\s*\S*"+re.escape(base)+r"\s*<<\s*'?(\w+)'?\n(.*?)\n\1", cmd, re.S):
            doc=doc+m.group(2)+'\n'; applied+=1
    open(OUT+'/'+run+'.md','w').write(doc)
    print('%-22s %-44s %4d lines %5d words | edits %3d unmatched %3d aborted %2d' % (run,base,doc.count('\n')+1,len(doc.split()),applied,failed,aborted))
    for l in log[:5]: print('      !',l)

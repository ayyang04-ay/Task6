import json,glob,os,re,sys
B,OUT=sys.argv[1],sys.argv[2]
def results(p):
    d=json.load(open(p)); data=d['contexts'][0]['conversation']['data']
    seq=[c for el in data for c in (el.get('contents') or []) if isinstance(c,dict) and c.get('type') in ('ToolUse','ToolResult')]
    out=[]
    for i,c in enumerate(seq):
        if c.get('type')=='ToolUse':
            r=seq[i+1] if i+1<len(seq) and seq[i+1].get('type')=='ToolResult' else None
            txt=''
            if r:
                for x in (r.get('content') or []):
                    if isinstance(x,dict) and x.get('type')=='Stdout': txt+=x.get('data') or ''
            out.append((c.get('name'), c.get('parameters') or {}, txt))
    return out
for p in sorted(glob.glob(B+'/transcripts/*.json')):
    run=os.path.basename(p).replace('.json','')
    doc=open(OUT+'/'+run+'.md').read(); lines=doc.split('\n')
    md=None
    prs=results(p)
    for nm,prm,_ in prs:
        if nm!='bash' and prm.get('command')=='create' and str(prm.get('path','')).endswith('.md'): md=os.path.basename(prm['path']); break
    # word count check (last one)
    wc=None
    for nm,prm,txt in prs:
        if nm=='bash' and md in prm.get('command','') and re.search(r'wc -w',prm['command']):
            m=re.search(r'(\d+)\s+\S*'+re.escape(md),txt)
            if m: wc=int(m.group(1))
    mine=len(doc.split())
    # line-number observations: grep -n output "NNN:text"
    ok=0;bad=0;ex=[]
    for nm,prm,txt in prs:
        if nm!='bash': continue
        cmd=prm.get('command','')
        if md not in cmd or not re.search(r'grep -n|sed -n|nl ',cmd): continue
        for m in re.finditer(r'^(\d+)[:\-](.*)$',txt,re.M):
            ln=int(m.group(1)); t=m.group(2)
            if ln<1 or ln>len(lines): bad+=1; ex.append(('range',ln,t[:50])); continue
            if lines[ln-1].strip()==t.strip(): ok+=1
            else:
                # may be a mid-edit observation; check the text exists somewhere
                if t.strip() and t.strip() in doc: ok+=1
                else: bad+=1; ex.append((ln,lines[ln-1][:45],t[:45]))
    wcs = ('wc -w %d vs mine %d  %s'%(wc,mine,'MATCH' if wc==mine else 'DIFF %+d'%(mine-wc))) if wc else 'no wc -w'
    print('%-22s %4d lines | line-obs ok %3d bad %3d | %s' % (run,len(lines),ok,bad,wcs))
    for e in ex[:3]: print('      !',e)

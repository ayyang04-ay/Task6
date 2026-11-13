"""Recover a deliverable whose text lives in a generator script rather than an .md file.

Replays edits to the script, then walks its AST and emits every string constant in
source order. This is the memo's text, not its rendered Markdown: section order is
preserved but the renderer's formatting is not reproduced. Adequate for screening
and quoting; not for line numbers.
"""
import json, ast, sys, re

parsed, script_hint, out = sys.argv[1], sys.argv[2], sys.argv[3]
j = json.load(open(parsed))
src = None; applied = 0
for nm, prm in j['calls']:
    if nm != 'bash' and prm.get('command') == 'create' and script_hint in str(prm.get('path', '')):
        src = prm.get('file_text') or ''; applied += 1
    elif nm != 'bash' and prm.get('command') == 'str_replace' and script_hint in str(prm.get('path', '')) and src is not None:
        o, n = prm.get('old_str', ''), prm.get('new_str', '')
        if o and o in src: src = src.replace(o, n, 1); applied += 1
if src is None:
    print('no create call matching', script_hint); sys.exit(1)

def render(node):
    """Literal text of a Constant or an f-string, with interpolations as {...}."""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.JoinedStr):
        out = []
        for part in node.values:
            if isinstance(part, ast.Constant) and isinstance(part.value, str): out.append(part.value)
            else: out.append('{...}')
        return ''.join(out)
    return None

tree = ast.parse(src)
seen = set(); chunks = []
for node in ast.walk(tree):
    if isinstance(node, (ast.Constant, ast.JoinedStr)):
        v = render(node)
        if v is None: continue
        if len(v) < 25: continue                       # skip identifiers, format fragments
        if re.fullmatch(r'[\w\s./%{}:,\-\[\]()]*', v) and len(v) < 40: continue
        key = (node.lineno, v[:40])
        if key in seen: continue
        seen.add(key); chunks.append((node.lineno, v))
chunks.sort()
text = '\n\n'.join(c for _, c in chunks)
open(out, 'w').write(text)
print('%s: edits applied %d | %d string constants | %d chars, %d words'
      % (parsed.split('attempt_')[1][:13], applied, len(chunks), len(text), len(text.split())))

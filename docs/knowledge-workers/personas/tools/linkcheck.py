import os, re, sys, unicodedata
sys.stdout.reconfigure(encoding='utf-8')
root = sys.argv[1]
def slug(h):
    h = h.strip().lower()
    out = []
    for ch in h:
        if ch.isalnum() or ch in ' -_':
            out.append(ch)
        elif unicodedata.category(ch).startswith('L') or unicodedata.category(ch).startswith('N'):
            out.append(ch)
    return ''.join(out).replace(' ', '-')
def anchors(path):
    s = set()
    with open(path, encoding='utf-8') as f:
        in_code = False
        for line in f:
            if line.startswith('```'): in_code = not in_code; continue
            if in_code: continue
            m = re.match(r'^(#+)\s+(.*)', line)
            if m: s.add(slug(m.group(2)))
    return s
bad = 0; total = 0
for dp, dn, fn in os.walk(root):
    for f in fn:
        if not f.endswith('.md'): continue
        p = os.path.join(dp, f)
        txt = open(p, encoding='utf-8').read()
        txt = re.sub(r'```.*?```', '', txt, flags=re.S)
        for m in re.finditer(r'\]\(([^)\s]+)\)', txt):
            link = m.group(1)
            if link.startswith('http'): continue
            total += 1
            path, _, anc = link.partition('#')
            target = os.path.normpath(os.path.join(dp, path)) if path else p
            if not os.path.exists(target):
                print(f'MISSING FILE  {os.path.relpath(p, root)} -> {link}'); bad += 1; continue
            if anc and target.endswith('.md') and anc not in anchors(target):
                print(f'MISSING ANCHOR {os.path.relpath(p, root)} -> {link}'); bad += 1
print(f'checked {total} relative links, {bad} problems')

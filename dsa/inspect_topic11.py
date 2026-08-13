import re, sys

sys.stdout.reconfigure(encoding='utf-8')

v4_trie = r"F:\dsa\bookfinal - Copy\v4\bookfinal\Topic11_Trie.html"
with open(v4_trie, "r", encoding="utf-8") as f:
    html = f.read()

pages_raw = re.split(r'<!-- PAGE \d+:', html)[1:]
print(f"Original Topic11_Trie has {len(pages_raw)} pages.")

for i, p_str in enumerate(pages_raw, 1):
    comment_title = p_str[:p_str.find('-->')].strip()
    ph_end = p_str.find('</div>\n</div>')
    if ph_end == -1: ph_end = p_str.find('</div></div>')
    body = p_str[ph_end+12:] if ph_end != -1 else p_str
    body = re.sub(r'</div>\s*</div>\s*$', '', body).strip()
    print(f"Page {i:2d}: [{comment_title}] -> {len(body)} chars")

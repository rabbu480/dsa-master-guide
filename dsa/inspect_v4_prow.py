import re

v4_file = r"F:\dsa\bookfinal - Copy\v4\bookfinal\Topic11_Trie.html"
with open(v4_file, "r", encoding="utf-8", errors="ignore") as f:
    t = f.read()

# Find first prow block
m = re.search(r'<div class=["\']prow["\'][\s\S]*?</div>\s*</div>\s*</div>', t)
if m:
    print("Original prow layout in v4 Topic 11:")
    print("="*60)
    print(m.group(0)[:1200])

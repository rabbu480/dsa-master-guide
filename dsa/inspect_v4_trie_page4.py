import re

v4_file = r"F:\dsa\bookfinal - Copy\v4\bookfinal\Topic11_Trie.html"
with open(v4_file, "r", encoding="utf-8", errors="ignore") as f:
    html = f.read()

# Let's inspect Page 4 (Replace Words & Map Sum) in v4
pos = html.find("PREFIX REPLACEMENT")
if pos != -1:
    print("Found PREFIX REPLACEMENT in v4:")
    print("="*60)
    print(html[pos-100:pos+1500])

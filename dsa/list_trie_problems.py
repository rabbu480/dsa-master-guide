import re

path = r"F:\dsa\bookfinal\Topic11_Trie.html"
with open(path, "r", encoding="utf-8", errors="ignore") as f:
    t = f.read()

# Find all problem titles / LC references
matches = re.findall(r'(LC\s*\d+|[A-Z0-9\s—\-\(\)]+LC\s*\d+)', t)
print("LC Problems found in Topic11_Trie.html:")
for m in matches:
    print(" -", m.strip())

# Also search for ptitle or psub or bh
matches2 = re.findall(r'class=["\']p(?:title|sub|tag2|tag)["\'][^>]*>(.*?)</div>', t)
print("\nProblem headers found:")
for m in matches2:
    print(" -", m.strip())

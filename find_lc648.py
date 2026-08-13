import re

path = r"F:\dsa\bookfinal\Topic11_Trie.html"
with open(path, "r", encoding="utf-8") as f:
    t = f.read()

# Find LC 648 or Replace Words
pos = t.find("Replace Words")
if pos != -1:
    print("Found 'Replace Words' in Topic11_Trie.html around position:", pos)
    print("="*60)
    print(t[max(0, pos-200):pos+800])
else:
    print("'Replace Words' not found in Topic11_Trie.html")

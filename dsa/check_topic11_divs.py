import re

with open(r"F:\dsa\bookfinal\Topic11_Trie.html", "r", encoding="utf-8") as f:
    t = f.read()

divs = re.findall(r'<div class=["\']page["\']', t)
print(f"Total <div class='page'> in Topic11 HTML: {len(divs)}")

# Find where each page div starts
page_starts = [m.start() for m in re.finditer(r'<div class=["\']page["\']', t)]
for i, start in enumerate(page_starts, 1):
    snippet = t[start:start+120].replace('\n', ' ')
    print(f"Div {i}: {snippet}")

import re

with open('F:/dsa/bookfinal/Topic02_Arrays_Strings_Hashing.html', 'r', encoding='utf-8') as f:
    text = f.read()

# count occurrence of <div class="page">
page_matches = list(re.finditer(r'<div class="page">', text))
print("Page count in Topic02 HTML:", len(page_matches))

# print page titles and page numbers
for i, m in enumerate(page_matches):
    start = m.start()
    end = page_matches[i+1].start() if i+1 < len(page_matches) else len(text)
    chunk = text[start:end]
    pn_match = re.search(r'PAGE \d+ OF \d+', chunk)
    h1_match = re.search(r'<h1>(.*?)</h1>', chunk)
    pn_str = pn_match.group(0) if pn_match else "No PN"
    h1_str = h1_match.group(1) if h1_match else "No H1"
    print(f"Page {i+1}: {pn_str} | H1: {h1_str} | Chunk length: {len(chunk)} chars")

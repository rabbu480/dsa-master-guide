import re

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'r', encoding='utf-8') as f:
    text = f.read()

pages = list(re.finditer(r'<div class="page">', text))
print("Topic03 current page count:", len(pages))

for i, m in enumerate(pages):
    start = m.start()
    end = pages[i+1].start() if i+1 < len(pages) else len(text)
    chunk = text[start:end]
    h_list = re.findall(r'<div class="(?:ph|bh|ptitle|section-header|ptag2)[^"]*">(.*?)</div>', chunk)
    clean_h = [re.sub(r'<[^>]+>', '', h).strip().encode('ascii', 'ignore').decode('ascii') for h in h_list]
    print(f"Page {i+1} ({len(chunk)} chars):", clean_h[:3])

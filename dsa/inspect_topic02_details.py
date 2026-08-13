import re

with open('F:/dsa/bookfinal/Topic02_Arrays_Strings_Hashing.html', 'r', encoding='utf-8') as f:
    text = f.read()

page_matches = list(re.finditer(r'<div class="page">', text))

for i, m in enumerate(page_matches):
    start = m.start()
    end = page_matches[i+1].start() if i+1 < len(page_matches) else len(text)
    chunk = text[start:end]
    print(f"=== PAGE {i+1} ===")
    headers = re.findall(r'<div class="(?:bh|ptitle|section-header|ptag2)[^"]*">(.*?)</div>', chunk)
    for h in headers[:5]:
        clean = re.sub(r'<[^>]+>', '', h).strip()
        print("  -", clean.encode('ascii', 'ignore').decode('ascii'))

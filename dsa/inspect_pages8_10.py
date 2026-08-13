import re

with open('F:/dsa/bookfinal/Topic02_Arrays_Strings_Hashing.html', 'r', encoding='utf-8') as f:
    text = f.read()

page_matches = list(re.finditer(r'<div class="page">', text))

for i in [7, 8, 9]: # pages 8, 9, 10
    start = page_matches[i].start()
    end = page_matches[i+1].start() if i+1 < len(page_matches) else len(text)
    chunk = text[start:end]
    print(f"=== PAGE {i+1} ===")
    print(chunk[:1000].encode('ascii', 'ignore').decode('ascii'))

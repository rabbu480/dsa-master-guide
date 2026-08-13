import re

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'rb') as f:
    raw = f.read()

text = raw.decode('utf-8').replace('\r\n', '\n').replace('\r', '\n')

# Count page divs
pages = list(re.finditer(r'<div class="page">', text))
print(f"Total page divs: {len(pages)}")

# Show what comes just before each page div (30 chars)
for i, m in enumerate(pages):
    snippet = text[max(0, m.start()-80):m.start()+30]
    print(f"\n--- Page {i+1} boundary ---")
    print(repr(snippet))

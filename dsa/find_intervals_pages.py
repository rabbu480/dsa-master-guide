import re

with open('F:/dsa/bookfinal/Topic16_Intervals.html', 'r', encoding='utf-8') as f:
    content = f.read()

matches = re.findall(r'<div class="page"[^>]*>', content)
print('Total page divs in Topic16_Intervals.html:', len(matches))
for i, m in enumerate(matches, 1):
    print(f"Page {i:2d}: {m}")

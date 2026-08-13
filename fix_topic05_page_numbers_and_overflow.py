import re

filepath = 'F:/dsa/bookfinal/Topic05_BinarySearch.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove orphaned <span class="page-num">...</span> tags
content = re.sub(r'\s*<span class="page-num">.*?</span>', '', content)

# 2. Fix page number counter in .ph headers
pages = content.split('<div class="page"')
new_pages = [pages[0]]

for idx, page in enumerate(pages[1:], 1):
    # Update PAGE X OF 10 in .ph
    page_fixed = re.sub(
        r'<div class="pn">PAGE \d+ OF \d+</div>',
        f'<div class="pn">PAGE {idx} OF 10</div>',
        page
    )
    new_pages.append(page_fixed)

content = '<div class="page"'.join(new_pages)

# 3. Reduce margin-top/bottom on section-box to prevent Page 1 overflow
content = content.replace('margin-top:8px', 'margin-top:4px')
content = content.replace('margin-bottom:12px', 'margin-bottom:6px')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed Topic 05 page numbers and margins successfully!")

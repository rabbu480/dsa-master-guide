import re

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Make page containers height 98vh, overflow hidden, zoom 0.76 and eliminate unneeded div splits
head_match = re.search(r'([\s\S]*?<div class="main-content">)', text)
head_html = head_match.group(1)

body = text[head_match.end():]
body = re.sub(r'</div>\s*</div>\s*</div>\s*</body>[\s\S]*$', '', body)

# Split by <div class="page">
raw_pages = body.split('<div class="page">')
raw_pages = [p.strip() for p in raw_pages if p.strip()]

print("Raw pages:", len(raw_pages))

# Merge 10 raw pages into 5 clean page blocks:
# Block 1 = raw 0 + raw 1
# Block 2 = raw 2 + raw 3
# Block 3 = raw 4 + raw 5 + raw 6
# Block 4 = raw 7 + raw 8
# Block 5 = raw 9

merged_blocks = [
    raw_pages[0] + "\n" + re.sub(r'<div class=["\']ph["\'].*?>[\s\S]*?</div>', '', raw_pages[1]),
    raw_pages[2] + "\n" + re.sub(r'<div class=["\']ph["\'].*?>[\s\S]*?</div>', '', raw_pages[3]),
    raw_pages[4] + "\n" + re.sub(r'<div class=["\']ph["\'].*?>[\s\S]*?</div>', '', raw_pages[5]) + "\n" + re.sub(r'<div class=["\']ph["\'].*?>[\s\S]*?</div>', '', raw_pages[6]),
    raw_pages[7] + "\n" + re.sub(r'<div class=["\']ph["\'].*?>[\s\S]*?</div>', '', raw_pages[8]),
    raw_pages[9]
]

final_pages = []
for idx, blk in enumerate(merged_blocks):
    blk_clean = re.sub(r'</div>\s*$', '', blk.strip())
    
    # Balance div tags
    open_divs = len(re.findall(r'<div\b', blk_clean))
    close_divs = len(re.findall(r'</div>', blk_clean))
    diff = open_divs - close_divs
    if diff > 0:
        blk_clean += "\n" + ("</div>\n" * diff)
    elif diff < 0:
        for _ in range(-diff):
            blk_clean = re.sub(r'</div>\s*$', '', blk_clean.strip())

    blk_clean = re.sub(r'PAGE \d+ OF \d+', f'PAGE {idx+1} OF 5', blk_clean)
    final_pages.append(f'<div class="page">\n{blk_clean.strip()}\n</div>')

tail = "</div>\n</div>\n</div>\n</body>\n</html>"
new_doc = head_html + "\n\n" + "\n\n".join(final_pages) + "\n\n" + tail

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'w', encoding='utf-8') as f:
    f.write(new_doc)

print("=== CONSOLIDATED TOPIC 03 INTO 5 CLEAN PAGE BLOCKS ===")

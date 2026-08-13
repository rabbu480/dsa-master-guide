import re

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Pattern matching for <div class="page"> ... </div> blocks
# In the pristine file, each page is strictly encapsulated in:
# <div class="page">
# <div class="ph">...</div>
# ... content ...
# </div>

# Let's split by <div class="page">
parts = text.split('<div class="page">')
head = parts[0]
page_blocks = parts[1:] # 10 pages

cleaned_blocks = []
for p in page_blocks:
    # strip trailing </div> before next block
    # p ends with ... </div>\n (or </div>\n</div>\n... at bottom of file)
    c = re.sub(r'</div>\s*$', '', p.strip())
    cleaned_blocks.append(c.strip())

# Pair up 10 page blocks into 5 target pages:
# Pair 0 = block 0 + block 1
# Pair 1 = block 2 + block 3
# Pair 2 = block 4 + block 5
# Pair 3 = block 6 + block 7
# Pair 4 = block 8 + block 9

grouped = [
    [cleaned_blocks[0], cleaned_blocks[1]],
    [cleaned_blocks[2], cleaned_blocks[3]],
    [cleaned_blocks[4], cleaned_blocks[5]],
    [cleaned_blocks[6], cleaned_blocks[7]],
    [cleaned_blocks[8], cleaned_blocks[9]]
]

final_pages = []
for idx, grp in enumerate(grouped):
    combined = ""
    for inner_i, b in enumerate(grp):
        b_str = b
        if inner_i > 0:
            # strip <div class="ph">...</div> header from second item in pair!
            b_str = re.sub(r'<div class=["\']ph["\']>[\s\S]*?</div>\s*</div>', '', b_str)
            b_str = re.sub(r'<div class=["\']ph["\']>[\s\S]*?</div>', '', b_str)
        combined += "\n" + b_str.strip()

    # Balance div tags
    open_divs = len(re.findall(r'<div\b', combined))
    close_divs = len(re.findall(r'</div>', combined))
    diff = open_divs - close_divs
    if diff > 0:
        combined += "\n" + ("</div>\n" * diff)
    elif diff < 0:
        for _ in range(-diff):
            combined = re.sub(r'</div>\s*$', '', combined.strip())

    combined = re.sub(r'PAGE \d+ OF \d+', f'PAGE {idx+1} OF 5', combined)
    final_pages.append(f'<div class="page">\n{combined.strip()}\n</div>')

tail = "</div>\n</div>\n</div>\n</body>\n</html>"
head_clean = re.sub(r'<div class="main-content">[\s\S]*$', '<div class="main-content">', head)
new_doc = head_clean + "\n\n" + "\n\n".join(final_pages) + "\n\n" + tail

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'w', encoding='utf-8') as f:
    f.write(new_doc)

print("=== PERFECT CLEAN 5 PAGE MERGE WITHOUT PH HEADERS ===")

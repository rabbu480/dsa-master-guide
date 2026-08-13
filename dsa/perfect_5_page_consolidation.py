import re

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract head and body
head_match = re.search(r'([\s\S]*?<div class="main-content">)', text)
head_html = head_match.group(1)

body = text[head_match.end():]
body = re.sub(r'</div>\s*</div>\s*</div>\s*</body>[\s\S]*$', '', body)

# Split strictly by <div class="page">
parts = body.split('<div class="page">')

pages_content = []
for p in parts:
    p_str = p.strip()
    if not p_str:
        continue
    # Strip any trailing unclosed </div> from the page content
    p_str = re.sub(r'</div>\s*$', '', p_str)
    pages_content.append(p_str)

print("Original page content blocks count:", len(pages_content))

# Merge 10 page content blocks into 5 target pages:
# Target 1 = block 0 + block 1
# Target 2 = block 2 + block 3
# Target 3 = block 4 + block 5
# Target 4 = block 6 + block 7
# Target 5 = block 8 + block 9

grouped = [
    [pages_content[0], pages_content[1]],
    [pages_content[2], pages_content[3]],
    [pages_content[4], pages_content[5]],
    [pages_content[6], pages_content[7]],
    [pages_content[8], pages_content[9]]
]

final_page_blocks = []
for idx, grp in enumerate(grouped):
    combined = ""
    for inner_idx, block in enumerate(grp):
        b_clean = block.strip()
        if inner_idx > 0:
            # strip ph header from second item in group
            b_clean = re.sub(r'<div class=["\']ph["\'].*?>[\s\S]*?</div>', '', b_clean)
        combined += "\n" + b_clean.strip()

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
    final_page_blocks.append(f'<div class="page">\n{combined.strip()}\n</div>')

tail = "</div>\n</div>\n</div>\n</body>\n</html>"
new_doc = head_html + "\n\n" + "\n\n".join(final_page_blocks) + "\n\n" + tail

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'w', encoding='utf-8') as f:
    f.write(new_doc)

print("=== PERFECT 5 PAGE CONSOLIDATION FOR TOPIC 03 COMPLETE ===")

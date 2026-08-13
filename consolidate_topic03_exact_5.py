import re

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract head and body cleanly
head_match = re.search(r'([\s\S]*?<div class="main-content">)', text)
head_html = head_match.group(1)

body = text[head_match.end():]
body = re.sub(r'</div>\s*</div>\s*</div>\s*</body>[\s\S]*$', '', body)

# Split by <div class="page">
raw_pages = body.split('<div class="page">')
raw_pages = [p.strip() for p in raw_pages if p.strip()]

print("Pristine file raw page blocks:", len(raw_pages))

# Pair raw pages into 5 target A4 pages:
# Target 1 = raw 0 + raw 1
# Target 2 = raw 2 + raw 3
# Target 3 = raw 4 + raw 5
# Target 4 = raw 6 + raw 7
# Target 5 = raw 8 + raw 9

grouped = [
    [raw_pages[0], raw_pages[1]],
    [raw_pages[2], raw_pages[3]],
    [raw_pages[4], raw_pages[5]],
    [raw_pages[6], raw_pages[7]],
    [raw_pages[8], raw_pages[9]]
]

final_pages = []
for idx, grp in enumerate(grouped):
    combined = ""
    for inner_idx, p in enumerate(grp):
        # Clean trailing </div> from p
        p_clean = re.sub(r'</div>\s*$', '', p.strip())
        if inner_idx > 0:
            # strip ph header from second item in pair
            p_clean = re.sub(r'<div class=["\']ph["\'].*?>[\s\S]*?</div>', '', p_clean)
        combined += "\n" + p_clean.strip()

    # Balance div tags inside the combined page
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
new_doc = head_html + "\n\n" + "\n\n".join(final_pages) + "\n\n" + tail

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'w', encoding='utf-8') as f:
    f.write(new_doc)

print("=== CONSOLIDATED TOPIC 03 INTO EXACTLY 5 PAGES ===")

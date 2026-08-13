import os
import glob
import re

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace <div class="page"> tags to ensure exactly 5 top-level page divs
# Let's inspect ph headers inside Topic03
parts = text.split('<div class="ph">')
head_html = parts[0]
sections = parts[1:]

print("Number of ph sections:", len(sections))

# Build 5 distinct page blocks
# Page 1: section 0 (Discovery & Real World Story)
# Page 2: section 1 (Side-by-Side Templates)
# Page 3: section 2 + section 3 (Palindrome, Two Sum II, 3Sum)
# Page 4: section 4 + section 5 (Container Water, Trapping Water)
# Page 5: section 6 (Decision Tree & Dry Run)

merged_sections = [
    [sections[0]],
    [sections[1]],
    [sections[2]],
    [sections[3], sections[4]],
    [sections[5]]
]

pages = []
for idx, sec_grp in enumerate(merged_sections):
    combined = ""
    for inner_i, sec in enumerate(sec_grp):
        sec_str = f'<div class="ph">{sec}'
        if inner_i > 0:
            sec_clean = re.sub(r'<div class=["\']ph["\'].*?>[\s\S]*?</div>', '', sec_str)
            combined += "\n" + sec_clean
        else:
            combined += "\n" + sec_str

    # Balance div tags inside page
    open_divs = len(re.findall(r'<div\b', combined))
    close_divs = len(re.findall(r'</div>', combined))
    diff = open_divs - close_divs
    if diff > 0:
        combined += "\n" + ("</div>\n" * diff)
    elif diff < 0:
        for _ in range(-diff):
            combined = re.sub(r'</div>\s*$', '', combined.strip())

    combined = re.sub(r'PAGE \d+ OF \d+', f'PAGE {idx+1} OF 5', combined)
    pages.append(f'<div class="page">\n{combined.strip()}\n</div>')

tail = "</div>\n</div>\n</div>\n</body>\n</html>"
new_doc = head_html + "\n\n" + "\n\n".join(pages) + "\n\n" + tail

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'w', encoding='utf-8') as f:
    f.write(new_doc)

print("=== EXACT 5 PAGES TOPIC 03 BUILT ===")

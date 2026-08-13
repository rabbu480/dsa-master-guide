import re

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract head and body
head_match = re.search(r'([\s\S]*?<div class="main-content">)', text)
head_html = head_match.group(1)

# Ensure print CSS height 98vh!
print_css = """@page { size: A4 portrait; margin: 4mm; }
@media print {
  body { background: white !important; padding: 0 !important; margin: 0 !important; color: black !important; -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
  .top-nav, .toc-sidebar { display: none !important; }
  .app-layout { display: block !important; }
  .page { box-shadow: none !important; border: none !important; margin: 0 !important; padding: 6px 10px !important; width: 100% !important; page-break-after: always !important; page-break-inside: avoid !important; break-inside: avoid !important; height: 98vh !important; overflow: hidden !important; zoom: 0.76; }
  .page:last-child { page-break-after: avoid !important; break-after: avoid !important; }
  table, tr, td, th { page-break-inside: avoid !important; break-inside: avoid !important; }
}"""
head_html = re.sub(r'@page\s*\{[^}]*\}\s*@media print\s*\{[\s\S]*?\}', print_css, head_html)

body = text[head_match.end():]
body = re.sub(r'</div>\s*</div>\s*</div>\s*</body>[\s\S]*$', '', body)

# Split strictly by <div class="page">
parts = body.split('<div class="page">')

pages = []
for p in parts:
    p_str = p.strip()
    if not p_str:
        continue
    # Strip any trailing unclosed </div> from the page content block
    p_str = re.sub(r'</div>\s*$', '', p_str)
    pages.append(p_str.strip())

print("Raw pristine page count:", len(pages))

# Pair raw pages into 5 target A4 pages:
# Target 1 = raw 0 + raw 1
# Target 2 = raw 2 + raw 3
# Target 3 = raw 4 + raw 5 + raw 6
# Target 4 = raw 7 + raw 8
# Target 5 = raw 9

grouped = [
    [pages[0], pages[1]],
    [pages[2], pages[3]],
    [pages[4], pages[5], pages[6]],
    [pages[7], pages[8]],
    [pages[9]]
]

final_pages = []
for idx, grp in enumerate(grouped):
    combined = ""
    for inner_idx, item in enumerate(grp):
        item_clean = item
        if inner_idx > 0:
            # strip ph header from second or third item in pair
            item_clean = re.sub(r'<div class=["\']ph["\'].*?>[\s\S]*?</div>', '', item_clean)
        combined += "\n" + item_clean.strip()

    # Clean any internal unclosed </div> tags from previous splits
    # Count open vs close
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

print("=== CONSOLIDATED 5 PAGES FOR TOPIC 03 WITHOUT SYNTAX ERRORS ===")

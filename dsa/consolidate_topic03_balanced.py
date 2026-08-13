import re

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Make CSS slightly denser for Topic 03:
# font-size: 10px; line-height: 1.28; padding: 10px 14px;
text = text.replace('font-size: 11px;', 'font-size: 10px;')
text = text.replace('line-height: 1.36;', 'line-height: 1.28;')
text = text.replace('padding: 14px 18px;', 'padding: 10px 14px;')
text = text.replace('margin-bottom: 30px;', 'margin-bottom: 20px;')
text = text.replace('margin-bottom: 12px;', 'margin-bottom: 6px;')
text = text.replace('margin-bottom: 14px;', 'margin-bottom: 6px;')

# Ensure print CSS has height 98vh, overflow hidden, zoom 0.76
print_css = """@page { size: A4 portrait; margin: 4mm; }
@media print {
  body { background: white !important; padding: 0 !important; margin: 0 !important; color: black !important; -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
  .top-nav, .toc-sidebar { display: none !important; }
  .app-layout { display: block !important; }
  .page { box-shadow: none !important; border: none !important; margin: 0 !important; padding: 5px 8px !important; width: 100% !important; page-break-after: always !important; page-break-inside: avoid !important; break-inside: avoid !important; height: 98vh !important; overflow: hidden !important; zoom: 0.76; }
  .page:last-child { page-break-after: avoid !important; break-after: avoid !important; }
  table, tr, td, th { page-break-inside: avoid !important; break-inside: avoid !important; }
}"""

text = re.sub(r'@page\s*\{[^}]*\}\s*@media print\s*\{[\s\S]*?\}', print_css, text)

# Now, let's pair up the 10 page blocks into 5 top-level page blocks!
# Split by <div class="page">
head_match = re.search(r'([\s\S]*?<div class="main-content">)', text)
head_html = head_match.group(1)

body = text[head_match.end():]
body = re.sub(r'</div>\s*</div>\s*</div>\s*</body>[\s\S]*$', '', body)

raw_pages = body.split('<div class="page">')
raw_pages = [p.strip() for p in raw_pages if p.strip()]

# Pair up raw 10 pages:
# New Page 1 = raw 0 + raw 1
# New Page 2 = raw 2 + raw 3
# New Page 3 = raw 4 + raw 5 + raw 6
# New Page 4 = raw 7 + raw 8
# New Page 5 = raw 9

merged_groups = [
    [raw_pages[0], raw_pages[1]],
    [raw_pages[2], raw_pages[3]],
    [raw_pages[4], raw_pages[5], raw_pages[6]],
    [raw_pages[7], raw_pages[8]],
    [raw_pages[9]]
]

final_pages = []
for idx, grp in enumerate(merged_groups):
    combined = ""
    for inner_idx, p in enumerate(grp):
        # strip outer </div> wrapper from p
        p_clean = re.sub(r'</div>\s*$', '', p.strip())
        if inner_idx > 0:
            p_clean = re.sub(r'<div class=["\']ph["\'].*?>[\s\S]*?</div>', '', p_clean)
        combined += "\n" + p_clean.strip()

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
new_doc = head_html + "\n\n" + "\n\n".join(final_pages) + "\n\n" + tail

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'w', encoding='utf-8') as f:
    f.write(new_doc)

print("=== CONSOLIDATED TOPIC 03 INTO EXACTLY 5 PAGES ===")

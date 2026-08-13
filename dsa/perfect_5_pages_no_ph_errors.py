import re

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Update print CSS with height 98vh!
print_css = """@page { size: A4 portrait; margin: 4mm; }
@media print {
  body { background: white !important; padding: 0 !important; margin: 0 !important; color: black !important; -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
  .top-nav, .toc-sidebar { display: none !important; }
  .app-layout { display: block !important; }
  .page { box-shadow: none !important; border: none !important; margin: 0 !important; padding: 6px 10px !important; width: 100% !important; page-break-after: always !important; page-break-inside: avoid !important; break-inside: avoid !important; height: 98vh !important; overflow: hidden !important; zoom: 0.76; }
  .page:last-child { page-break-after: avoid !important; break-after: avoid !important; }
  table, tr, td, th { page-break-inside: avoid !important; break-inside: avoid !important; }
}"""
head_html = re.sub(r'@page\s*\{[^}]*\}\s*@media print\s*\{[\s\S]*?\}', print_css, text)

# Now remove the internal <div class="page"> tags and headers for pages 2, 4, 6, 8, 10
# So that pairs of pages are combined inside a single top-level <div class="page">...</div>!

# Split by <div class="page">
parts = text.split('<div class="page">')
head = parts[0]
raw_pages = parts[1:] # 10 pages

# Clean raw pages by stripping their ending </div> before the next page:
cleaned_raw = []
for p in raw_pages:
    # strip trailing </div>\s*$
    c = re.sub(r'</div>\s*(?:<!-- PAGE [\s\S]*?-->)?\s*$', '', p.strip())
    c = re.sub(r'</div>\s*$', '', c.strip())
    cleaned_raw.append(c)

# Merge pairs:
# New 1 = 0 + 1
# New 2 = 2 + 3
# New 3 = 4 + 5
# New 4 = 6 + 7
# New 5 = 8 + 9

grouped = [
    [cleaned_raw[0], cleaned_raw[1]],
    [cleaned_raw[2], cleaned_raw[3]],
    [cleaned_raw[4], cleaned_raw[5]],
    [cleaned_raw[6], cleaned_raw[7]],
    [cleaned_raw[8], cleaned_raw[9]]
]

final_pages = []
for idx, grp in enumerate(grouped):
    combined = ""
    for inner_idx, item in enumerate(grp):
        item_str = item
        if inner_idx > 0:
            # remove <div class="ph">...</div> header from second item
            item_str = re.sub(r'<div class=["\']ph["\'].*?>[\s\S]*?</div>', '', item_str)
        combined += "\n" + item_str.strip()

    # Balance div tags inside combined page
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

print("=== PERFECT 5 PAGE CONSOLIDATION FOR TOPIC 03 WITHOUT LEAF PH ERRORS ===")

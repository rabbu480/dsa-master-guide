import re

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace <div class="page"> boundaries for pages 2, 4, 6, 8 with empty string to merge adjacent pages cleanly!
# Page 1 = Old 1 + 2
# Page 2 = Old 3 + 4
# Page 3 = Old 5 + 6
# Page 4 = Old 7 + 8
# Page 5 = Old 9 + 10

# Let's inspect where page comments are:
# <!-- PAGE 2...
# <!-- PAGE 3...
# <!-- PAGE 4...

# Strip ph headers of page 2, 4, 6, 8, 10
# Also strip <div class="page"> and its matching closing </div> before comments!

# Split by <!-- PAGE
sections = text.split('<!-- PAGE ')
head = sections[0]
page_blocks = sections[1:] # 10 blocks

print("Found page blocks:", len(page_blocks))

# Group page_blocks:
# New 1 = block 0 (Page 1) + block 1 (Page 2)
# New 2 = block 2 (Page 3) + block 3 (Page 4)
# New 3 = block 4 (Page 5) + block 5 (Page 6)
# New 4 = block 6 (Page 7) + block 7 (Page 8)
# New 5 = block 8 (Page 9) + block 9 (Page 10)

grouped = [
    [page_blocks[0], page_blocks[1]],
    [page_blocks[2], page_blocks[3]],
    [page_blocks[4], page_blocks[5]],
    [page_blocks[6], page_blocks[7]],
    [page_blocks[8], page_blocks[9]]
]

final_pages = []
for idx, grp in enumerate(grouped):
    combined = ""
    for inner_idx, blk in enumerate(grp):
        blk_str = '<!-- PAGE ' + blk
        if inner_idx > 0:
            # remove <div class="ph">...</div> header from second block
            blk_str = re.sub(r'<div class=["\']ph["\'].*?>[\s\S]*?</div>', '', blk_str)
            # remove leading <div class="page">
            blk_str = re.sub(r'<div class=["\']page["\']>\s*', '', blk_str)
        
        # remove trailing </div> before next block
        blk_str = re.sub(r'</div>\s*$', '', blk_str.strip())
        combined += "\n" + blk_str.strip()

    # Balance divs
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

# Fix print CSS
print_css = """@page { size: A4 portrait; margin: 4mm; }
@media print {
  body { background: white !important; padding: 0 !important; margin: 0 !important; color: black !important; -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
  .top-nav, .toc-sidebar { display: none !important; }
  .app-layout { display: block !important; }
  .page { box-shadow: none !important; border: none !important; margin: 0 !important; padding: 6px 10px !important; width: 100% !important; page-break-after: always !important; page-break-inside: avoid !important; break-inside: avoid !important; height: 98vh !important; overflow: hidden !important; zoom: 0.76; }
  .page:last-child { page-break-after: avoid !important; break-after: avoid !important; }
  table, tr, td, th { page-break-inside: avoid !important; break-inside: avoid !important; }
}"""
head = re.sub(r'@page\s*\{[^}]*\}\s*@media print\s*\{[\s\S]*?\}', print_css, head)

tail = "</div>\n</div>\n</div>\n</body>\n</html>"
new_doc = head + "\n\n" + "\n\n".join(final_pages) + "\n\n" + tail

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'w', encoding='utf-8') as f:
    f.write(new_doc)

print("=== PERFECT CLEAN 5 PAGE REBUILD USING PAGE COMMENTS ===")

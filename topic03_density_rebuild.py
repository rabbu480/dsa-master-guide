import re, shutil

shutil.copy(r'F:\dsa\bookfinal - Copy\v4\bookfinal\Topic03_TwoPointers.html',
            r'F:\dsa\bookfinal\Topic03_TwoPointers.html')

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'rb') as f:
    raw = f.read()

text = raw.decode('utf-8').replace('\r\n', '\n').replace('\r', '\n')

# === STRATEGY: Reduce body font-size and all spacing to fit 2 pages into 1 ===
# Current: font-size: 11px, line-height: 1.36
# New: font-size: 9px, line-height: 1.2
# Also reduce padding in boxes, ph, prow, etc.

# Reduce body font-size
text = re.sub(r'(body\s*\{[^}]*font-size:\s*)\d+px', r'\g<1>9px', text)
text = re.sub(r'(body\s*\{[^}]*line-height:\s*)\d+\.?\d*', r'\g<1>1.2', text)

# Reduce page padding
text = text.replace('padding: 14px 18px;', 'padding: 6px 10px;')

# Reduce ph (header) bottom margin
text = text.replace('margin-bottom: 14px;', 'margin-bottom: 6px;')

# Reduce box/bc padding
text = re.sub(r'\.bc\s*\{[^}]*\}', lambda m: re.sub(r'padding:\s*\d+px', 'padding: 3px', m.group(0)), text)

# Reduce pre font-size
text = re.sub(r'(pre\s*\{[^}]*font-size:\s*)\d+px', r'\g<1>8px', text)
# Add pre size if not present
if 'pre {' not in text:
    text = text.replace('.box {', 'pre { font-size: 8px; line-height: 1.15; }\n.box {', 1)

# Fix print CSS
print_css = """\
@page { size: A4 portrait; margin: 4mm; }
@media print {
  body { background: white !important; padding: 0 !important; margin: 0 !important; color: black !important; -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; font-size: 9px !important; line-height: 1.2 !important; }
  .top-nav, .toc-sidebar { display: none !important; }
  .app-layout { display: block !important; }
  .page { box-shadow: none !important; border: none !important; margin: 0 !important; padding: 4px 8px !important; width: 100% !important; page-break-after: always !important; page-break-inside: avoid !important; break-inside: avoid !important; height: 98vh !important; overflow: hidden !important; zoom: 0.85; }
  .page:last-child { page-break-after: avoid !important; break-after: avoid !important; }
  table, tr, td, th { page-break-inside: avoid !important; break-inside: avoid !important; }
  pre { font-size: 8px !important; line-height: 1.15 !important; }
  .ph { padding-bottom: 4px !important; margin-bottom: 6px !important; }
  .bc { padding: 4px !important; }
  .bh { padding: 3px 8px !important; }
}"""
text = re.sub(r'@page\s*\{[^}]*\}[\s\S]*?(?=</style>)', print_css + '\n', text)

# Remove even-page boundaries (merge pages 1+2, 3+4, 5+6, 7+8, 9+10)
for page_num in [2, 4, 6, 8, 10]:
    pattern = re.compile(
        r'\n<!-- PAGE ' + str(page_num) + r'[^\n]*-->\n<div class="page">\n<div class="ph">[\s\S]*?</div>\n</div>',
        re.MULTILINE
    )
    text_new, n = pattern.subn('', text)
    if n > 0:
        print(f"Removed page {page_num} boundary")
        text = text_new

# Fix page numbers
text = text.replace('PAGE 1 OF 10', 'PAGE 1 OF 5')
text = text.replace('PAGE 3 OF 10', 'PAGE 2 OF 5')
text = text.replace('PAGE 5 OF 10', 'PAGE 3 OF 5')
text = text.replace('PAGE 7 OF 10', 'PAGE 4 OF 5')
text = text.replace('PAGE 9 OF 10', 'PAGE 5 OF 5')

page_count = len(re.findall('<div class="page">', text))
print(f"Final page div count: {page_count}")

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'wb') as f:
    f.write(text.replace('\n', '\r\n').encode('utf-8'))

print("DONE")

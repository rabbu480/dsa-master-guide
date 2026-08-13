import re, shutil

shutil.copy(r'F:\dsa\bookfinal - Copy\v4\bookfinal\Topic03_TwoPointers.html',
            r'F:\dsa\bookfinal\Topic03_TwoPointers.html')

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'rb') as f:
    raw = f.read()

text = raw.decode('utf-8').replace('\r\n', '\n').replace('\r', '\n')

# Fix print CSS - height: 197vh to accommodate 2 merged pages, and remove overflow hidden
print_css = """\
@page { size: A4 portrait; margin: 4mm; }
@media print {
  body { background: white !important; padding: 0 !important; margin: 0 !important; color: black !important; -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
  .top-nav, .toc-sidebar { display: none !important; }
  .app-layout { display: block !important; }
  .page { box-shadow: none !important; border: none !important; margin: 0 !important; padding: 3px 10px !important; width: 100% !important; page-break-after: always !important; page-break-inside: avoid !important; break-inside: avoid !important; height: 197vh !important; overflow: hidden !important; zoom: 0.48; }
  .page:last-child { page-break-after: avoid !important; break-after: avoid !important; }
  table, tr, td, th { page-break-inside: avoid !important; break-inside: avoid !important; }
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

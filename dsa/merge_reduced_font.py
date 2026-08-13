import re, shutil

shutil.copy(r'F:\dsa\bookfinal - Copy\v4\bookfinal\Topic03_TwoPointers.html',
            r'F:\dsa\bookfinal\Topic03_TwoPointers.html')

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'rb') as f:
    raw = f.read()

text = raw.decode('utf-8').replace('\r\n', '\n').replace('\r', '\n')

# Remove even-page boundaries FIRST (before CSS modification)
for page_num in [2, 4, 6, 8, 10]:
    pattern = re.compile(
        r'\n<!-- PAGE ' + str(page_num) + r'[^\n]*-->\n<div class="page">\n<div class="ph">[\s\S]*?</div>\n</div>',
        re.MULTILINE
    )
    text_new, n = pattern.subn('', text)
    if n > 0:
        print(f"Removed page {page_num} boundary")
        text = text_new

# Now replace the .page CSS (screen styles) - reduce font-size and line-height
text = text.replace(
    'body { font-family: \'Inter\', sans-serif; background: #e2e8f0; color: var(--txt); font-size: 11px; line-height: 1.36; padding: 20px; }',
    'body { font-family: \'Inter\', sans-serif; background: #e2e8f0; color: var(--txt); font-size: 9px; line-height: 1.22; padding: 20px; }'
)

# Fix print CSS - match Topic02's working CSS but with zoom 0.76 
print_css = """\
@page { size: A4 portrait; margin: 4mm; }
@media print {
  body { background: white !important; padding: 0 !important; margin: 0 !important; color: black !important; -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; font-size: 9px !important; line-height: 1.22 !important; }
  .top-nav, .toc-sidebar { display: none !important; }
  .app-layout { display: block !important; }
  .page { box-shadow: none !important; border: none !important; margin: 0 !important; padding: 4px 8px !important; width: 100% !important; page-break-after: always !important; page-break-inside: avoid !important; break-inside: avoid !important; height: 98vh !important; overflow: hidden !important; zoom: 0.85; }
  .page:last-child { page-break-after: avoid !important; break-after: avoid !important; }
  table, tr, td, th { page-break-inside: avoid !important; break-inside: avoid !important; }
  pre { font-size: 8px !important; line-height: 1.2 !important; }
}"""
text = re.sub(r'@page\s*\{[^}]*\}[\s\S]*?(?=</style>)', print_css + '\n', text)

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

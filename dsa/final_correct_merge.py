import re, shutil

shutil.copy(r'F:\dsa\bookfinal - Copy\v4\bookfinal\Topic03_TwoPointers.html',
            r'F:\dsa\bookfinal\Topic03_TwoPointers.html')

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'rb') as f:
    raw = f.read()

text = raw.decode('utf-8').replace('\r\n', '\n').replace('\r', '\n')

# Fix print CSS
print_css = """\
@page { size: A4 portrait; margin: 4mm; }
@media print {
  body { background: white !important; padding: 0 !important; margin: 0 !important; color: black !important; -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
  .top-nav, .toc-sidebar { display: none !important; }
  .app-layout { display: block !important; }
  .page { box-shadow: none !important; border: none !important; margin: 0 !important; padding: 6px 10px !important; width: 100% !important; page-break-after: always !important; page-break-inside: avoid !important; break-inside: avoid !important; height: 98vh !important; overflow: hidden !important; zoom: 0.76; }
  .page:last-child { page-break-after: avoid !important; break-after: avoid !important; }
  table, tr, td, th { page-break-inside: avoid !important; break-inside: avoid !important; }
}"""
text = re.sub(r'@page\s*\{[^}]*\}[\s\S]*?(?=</style>)', print_css + '\n', text)

# Now remove the even-page boundaries.
# From debug: the boundary before PAGE 2 is:
# </p>\n    </div>\n  </div>\n</div>\n</div>\n\n<!-- PAGE 2: ...
# Pattern is: \n\n<!-- PAGE N: ... -->\n<div class="page">\n<div class="ph">...\n</div>
#
# The difference from before is no \n in the look-behind.
# Let's just match: \n<!-- PAGE N: ... -->\n<div class="page">\n<div class="ph">...HEADER...\n</div>

for page_num in [2, 4, 6, 8, 10]:
    pattern = re.compile(
        r'\n<!-- PAGE ' + str(page_num) + r'[^\n]*-->\n<div class="page">\n<div class="ph">[\s\S]*?</div>\n</div>',
        re.MULTILINE
    )
    text_new, n = pattern.subn('', text)
    if n > 0:
        print(f"Removed page {page_num} boundary ({n} match)")
        text = text_new
    else:
        print(f"WARNING: page {page_num} not found!")
        idx = text.find(f'<!-- PAGE {page_num}')
        if idx >= 0:
            print(f"  Context: {repr(text[idx-20:idx+200])}")

count = len(re.findall('<div class="page">', text))
print(f"\nPage divs after removal: {count}")

# Fix page numbers
text = text.replace('PAGE 1 OF 10', 'PAGE 1 OF 5')
text = text.replace('PAGE 3 OF 10', 'PAGE 2 OF 5')
text = text.replace('PAGE 5 OF 10', 'PAGE 3 OF 5')
text = text.replace('PAGE 7 OF 10', 'PAGE 4 OF 5')
text = text.replace('PAGE 9 OF 10', 'PAGE 5 OF 5')

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'wb') as f:
    f.write(text.replace('\n', '\r\n').encode('utf-8'))

print("DONE")

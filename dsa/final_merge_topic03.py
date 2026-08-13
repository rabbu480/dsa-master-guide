import re

# Restore pristine
import shutil
shutil.copy(r'F:\dsa\bookfinal - Copy\v4\bookfinal\Topic03_TwoPointers.html',
            r'F:\dsa\bookfinal\Topic03_TwoPointers.html')

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'rb') as f:
    raw = f.read()

text = raw.decode('utf-8').replace('\r\n', '\n').replace('\r', '\n')

# Fix print CSS - remove duplicate @media print blocks
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

# Show all page boundaries precisely
pages = list(re.finditer(r'<div class="page">', text))
print(f"Page divs before: {len(pages)}")
for i, m in enumerate(pages):
    snippet_before = text[max(0, m.start()-60):m.start()]
    print(f"  Page {i+1}: before='{repr(snippet_before)}'")

# The 5 target pages are:
# Keep: pages 1,3,5,7,9 (odd pages in original 1-indexed)
# Merge into: pages 2,4,6,8,10 (remove their <div class="page"> + <div class="ph"> headers)
# 
# Strategy: find all 10 page starts, then for even-indexed ones (0-indexed: 1,3,5,7,9)
# remove from their `</div>\n</div>\n\n<!-- PAGE...` or `</div>\n\n<!-- PAGE...` 
# back-boundary up to and including their <div class="ph">...</div> closing tag

# Let's use a different strategy: find and delete JUST the even-page page div opening + ph header
# Pattern for each even page:
# \n\n<!-- PAGE N: ... -->\n<div class="page">\n<div class="ph">...\n</div>

for page_num in [2, 4, 6, 8, 10]:
    pattern = re.compile(
        r'\n\n<!-- PAGE ' + str(page_num) + r'[^-]*-->\n<div class="page">\n<div class="ph">[\s\S]*?</div>\n</div>',
        re.MULTILINE
    )
    text_new, n = pattern.subn('', text)
    if n > 0:
        print(f"  Removed page {page_num} boundary (1 match)")
        text = text_new
    else:
        print(f"  WARNING: page {page_num} pattern not found!")
        # Show what's near this page number
        idx = text.find(f'<!-- PAGE {page_num}')
        if idx >= 0:
            print(f"    Context: '{repr(text[idx-5:idx+100])}'")

pages_after = list(re.finditer(r'<div class="page">', text))
print(f"Page divs after: {len(pages_after)}")

# Fix page numbers
text = text.replace('PAGE 1 OF 10', 'PAGE 1 OF 5')
text = text.replace('PAGE 3 OF 10', 'PAGE 2 OF 5')
text = text.replace('PAGE 5 OF 10', 'PAGE 3 OF 5')
text = text.replace('PAGE 7 OF 10', 'PAGE 4 OF 5')
text = text.replace('PAGE 9 OF 10', 'PAGE 5 OF 5')

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'wb') as f:
    f.write(text.replace('\n', '\r\n').encode('utf-8'))

print("DONE")

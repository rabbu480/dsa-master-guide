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

# Find the index of all <!-- PAGE N --> comments
page_comment_re = re.compile(r'<!-- PAGE (\d+)[^-]*-->')
comments = list(page_comment_re.finditer(text))
for c in comments:
    print(f"  Found comment: PAGE {c.group(1)} at index {c.start()}")

# For pages 2, 4, 6, 8, 10: remove from comment start to end of </div> that closes the ph header
# Look at the exact context around page 2's comment

idx2 = text.find('<!-- PAGE 2:')
print("\nContext around PAGE 2 comment:")
print(repr(text[idx2-5:idx2+250]))

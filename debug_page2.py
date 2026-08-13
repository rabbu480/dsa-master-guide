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

# Diagnose: PAGE 2 comment is found but not PAGE 2's page div opening
# This means PAGE 1 and PAGE 2 are NOT separated by \n\n - let's see exact chars before PAGE 2 comment
idx2 = text.find('<!-- PAGE 2:')
print("Chars before PAGE 2 comment:", repr(text[idx2-30:idx2]))
print("Chars after PAGE 2 comment:", repr(text[idx2:idx2+200]))

# Apparently PAGE 2 comment exists but the file has no <!-- PAGE 2 comment in diagnose output
# Let's find ALL the page comments differently
print("\nAll page comments in pristine file:")
for m in re.finditer(r'<!-- PAGE \d', text):
    print(f"  '{text[m.start():m.start()+30]}' at {m.start()}")

print(f"\nTotal <div class='page'> divs: {len(re.findall(r'<div class=\"page\">', text))}")

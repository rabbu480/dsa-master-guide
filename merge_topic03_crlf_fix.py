import re

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'rb') as f:
    raw = f.read()

# Decode, normalize to LF
text = raw.decode('utf-8').replace('\r\n', '\n').replace('\r', '\n')

# Count page divs before
before = len(re.findall(r'<div class=["\']page["\']', text))
print(f"Page divs BEFORE: {before}")

# ---------- fix print CSS (remove duplicate @media print blocks) ----------
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

# Remove ALL @page / @media print blocks and replace with one clean copy
text = re.sub(r'@page\s*\{[^}]*\}[\s\S]*?(?=</style>)', print_css + '\n', text)

# ---------- Remove even page boundaries (merge pairs) ----------
# Pages 2, 4, 6, 8, 10 start with:
#   </div>\n</div>\n\n<!-- PAGE N: ... -->\n<div class="page">\n<div class="ph">\n...header...\n</div>
# We want to delete that entire block (closing the prior page + opening the new one + its header)
# so that both halves end up inside the PREVIOUS page's <div class="page"> container.

# Pattern: closes previous page (two </div>), comment, opens new page, header block
boundary_pattern = re.compile(
    r'</div>\n</div>\n\n<!-- PAGE (2|4|6|8|10)[^-]*-->\n<div class="page">\n<div class="ph">[\s\S]*?</div>\n</div>',
    re.MULTILINE
)

def remove_boundary(m):
    return ''  # delete the closing divs + new page opening + ph header

text, count = boundary_pattern.subn(remove_boundary, text)
print(f"Boundaries removed: {count}")

# Fix page numbers in remaining headers (pages 1,3,5,7,9 become 1–5)
text = text.replace('PAGE 1 OF 10', 'PAGE 1 OF 5')
text = text.replace('PAGE 3 OF 10', 'PAGE 2 OF 5')
text = text.replace('PAGE 5 OF 10', 'PAGE 3 OF 5')
text = text.replace('PAGE 7 OF 10', 'PAGE 4 OF 5')
text = text.replace('PAGE 9 OF 10', 'PAGE 5 OF 5')

after = len(re.findall(r'<div class=["\']page["\']', text))
print(f"Page divs AFTER: {after}")

# Write back with CRLF
with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'wb') as f:
    f.write(text.replace('\n', '\r\n').encode('utf-8'))

print("DONE")

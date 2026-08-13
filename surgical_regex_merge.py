import re

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Make CSS print zoom 0.76 and height 98vh
print_css = """@page { size: A4 portrait; margin: 4mm; }
@media print {
  body { background: white !important; padding: 0 !important; margin: 0 !important; color: black !important; -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
  .top-nav, .toc-sidebar { display: none !important; }
  .app-layout { display: block !important; }
  .page { box-shadow: none !important; border: none !important; margin: 0 !important; padding: 6px 10px !important; width: 100% !important; page-break-after: always !important; page-break-inside: avoid !important; break-inside: avoid !important; height: 98vh !important; overflow: hidden !important; zoom: 0.76; }
  .page:last-child { page-break-after: avoid !important; break-after: avoid !important; }
  table, tr, td, th { page-break-inside: avoid !important; break-inside: avoid !important; }
}"""

text = re.sub(r'@page\s*\{[^}]*\}\s*@media print\s*\{[\s\S]*?\}', print_css, text)

# Simply replace:
# </div>\n\n<!-- PAGE 2: API & SIDE-BY-SIDE TEMPLATES -->\n<div class="page">\n<div class="ph">[\s\S]*?</div>
# with empty string or comment!

pages_to_remove = [
    r'</div>\s*\n\s*<!-- PAGE 2: API & SIDE-BY-SIDE TEMPLATES -->\s*<div class="page">\s*<div class="ph">[\s\S]*?</div>',
    r'</div>\s*\n\s*<!-- PAGE 4: CORE PATTERNS \(3SUM\) -->\s*<div class="page">\s*<div class="ph">[\s\S]*?</div>',
    r'</div>\s*\n\s*<!-- PAGE 6: CORE PATTERNS \(TRAPPING RAIN WATER\) -->\s*<div class="page">\s*<div class="ph">[\s\S]*?</div>',
    r'</div>\s*\n\s*<!-- PAGE 8: NEETCODE SUITE \(PART 1\) -->\s*<div class="page">\s*<div class="ph">[\s\S]*?</div>',
    r'</div>\s*\n\s*<!-- PAGE 10: DRY RUN, PROOFS & CHEAT SHEET -->\s*<div class="page">\s*<div class="ph">[\s\S]*?</div>'
]

for pat in pages_to_remove:
    text = re.sub(pat, '<!-- MERGED -->', text)

# Update page number strings
text = text.replace('PAGE 1 OF 10', 'PAGE 1 OF 5')
text = text.replace('PAGE 3 OF 10', 'PAGE 2 OF 5')
text = text.replace('PAGE 5 OF 10', 'PAGE 3 OF 5')
text = text.replace('PAGE 7 OF 10', 'PAGE 4 OF 5')
text = text.replace('PAGE 9 OF 10', 'PAGE 5 OF 5')

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("=== SURGICAL REGEX MERGE FOR TOPIC 03 COMPLETE ===")

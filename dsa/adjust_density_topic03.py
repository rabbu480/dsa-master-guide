import re

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace margin and padding in CSS to make content fit cleanly without trailing overflow
text = text.replace('font-size: 11px;', 'font-size: 10.5px;')
text = text.replace('line-height: 1.36;', 'line-height: 1.32;')
text = text.replace('padding: 14px 18px;', 'padding: 10px 14px;')
text = text.replace('margin-bottom: 30px;', 'margin-bottom: 20px;')

# Ensure print CSS has height 98vh, overflow hidden, zoom 0.76
print_css = """@page { size: A4 portrait; margin: 4mm; }
@media print {
  body { background: white !important; padding: 0 !important; margin: 0 !important; color: black !important; -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
  .top-nav, .toc-sidebar { display: none !important; }
  .app-layout { display: block !important; }
  .page { box-shadow: none !important; border: none !important; margin: 0 !important; padding: 5px 8px !important; width: 100% !important; page-break-after: always !important; page-break-inside: avoid !important; break-inside: avoid !important; height: 98vh !important; overflow: hidden !important; zoom: 0.76; }
  .page:last-child { page-break-after: avoid !important; break-after: avoid !important; }
  table, tr, td, th { page-break-inside: avoid !important; break-inside: avoid !important; }
}"""

text = re.sub(r'@page\s*\{[^}]*\}\s*@media print\s*\{[\s\S]*?\}', print_css, text)

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("=== ADJUSTED DENSITY STYLING FOR TOPIC 03 ===")

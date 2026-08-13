import re

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Update @media print .page CSS to include height: 98vh !important; overflow: hidden !important; zoom: 0.76;
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

# Add closing </div> for each page block if unclosed
parts = text.split('<div class="page">')
head = parts[0]
pages = parts[1:]

fixed_pages = []
for p in pages:
    p_clean = re.sub(r'</div>\s*</div>\s*</div>\s*</body>[\s\S]*$', '', p)
    open_divs = len(re.findall(r'<div\b', p_clean))
    close_divs = len(re.findall(r'</div>', p_clean))
    diff = open_divs - close_divs
    if diff > 0:
        p_clean += "\n" + ("</div>\n" * diff)
    elif diff < 0:
        for _ in range(-diff):
            p_clean = re.sub(r'</div>\s*$', '', p_clean.strip())
    fixed_pages.append('<div class="page">\n' + p_clean.strip() + '\n</div>')

tail = "</div>\n</div>\n</div>\n</body>\n</html>"
new_doc = head + "\n\n" + "\n\n".join(fixed_pages) + "\n\n" + tail

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'w', encoding='utf-8') as f:
    f.write(new_doc)

print("=== TOPIC 03 PRINT CSS & DIV BALANCING FIXED ===")

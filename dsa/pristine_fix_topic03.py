import os
import glob
import re

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract head before body
head_match = re.search(r'([\s\S]*?<div class="main-content">)', text)
head_html = head_match.group(1)

# Ensure height: 98vh !important; overflow: hidden !important; zoom: 0.76;
print_css = """@page { size: A4 portrait; margin: 4mm; }
@media print {
  body { background: white !important; padding: 0 !important; margin: 0 !important; color: black !important; -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
  .top-nav, .toc-sidebar { display: none !important; }
  .app-layout { display: block !important; }
  .page { box-shadow: none !important; border: none !important; margin: 0 !important; padding: 6px 10px !important; width: 100% !important; page-break-after: always !important; page-break-inside: avoid !important; break-inside: avoid !important; height: 98vh !important; overflow: hidden !important; zoom: 0.76; }
  .page:last-child { page-break-after: avoid !important; break-after: avoid !important; }
  table, tr, td, th { page-break-inside: avoid !important; break-inside: avoid !important; }
}"""
head_html = re.sub(r'@page\s*\{[^}]*\}\s*@media print\s*\{[\s\S]*?\}', print_css, head_html)

body = text[head_match.end():]
body = re.sub(r'</div>\s*</div>\s*</div>\s*</body>[\s\S]*$', '', body)

# Split by <div class="ph">
ph_sections = body.split('<div class="ph">')
ph_sections = [s.strip() for s in ph_sections if s.strip()]

print(f"Topic03 ph_sections count: {len(ph_sections)}")

# We want exactly 5 pages!
target_count = 5
chunk_size = (len(ph_sections) + target_count - 1) // target_count
grouped = []
for i in range(0, len(ph_sections), chunk_size):
    grouped.append(ph_sections[i:i+chunk_size])

while len(grouped) > target_count:
    last = grouped.pop()
    grouped[-1].extend(last)

formatted_pages = []
for idx, grp in enumerate(grouped):
    combined = ""
    for inner_idx, p in enumerate(grp):
        p_str = f'<div class="ph">{p}' if not p.startswith('<div class="ph">') else p
        if inner_idx > 0:
            p_clean = re.sub(r'<div class=["\']ph["\'].*?>[\s\S]*?</div>', '', p_str)
            combined += "\n" + p_clean
        else:
            combined += "\n" + p_str

    # Balance div tags
    open_divs = len(re.findall(r'<div\b', combined))
    close_divs = len(re.findall(r'</div>', combined))
    diff = open_divs - close_divs
    if diff > 0:
        combined += "\n" + ("</div>\n" * diff)
    elif diff < 0:
        for _ in range(-diff):
            combined = re.sub(r'</div>\s*$', '', combined.strip())

    combined = re.sub(r'PAGE \d+ OF \d+', f'PAGE {idx+1} OF 5', combined)
    formatted_pages.append(f'<div class="page">\n{combined.strip()}\n</div>')

tail = "</div>\n</div>\n</div>\n</body>\n</html>"
new_doc = head_html + "\n\n" + "\n\n".join(formatted_pages) + "\n\n" + tail

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'w', encoding='utf-8') as f:
    f.write(new_doc)

print(f"=== TOPIC 03 PERFECTLY BUILT INTO {len(formatted_pages)} DENSE A4 PAGES ===")

import os
import glob
import re

for fname in ['Topic05_BinarySearch.html', 'Topic08_Queue_Deque.html']:
    filepath = os.path.join('F:/dsa/bookfinal', fname)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    head_match = re.search(r'([\s\S]*?<div class="main-content">)', content)
    if not head_match:
        continue
    head_html = head_match.group(1)

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

    body = content[head_match.end():]
    body = re.sub(r'</div>\s*</div>\s*</div>\s*</body>[\s\S]*$', '', body)

    # Clean out any unclosed div page wrappers
    body_clean = re.sub(r'<div class=["\']page["\']>\s*', '', body)
    body_clean = re.sub(r'</div>\s*$', '', body_clean)

    # Split by <div class="header-top"> or <div class="ph">
    sections = re.split(r'(?=<div class=["\'](?:header-top|ph)["\'])', body_clean)
    sections = [s.strip() for s in sections if s.strip()]

    target_count = 5
    chunk_size = (len(sections) + target_count - 1) // target_count
    grouped = []
    for i in range(0, len(sections), chunk_size):
        grouped.append(sections[i:i+chunk_size])
    while len(grouped) > target_count:
        last = grouped.pop()
        grouped[-1].extend(last)

    fixed_pages = []
    for idx, grp in enumerate(grouped):
        sec_clean = "\n".join(grp)
        # Count open vs close
        open_divs = len(re.findall(r'<div\b', sec_clean))
        close_divs = len(re.findall(r'</div>', sec_clean))
        diff = open_divs - close_divs
        if diff > 0:
            sec_clean += "\n" + ("</div>\n" * diff)
        elif diff < 0:
            for _ in range(-diff):
                sec_clean = re.sub(r'</div>\s*$', '', sec_clean.strip())

        sec_clean = re.sub(r'PAGE \d+ OF \d+', f'PAGE {idx+1} OF {len(grouped)}', sec_clean)
        fixed_pages.append(f'<div class="page">\n{sec_clean.strip()}\n</div>')

    tail = "</div>\n</div>\n</div>\n</body>\n</html>"
    new_doc = head_html + "\n\n" + "\n\n".join(fixed_pages) + "\n\n" + tail
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_doc)
    print(f"Pristine fix for {fname}: {len(fixed_pages)} pages created.")

print("=== PRISTINE FIX TOPIC 05 AND 08 COMPLETE ===")

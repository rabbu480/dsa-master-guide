import os
import glob
import re

files = sorted(glob.glob('F:/dsa/bookfinal/Topic*.html'))

for filepath in files:
    if 'Topic01_' in filepath or 'Topic02_' in filepath:
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find main-content start
    head_match = re.search(r'([\s\S]*?<div class="main-content">)', content)
    if not head_match:
        continue
    head_html = head_match.group(1)
    
    # Standardize print CSS with height: 98vh !important; overflow: hidden !important; zoom: 0.76;
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

    # Extract all top-level <div class="page"> blocks cleanly
    pages = re.findall(r'<div class=["\']page["\']>\s*([\s\S]*?)\s*</div>', body)
    if not pages:
        # Split by <div class="ph">
        ph_sections = body.split('<div class="ph">')
        pages = [s.strip() for s in ph_sections if s.strip()]

    # Format into exactly 5 or 6 pages
    target_count = 5
    chunk_size = (len(pages) + target_count - 1) // target_count
    grouped = []
    for i in range(0, len(pages), chunk_size):
        grouped.append(pages[i:i+chunk_size])
    while len(grouped) > target_count:
        last = grouped.pop()
        grouped[-1].extend(last)

    new_pages = []
    for idx, grp in enumerate(grouped):
        combined = ""
        for inner_idx, p in enumerate(grp):
            p_str = p if p.startswith('<div class="ph">') else f'<div class="ph">{p}' if '<h1>' in p else p
            if inner_idx > 0:
                p_clean = re.sub(r'<div class=["\']ph["\'].*?>[\s\S]*?</div>', '', p_str)
                combined += "\n" + p_clean
            else:
                combined += "\n" + p_str
        combined = re.sub(r'PAGE \d+ OF \d+', f'PAGE {idx+1} OF {len(grouped)}', combined)
        new_pages.append(f'<div class="page">\n{combined.strip()}\n</div>')

    tail = "</div>\n</div>\n</div>\n</body>\n</html>"
    new_doc = head_html + "\n\n" + "\n\n".join(new_pages) + "\n\n" + tail
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_doc)
    print(f"Cleanly formatted {os.path.basename(filepath)} into {len(new_pages)} pages.")

print("=== REBUILD COMPLETE ===")

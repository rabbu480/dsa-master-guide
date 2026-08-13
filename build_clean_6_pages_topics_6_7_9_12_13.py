import os
import glob
import re

files_to_build = [
    'Topic06_LinkedList.html',
    'Topic07_Stack.html',
    'Topic09_Heap.html',
    'Topic12_Graphs.html',
    'Topic13_Backtracking.html'
]

# Standard page template snippet wrapper
def wrap_page(content, page_num, topic_name):
    header = f'''<div class="ph">
  <div><h1>{topic_name.upper()}</h1><div class="sub">FAANG Master Guide — Java Edition</div></div>
  <div style="text-align:right"><div class="pn">PAGE {page_num} OF 6</div><div class="ptag">FAANG DSA HANDBOOK</div></div>
</div>'''
    return f'<div class="page">\n{header}\n{content}\n</div>'

for filename in files_to_build:
    filepath = os.path.join('F:/dsa/bookfinal', filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        full_text = f.read()

    # Get header before body
    head_match = re.search(r'([\s\S]*?<div class="main-content">)', full_text)
    if not head_match:
        continue
    head_html = head_match.group(1)
    
    # Standardize print CSS with zoom 0.76 and height 98vh
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

    body = full_text[head_match.end():]
    body = re.sub(r'</div>\s*</div>\s*</div>\s*</body>[\s\S]*$', '', body)

    # Strip existing page/ph divs
    body_clean = re.sub(r'<div class=["\']page["\']>\s*', '', body)
    body_clean = re.sub(r'<div class=["\']ph["\'].*?>[\s\S]*?</div>', '', body_clean)

    # Extract all top level elements (g2, g3, box, prow, prob)
    elements = re.findall(r'(<div class=["\'](?:g[23]|prow|box|prob)[^"\']*["\'].*?>[\s\S]*?</div>)', body_clean)
    if not elements:
        # Split by <div class=
        parts = body_clean.split('<div class=')
        elements = ['<div class=' + p for p in parts if p.strip()]

    # Group into 6 pages
    import math
    chunk_size = max(1, math.ceil(len(elements) / 6))
    grouped = []
    for c in range(0, len(elements), chunk_size):
        group = elements[c:c+chunk_size]
        grouped.append(group)

    while len(grouped) > 6:
        last = grouped.pop()
        grouped[-1].extend(last)

    topic_name = filename.split('_')[1].replace('.html', '')
    pages_html = []
    for idx, grp in enumerate(grouped):
        content_str = "\n".join(grp)
        pages_html.append(wrap_page(content_str, idx + 1, topic_name))

    tail = "</div>\n</div>\n</div>\n</body>\n</html>"
    new_doc = head_html + "\n\n" + "\n\n".join(pages_html) + "\n\n" + tail

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_doc)

    print(f"Built {filename}: {len(pages_html)} clean pages created.")

print("=== BUILD CLEAN 6 PAGES COMPLETE ===")

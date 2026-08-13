import os
import glob
import re

files_to_fix = [
    'Topic06_LinkedList.html',
    'Topic07_Stack.html',
    'Topic09_Heap.html',
    'Topic12_Graphs.html',
    'Topic13_Backtracking.html'
]

for filename in files_to_fix:
    filepath = os.path.join('F:/dsa/bookfinal', filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find main-content start
    head_match = re.search(r'([\s\S]*?<div class="main-content">)', content)
    if not head_match:
        continue
    head_html = head_match.group(1)
    
    # Ensure standard print CSS
    print_css = """@page { size: A4 portrait; margin: 4mm; }
@media print {
  body { background: white !important; padding: 0 !important; margin: 0 !important; color: black !important; -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
  .top-nav, .toc-sidebar { display: none !important; }
  .app-layout { display: block !important; }
  .page { box-shadow: none !important; border: none !important; margin: 0 !important; padding: 6px 10px !important; width: 100% !important; page-break-after: always !important; page-break-inside: avoid !important; break-inside: avoid !important; height: 98vh !important; overflow: hidden !important; zoom: 0.70; }
  .page:last-child { page-break-after: avoid !important; break-after: avoid !important; }
  table, tr, td, th { page-break-inside: avoid !important; break-inside: avoid !important; }
}"""
    head_html = re.sub(r'@page\s*\{[^}]*\}\s*@media print\s*\{[\s\S]*?\}', print_css, head_html)
    
    body = content[head_match.end():]
    body = re.sub(r'</div>\s*</div>\s*</div>\s*</body>[\s\S]*$', '', body)
    
    # Split by <div class="header-top"> or <div class="ph">
    sections = re.split(r'(?=<div class=["\'](?:header-top|ph)["\'])', body)
    sections = [s.strip() for s in sections if s.strip()]
    
    page_blocks = []
    for s in sections:
        # Wrap each section cleanly inside <div class="page">
        # Remove any residual outer <div class="page"> tag
        s_clean = re.sub(r'^<div class=["\']page["\']>\s*', '', s)
        s_clean = re.sub(r'</div>\s*$', '', s_clean)
        page_blocks.append(f'<div class="page">\n{s_clean.strip()}\n</div>')
        
    tail = "</div>\n</div>\n</div>\n</body>\n</html>"
    new_doc = head_html + "\n\n" + "\n\n".join(page_blocks) + "\n\n" + tail
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_doc)
        
    print(f"Fixed {filename}: created {len(page_blocks)} page blocks.")

print("=== FIX 5 TOPICS COMPLETE ===")

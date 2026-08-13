import os
import glob
import re

topics_to_fix = [
    'Topic06_LinkedList.html',
    'Topic07_Stack.html',
    'Topic09_Heap.html',
    'Topic12_Graphs.html',
    'Topic13_Backtracking.html'
]

for filename in topics_to_fix:
    filepath = os.path.join('F:/dsa/bookfinal', filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract head (before main-content) and tail
    head_match = re.search(r'([\s\S]*?<div class="main-content">)', content)
    if not head_match:
        continue
    head_html = head_match.group(1)
    
    # Set zoom to 0.68 for perfect 6-page fit
    head_html = re.sub(r'zoom:\s*0\.\d+;', 'zoom: 0.68;', head_html)
    
    body_html = content[len(head_html):]
    body_html = re.sub(r'</div>\s*</div>\s*</div>\s*</body>[\s\S]*$', '', body_html)
    
    # Strip all <div class="page"> and </div> wrappers from body
    # We strip page wrapper divs to get raw boxes and headers
    raw_blocks = re.findall(r'(<div class=["\']ph["\'].*?>[\s\S]*?</div>|<div class=["\']g[23]["\'].*?>[\s\S]*?</div>\s*</div>|<div class=["\']prow["\'].*?>[\s\S]*?</div>\s*</div>|<div class=["\']box[^"\']*["\'].*?>[\s\S]*?</div>\s*</div>|<div class=["\']prob["\'].*?>[\s\S]*?</div>\s*</div>)', body_html)
    
    if not raw_blocks:
        # Fallback: split by ph (page header)
        raw_blocks = body_html.split('<div class="ph">')
        
    # Group raw_blocks into 6 pages
    import math
    chunk_size = math.ceil(len(raw_blocks) / 6)
    grouped = []
    for c in range(0, len(raw_blocks), chunk_size):
        group = raw_blocks[c:c+chunk_size]
        grouped.append(group)
        
    while len(grouped) > 6:
        last = grouped.pop()
        grouped[-1].extend(last)
        
    final_pages = []
    for idx, grp in enumerate(grouped):
        page_content = "\n".join(grp)
        # Update page number text
        page_content = re.sub(r'PAGE \d+ OF \d+', f'PAGE {idx+1} OF 6', page_content)
        final_pages.append(f'<div class="page">\n{page_content.strip()}\n</div>')
        
    tail = "</div>\n</div>\n</div>\n</body>\n</html>"
    new_doc = head_html + "\n\n" + "\n\n".join(final_pages) + "\n\n" + tail
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_doc)
        
    print(f"Fixed {filename} to exact 6 dense pages.")

print("=== EXACT 6 PAGES REFACTOR COMPLETE ===")

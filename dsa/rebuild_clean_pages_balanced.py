import os
import glob
import re

files_to_clean = [
    'Topic06_LinkedList.html',
    'Topic07_Stack.html',
    'Topic09_Heap.html',
    'Topic12_Graphs.html',
    'Topic13_Backtracking.html'
]

for filename in files_to_clean:
    filepath = os.path.join('F:/dsa/bookfinal', filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # Get header before body
    head_match = re.search(r'([\s\S]*?<div class="main-content">)', text)
    if not head_match:
        continue
    head_html = head_match.group(1)
    
    # Ensure zoom is 0.70
    head_html = re.sub(r'zoom:\s*0\.\d+;', 'zoom: 0.70;', head_html)
    
    body = text[len(head_html):]
    body = re.sub(r'</div>\s*</div>\s*</div>\s*</body>[\s\S]*$', '', body)
    
    # Strip any broken <div class="page"> and <div class="ph"> wrappers
    body_clean = re.sub(r'<div class=["\']page["\']>\s*', '', body)
    body_clean = re.sub(r'</div>\s*<!-- PAGE \d+ OF \d+ -->', '', body_clean)
    
    # Extract all top-level boxes (.g2, .g3, .prow, .box, .prob)
    boxes = re.findall(r'(<div class=["\'](?:g[23]|prow|box|prob)[^"\']*["\'].*?>[\s\S]*?</div>\s*</div>)', body_clean)
    if not boxes:
        # Fallback split
        boxes = [b for b in body_clean.split('<div class=') if b.strip()]
        boxes = ['<div class=' + b for b in boxes]
        
    print(f"{filename}: Extracted {len(boxes)} clean boxes.")
    
    # Group boxes into 6 pages
    import math
    chunk_size = math.ceil(len(boxes) / 6)
    grouped = []
    for c in range(0, len(boxes), chunk_size):
        group = boxes[c:c+chunk_size]
        grouped.append(group)
        
    while len(grouped) > 6:
        last = grouped.pop()
        grouped[-1].extend(last)
        
    page_htmls = []
    for idx, grp in enumerate(grouped):
        header_text = f'<div class="ph"><div><h1>{filename.split("_")[1].replace(".html","").upper()}</h1><div class="sub">FAANG Master Guide — Java Edition</div></div><div style="text-align:right"><div class="pn">PAGE {idx+1} OF 6</div><div class="ptag">FAANG DSA HANDBOOK</div></div></div>'
        page_body = "\n".join(grp)
        page_htmls.append(f'<div class="page">\n{header_text}\n{page_body}\n</div>')
        
    tail = "</div>\n</div>\n</div>\n</body>\n</html>"
    new_doc = head_html + "\n\n" + "\n\n".join(page_htmls) + "\n\n" + tail
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_doc)
        
    print(f"-> Successfully rebuilt {filename} into 6 clean A4 pages.")

print("=== REBUILD CLEAN PAGES BALANCED COMPLETE ===")

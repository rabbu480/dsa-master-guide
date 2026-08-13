import os
import glob
import re
import math

files_to_merge = [
    'Topic06_LinkedList.html',
    'Topic07_Stack.html',
    'Topic09_Heap.html',
    'Topic12_Graphs.html',
    'Topic13_Backtracking.html'
]

for filename in files_to_merge:
    filepath = os.path.join('F:/dsa/bookfinal', filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    head_match = re.search(r'([\s\S]*?<div class="main-content">)', content)
    if not head_match:
        continue
    head_html = head_match.group(1)
    
    # Extract existing <div class="page">...</div> blocks
    pages = re.findall(r'<div class=["\']page["\']>\s*([\s\S]*?)\s*</div>', content)
    if not pages:
        continue
        
    print(f"{filename}: Found {len(pages)} pages to merge into 6.")
    
    # Merge 9 pages into 6 pages
    chunk_size = math.ceil(len(pages) / 6)
    grouped = []
    for c in range(0, len(pages), chunk_size):
        group = pages[c:c+chunk_size]
        grouped.append(group)
        
    while len(grouped) > 6:
        last = grouped.pop()
        grouped[-1].extend(last)
        
    final_pages = []
    for idx, grp in enumerate(grouped):
        combined = ""
        for inner_idx, p in enumerate(grp):
            if inner_idx > 0:
                # Remove header top or ph from secondary merged pages
                p_clean = re.sub(r'<div class=["\'](?:header-top|ph)["\'].*?>[\s\S]*?</div>', '', p)
                combined += "\n" + p_clean
            else:
                combined += "\n" + p
                
        # Re-index page header: PAGE X OF 6
        combined = re.sub(r'PAGE \d+ OF \d+', f'PAGE {idx+1} OF 6', combined)
        final_pages.append(f'<div class="page">\n{combined.strip()}\n</div>')
        
    tail = "</div>\n</div>\n</div>\n</body>\n</html>"
    new_doc = head_html + "\n\n" + "\n\n".join(final_pages) + "\n\n" + tail
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_doc)
        
    print(f"-> Merged {filename} into {len(final_pages)} dense pages.")

print("=== CONSOLIDATION TO 6 PAGES COMPLETE ===")

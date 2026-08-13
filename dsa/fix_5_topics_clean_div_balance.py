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

    # Extract head
    head_match = re.search(r'([\s\S]*?<div class="main-content">)', content)
    if not head_match:
        continue
    head_html = head_match.group(1)
    
    body = content[head_match.end():]
    body = re.sub(r'</div>\s*</div>\s*</div>\s*</body>[\s\S]*$', '', body)
    
    # Clean out any existing <div class="page"> or closing divs wrapping pages
    body_clean = re.sub(r'<div class=["\']page["\']>\s*', '', body)
    
    # Split into sections using header-top or ph
    raw_sections = re.split(r'(?=<div class=["\'](?:header-top|ph)["\'])', body_clean)
    raw_sections = [s.strip() for s in raw_sections if s.strip()]
    
    # Let's balance div tags in each section
    balanced_pages = []
    for idx, sec in enumerate(raw_sections):
        # Count open vs close divs
        open_divs = len(re.findall(r'<div\b', sec))
        close_divs = len(re.findall(r'</div>', sec))
        diff = open_divs - close_divs
        
        # If open > close, append missing </div>
        sec_fixed = sec
        if diff > 0:
            sec_fixed += "\n" + ("</div>\n" * diff)
        elif diff < 0:
            # Strip extra </div> from end
            for _ in range(-diff):
                sec_fixed = re.sub(r'</div>\s*$', '', sec_fixed.strip())
                
        page_html = f'<div class="page">\n{sec_fixed.strip()}\n</div>'
        balanced_pages.append(page_html)
        
    tail = "</div>\n</div>\n</div>\n</body>\n</html>"
    new_doc = head_html + "\n\n" + "\n\n".join(balanced_pages) + "\n\n" + tail
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_doc)
        
    print(f"Balanced div tags for {filename}: created {len(balanced_pages)} pages.")

print("=== DIV BALANCE FIX COMPLETE ===")

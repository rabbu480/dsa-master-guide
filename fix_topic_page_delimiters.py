import os
import glob
import re

files_to_format = [
    'Topic06_LinkedList.html',
    'Topic07_Stack.html',
    'Topic09_Heap.html',
    'Topic12_Graphs.html',
    'Topic13_Backtracking.html'
]

for filename in files_to_format:
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
    
    # Split by <div class="ph">
    ph_sections = body.split('<div class="ph">')
    ph_sections = [s.strip() for s in ph_sections if s.strip()]
    
    formatted_pages = []
    for idx, sec in enumerate(ph_sections):
        # Strip trailing </div> if present at end of page block
        sec_clean = re.sub(r'</div>\s*$', '', sec).strip()
        # Ensure page starts with <div class="page"> and ends with </div>
        page_html = f'<div class="page">\n<div class="ph">{sec_clean}\n</div>\n</div>'
        formatted_pages.append(page_html)
        
    tail = "</div>\n</div>\n</div>\n</body>\n</html>"
    new_doc = head_html + "\n\n" + "\n\n".join(formatted_pages) + "\n\n" + tail
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_doc)
        
    print(f"Formatted {filename} into {len(formatted_pages)} top-level page divs.")

print("=== TOP LEVEL PAGE DIVS FORMATTED WITH CLOSING TAGS ===")

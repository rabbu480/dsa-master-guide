import os
import glob
import re

topics = [
    'Topic06_LinkedList.html',
    'Topic07_Stack.html',
    'Topic09_Heap.html',
    'Topic12_Graphs.html',
    'Topic13_Backtracking.html'
]

for filename in topics:
    filepath = os.path.join('F:/dsa/bookfinal', filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find header before main-content
    head_match = re.search(r'([\s\S]*?<div class="main-content">)', content)
    if not head_match:
        continue
    head_html = head_match.group(1)
    
    # Ensure zoom is 0.70
    head_html = re.sub(r'zoom:\s*0\.\d+;', 'zoom: 0.70;', head_html)
    
    body = content[len(head_html):]
    body = re.sub(r'</div>\s*</div>\s*</div>\s*</body>[\s\S]*$', '', body)
    
    # Split body by <div class="ph">
    ph_blocks = body.split('<div class="ph">')
    ph_blocks = [b.strip() for b in ph_blocks if b.strip()]
    
    pages_html = []
    for idx, b in enumerate(ph_blocks):
        full_block = '<div class="ph">' + b
        # Update page number to PAGE (idx+1) OF N
        full_block = re.sub(r'PAGE \d+ OF \d+', f'PAGE {idx+1} OF {len(ph_blocks)}', full_block)
        pages_html.append(f'<div class="page">\n{full_block}\n</div>')
        
    tail = "</div>\n</div>\n</div>\n</body>\n</html>"
    new_doc = head_html + "\n\n" + "\n\n".join(pages_html) + "\n\n" + tail
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_doc)
        
    print(f"Rebuilt {filename}: generated {len(pages_html)} clean page blocks.")

print("=== REBUILD COMPLETE ===")

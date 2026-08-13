import os
import glob
import re

files_to_process = [
    'Topic06_LinkedList.html',
    'Topic07_Stack.html',
    'Topic08_Queue_Deque.html',
    'Topic09_Heap.html',
    'Topic10_Trees.html',
    'Topic11_Trie.html',
    'Topic12_Graphs.html',
    'Topic13_Backtracking.html',
    'Topic14_DynamicProgramming.html',
    'Topic15_Greedy.html',
    'Topic16_Intervals.html',
    'Topic17_BitManipulation.html',
    'Topic18_Math.html',
    'Topic19_AdvancedDS.html'
]

def consolidate_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by <div class="page">
    parts = re.split(r'(<div class=["\']page["\'].*?>)', content)
    if len(parts) <= 1:
        return
    
    header_html = parts[0]
    page_blocks = []
    
    for i in range(1, len(parts), 2):
        tag = parts[i]
        body = parts[i+1]
        # Find matching closing div for page
        page_blocks.append(tag + body)
        
    print(f"File {os.path.basename(filepath)} has {len(page_blocks)} page blocks.")
    
    # We want to merge these into 6 dense pages if > 6
    if len(page_blocks) > 6:
        # Group into 6 chunks
        import math
        chunk_size = math.ceil(len(page_blocks) / 6)
        grouped = []
        for c in range(0, len(page_blocks), chunk_size):
            group = page_blocks[c:c+chunk_size]
            grouped.append(group)
            
        while len(grouped) > 6:
            last = grouped.pop()
            grouped[-1].extend(last)
            
        final_pages = []
        for idx, grp in enumerate(grouped):
            combined_body = ""
            for inner_idx, p_str in enumerate(grp):
                # Extract inner content from <div class="page">...</div>
                inner_content = re.sub(r'^<div class=["\']page["\'].*?>', '', p_str, flags=re.DOTALL)
                # Remove ending </div> from the page wrapper if present at end
                inner_content = re.sub(r'</div>\s*$', '', inner_content.strip(), flags=re.DOTALL)
                
                if inner_idx > 0:
                    # Strip page header from secondary merged sub-pages
                    inner_content = re.sub(r'<div class=["\']ph["\'].*?>[\s\S]*?</div>', '', inner_content)
                combined_body += "\n" + inner_content
                
            # Re-index header in first page of group
            combined_body = re.sub(r'PAGE \d+ OF \d+', f'PAGE {idx+1} OF 6', combined_body)
            final_pages.append(f'<div class="page">\n{combined_body.strip()}\n</div>')
            
        # Re-assemble document
        # Get head before first page and tail after last page
        main_content_head = header_html
        tail = "</div>\n</div>\n</div>\n</body>\n</html>"
        
        new_doc = main_content_head + "\n\n" + "\n\n".join(final_pages) + "\n\n" + tail
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_doc)
        print(f"-> Consolidated {os.path.basename(filepath)} to 6 pages.")

for f in files_to_process:
    consolidate_file(os.path.join('F:/dsa/bookfinal', f))

print("=== ALL REMAINING TOPICS CONSOLIDATED TO 6 DENSE A4 PAGES ===")

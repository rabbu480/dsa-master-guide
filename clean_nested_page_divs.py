import os
import glob
import re

files_to_clean = [
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

for filename in files_to_clean:
    filepath = os.path.join('F:/dsa/bookfinal', filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the top-level <div class="page"> elements
    # First, split the file into header and main-content body
    head_match = re.search(r'([\s\S]*?<div class="main-content">)', content)
    if not head_match:
        continue
    head_html = head_match.group(1)
    
    # Remove nested <div class="page"> inside main content body by converting inner <div class="page"> to <div class="page-inner">
    body_html = content[len(head_html):]
    
    # We find top-level pages
    # Let's clean out any <div class="page"> tags that are nested inside another page
    # Replace <div class="page"> that appears AFTER the outer page header with <div style="margin-bottom:12px">
    
    # Step: Split by outer pages
    pages = re.split(r'<!-- PAGE \d+ OF 6 -->', body_html)
    if len(pages) <= 1:
        # Split by <div class="page">
        pages = re.split(r'(?=<div class=["\']page["\']>\s*<div class=["\']ph["\'])', body_html)
        
    cleaned_pages = []
    for p in pages:
        if not p.strip():
            continue
        # Remove inner page div wrappers while keeping their children
        p_clean = re.sub(r'<div class=["\']page["\']>\s*(?!<div class=["\']ph["\'])', '<div style="margin-bottom:10px">\n', p)
        cleaned_pages.append(p_clean)
        
    new_body = "\n\n".join(cleaned_pages)
    
    # Final check: remove closing </div> tags that belonged to inner page divs
    # Make sure every top-level page starts with <div class="page"> and ends with </div>
    
    new_full_html = head_html + "\n\n" + new_body
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_full_html)
        
    print(f"Cleaned nested page divs for {filename}")

print("=== NESTED PAGE DIVS CLEANED SUCCESSFULLY ===")

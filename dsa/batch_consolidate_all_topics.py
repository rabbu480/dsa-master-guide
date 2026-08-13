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

print("=== STARTING BATCH A4 CONSOLIDATION ===")

for filename in files_to_process:
    filepath = os.path.join('F:/dsa/bookfinal', filename)
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update CSS font size & line-height slightly for dense packing
    content = re.sub(r'body\s*\{[^}]*font-size:[^;]*;[^}]*\}', "body { font-family: 'Inter', sans-serif; background: #e2e8f0; color: var(--txt); font-size: 11px; line-height: 1.35; padding: 20px; }", content)
    content = re.sub(r'\.page\s*\{[^}]*padding:[^;]*;[^}]*\}', "page { background: white; max-width: 1100px; margin: 0 auto 30px auto; padding: 14px 18px; border-radius: 8px; box-shadow: 0 8px 24px rgba(0,0,0,0.10); page-break-after: always; page-break-inside: avoid; }", content)
    content = re.sub(r'pre\s*\{[^}]*font-size:[^;]*;[^}]*\}', "pre { background: #f1f5f9; border: 1px solid #e2e8f0; border-radius: 4px; padding: 4px 6px; font-size: 0.68rem; line-height: 1.35; overflow-x: hidden; white-space: pre-wrap; word-break: break-all; }", content)
    content = re.sub(r'table\s*\{[^}]*font-size:[^;]*;[^}]*\}', "table { width: 100%; border-collapse: collapse; font-size: 0.72rem; }", content)

    # Extract all page blocks
    pages = re.findall(r'<div class=["\']page["\'].*?>([\s\S]*?)</div>\s*(?=<!-- =* -->|<div class=["\']page["\']|</body>)', content)
    if not pages:
        print(f"Skipping {filename}: pages not matched cleanly")
        continue
    
    print(f"Processing {filename}: Found {len(pages)} original pages.")

    # Combine pages if total_pages > 6 by merging page contents
    if len(pages) > 6:
        # Group pages into 6 dense pages
        new_pages = []
        num_orig = len(pages)
        # Determine grouping indices
        # E.g. for 10 pages -> group into 6 pages: [0,1], [2,3], [4,5], [6,7], [8], [9] or balanced
        import math
        chunk_size = math.ceil(num_orig / 6)
        
        grouped_contents = []
        for i in range(0, num_orig, chunk_size):
            group = pages[i:i+chunk_size]
            # Strip headers from non-first subpages in group
            combined_inner = ""
            for idx, p in enumerate(group):
                if idx > 0:
                    # Remove page header (.ph) from subsequent merged pages
                    p_clean = re.sub(r'<div class=["\']ph["\'].*?>[\s\S]*?</div>', '', p)
                    combined_inner += p_clean
                else:
                    combined_inner += p
            grouped_contents.append(combined_inner)
            
        # Guarantee exactly 6 pages if grouping produced less
        while len(grouped_contents) > 6:
            # Merge last two
            last = grouped_contents.pop()
            grouped_contents[-1] += last
            
        # Re-index page numbers in headers (PAGE X OF 6)
        final_pages_html = []
        for p_idx, p_content in enumerate(grouped_contents):
            # Replace PAGE X OF Y with PAGE (p_idx+1) OF 6
            p_content_indexed = re.sub(r'PAGE \d+ OF \d+', f'PAGE {p_idx+1} OF 6', p_content)
            # Wrap in <div class="page">
            page_div = f'<div class="page">\n{p_content_indexed.strip()}\n</div>'
            final_pages_html.append(page_div)
            
        # Reconstruct HTML file
        head_match = re.search(r'([\s\S]*?<div class="main-content">)', content)
        tail_match = re.search(r'(</div>\s*</div>\s*</div>\s*</body>[\s\S]*)', content)
        
        if head_match and tail_match:
            new_full_html = head_match.group(1) + "\n\n" + "\n\n".join(final_pages_html) + "\n\n" + tail_match.group(1)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_full_html)
            print(f"Successfully consolidated {filename} into 6 dense A4 pages.")

print("=== BATCH CONSOLIDATION COMPLETE ===")

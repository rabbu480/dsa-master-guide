import os
import glob
import re

files = sorted(glob.glob('F:/dsa/bookfinal/Topic*.html'))

for filepath in files:
    if 'Topic01_' in filepath or 'Topic02_' in filepath:
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find main-content start
    head_match = re.search(r'([\s\S]*?<div class="main-content">)', content)
    if not head_match:
        continue
    head_html = head_match.group(1)
    body = content[head_match.end():]
    body = re.sub(r'</div>\s*</div>\s*</div>\s*</body>[\s\S]*$', '', body)

    # Extract all <div class="page">...</div> blocks
    pages = re.findall(r'<div class=["\']page["\']>\s*([\s\S]*?)\s*</div>', body)
    if not pages:
        continue

    # Merge into 6 pages if count > 6
    if len(pages) > 6:
        # Group into 6 chunks
        chunk_size = (len(pages) + 5) // 6
        grouped = []
        for i in range(0, len(pages), chunk_size):
            grouped.append(pages[i:i+chunk_size])
        while len(grouped) > 6:
            last = grouped.pop()
            grouped[-1].extend(last)

        new_pages = []
        for idx, grp in enumerate(grouped):
            combined = ""
            for inner_idx, p in enumerate(grp):
                if inner_idx > 0:
                    # Strip ph from secondary merged sub-pages
                    p_clean = re.sub(r'<div class=["\']ph["\'].*?>[\s\S]*?</div>', '', p)
                    combined += "\n" + p_clean
                else:
                    combined += "\n" + p
            # Update page number header
            combined = re.sub(r'PAGE \d+ OF \d+', f'PAGE {idx+1} OF 6', combined)
            new_pages.append(f'<div class="page">\n{combined.strip()}\n</div>')

        tail = "</div>\n</div>\n</div>\n</body>\n</html>"
        new_doc = head_html + "\n\n" + "\n\n".join(new_pages) + "\n\n" + tail
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_doc)
        print(f"Refactored {os.path.basename(filepath)} from {len(pages)} to {len(new_pages)} pages.")

print("=== REFACTORED ALL TOPICS TO 6 PAGES ===")

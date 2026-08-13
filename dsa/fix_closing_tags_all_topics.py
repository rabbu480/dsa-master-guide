import os
import glob
import re

files_to_fix = sorted(glob.glob('F:/dsa/bookfinal/Topic*.html'))

for filepath in files_to_fix:
    if 'Topic01_' in filepath or 'Topic02_' in filepath:
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if page divs are properly closed
    # Count open vs close
    open_count = len(re.findall(r'<div class=["\']page["\']', content))
    
    # If the file has page blocks, let's ensure each page block has a closing </div> before the next page block!
    # Split by <div class="page">
    parts = content.split('<div class="page">')
    head = parts[0]
    pages = parts[1:]

    fixed_pages = []
    for p in pages:
        # Check inside this page block before </div></div></div></body>
        p_clean = re.sub(r'</div>\s*</div>\s*</div>\s*</body>[\s\S]*$', '', p)
        # Ensure it ends with </div> for <div class="page">
        # Let's count open divs and close divs in p_clean
        open_divs = len(re.findall(r'<div\b', p_clean))
        close_divs = len(re.findall(r'</div>', p_clean))
        diff = open_divs - close_divs
        if diff > 0:
            p_clean += "\n" + ("</div>\n" * diff)
        elif diff < 0:
            for _ in range(-diff):
                p_clean = re.sub(r'</div>\s*$', '', p_clean.strip())
        fixed_pages.append('<div class="page">\n' + p_clean.strip() + '\n</div>')

    tail = "</div>\n</div>\n</div>\n</body>\n</html>"
    new_doc = head + "\n\n" + "\n\n".join(fixed_pages) + "\n\n" + tail
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_doc)
    print(f"Fixed closing tags for {os.path.basename(filepath)}: {len(fixed_pages)} pages.")

print("=== FIX CLOSING TAGS COMPLETE ===")

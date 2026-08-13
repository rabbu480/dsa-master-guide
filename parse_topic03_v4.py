import re, os

v4_file = r"F:\dsa\bookfinal - Copy\v4\bookfinal\Topic03_TwoPointers.html"
with open(v4_file, "r", encoding="utf-8") as f:
    html = f.read()

# Extract CSS header (everything before first <div class="page">)
header_end = html.find('<div class="page">')
css_header = html[:header_end]

# Extract all <div class="page">...</div> blocks
raw_pages = []
pos = header_end
while True:
    start = html.find('<div class="page">', pos)
    if start == -1:
        break
    # Find matching </div> for page. Since pages end with </div> before next <!-- PAGE or </div>\n</div>,
    # let's locate the page content
    next_start = html.find('<div class="page">', start + 18)
    if next_start != -1:
        page_content = html[start:next_start]
        pos = next_start
    else:
        # last page
        end_app = html.find('</div>\n</div>\n</div>\n</body>', start)
        if end_app == -1: end_app = html.find('</body>', start)
        page_content = html[start:end_app]
        pos = len(html)
    
    # strip <div class="page"> and trailing </div>s
    # remove <div class="ph">...</div> header block inside
    ph_end = page_content.find('</div>\n</div>', page_content.find('<div class="ph">'))
    if ph_end != -1:
        body_inner = page_content[ph_end+12:].strip()
    else:
        body_inner = page_content.strip()
    
    # clean up trailing closing divs
    body_inner = re.sub(r'</div>\s*$', '', body_inner).strip()
    raw_pages.append(body_inner)

print(f"Extracted {len(raw_pages)} page bodies.")
for i, p in enumerate(raw_pages, 1):
    print(f"--- Page {i} ({len(p)} chars) ---")
    print(p[:150].replace('\n', ' '))

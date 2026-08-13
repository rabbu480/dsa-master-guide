import re, os, sys

sys.stdout.reconfigure(encoding='utf-8')

v4_file = r"F:\dsa\bookfinal - Copy\v4\bookfinal\Topic03_TwoPointers.html"
with open(v4_file, "r", encoding="utf-8") as f:
    html = f.read()

# Split by <!-- PAGE
pages_raw = re.split(r'<!-- PAGE \d+:', html)[1:]

print(f"Found {len(pages_raw)} sections split by comment.")

pages_inner = []
for i, p_str in enumerate(pages_raw, 1):
    # Find page header
    comment_title = p_str[:p_str.find('-->')].strip()
    
    # Extract inner content between <div class="ph">...</div> and end of page div
    ph_end = p_str.find('</div>\n</div>')
    if ph_end == -1: ph_end = p_str.find('</div></div>')
    
    # Body starts after ph_end
    body = p_str[ph_end+12:] if ph_end != -1 else p_str
    
    # Remove trailing </div>\n</div> at end of page
    body = re.sub(r'</div>\s*</div>\s*$', '', body).strip()
    pages_inner.append((comment_title, body))
    print(f"Page {i:2d}: [{comment_title}] -> {len(body)} chars")


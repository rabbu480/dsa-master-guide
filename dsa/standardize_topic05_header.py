import re

filepath = 'F:/dsa/bookfinal/Topic05_BinarySearch.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Add .ph style into <style> if missing
ph_css = """
.ph { display:flex; justify-content:space-between; align-items:center; border-bottom: 3px solid var(--primary); padding-bottom: 6px; margin-bottom: 10px; }
.ph h1 { font-size: 1.5rem; font-weight: 900; color: var(--primary); letter-spacing: 0.5px; margin:0; }
.ph .sub { font-size: 0.82rem; font-weight: 600; color: #475569; margin-top: 2px; }
.ph .pn { background: var(--primary); color: white; padding: 3px 12px; border-radius: 16px; font-weight: 800; font-size: 0.85rem; text-align: right; }
.ph .ptag { font-size: 0.72rem; color: #475569; font-weight: 600; margin-top: 3px; }
"""

if '.ph {' not in content:
    content = content.replace('</style>', ph_css + '\n</style>')

# Replace <div class="header-top"...> blocks with <div class="ph">
def replace_header(match):
    full = match.group(0)
    title_match = re.search(r'<h1>(.*?)</h1>', full)
    page_match = re.search(r'PAGE (\d+) OF (\d+)', full)
    
    title = title_match.group(1) if title_match else "BINARY SEARCH MASTERCLASS"
    curr_p = page_match.group(1) if page_match else "1"
    total_p = page_match.group(2) if page_match else "10"
    
    return f"""<div class="ph">
    <div><h1>{title}</h1><div class="sub">FAANG Master Guide — Binary Search</div></div>
    <div style="text-align:right"><div class="pn">PAGE {curr_p} OF {total_p}</div><div class="ptag">BINARY SEARCH · TEMPLATES · NEETCODE</div></div>
</div>"""

pattern = r'<div class="header-top"[^>]*>.*?</div>'
content = re.sub(pattern, replace_header, content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Standardized Topic 05 page headers to .ph pattern successfully!")

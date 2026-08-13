import glob
import os
import re

html_files = sorted(glob.glob("F:/dsa/bookfinal/*.html"))

fixed_count = 0
for filepath in html_files:
    fname = os.path.basename(filepath)
    if fname == "index.html":
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    orig = content
    
    # 1. Ensure .page CSS has min-height: auto and clean margin/padding
    # Fix any residual min-height: 960px or 1000px
    content = re.sub(r'min-height\s*:\s*\d+px\s*;?', 'min-height: auto;', content)
    
    # 2. Fix flex vertical stretch inside .page
    content = re.sub(r'justify-content\s*:\s*space-between\s*;?', '', content)
    
    # 3. Ensure @media print has page-break-after: always
    if '@media print' in content:
        content = re.sub(r'@media print\s*\{([^}]+)\}', 
                         lambda m: m.group(0).replace('zoom: 0.81;', 'zoom: 0.72;'), content)
    
    if content != orig:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        fixed_count += 1
        print(f"Refined styling in {fname}")

print(f"Total HTML files refined: {fixed_count}")

import glob
import os
import re

files = sorted(glob.glob('F:/dsa/bookfinal/*.html'))
print(f"Total HTML files: {len(files)}")
print("-" * 65)

for f in files:
    size_kb = os.path.getsize(f) / 1024
    with open(f, 'r', encoding='utf-8') as fp:
        html = fp.read()
    
    pages = len(re.findall(r'<div class="page"', html))
    boxes = len(re.findall(r'class="section-box', html))
    code_blocks = len(re.findall(r'<pre>', html))
    
    print(f"{os.path.basename(f):38s} | {pages:2d} pages | {boxes:2d} boxes | {code_blocks:2d} code | {size_kb:6.1f} KB")

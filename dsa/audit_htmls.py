import glob
import os
import re

files = sorted(glob.glob("F:/dsa/bookfinal/*.html"))
print(f"{'Filename':38s} | {'Size KB':7s} | {'Pages':6s} | {'Mermaid':7s} | {'Code':6s}")
print("-" * 75)
for f in files:
    name = os.path.basename(f)
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        html = fp.read()
    pages = len(re.findall(r'class=["\']page["\']', html))
    size_kb = round(os.path.getsize(f) / 1024, 1)
    has_mermaid = 'mermaid' in html
    has_code = '<code>' in html or '<pre>' in html
    print(f"{name:38s} | {size_kb:6.1f} KB | {pages:5d}  | {str(has_mermaid):7s} | {str(has_code)}")

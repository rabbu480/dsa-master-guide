import os
import glob
import re

html_files = sorted(glob.glob('F:/dsa/bookfinal/*.html'))

print(f"=== HANDBOOK PAGE DENSITY & STRUCTURE SWEEP ===")
print(f"{'Filename':<36} | {'Pages':<6} | {'Boxes/Tables per Page (Avg)':<30}")
print("-" * 75)

for filepath in html_files:
    filename = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    pages = re.findall(r'<div class=["\']page["\'].*?>([\s\S]*?)</div>\s*<!-- =* -->', content)
    if not pages:
        pages = re.findall(r'<div class=["\']page["\'].*?>([\s\S]*?)</div>', content)
    
    total_pages = len(pages)
    total_boxes = len(re.findall(r'class=["\'](?:box|section-box|prow|prob|aha|rule|rule-box)', content))
    avg_boxes = total_boxes / total_pages if total_pages > 0 else 0
    
    print(f"{filename:<36} | {total_pages:<6} | {avg_boxes:<30.1f}")

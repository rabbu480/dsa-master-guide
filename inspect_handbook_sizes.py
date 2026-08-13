import os
import glob
import re

html_files = sorted(glob.glob('F:/dsa/bookfinal/*.html'))

print(f"{'Filename':<36} | {'HTML Pages':<10} | {'Line Count':<10} | {'File Size (KB)':<12}")
print("-" * 75)

for filepath in html_files:
    filename = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    pages = len(re.findall(r'class=["\']page["\']', content))
    lines = len(content.splitlines())
    size_kb = len(content.encode('utf-8')) / 1024
    print(f"{filename:<36} | {pages:<10} | {lines:<10} | {size_kb:<12.1f}")

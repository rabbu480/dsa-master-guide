import glob
import os
import re

pdf_files = sorted(glob.glob('F:/dsa/bookfinal/*.pdf'))

print("=== FINAL FAANG DSA HANDBOOK PDF PAGE AUDIT ===")
total_pages = 0
for pdf_path in pdf_files:
    if 'FAANG_DSA_Master_Handbook.pdf' in pdf_path:
        continue
    with open(pdf_path, 'rb') as f:
        data = f.read()
    # Count /Type /Page
    n_pages = len(re.findall(rb'/Type\s*/Page\b', data))
    total_pages += n_pages
    print(f"{os.path.basename(pdf_path):<40} | PDF Pages: {n_pages:>2}")

print("-" * 55)
print(f"TOTAL MASTER HANDBOOK PAGES: {total_pages}")

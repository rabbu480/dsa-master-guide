import glob
import os
import re

try:
    import pypdf
except ImportError:
    import PyPDF2 as pypdf

bookfinal_dir = r"F:\dsa\bookfinal"
html_files = sorted(glob.glob(os.path.join(bookfinal_dir, "*.html")))

print(f"{'Filename':38s} | {'HTML Pages':10s} | {'PDF Pages':10s} | {'Status':15s}")
print("-" * 80)

mismatches = []
for html_file in html_files:
    fname = os.path.basename(html_file)
    if fname == "index.html":
        continue
    pdf_name = fname.replace(".html", ".pdf")
    pdf_path = os.path.join(bookfinal_dir, pdf_name)
    
    with open(html_file, 'r', encoding='utf-8') as fp:
        html_content = fp.read()
    
    html_page_count = len(re.findall(r'<div class="page"', html_content))
    
    pdf_page_count = 0
    if os.path.exists(pdf_path):
        reader = pypdf.PdfReader(pdf_path)
        pdf_page_count = len(reader.pages)
    
    status = "[OK] PERFECT" if html_page_count == pdf_page_count else "[FAIL] MISMATCH"
    print(f"{fname:38s} | {html_page_count:10d} | {pdf_page_count:10d} | {status:15s}")
    
    if html_page_count != pdf_page_count:
        mismatches.append((fname, html_page_count, pdf_page_count))

print("-" * 80)
print(f"Total files checked: {len(html_files) - 1}")
print(f"Perfect 1:1 page alignment: {len(html_files) - 1 - len(mismatches)}")
print(f"Mismatched / Overflow files: {len(mismatches)}")
if mismatches:
    print("\nDetailed Mismatches:")
    for fname, h_cnt, p_cnt in mismatches:
        print(f" - {fname}: HTML declared {h_cnt} pages, but PDF rendered {p_cnt} pages! ({p_cnt - h_cnt} spilled overflow pages)")

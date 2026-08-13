import glob
import os
import re
try:
    import pypdf
except ImportError:
    import PyPDF2 as pypdf

bookfinal_dir = r"F:\dsa\bookfinal"
html_files = sorted(glob.glob(os.path.join(bookfinal_dir, "*.html")))

print(f"{'Filename':38s} | {'Lines':6s} | {'HTML Pgs':8s} | {'PDF Pgs':8s} | {'Status':12s}")
print("-" * 80)

for filepath in html_files:
    fname = os.path.basename(filepath)
    pdf_name = fname.replace(".html", ".pdf")
    pdf_path = os.path.join(bookfinal_dir, pdf_name)

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    line_count = len(content.splitlines())
    html_pages = len(re.findall(r'<div class="page"', content))

    pdf_pages = 0
    if os.path.exists(pdf_path):
        reader = pypdf.PdfReader(pdf_path)
        pdf_pages = len(reader.pages)

    status = "OK" if html_pages == pdf_pages else "MISMATCH"
    print(f"{fname:38s} | {line_count:6d} | {html_pages:8d} | {pdf_pages:8d} | {status:12s}")

import os, glob, fitz, re

book_dir = r"F:\dsa\bookfinal"
html_files = sorted(glob.glob(os.path.join(book_dir, "Topic*.html")))

print(f"{'Filename':<35} | {'HTML .page divs':<15} | {'PDF Pages':<10}")
print("-" * 65)

for h in html_files:
    basename = os.path.basename(h)
    pdfname = h.replace(".html", ".pdf")
    
    with open(h, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    page_divs = len(re.findall(r'<div class=["\']page["\']', content))
    
    pdf_pages = "N/A"
    if os.path.exists(pdfname):
        try:
            doc = fitz.open(pdfname)
            pdf_pages = str(len(doc))
            doc.close()
        except Exception as e:
            pdf_pages = "Error"
            
    print(f"{basename:<35} | {page_divs:<15} | {pdf_pages:<10}")

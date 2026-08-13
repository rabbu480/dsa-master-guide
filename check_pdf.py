import fitz # PyMuPDF
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = "F:/dsa/bookfinal/Topic03_TwoPointers.pdf"
if len(sys.argv) > 1:
    pdf_path = sys.argv[1]

doc = fitz.open(pdf_path)

print(f"================ TOTAL PDF PAGES ({pdf_path}): {len(doc)} ================")

for i, page in enumerate(doc):
    text = page.get_text()
    first_line = text.split('\n')[0] if text else "EMPTY"
    print(f"Page {i+1}: {len(text)} chars | Start: {first_line[:60]}")

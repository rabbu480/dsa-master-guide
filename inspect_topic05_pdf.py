import PyPDF2
import sys

sys.stdout.reconfigure(encoding='utf-8')

reader = PyPDF2.PdfReader("F:/dsa/bookfinal/Topic05_BinarySearch.pdf")
print(f"Total pages in Topic05 PDF: {len(reader.pages)}")

for idx, page in enumerate(reader.pages):
    text = page.extract_text()
    first_line = text.split('\n')[0] if text else "EMPTY"
    print(f"Page {idx+1}: {first_line[:80]}")

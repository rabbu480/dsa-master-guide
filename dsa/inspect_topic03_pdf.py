import fitz

doc = fitz.open(r"F:\dsa\bookfinal\Topic03_TwoPointers.pdf")
print("Total pages in PDF:", len(doc))
for i in range(len(doc)):
    page = doc[i]
    text = page.get_text()
    t_clean = text[:60].replace('\n', ' ')
    print(f"Page {i+1} has {len(text)} chars: {t_clean}")
doc.close()

import fitz

doc = fitz.open(r"F:\dsa\bookfinal\Topic11_Trie.pdf")
print("Total pages in Topic11 PDF:", len(doc))
for i in range(len(doc)):
    page = doc[i]
    text = page.get_text()
    t_clean = text[:80].replace('\n', ' ')
    print(f"Page {i+1} has {len(text)} chars: {t_clean}")
doc.close()

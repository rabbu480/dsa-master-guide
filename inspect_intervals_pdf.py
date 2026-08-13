import PyPDF2

reader = PyPDF2.PdfReader('F:/dsa/bookfinal/Topic16_Intervals.pdf')
print('Topic16_Intervals.pdf rendered page count:', len(reader.pages))

for i, p in enumerate(reader.pages, 1):
    txt = p.extract_text()
    lines = [line.strip() for line in txt.split('\n') if line.strip()]
    page_tag = [l for l in lines if 'PAGE ' in l or 'Page ' in l]
    ascii_tag = [t.encode('ascii', 'ignore').decode('ascii') for t in page_tag]
    print(f"PDF Page {i:2d} | Tag: {ascii_tag}")

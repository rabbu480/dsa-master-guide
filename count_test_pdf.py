import fitz

d = fitz.open('F:/dsa/bookfinal/Topic03_test.pdf')
print(f"Topic03 test PDF pages: {len(d)}")
d.close()

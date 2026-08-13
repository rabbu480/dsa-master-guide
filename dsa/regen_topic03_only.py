import subprocess, os, fitz

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
if not os.path.exists(chrome_path):
    chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

html = 'F:/dsa/bookfinal/Topic03_TwoPointers.html'
pdf_out = 'F:/dsa/bookfinal/Topic03_TwoPointers.pdf'

# Delete old PDF first
if os.path.exists(pdf_out):
    os.remove(pdf_out)
    print("Deleted old PDF")

cmd = [
    chrome_path,
    '--headless',
    '--disable-gpu',
    '--no-pdf-header-footer',
    f'--print-to-pdf={pdf_out}',
    html
]
result = subprocess.run(cmd, check=True, capture_output=True, text=True)
print(f"Chrome stdout: {result.stdout}")
print(f"Chrome stderr: {result.stderr}")

if os.path.exists(pdf_out):
    d = fitz.open(pdf_out)
    print(f"PDF page count: {len(d)}")
    d.close()
else:
    print("ERROR: PDF not generated!")

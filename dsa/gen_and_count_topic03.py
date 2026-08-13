import subprocess, os, fitz

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
html = 'F:/dsa/bookfinal/Topic03_TwoPointers.html'
pdf_out = 'F:/dsa/bookfinal/Topic03_TwoPointers.pdf'

if os.path.exists(pdf_out):
    os.remove(pdf_out)

cmd = [chrome_path, '--headless', '--disable-gpu', '--no-pdf-header-footer', f'--print-to-pdf={pdf_out}', html]
result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)

if os.path.exists(pdf_out):
    d = fitz.open(pdf_out)
    print(f"Topic03 PDF pages: {len(d)}")
    d.close()
else:
    print("ERROR: PDF not generated!")
    print("stderr:", result.stderr[:500])

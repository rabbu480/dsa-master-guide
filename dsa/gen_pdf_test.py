import os
import subprocess

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
html_path = r"F:\dsa\bookfinal\Topic00_Orientation.html".replace("\\", "/")
pdf_path = r"F:\dsa\bookfinal\test_out.pdf"

cmd = [
    chrome,
    "--headless=new",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_path}",
    f"file:///{html_path}"
]

res = subprocess.run(cmd, capture_output=True, text=True)
print("Return code:", res.returncode)
print("PDF exists:", os.path.exists(pdf_path))
if os.path.exists(pdf_path):
    print("Size KB:", os.path.getsize(pdf_path) / 1024)

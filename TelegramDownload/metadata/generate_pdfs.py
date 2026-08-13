import os
import subprocess
import glob

v17_dir = r"C:\Users\rabba\Downloads\TelegramDownload\metadata\v17"
pdf_dir = r"C:\Users\rabba\Downloads\TelegramDownload\metadata\pdf_output"
os.makedirs(pdf_dir, exist_ok=True)

chrome_paths = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
]

browser_exe = None
for p in chrome_paths:
    if os.path.exists(p):
        browser_exe = p
        break

if not browser_exe:
    print("Could not find Chrome or Edge executable.")
    exit(1)

html_files = glob.glob(os.path.join(v17_dir, "*.html"))
for html_file in html_files:
    fname = os.path.basename(html_file)
    pdf_name = fname.replace(".html", ".pdf")
    pdf_path = os.path.join(pdf_dir, pdf_name)
    
    print(f"Generating PDF for {fname}...")
    safe_html_file = html_file.replace('\\', '/')
    cmd = [
        browser_exe,
        "--headless",
        "--disable-gpu",
        "--run-all-compositor-stages-before-draw",
        f"--print-to-pdf={pdf_path}",
        f"file:///{safe_html_file}"
    ]
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    if os.path.exists(pdf_path):
        print(f"[{os.path.getsize(pdf_path)//1024}KB] Created {pdf_name}")
    else:
        print(f"Failed to create {pdf_name}")

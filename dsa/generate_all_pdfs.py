import glob
import os
import subprocess

chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
bookfinal_dir = r"F:\dsa\bookfinal"

html_files = sorted(glob.glob(os.path.join(bookfinal_dir, "*.html")))

print(f"Generating PDFs for {len(html_files)} HTML files using Chrome headless...\n")

success_count = 0
for html_file in html_files:
    fname = os.path.basename(html_file)
    pdf_name = fname.replace(".html", ".pdf")
    pdf_path = os.path.join(bookfinal_dir, pdf_name)
    
    clean_path = html_file.replace("\\", "/")
    safe_html_url = f"file:///{clean_path}"
    
    cmd = [
        chrome_exe,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        safe_html_url
    ]
    
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(pdf_path):
        size_kb = round(os.path.getsize(pdf_path) / 1024, 1)
        print(f"[OK] [{size_kb:6.1f} KB] {pdf_name:40s}")
        success_count += 1
    else:
        print(f"[FAIL] Failed to generate {pdf_name}")

print(f"\nCompleted! Generated {success_count} / {len(html_files)} PDFs.")

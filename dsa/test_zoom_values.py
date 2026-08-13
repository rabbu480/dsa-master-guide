import re, subprocess, os, fitz, shutil

# Try different zoom values
for zoom in [0.43, 0.45, 0.47, 0.5]:
    shutil.copy(r'F:\dsa\bookfinal - Copy\v4\bookfinal\Topic03_TwoPointers.html',
                r'F:\dsa\bookfinal\Topic03_test_zoom.html')
    
    with open('F:/dsa/bookfinal/Topic03_test_zoom.html', 'rb') as f:
        raw = f.read()
    text = raw.decode('utf-8').replace('\r\n', '\n').replace('\r', '\n')

    # Remove even-page boundaries
    for page_num in [2, 4, 6, 8, 10]:
        pattern = re.compile(
            r'\n<!-- PAGE ' + str(page_num) + r'[^\n]*-->\n<div class="page">\n<div class="ph">[\s\S]*?</div>\n</div>',
            re.MULTILINE
        )
        text, _ = pattern.subn('', text)

    print_css = f"""\
@page {{ size: A4 portrait; margin: 4mm; }}
@media print {{
  body {{ background: white !important; padding: 0 !important; margin: 0 !important; color: black !important; -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }}
  .top-nav, .toc-sidebar {{ display: none !important; }}
  .app-layout {{ display: block !important; }}
  .page {{ box-shadow: none !important; border: none !important; margin: 0 !important; padding: 4px 8px !important; width: 100% !important; page-break-after: always !important; page-break-inside: avoid !important; break-inside: avoid !important; zoom: {zoom}; }}
  .page:last-child {{ page-break-after: avoid !important; break-after: avoid !important; }}
}}"""
    text = re.sub(r'@page\s*\{[^}]*\}[\s\S]*?(?=</style>)', print_css + '\n', text)

    with open('F:/dsa/bookfinal/Topic03_test_zoom.html', 'wb') as f:
        f.write(text.replace('\n', '\r\n').encode('utf-8'))

    chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    pdf_out = 'F:/dsa/bookfinal/Topic03_test_zoom.pdf'
    if os.path.exists(pdf_out):
        os.remove(pdf_out)
    cmd = [chrome_path, '--headless', '--disable-gpu', '--no-pdf-header-footer', f'--print-to-pdf={pdf_out}', 'F:/dsa/bookfinal/Topic03_test_zoom.html']
    subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    
    if os.path.exists(pdf_out):
        d = fitz.open(pdf_out)
        pages = len(d)
        d.close()
        print(f"zoom={zoom} -> {pages} PDF pages")
    else:
        print(f"zoom={zoom} -> FAILED")

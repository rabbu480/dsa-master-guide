import os, sys, subprocess, fitz

sys.stdout.reconfigure(encoding='utf-8')

html_file = r"F:\dsa\bookfinal\Topic11_Trie.html"
with open(html_file, "r", encoding="utf-8", errors="ignore") as f:
    html = f.read()

# Replace print_fit_css with zoom: 0.76 and padding adjustments
print_fit_css = """
@media print {
    body { background: white !important; padding: 0 !important; margin: 0 !important; color: black !important; -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
    .page {
        box-shadow: none !important;
        border: none !important;
        margin: 0 !important;
        padding: 6px 10px !important;
        width: 100% !important;
        page-break-after: always !important;
        break-after: page !important;
        page-break-inside: avoid !important;
        break-inside: avoid !important;
        min-height: auto !important;
        zoom: 0.76 !important;
    }
    .page:last-child { page-break-after: avoid !important; break-after: avoid !important; }
    pre {
        background: #f1f5f9 !important;
        color: #0b1a33 !important;
        border: 1px solid #cbd5e1 !important;
        font-family: 'JetBrains Mono', 'Fira Code', monospace !important;
        font-size: 0.66rem !important;
        line-height: 1.22 !important;
        padding: 4px 8px !important;
        white-space: pre-wrap !important;
    }
    .card-body { padding: 6px 10px 8px !important; }
    .aha-box { padding: 4px 8px !important; margin: 4px 0 !important; }
}
"""

style_end = html.find('</style>')
html_mod = html[:style_end] + print_fit_css + '\n' + html[style_end:]

with open(html_file, "w", encoding="utf-8") as f:
    f.write(html_mod)

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
pdf_out = r"F:\dsa\bookfinal\Topic11_Trie.pdf"

if os.path.exists(pdf_out): os.remove(pdf_out)

cmd = [chrome_path, '--headless', '--disable-gpu', '--no-pdf-header-footer', f'--print-to-pdf={pdf_out}', html_file]
subprocess.run(cmd, check=True)

doc = fitz.open(pdf_out)
print("==========================================")
print(f"Generated Topic 11 PDF Page Count: {len(doc)} pages")
print("==========================================")

for i in range(len(doc)):
    page = doc[i]
    text = page.get_text()
    t_clean = text[:70].replace('\n', ' ')
    print(f"Page {i+1} has {len(text)} chars: {t_clean}")

doc.close()

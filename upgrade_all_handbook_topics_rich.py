import re, os, sys, glob, subprocess, fitz

sys.stdout.reconfigure(encoding='utf-8')

book_dir = r"F:\dsa\bookfinal"
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

new_print_css = """
body { font-family: 'Inter', sans-serif; background: #e2e8f0; color: var(--txt); font-size: 10.5px; line-height: 1.34; padding: 15px; }

.page {
  background: white; max-width: 1100px; margin: 0 auto 20px auto;
  padding: 10px 14px; border-radius: 8px;
  box-shadow: 0 6px 20px rgba(0,0,0,0.08);
  page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;
}

.ph { display:flex; justify-content:space-between; align-items:center;
  border-bottom: 2.5px solid var(--pri); padding-bottom: 4px; margin-bottom: 8px; }
.ph h1 { font-size: 1.45rem; font-weight: 900; color: var(--pri); letter-spacing: 0.5px; }
.ph .sub { font-size: 0.8rem; font-weight: 600; color: var(--sub); margin-top: 1px; }
.ph .pn { background: var(--pri); color: white; padding: 2px 10px; border-radius: 12px;
  font-weight: 800; font-size: 0.78rem; text-align: right; }
.ph .ptag { font-size: 0.7rem; color: var(--sub); font-weight: 600; margin-top: 2px; }

.box { border: 1.5px solid var(--pri); border-radius: 6px; overflow: hidden; margin-bottom: 8px; background: white; }
.box.pur { border-color: var(--pur); }
.box.grn { border-color: var(--grn); }
.box.amb { border-color: var(--amb); }
.box.red { border-color: var(--red); }
.box.sky { border-color: var(--sky); }

.bh { background: var(--pri); color: white; padding: 4px 8px; font-weight: 800; font-size: 0.82rem; display: flex; justify-content: space-between; align-items: center; }
.box.pur .bh { background: var(--pur); }
.box.grn .bh { background: var(--grn); }
.box.amb .bh { background: var(--amb); }
.box.red .bh { background: var(--red); }
.box.sky .bh { background: var(--sky); }

.bc { padding: 6px 8px; font-size: 0.78rem; color: var(--txt); }

.prob-card { border: 1.5px solid var(--pri); border-radius: 6px; margin-bottom: 10px; background: white; overflow: hidden; }
.prob-header { background: #f1f5f9; padding: 6px 10px; border-bottom: 1.5px solid var(--bdr); display: flex; justify-content: space-between; align-items: center; }
.prob-title { font-weight: 800; font-size: 0.88rem; color: var(--pri); }
.prob-badge { background: var(--sec); color: white; padding: 2px 8px; border-radius: 10px; font-size: 0.72rem; font-weight: 700; }

.prob-body { padding: 8px 10px; }
.io-box { background: #f8fafc; border: 1px solid var(--bdr); border-left: 3.5px solid var(--sec); padding: 5px 8px; margin: 4px 0; border-radius: 4px; font-family: 'Fira Code', monospace; font-size: 0.74rem; }
.dry-box { background: #fefce8; border: 1px solid #fef08a; border-left: 3.5px solid var(--amb); padding: 5px 8px; margin: 4px 0; border-radius: 4px; font-size: 0.76rem; }

pre { font-family: 'Fira Code', monospace; font-size: 0.72rem; line-height: 1.25; background: #0f172a; color: #f8fafc; padding: 6px 8px; border-radius: 4px; margin: 4px 0; overflow-x: auto; }
table { font-size: 0.74rem; border-collapse: collapse; width: 100%; margin: 4px 0; }
th, td { padding: 4px 6px; border: 1px solid var(--bdr); text-align: left; }
th { background: #f1f5f9; font-weight: 700; color: var(--pri); }

@page { size: A4 portrait; margin: 3mm; }
@media print {
  body { background: white !important; padding: 0 !important; margin: 0 !important; color: black !important; -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
  .top-nav, .toc-sidebar { display: none !important; }
  .app-layout { display: block !important; }
  .page { box-shadow: none !important; border: none !important; margin: 0 !important; padding: 4px 6px !important; width: 100% !important; page-break-after: always !important; break-after: page !important; page-break-inside: avoid !important; break-inside: avoid !important; zoom: 0.85; }
  .page:last-child { page-break-after: avoid !important; break-after: avoid !important; }
  table, tr, td, th { page-break-inside: avoid !important; break-inside: avoid !important; }
}
"""

def upgrade_topic_css_and_pdf(t_path):
    filename = os.path.basename(t_path)
    pdf_path = t_path.replace(".html", ".pdf")
    
    with open(t_path, "r", encoding="utf-8", errors="ignore") as f:
        html = f.read()
        
    head_end = html.find('</head>')
    if head_end == -1: return
    
    style_part = html[:head_end]
    style_part = re.sub(r'@page\s*\{[^}]*\}[\s\S]*?(?=</style>)', '', style_part)
    
    full_html = style_part.replace('</style>', new_print_css + '\n</style>') + html[head_end:]
    
    with open(t_path, "w", encoding="utf-8") as f:
        f.write(full_html)
        
    if os.path.exists(pdf_path): os.remove(pdf_path)
    cmd = [chrome_path, '--headless', '--disable-gpu', '--no-pdf-header-footer', f'--print-to-pdf={pdf_path}', t_path]
    subprocess.run(cmd, check=True)
    
    doc = fitz.open(pdf_path)
    print(f"[{filename}] -> Generated PDF Pages: {len(doc)}")
    doc.close()

html_files = sorted(glob.glob(os.path.join(book_dir, "Topic*.html")))
print("Upgrading CSS and re-generating PDFs for all topics...")
for h in html_files:
    upgrade_topic_css_and_pdf(h)

print("\nAll topics updated!")

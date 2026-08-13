import re, os, sys, glob, subprocess, fitz

sys.stdout.reconfigure(encoding='utf-8')

book_dir = r"F:\dsa\bookfinal"
v4_dir = r"F:\dsa\bookfinal - Copy\v4\bookfinal"
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

new_print_css = """
body { font-family: 'Inter', sans-serif; background: #e2e8f0; color: var(--txt); font-size: 10px; line-height: 1.28; padding: 15px; }

.page {
  background: white; max-width: 1100px; margin: 0 auto 20px auto;
  padding: 8px 12px; border-radius: 8px;
  box-shadow: 0 6px 20px rgba(0,0,0,0.08);
  page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;
}

.ph { display:flex; justify-content:space-between; align-items:center;
  border-bottom: 2.5px solid var(--pri); padding-bottom: 3px; margin-bottom: 5px; }
.ph h1 { font-size: 1.4rem; font-weight: 900; color: var(--pri); letter-spacing: 0.5px; }
.ph .sub { font-size: 0.78rem; font-weight: 600; color: var(--sub); margin-top: 1px; }
.ph .pn { background: var(--pri); color: white; padding: 2px 8px; border-radius: 12px;
  font-weight: 800; font-size: 0.75rem; text-align: right; }
.ph .ptag { font-size: 0.68rem; color: var(--sub); font-weight: 600; margin-top: 2px; }

.box { margin-bottom: 5px; }
.bh { padding: 3px 6px; font-size: 0.78rem; }
.bc { padding: 4px 6px; font-size: 0.74rem; }
pre { font-size: 0.71rem; line-height: 1.18; margin: 0; }
table { font-size: 0.71rem; border-collapse: collapse; width: 100%; }
th, td { padding: 2px 4px; border: 1px solid var(--bdr); }

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

def count_open_divs(html_snippet):
    opens = len(re.findall(r'<div[\s>]', html_snippet))
    closes = len(re.findall(r'</div>', html_snippet))
    return opens - closes

def process_topic(t_num_str):
    if t_num_str in ["01", "02"]: return # already verified 100%
    
    pattern = f"Topic{t_num_str}_*.html"
    v4_matches = glob.glob(os.path.join(v4_dir, pattern))
    if not v4_matches: v4_matches = glob.glob(os.path.join(book_dir, pattern))
    if not v4_matches: return
    
    src_file = v4_matches[0]
    filename = os.path.basename(src_file)
    dst_file = os.path.join(book_dir, filename)
    pdf_file = dst_file.replace(".html", ".pdf")
    
    with open(src_file, "r", encoding="utf-8", errors="ignore") as f:
        html = f.read()
        
    head_end = html.find('</head>')
    style_part = html[:head_end]
    style_part = re.sub(r'@page\s*\{[^}]*\}[\s\S]*?(?=</style>)', '', style_part)
    head_code = style_part.replace('</style>', new_print_css + '\n</style>') + '\n</head>\n<body>\n<div class="container">\n<div class="app-layout">\n<div class="main-content">\n'

    title_m = re.search(r'<h1>(.*?)</h1>', html)
    topic_title = title_m.group(1) if title_m else f"TOPIC {t_num_str}"

    pages_raw = re.split(r'<!-- PAGE \d+:', html)[1:]
    pages_clean = []
    
    for p in pages_raw:
        ph_start = p.find('<div class="ph">')
        if ph_start != -1:
            ph_end = p.find('</div>\n</div>', ph_start)
            if ph_end == -1: ph_end = p.find('</div></div>', ph_start)
            body = p[ph_end+12:] if ph_end != -1 else p
        else:
            body = p
            
        diff = count_open_divs(body)
        if diff > 0: body += '</div>' * diff
        elif diff < 0: body = ('<div>' * abs(diff)) + body
        pages_clean.append(body)

    total_orig = len(pages_clean)
    if total_orig < 2: return
    
    # 6 dense pages layout
    p1 = f"""<div class="page"><div class="ph"><div><h1>{topic_title}</h1><div class="sub">FAANG Master Guide — Foundation &amp; Templates</div></div><div style="text-align:right"><div class="pn">PAGE 1 OF 6</div></div></div>{pages_clean[0]}<div style="margin-top:4px"></div>{pages_clean[1]}</div>"""
    p2 = f"""<div class="page"><div class="ph"><div><h1>{topic_title}</h1><div class="sub">Core Patterns — Part 1 &amp; Part 2</div></div><div style="text-align:right"><div class="pn">PAGE 2 OF 6</div></div></div>{pages_clean[2]}<div style="margin-top:4px"></div>{pages_clean[3]}</div>"""
    p3 = f"""<div class="page"><div class="ph"><div><h1>{topic_title}</h1><div class="sub">Core Patterns — Part 3 &amp; Part 4</div></div><div style="text-align:right"><div class="pn">PAGE 3 OF 6</div></div></div>{pages_clean[4]}<div style="margin-top:4px"></div>{pages_clean[5]}</div>"""
    p4 = f"""<div class="page"><div class="ph"><div><h1>{topic_title}</h1><div class="sub">Decision Tree &amp; Trigger Words</div></div><div style="text-align:right"><div class="pn">PAGE 4 OF 6</div></div></div>{pages_clean[6]}</div>"""
    p5 = f"""<div class="page"><div class="ph"><div><h1>{topic_title}</h1><div class="sub">FAANG Problem Ladder &amp; Pattern Summary</div></div><div style="text-align:right"><div class="pn">PAGE 5 OF 6</div></div></div>{pages_clean[7]}<div style="margin-top:4px"></div>{pages_clean[8]}</div>"""
    p6 = f"""<div class="page"><div class="ph"><div><h1>{topic_title}</h1><div class="sub">Dry Run, Math Proofs &amp; FAANG Cheat Sheet</div></div><div style="text-align:right"><div class="pn">PAGE 6 OF 6</div></div></div>{pages_clean[9]}</div>"""
    
    full_html = head_code + p1 + p2 + p3 + p4 + p5 + p6 + '\n</div>\n</div>\n</div>\n</body>\n</html>'
    
    with open(dst_file, "w", encoding="utf-8") as f:
        f.write(full_html)
        
    if os.path.exists(pdf_file): os.remove(pdf_file)
    cmd = [chrome_path, '--headless', '--disable-gpu', '--no-pdf-header-footer', f'--print-to-pdf={pdf_file}', dst_file]
    subprocess.run(cmd, check=True)
    
    doc = fitz.open(pdf_file)
    print(f"[{filename}] -> HTML divs: 6 | PDF Pages: {len(doc)}")
    doc.close()

topic_ids = [f"{i:02d}" for i in range(3, 20)]
print("Fixing div nesting and re-generating PDFs for Topics 03 to 19...")
for tid in topic_ids:
    process_topic(tid)

print("DONE!")

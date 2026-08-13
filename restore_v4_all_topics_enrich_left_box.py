import os, sys, re, glob, subprocess, fitz

sys.stdout.reconfigure(encoding='utf-8')

book_dir = r"F:\dsa\bookfinal"
v4_dir = r"F:\dsa\bookfinal - Copy\v4\bookfinal"
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

print_fix_css = """
@media print {
  pre {
    background: #f8fafc !important;
    color: #0f172a !important;
    border: 1.5px solid #cbd5e1 !important;
    font-family: 'Fira Code', monospace !important;
    font-size: 0.72rem !important;
    line-height: 1.22 !important;
    padding: 6px 8px !important;
    white-space: pre-wrap !important;
  }
}
"""

def count_open_divs(snippet):
    return len(re.findall(r'<div[\s>]', snippet)) - len(re.findall(r'</div>', snippet))

def process_topic(t_num_str):
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
    if head_end == -1: return
    
    style_part = html[:head_end]
    if "@media print" in style_part and "background: #f8fafc" not in style_part:
        style_part = style_part.replace('</style>', print_fix_css + '\n</style>')
        
    head_and_main = style_part + html[head_end:html.find('<div class="main-content">') + len('<div class="main-content">')]

    title_m = re.search(r'<h1>(.*?)</h1>', html)
    topic_title = title_m.group(1) if title_m else f"TOPIC {t_num_str}"

    pages_raw = re.split(r'<!-- PAGE \d+:', html)[1:]
    if not pages_raw:
        pages_raw = html.split('<div class="page">')[1:]
        
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
    if total_orig == 10:
        p1 = f"""\n<!-- PAGE 1 -->\n<div class="page"><div class="ph"><div><h1>{topic_title}</h1><div class="sub">Foundation &amp; Templates</div></div><div style="text-align:right"><div class="pn">PAGE 1 OF 6</div></div></div>{pages_clean[0]}<div style="margin-top:4px"></div>{pages_clean[1]}</div>"""
        p2 = f"""\n<!-- PAGE 2 -->\n<div class="page"><div class="ph"><div><h1>{topic_title}</h1><div class="sub">Core Patterns — Part 1 &amp; Part 2</div></div><div style="text-align:right"><div class="pn">PAGE 2 OF 6</div></div></div>{pages_clean[2]}<div style="margin-top:4px"></div>{pages_clean[3]}</div>"""
        p3 = f"""\n<!-- PAGE 3 -->\n<div class="page"><div class="ph"><div><h1>{topic_title}</h1><div class="sub">Core Patterns — Part 3 &amp; Part 4</div></div><div style="text-align:right"><div class="pn">PAGE 3 OF 6</div></div></div>{pages_clean[4]}<div style="margin-top:4px"></div>{pages_clean[5]}</div>"""
        p4 = f"""\n<!-- PAGE 4 -->\n<div class="page"><div class="ph"><div><h1>{topic_title}</h1><div class="sub">Decision Tree &amp; Trigger Words</div></div><div style="text-align:right"><div class="pn">PAGE 4 OF 6</div></div></div>{pages_clean[6]}</div>"""
        p5 = f"""\n<!-- PAGE 5 -->\n<div class="page"><div class="ph"><div><h1>{topic_title}</h1><div class="sub">FAANG Problem Ladder (All 10 Problems)</div></div><div style="text-align:right"><div class="pn">PAGE 5 OF 6</div></div></div>{pages_clean[7]}<div style="margin-top:4px"></div>{pages_clean[8]}</div>"""
        p6 = f"""\n<!-- PAGE 6 -->\n<div class="page"><div class="ph"><div><h1>{topic_title}</h1><div class="sub">Dry Run, Proofs &amp; Cheat Sheet</div></div><div style="text-align:right"><div class="pn">PAGE 6 OF 6</div></div></div>{pages_clean[9]}</div>"""
        merged_pages = [p1, p2, p3, p4, p5, p6]
    else:
        merged_pages = []
        for i in range(0, total_orig, 2):
            p_idx = len(merged_pages) + 1
            if i + 1 < total_orig:
                p_content = f"{pages_clean[i]}<div style='margin-top:4px'></div>{pages_clean[i+1]}"
            else:
                p_content = pages_clean[i]
            p_block = f"""\n<div class="page"><div class="ph"><div><h1>{topic_title}</h1><div class="sub">FAANG Master Guide</div></div><div style="text-align:right"><div class="pn">PAGE {p_idx}</div></div></div>{p_content}</div>"""
            merged_pages.append(p_block)

    full_html = head_and_main + "".join(merged_pages) + '\n</div>\n</div>\n</div>\n</body>\n</html>'
    
    with open(dst_file, "w", encoding="utf-8") as f:
        f.write(full_html)
        
    if os.path.exists(pdf_file): os.remove(pdf_file)
    cmd = [chrome_path, '--headless', '--disable-gpu', '--no-pdf-header-footer', f'--print-to-pdf={pdf_file}', dst_file]
    subprocess.run(cmd, check=True)
    
    doc = fitz.open(pdf_file)
    print(f"[{filename}] -> Original Sections: {total_orig} | PDF Pages: {len(doc)}")
    doc.close()

topic_ids = [f"{i:02d}" for i in range(1, 20)]
print("Restoring v4 layout & updating all topic PDFs...")
for tid in topic_ids:
    process_topic(tid)

print("COMPLETE!")

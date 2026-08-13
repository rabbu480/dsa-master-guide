import os, sys, re, subprocess, fitz

sys.stdout.reconfigure(encoding='utf-8')

v4_file = r"F:\dsa\bookfinal - Copy\v4\bookfinal\Topic11_Trie.html"
with open(v4_file, "r", encoding="utf-8") as f:
    html = f.read()

# Extract head and replace print CSS
head_end = html.find('</head>')
style_part = html[:head_end]

# Add print rule override so pre has light background when printed
print_fix_css = """
@page { size: A4 portrait; margin: 3mm; }
@media print {
  body { background: white !important; padding: 0 !important; margin: 0 !important; color: black !important; -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
  .top-nav, .toc-sidebar { display: none !important; }
  .app-layout { display: block !important; }
  .page { box-shadow: none !important; border: none !important; margin: 0 !important; padding: 4px 6px !important; width: 100% !important; page-break-after: always !important; break-after: page !important; page-break-inside: avoid !important; break-inside: avoid !important; zoom: 0.85; }
  .page:last-child { page-break-after: avoid !important; break-after: avoid !important; }
  table, tr, td, th { page-break-inside: avoid !important; break-inside: avoid !important; }
  
  /* LIGHT BACKGROUND FOR PRINTING PRE CODE BLOCKS */
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

style_part = re.sub(r'@page\s*\{[^}]*\}[\s\S]*?(?=</style>)', '', style_part)
head_code = style_part.replace('</style>', print_fix_css + '\n</style>') + '\n</head>\n<body>\n<div class="container">\n<div class="app-layout">\n<div class="main-content">\n'

# Parse all 10 original pages from v4
pages_raw = re.split(r'<!-- PAGE \d+:', html)[1:]

def count_open_divs(snippet):
    return len(re.findall(r'<div[\s>]', snippet)) - len(re.findall(r'</div>', snippet))

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

title_m = re.search(r'<h1>(.*?)</h1>', html)
topic_title = title_m.group(1) if title_m else "TRIE DATA STRUCTURE"

# Build 6 dense pages containing ALL 10 original v4 sections (NOTHING deleted!)
p1 = f"""<div class="page"><div class="ph"><div><h1>{topic_title}</h1><div class="sub">FAANG Master Guide — Foundation &amp; Templates</div></div><div style="text-align:right"><div class="pn">PAGE 1 OF 6</div></div></div>{pages_clean[0]}<div style="margin-top:4px"></div>{pages_clean[1]}</div>"""
p2 = f"""<div class="page"><div class="ph"><div><h1>{topic_title}</h1><div class="sub">Core Patterns — Part 1 &amp; Part 2</div></div><div style="text-align:right"><div class="pn">PAGE 2 OF 6</div></div></div>{pages_clean[2]}<div style="margin-top:4px"></div>{pages_clean[3]}</div>"""
p3 = f"""<div class="page"><div class="ph"><div><h1>{topic_title}</h1><div class="sub">Core Patterns — Part 3 &amp; Part 4</div></div><div style="text-align:right"><div class="pn">PAGE 3 OF 6</div></div></div>{pages_clean[4]}<div style="margin-top:4px"></div>{pages_clean[5]}</div>"""
p4 = f"""<div class="page"><div class="ph"><div><h1>{topic_title}</h1><div class="sub">Decision Tree &amp; Trigger Words</div></div><div style="text-align:right"><div class="pn">PAGE 4 OF 6</div></div></div>{pages_clean[6]}</div>"""
p5 = f"""<div class="page"><div class="ph"><div><h1>{topic_title}</h1><div class="sub">FAANG Problem Ladder (All 10 Problems)</div></div><div style="text-align:right"><div class="pn">PAGE 5 OF 6</div></div></div>{pages_clean[7]}<div style="margin-top:4px"></div>{pages_clean[8]}</div>"""
p6 = f"""<div class="page"><div class="ph"><div><h1>{topic_title}</h1><div class="sub">Dry Run, Math Proofs &amp; FAANG Cheat Sheet</div></div><div style="text-align:right"><div class="pn">PAGE 6 OF 6</div></div></div>{pages_clean[9]}</div>"""

full_html = head_code + p1 + p2 + p3 + p4 + p5 + p6 + '\n</div>\n</div>\n</div>\n</body>\n</html>'

out_html = r"F:\dsa\bookfinal\Topic11_Trie.html"
with open(out_html, "w", encoding="utf-8") as f:
    f.write(full_html)

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
pdf_out = r"F:\dsa\bookfinal\Topic11_Trie.pdf"

if os.path.exists(pdf_out): os.remove(pdf_out)

cmd = [chrome_path, '--headless', '--disable-gpu', '--no-pdf-header-footer', f'--print-to-pdf={pdf_out}', out_html]
subprocess.run(cmd, check=True)

doc = fitz.open(pdf_out)
print("==========================================")
print(f"Generated PDF Page Count: {len(doc)} pages")
print("==========================================")
for i in range(len(doc)):
    page = doc[i]
    text = page.get_text()
    t_clean = text[:70].replace('\n', ' ')
    print(f"Page {i+1} has {len(text)} chars: {t_clean}")
doc.close()

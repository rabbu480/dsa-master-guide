import re, os, sys, subprocess, fitz

sys.stdout.reconfigure(encoding='utf-8')

v4_file = r"F:\dsa\bookfinal - Copy\v4\bookfinal\Topic11_Trie.html"
with open(v4_file, "r", encoding="utf-8") as f:
    html = f.read()

head_end = html.find('</head>')
style_part = html[:head_end]
style_part = re.sub(r'@page\s*\{[^}]*\}[\s\S]*?(?=</style>)', '', style_part)

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

head_code = style_part.replace('</style>', new_print_css + '\n</style>') + '\n</head>\n<body>\n<div class="container">\n<div class="app-layout">\n<div class="main-content">\n'

pages_raw = re.split(r'<!-- PAGE \d+:', html)[1:]
pages_content = []
for p in pages_raw:
    ph_end = p.find('</div>\n</div>')
    if ph_end == -1: ph_end = p.find('</div></div>')
    body = p[ph_end+12:] if ph_end != -1 else p
    body = re.sub(r'</div>\s*</div>\s*$', '', body).strip()
    pages_content.append(body)

p1 = f"""
<div class="page">
<div class="ph">
  <div><h1>TRIE DATA STRUCTURE</h1><div class="sub">FAANG Master Guide — Java Edition &amp; Toolkit</div></div>
  <div style="text-align:right"><div class="pn">PAGE 1 OF 7</div><div class="ptag">FOUNDATION · PREFIX TREE · API TEMPLATE</div></div>
</div>
{pages_content[0]}
<div style="margin-top:4px"></div>
{pages_content[1]}
</div>
"""

p2 = f"""
<div class="page">
<div class="ph">
  <div><h1>TRIE DATA STRUCTURE</h1><div class="sub">Core Patterns — Wildcard Search, Prefix Replacement &amp; Map Sum</div></div>
  <div style="text-align:right"><div class="pn">PAGE 2 OF 7</div><div class="ptag">WILDCARD · PREFIX REPLACE · MAP SUM</div></div>
</div>
{pages_content[2]}
<div style="margin-top:4px"></div>
{pages_content[3]}
</div>
"""

p3 = f"""
<div class="page">
<div class="ph">
  <div><h1>TRIE DATA STRUCTURE</h1><div class="sub">Advanced Patterns — Grid DFS Pruning &amp; Bitwise 31-Bit Binary Trie</div></div>
  <div style="text-align:right"><div class="pn">PAGE 3 OF 7</div><div class="ptag">WORD SEARCH II · BITWISE XOR · 31-BIT TRIE</div></div>
</div>
{pages_content[4]}
<div style="margin-top:4px"></div>
{pages_content[5]}
</div>
"""

p4 = f"""
<div class="page">
<div class="ph">
  <div><h1>TRIE DATA STRUCTURE</h1><div class="sub">Decision Tree &amp; Trigger Words</div></div>
  <div style="text-align:right"><div class="pn">PAGE 4 OF 7</div><div class="ptag">DECISION TREE · PATTERN TRIGGERS</div></div>
</div>
{pages_content[6]}
</div>
"""

p5 = f"""
<div class="page">
<div class="ph">
  <div><h1>TRIE DATA STRUCTURE</h1><div class="sub">FAANG Problem Ladder — Part 1</div></div>
  <div style="text-align:right"><div class="pn">PAGE 5 OF 7</div><div class="ptag">PROBLEM LADDER · PRACTICE PROBLEMS</div></div>
</div>
{pages_content[7]}
</div>
"""

p6 = f"""
<div class="page">
<div class="ph">
  <div><h1>TRIE DATA STRUCTURE</h1><div class="sub">FAANG Problem Ladder — Part 2 &amp; Pattern Summary</div></div>
  <div style="text-align:right"><div class="pn">PAGE 6 OF 7</div><div class="ptag">ADVANCED PROBLEMS · SUMMARY TABLE</div></div>
</div>
{pages_content[8]}
</div>
"""

p7 = f"""
<div class="page">
<div class="ph">
  <div><h1>TRIE DATA STRUCTURE</h1><div class="sub">Dry Run, Math Proofs &amp; FAANG Cheat Sheet</div></div>
  <div style="text-align:right"><div class="pn">PAGE 7 OF 7</div><div class="ptag">DRY RUN · PROOFS · CHEAT SHEET</div></div>
</div>
{pages_content[9]}
</div>
"""

full_html = head_code + p1 + p2 + p3 + p4 + p5 + p6 + p7 + '\n</div>\n</div>\n</div>\n</body>\n</html>'

out_html = r"F:\dsa\bookfinal\Topic11_Trie.html"
with open(out_html, "w", encoding="utf-8") as f:
    f.write(full_html)

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
pdf_out = r"F:\dsa\bookfinal\Topic11_Trie.pdf"

if os.path.exists(pdf_out):
    os.remove(pdf_out)

cmd = [chrome_path, '--headless', '--disable-gpu', '--no-pdf-header-footer', f'--print-to-pdf={pdf_out}', out_html]
subprocess.run(cmd, check=True)

doc = fitz.open(pdf_out)
print("==========================================")
print(f"Topic 11 Generated PDF Page Count: {len(doc)} pages")
print("==========================================")

for i in range(len(doc)):
    page = doc[i]
    text = page.get_text()
    t_clean = text[:60].replace('\n', ' ')
    print(f"Page {i+1} has {len(text)} chars: {t_clean}")

doc.close()

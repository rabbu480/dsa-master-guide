import re, os, sys, subprocess, fitz

sys.stdout.reconfigure(encoding='utf-8')

v4_file = r"F:\dsa\bookfinal - Copy\v4\bookfinal\Topic03_TwoPointers.html"
with open(v4_file, "r", encoding="utf-8") as f:
    html = f.read()

# Get head and style
head_end = html.find('</head>')
style_part = html[:head_end]

# Standardize CSS for high density readable output (matching Topic 01 / Topic 02)
# Remove old @page / @media print blocks in style_part
style_part = re.sub(r'@page\s*\{[^}]*\}[\s\S]*?(?=</style>)', '', style_part)

new_print_css = """
body { font-family: 'Inter', sans-serif; background: #e2e8f0; color: var(--txt); font-size: 10.5px; line-height: 1.32; padding: 15px; }

.page {
  background: white; max-width: 1100px; margin: 0 auto 20px auto;
  padding: 10px 14px; border-radius: 8px;
  box-shadow: 0 6px 20px rgba(0,0,0,0.08);
  page-break-after: always; page-break-inside: avoid; break-inside: avoid;
}

.ph { display:flex; justify-content:space-between; align-items:center;
  border-bottom: 2.5px solid var(--pri); padding-bottom: 5px; margin-bottom: 8px; }
.ph h1 { font-size: 1.6rem; font-weight: 900; color: var(--pri); letter-spacing: 0.5px; }
.ph .sub { font-size: 0.82rem; font-weight: 600; color: var(--sub); margin-top: 1px; }
.ph .pn { background: var(--pri); color: white; padding: 2px 10px; border-radius: 14px;
  font-weight: 800; font-size: 0.8rem; text-align: right; }
.ph .ptag { font-size: 0.72rem; color: var(--sub); font-weight: 600; margin-top: 2px; }

.box { margin-bottom: 8px; }
.bh { padding: 4px 8px; font-size: 0.82rem; }
.bc { padding: 6px 8px; font-size: 0.78rem; }
pre { font-size: 0.75rem; line-height: 1.25; margin: 0; }
table { font-size: 0.75rem; border-collapse: collapse; width: 100%; }
th, td { padding: 4px 6px; border: 1px solid var(--bdr); }

@page { size: A4 portrait; margin: 4mm; }
@media print {
  body { background: white !important; padding: 0 !important; margin: 0 !important; color: black !important; -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
  .top-nav, .toc-sidebar { display: none !important; }
  .app-layout { display: block !important; }
  .page { box-shadow: none !important; border: none !important; margin: 0 !important; padding: 6px 10px !important; width: 100% !important; page-break-after: always !important; page-break-inside: avoid !important; break-inside: avoid !important; height: 98vh !important; overflow: hidden !important; zoom: 0.82; }
  .page:last-child { page-break-after: avoid !important; break-after: avoid !important; }
  table, tr, td, th { page-break-inside: avoid !important; break-inside: avoid !important; }
}
"""

# Inject CSS into head
head_code = style_part.replace('</style>', new_print_css + '\n</style>') + '\n</head>\n<body>\n<div class="container">\n<div class="app-layout">\n<div class="main-content">\n'

# Parse original pages
pages_raw = re.split(r'<!-- PAGE \d+:', html)[1:]
pages_content = []
for p in pages_raw:
    # get body after <div class="ph">...</div>
    ph_end = p.find('</div>\n</div>')
    if ph_end == -1: ph_end = p.find('</div></div>')
    body = p[ph_end+12:] if ph_end != -1 else p
    # strip trailing closing page div
    body = re.sub(r'</div>\s*</div>\s*$', '', body).strip()
    pages_content.append(body)

# Build 5 dense pages according to user's specified grouping:
# Group 1: Page 1 & 2
# Group 2: Page 3 & 4
# Group 3: Page 5, 6 & 7
# Group 4: Page 8 & 9
# Group 5: Page 10

p1 = f"""
<!-- PAGE 1: FOUNDATION & SIDE-BY-SIDE TEMPLATES -->
<div class="page">
<div class="ph">
  <div><h1>TWO POINTERS PATTERN</h1><div class="sub">FAANG Master Guide — Java Edition &amp; Templates</div></div>
  <div style="text-align:right"><div class="pn">PAGE 1 OF 5</div><div class="ptag">FOUNDATION · TEMPLATES · COMPLEXITY</div></div>
</div>
{pages_content[0]}
<div style="margin-top:10px"></div>
{pages_content[1]}
</div>
"""

p2 = f"""
<!-- PAGE 2: CORE PATTERNS (PART 1 & PART 2) -->
<div class="page">
<div class="ph">
  <div><h1>TWO POINTERS PATTERN</h1><div class="sub">Core Patterns — Valid Palindrome, Two Sum II &amp; 3Sum</div></div>
  <div style="text-align:right"><div class="pn">PAGE 2 OF 5</div><div class="ptag">PALINDROME · TWO SUM II · 3SUM</div></div>
</div>
{pages_content[2]}
<div style="margin-top:10px"></div>
{pages_content[3]}
</div>
"""

p3 = f"""
<!-- PAGE 3: CORE PATTERNS (PART 3 & PART 4) & DECISION TREE -->
<div class="page">
<div class="ph">
  <div><h1>TWO POINTERS PATTERN</h1><div class="sub">Core Patterns — Water Containers &amp; Decision Tree</div></div>
  <div style="text-align:right"><div class="pn">PAGE 3 OF 5</div><div class="ptag">CONTAINER WATER · TRAPPING RAIN · DECISION TREE</div></div>
</div>
<div class="g2" style="margin-bottom:10px">
<div>{pages_content[4]}</div>
<div>{pages_content[5]}</div>
</div>
{pages_content[6]}
</div>
"""

p4 = f"""
<!-- PAGE 4: PROBLEM LADDER (PARTS 1 & 2 + SUMMARY TABLE) -->
<div class="page">
<div class="ph">
  <div><h1>TWO POINTERS PATTERN</h1><div class="sub">FAANG Problem Ladder &amp; Pattern Summary</div></div>
  <div style="text-align:right"><div class="pn">PAGE 4 OF 5</div><div class="ptag">PROBLEM LADDER · PRACTICE PROBLEMS · SUMMARY</div></div>
</div>
{pages_content[7]}
<div style="margin-top:10px"></div>
{pages_content[8]}
</div>
"""

p5 = f"""
<!-- PAGE 5: DRY RUN, MATH PROOFS & CHEAT SHEET -->
<div class="page">
<div class="ph">
  <div><h1>TWO POINTERS PATTERN</h1><div class="sub">Dry Run, Math Proofs &amp; FAANG Cheat Sheet</div></div>
  <div style="text-align:right"><div class="pn">PAGE 5 OF 5</div><div class="ptag">DRY RUN · PROOFS · CHEAT SHEET</div></div>
</div>
{pages_content[9]}
</div>
"""

full_html = head_code + p1 + p2 + p3 + p4 + p5 + '\n</div>\n</div>\n</div>\n</body>\n</html>'

out_html = r"F:\dsa\bookfinal\Topic03_TwoPointers.html"
with open(out_html, "w", encoding="utf-8") as f:
    f.write(full_html)

print("Saved HTML to", out_html)

# Generate PDF via Chrome
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
pdf_out = r"F:\dsa\bookfinal\Topic03_TwoPointers.pdf"

if os.path.exists(pdf_out):
    os.remove(pdf_out)

cmd = [chrome_path, '--headless', '--disable-gpu', '--no-pdf-header-footer', f'--print-to-pdf={pdf_out}', out_html]
subprocess.run(cmd, check=True)

doc = fitz.open(pdf_out)
print("==========================================")
print(f"Generated PDF Page Count: {len(doc)} pages")
print("==========================================")
doc.close()

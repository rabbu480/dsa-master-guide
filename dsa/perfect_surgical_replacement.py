import re

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Exact boundary between Old Page 1 and Old Page 2:
target_p1_p2 = """</div>

<!-- PAGE 2: API & SIDE-BY-SIDE TEMPLATES -->
<div class="page">
<div class="ph">
  <div><h1>TWO POINTERS PATTERN</h1><div class="sub">Java Side-by-Side Pointer Templates</div></div>
  <div style="text-align:right"><div class="pn">PAGE 2 OF 10</div><div class="ptag">TEMPLATES · OPPOSITE DIRECTION · SAME DIRECTION</div></div>
</div>"""

target_p3_p4 = """</div>

<!-- PAGE 4: CORE PATTERNS (3SUM) -->
<div class="page">
<div class="ph">
  <div><h1>TWO POINTERS PATTERN</h1><div class="sub">Core Patterns — Part 2</div></div>
  <div style="text-align:right"><div class="pn">PAGE 4 OF 10</div><div class="ptag">3SUM · DUPLICATE SKIPPING</div></div>
</div>"""

target_p5_p6 = """</div>

<!-- PAGE 6: CORE PATTERNS (TRAPPING RAIN WATER) -->
<div class="page">
<div class="ph">
  <div><h1>TWO POINTERS PATTERN</h1><div class="sub">Core Patterns — Part 4</div></div>
  <div style="text-align:right"><div class="pn">PAGE 6 OF 10</div><div class="ptag">TRAPPING RAIN WATER · BOUNDARY MAX TRACKING</div></div>
</div>"""

target_p7_p8 = """</div>

<!-- PAGE 8: NEETCODE SUITE (PART 1) -->
<div class="page">
<div class="ph">
  <div><h1>TWO POINTERS PATTERN</h1><div class="sub">FAANG NeetCode Problem Suite — Easy &amp; Medium</div></div>
  <div style="text-align:right"><div class="pn">PAGE 8 OF 10</div><div class="ptag">NEETCODE 150 · EASY &amp; MEDIUM SOLUTIONS</div></div>
</div>"""

target_p9_p10 = """</div>

<!-- PAGE 10: DRY RUN, PROOFS & CHEAT SHEET -->
<div class="page">
<div class="ph">
  <div><h1>TWO POINTERS PATTERN</h1><div class="sub">Dry Run Trace, Proofs &amp; Revision Cheat Sheet</div></div>
  <div style="text-align:right"><div class="pn">PAGE 10 OF 10</div><div class="ptag">DRY RUN TRACE · PROOFS · CHEAT SHEET</div></div>
</div>"""

text = text.replace(target_p1_p2, "")
text = text.replace(target_p3_p4, "")
text = text.replace(target_p5_p6, "")
text = text.replace(target_p7_p8, "")
text = text.replace(target_p9_p10, "")

text = text.replace('PAGE 1 OF 10', 'PAGE 1 OF 5')
text = text.replace('PAGE 3 OF 10', 'PAGE 2 OF 5')
text = text.replace('PAGE 5 OF 10', 'PAGE 3 OF 5')
text = text.replace('PAGE 7 OF 10', 'PAGE 4 OF 5')
text = text.replace('PAGE 9 OF 10', 'PAGE 5 OF 5')

# Make print CSS height 98vh!
print_css = """@page { size: A4 portrait; margin: 4mm; }
@media print {
  body { background: white !important; padding: 0 !important; margin: 0 !important; color: black !important; -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
  .top-nav, .toc-sidebar { display: none !important; }
  .app-layout { display: block !important; }
  .page { box-shadow: none !important; border: none !important; margin: 0 !important; padding: 6px 10px !important; width: 100% !important; page-break-after: always !important; page-break-inside: avoid !important; break-inside: avoid !important; height: 98vh !important; overflow: hidden !important; zoom: 0.76; }
  .page:last-child { page-break-after: avoid !important; break-after: avoid !important; }
  table, tr, td, th { page-break-inside: avoid !important; break-inside: avoid !important; }
}"""
text = re.sub(r'@page\s*\{[^}]*\}\s*@media print\s*\{[\s\S]*?\}', print_css, text)

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("=== PERFECT SURGICAL STRING REPLACEMENT SUCCESSFUL ===")

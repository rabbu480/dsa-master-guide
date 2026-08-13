import re

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Exact replacement of boundary 2 (between old page 2 & page 3)
text = text.replace('</div>\n</div>\n\n<!-- PAGE 3: CORE PATTERNS (VALID PALINDROME & TWO SUM II) -->\n<div class="page">\n<div class="ph">\n  <div><h1>TWO POINTERS PATTERN</h1><div class="sub">Core Patterns — Part 1</div></div>\n  <div style="text-align:right"><div class="pn">PAGE 3 OF 10</div><div class="ptag">VALID PALINDROME · TWO SUM II</div></div>\n</div>', '<!-- MERGED P2-P3 -->')

# Exact replacement of boundary 4 (between old page 4 & page 5)
text = text.replace('</div>\n</div>\n\n<!-- PAGE 5: CORE PATTERNS (CONTAINER WITH MOST WATER) -->\n<div class="page">\n<div class="ph">\n  <div><h1>TWO POINTERS PATTERN</h1><div class="sub">Core Patterns — Part 3</div></div>\n  <div style="text-align:right"><div class="pn">PAGE 5 OF 10</div><div class="ptag">CONTAINER WITH MOST WATER · GREEDY SHRINKING</div></div>\n</div>', '<!-- MERGED P4-P5 -->')

# Exact replacement of boundary 6 (between old page 6 & page 7)
text = text.replace('</div>\n</div>\n\n<!-- PAGE 7: DECISION TREE & TRIGGER WORDS -->\n<div class="page">\n<div class="ph">\n  <div><h1>TWO POINTERS PATTERN</h1><div class="sub">Decision Tree &amp; Trigger Words</div></div>\n  <div style="text-align:right"><div class="pn">PAGE 7 OF 10</div><div class="ptag">DECISION TREE · TRIGGER WORDS · TRADE-OFFS</div></div>\n</div>', '<!-- MERGED P6-P7 -->')

# Exact replacement of boundary 8 (between old page 8 & page 9)
text = text.replace('</div>\n</div>\n\n<!-- PAGE 9: NEETCODE SUITE (PART 2) -->\n<div class="page">\n<div class="ph">\n  <div><h1>TWO POINTERS PATTERN</h1><div class="sub">FAANG NeetCode Problem Suite — Hard Problems</div></div>\n  <div style="text-align:right"><div class="pn">PAGE 9 OF 10</div><div class="ptag">NEETCODE 150 · HARD SOLUTIONS</div></div>\n</div>', '<!-- MERGED P8-P9 -->')

# Update header numbers
text = text.replace('PAGE 1 OF 10', 'PAGE 1 OF 5')
text = text.replace('PAGE 2 OF 10', 'PAGE 1 OF 5')
text = text.replace('PAGE 4 OF 10', 'PAGE 2 OF 5')
text = text.replace('PAGE 6 OF 10', 'PAGE 3 OF 5')
text = text.replace('PAGE 8 OF 10', 'PAGE 4 OF 5')
text = text.replace('PAGE 10 OF 10', 'PAGE 5 OF 5')

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

print("=== CLEAN EXACT STRING MERGE COMPLETE ===")

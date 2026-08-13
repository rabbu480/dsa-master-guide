import re

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Exact target string in Topic 03 between Page 1 and Page 2:
target_p1_p2 = """</div>
</div>

<!-- PAGE 2: API & SIDE-BY-SIDE TEMPLATES -->
<div class="page">
<div class="ph">
  <div><h1>TWO POINTERS PATTERN</h1><div class="sub">Java Side-by-Side Pointer Templates</div></div>
  <div style="text-align:right"><div class="pn">PAGE 2 OF 10</div><div class="ptag">TEMPLATES · OPPOSITE DIRECTION · SAME DIRECTION</div></div>
</div>"""

replacement_p1_p2 = """</div>"""

text = text.replace(target_p1_p2, replacement_p1_p2)
text = text.replace('PAGE 1 OF 10', 'PAGE 1 OF 5')

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("=== REPLACED EXACT TARGET P1 TO P2 STRING ===")

import re

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Merge page 1 & 2 into one page block
# Merge page 3 & 4 into one page block
# Merge page 5 & 6 into one page block
# Merge page 7 & 8 into one page block
# Merge page 9 & 10 into one page block

# Strip <div class="page"> and its closing </div> between pages 1 & 2, 3 & 4, 5 & 6, 7 & 8, 9 & 10
# Also strip ph header of page 2, 4, 6, 8, 10

# Let's replace the page boundaries cleanly:
# Boundary between P1 and P2:
text = re.sub(r'</div>\s*<!-- PAGE 2: API & SIDE-BY-SIDE TEMPLATES -->\s*<div class="page">\s*<div class="ph">[\s\S]*?</div>\s*</div>', '<!-- PAGE 1B -->', text)

# Boundary between P3 and P4:
text = re.sub(r'</div>\s*<!-- PAGE 4: CORE PATTERNS \(3SUM\) -->\s*<div class="page">\s*<div class="ph">[\s\S]*?</div>\s*</div>', '<!-- PAGE 2B -->', text)

# Boundary between P5 and P6:
text = re.sub(r'</div>\s*<!-- PAGE 6: CORE PATTERNS \(TRAPPING RAIN WATER\) -->\s*<div class="page">\s*<div class="ph">[\s\S]*?</div>\s*</div>', '<!-- PAGE 3B -->', text)

# Boundary between P7 and P8:
text = re.sub(r'</div>\s*<!-- PAGE 8: NEETCODE SUITE \(PART 1\) -->\s*<div class="page">\s*<div class="ph">[\s\S]*?</div>\s*</div>', '<!-- PAGE 4B -->', text)

# Boundary between P9 and P10:
text = re.sub(r'</div>\s*<!-- PAGE 10: DRY RUN, PROOFS & CHEAT SHEET -->\s*<div class="page">\s*<div class="ph">[\s\S]*?</div>\s*</div>', '<!-- PAGE 5B -->', text)

# Adjust page numbers in headers:
text = text.replace('PAGE 1 OF 10', 'PAGE 1 OF 5')
text = text.replace('PAGE 3 OF 10', 'PAGE 2 OF 5')
text = text.replace('PAGE 5 OF 10', 'PAGE 3 OF 5')
text = text.replace('PAGE 7 OF 10', 'PAGE 4 OF 5')
text = text.replace('PAGE 9 OF 10', 'PAGE 5 OF 5')

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("=== CLEAN SURGICAL MERGE FOR TOPIC 03 COMPLETE ===")

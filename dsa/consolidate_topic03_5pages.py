import re

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'r', encoding='utf-8') as f:
    text = f.read()

pages = list(re.finditer(r'<div class="page">', text))

# Head template
head_match = re.search(r'([\s\S]*?<div class="main-content">)', text)
head_html = head_match.group(1)

# Extract body contents of each page
page_bodies = []
for i, m in enumerate(pages):
    start = m.start()
    end = pages[i+1].start() if i+1 < len(pages) else len(text)
    chunk = text[start:end]
    # strip outer <div class="page"> and page header <div class="ph">...</div>
    inner = re.sub(r'^\s*<div class="page">\s*', '', chunk)
    inner = re.sub(r'</div>\s*</div>\s*</div>\s*</body>[\s\S]*$', '', inner)
    inner_clean = re.sub(r'<div class=["\']ph["\'].*?>[\s\S]*?</div>', '', inner).strip()
    page_bodies.append(inner_clean)

# Merge mapping according to user instruction:
# Page 1 = Old 1 + Old 2 (Discovery + Templates)
# Page 2 = Old 3 + Old 4 (Pattern 1, 2, 3: Palindrome, Two Sum II, 3Sum)
# Page 3 = Old 5 + Old 6 + Old 7 (Pattern 4, 5: Container Water, Trapping Rain Water + Decision Tree)
# Page 4 = Old 8 + Old 9 (Problem Ladder Part 1 & Part 2)
# Page 5 = Old 10 (Dry Run, Math Proof, Mastery Checklist, Golden Rules)

merged_groups = [
    [page_bodies[0], page_bodies[1]],               # Page 1 (Discovery + Side-by-Side Templates)
    [page_bodies[2], page_bodies[3]],               # Page 2 (Pattern 1, 2, 3)
    [page_bodies[4], page_bodies[5], page_bodies[6]], # Page 3 (Pattern 4, 5 + Decision Tree)
    [page_bodies[7], page_bodies[8]],               # Page 4 (Problem Ladder)
    [page_bodies[9]]                                 # Page 5 (Dry Run & Proofs)
]

page_titles = [
    "FOUNDATION &amp; SIDE-BY-SIDE TEMPLATES",
    "CORE PATTERNS — PALINDROME, TWO SUM II &amp; 3SUM",
    "ADVANCED PATTERNS &amp; DECISION TREE",
    "COMPLETE NEETCODE PROBLEM LADDER",
    "DRY RUN, MATH PROOFS &amp; CHEAT SHEET"
]

page_tags = [
    "FOUNDATION · TEMPLATES · CONVERGING",
    "PALINDROME · TWO SUM II · 3SUM",
    "CONTAINER WATER · TRAPPING WATER · DECISION TREE",
    "PROBLEM LADDER · EASY · MEDIUM · HARD",
    "DRY RUN · PROOFS · MASTERY CHECKLIST"
]

formatted_pages = []
for idx, grp in enumerate(merged_groups):
    combined_content = "\n\n".join(grp)
    header = f'''<div class="ph">
  <div><h1>TWO POINTERS MASTERCLASS</h1><div class="sub">{page_titles[idx]}</div></div>
  <div style="text-align:right"><div class="pn">PAGE {idx+1} OF 5</div><div class="ptag">{page_tags[idx]}</div></div>
</div>'''
    formatted_pages.append(f'<div class="page">\n{header}\n{combined_content}\n</div>')

tail = "</div>\n</div>\n</div>\n</body>\n</html>"
new_html = head_html + "\n\n" + "\n\n".join(formatted_pages) + "\n\n" + tail

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("=== TOPIC 03 CONSOLIDATED INTO EXACTLY 5 DENSE A4 PAGES ===")

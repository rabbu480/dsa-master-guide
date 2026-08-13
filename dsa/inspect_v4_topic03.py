import re

v4_file = r"F:\dsa\bookfinal - Copy\v4\bookfinal\Topic03_TwoPointers.html"
with open(v4_file, "r", encoding="utf-8") as f:
    html = f.read()

# Split by <div class="page">
pages = re.split(r'<div class=["\']page["\']>', html)[1:] # skip header

print(f"Original v4 Topic03 has {len(pages)} pages.")

for i, page_html in enumerate(pages, 1):
    # Find page title / headers
    title_m = re.search(r'<h1>(.*?)</h1>', page_html)
    sub_m = re.search(r'<div class="sub">(.*?)</div>', page_html)
    title = title_m.group(1) if title_m else "No Title"
    sub = sub_m.group(1) if sub_m else ""
    
    # Count boxes, pre tags, tables
    boxes = len(re.findall(r'class=["\']box', page_html))
    pres = len(re.findall(r'<pre>', page_html))
    tables = len(re.findall(r'<table>', page_html))
    
    print(f"Page {i:2d}: [{title}] ({sub}) -> {boxes} boxes, {pres} code blocks, {tables} tables")

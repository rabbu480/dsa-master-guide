import subprocess
import os

pdf_path = r"F:\dsa\bookfinal\Topic09_Heap.pdf"
# Use pdfinfo or chrome or custom check
with open(r"F:\dsa\bookfinal\Topic09_Heap.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

pages = []
cur = []
for line in lines:
    if '<div class="page">' in line:
        if cur: pages.append("".join(cur))
        cur = [line]
    else:
        cur.append(line)
if cur: pages.append("".join(cur))

print(f"HTML page count: {len(pages)}")
for idx, p in enumerate(pages):
    print(f"HTML Page {idx+1}: {len(p)} chars, lines={len(p.splitlines())}")

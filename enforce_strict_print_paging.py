import glob
import re

files = sorted(glob.glob('F:/dsa/bookfinal/*.html'))
print(f"Applying strict 1-to-1 page alignment to {len(files)} HTML files...")

for f in files:
    if f.endswith("index.html"):
        continue
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    # Ensure .page in @media print has strict height & break-inside avoid
    content = re.sub(
        r'\.page\s*\{\s*box-shadow:[^}]*\}',
        '.page { box-shadow: none !important; border: none !important; margin: 0 !important; padding: 4px 6px !important; width: 100% !important; page-break-after: always !important; page-break-inside: avoid !important; break-inside: avoid !important; height: 98vh !important; overflow: hidden !important; zoom: 0.72; }',
        content
    )
    
    with open(f, 'w', encoding='utf-8') as fp:
        fp.write(content)

print("Applied strict print paging to all files successfully!")

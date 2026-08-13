import os
import glob
import re

files_to_fix = sorted(glob.glob('F:/dsa/bookfinal/*.html'))

for filepath in files_to_fix:
    if 'index.html' in filepath:
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Standardize print CSS for perfect dense A4 pages
    print_css = """@page { size: A4 portrait; margin: 4mm; }
@media print {
  body { background: white !important; padding: 0 !important; margin: 0 !important; color: black !important; -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
  .top-nav, .toc-sidebar { display: none !important; }
  .app-layout { display: block !important; }
  .page { box-shadow: none !important; border: none !important; margin: 0 !important; padding: 6px 10px !important; width: 100% !important; page-break-after: always !important; page-break-inside: avoid !important; break-inside: avoid !important; height: 98vh !important; overflow: hidden !important; zoom: 0.70; }
  .page:last-child { page-break-after: avoid !important; break-after: avoid !important; }
  table, tr, td, th { page-break-inside: avoid !important; break-inside: avoid !important; }
}"""

    # Replace existing @media print block
    content_fixed = re.sub(r'@page\s*\{[^}]*\}\s*@media print\s*\{[\s\S]*?\}', print_css, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content_fixed)

print("=== ALL PRINT CSS STANDARDIZED TO ZOOM 0.70 ===")

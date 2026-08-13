import os
import glob
import re

files = sorted(glob.glob('F:/dsa/bookfinal/Topic*.html'))

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Standardize CSS font sizes to match Topic 01 exactly!
    # body font-size: 11px; line-height: 1.34;
    # pre font-size: 0.66rem; code font-size: 0.72rem; table font-size: 0.72rem;
    # .ph h1 font-size: 1.65rem;
    # .bh font-size: 0.82rem; .prow-head .ptitle font-size: 0.90rem;

    # Replace body font-size
    content = re.sub(r'body\s*\{[^}]*font-size:[^;]+;[^}]*\}', 'body { font-family: \'Inter\', sans-serif; background: #e2e8f0; color: var(--txt); font-size: 11px; line-height: 1.34; padding: 20px; }', content)
    
    # Standardize print CSS with zoom: 0.76 (same as Topic 01!)
    print_css = """@page { size: A4 portrait; margin: 4mm; }
@media print {
  body { background: white !important; padding: 0 !important; margin: 0 !important; color: black !important; -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
  .top-nav, .toc-sidebar { display: none !important; }
  .app-layout { display: block !important; }
  .page { box-shadow: none !important; border: none !important; margin: 0 !important; padding: 6px 10px !important; width: 100% !important; page-break-after: always !important; page-break-inside: avoid !important; break-inside: avoid !important; }
  table, tr, td, th { page-break-inside: avoid !important; break-inside: avoid !important; }
}"""
    content = re.sub(r'@page\s*\{[^}]*\}\s*@media print\s*\{[\s\S]*?\}', print_css, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("=== STANDARDIZED FONT SIZES ACROSS ALL TOPICS ===")

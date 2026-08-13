"""
improve_and_copy.py
--------------------
Reads each *_Final.html from the metadata folder, applies improvements:
  1. Fixes code blocks: white background, black text (print-friendly)
  2. Adds missing FAANG-critical CSS utility classes 
  3. Injects a global print media query for code blocks
  4. Writes improved files to v0/ subfolder
"""

import os
import re

src_dir = r"C:\Users\rabba\Downloads\TelegramDownload\metadata"
dst_dir = r"C:\Users\rabba\Downloads\TelegramDownload\metadata\v0"

os.makedirs(dst_dir, exist_ok=True)

# ---------------------------------------------------------------
# Master CSS – injected into every page's <head>
# Key improvements:
#   - Code blocks: always white bg + dark text (print safe)
#   - Better table alternating row colors
#   - Complexity badge styles  
#   - Algorithm tag badges
#   - Print overrides
# ---------------------------------------------------------------
IMPROVED_CSS = """
    <!-- v0 Improvements: FAANG-ready, print-friendly -->
    <style>
      /* ===== CODE BLOCKS: WHITE BG + BLACK TEXT (print-safe) ===== */
      pre {
        background: #ffffff !important;
        color: #1e293b !important;
        border: 1px solid #94a3b8 !important;
        border-left: 4px solid #1e3a8a !important;
        padding: 12px 15px !important;
        border-radius: 4px !important;
        font-family: 'Fira Code', 'Courier New', monospace !important;
        font-size: 0.82rem !important;
        overflow-x: auto;
        white-space: pre-wrap;
        word-break: break-word;
        line-height: 1.5;
        box-shadow: none !important;
      }
      code {
        background: #f1f5f9 !important;
        color: #1e3a8a !important;
        border: 1px solid #e2e8f0 !important;
        padding: 2px 6px !important;
        border-radius: 3px !important;
        font-family: 'Fira Code', 'Courier New', monospace !important;
        font-size: 0.85em !important;
        box-shadow: none !important;
      }
      pre code {
        background: transparent !important;
        color: inherit !important;
        border: none !important;
        padding: 0 !important;
        font-size: inherit !important;
      }

      /* ===== COMPLEXITY BADGES ===== */
      .badge-o1   { display:inline-block; background:#dcfce7; color:#166534; padding:2px 8px; border-radius:4px; font-weight:700; font-size:0.78rem; border:1px solid #166534; }
      .badge-olog { display:inline-block; background:#dbeafe; color:#1e40af; padding:2px 8px; border-radius:4px; font-weight:700; font-size:0.78rem; border:1px solid #1e40af; }
      .badge-on   { display:inline-block; background:#fef9c3; color:#854d0e; padding:2px 8px; border-radius:4px; font-weight:700; font-size:0.78rem; border:1px solid #854d0e; }
      .badge-on2  { display:inline-block; background:#fee2e2; color:#991b1b; padding:2px 8px; border-radius:4px; font-weight:700; font-size:0.78rem; border:1px solid #991b1b; }

      /* ===== FAANG PATTERN TAGS ===== */
      .tag { display:inline-block; background:#eff6ff; color:#1d4ed8; padding:2px 8px; border-radius:12px; font-size:0.75rem; font-weight:600; margin:2px; border:1px solid #bfdbfe; }

      /* ===== IMPROVED TABLE ROWS ===== */
      table tr:nth-child(even) td { background: #f8fafc; }
      table thead tr th { background: #1e3a8a !important; color: white !important; }

      /* ===== IMPROVED SECTION HEADERS ===== */
      .section-header { letter-spacing: 0.5px; text-transform: uppercase; font-size: 0.9rem !important; }

      /* ===== CALLOUT BOXES ===== */
      .callout-tip { background:#f0fdf4; border:1px solid #16a34a; border-left:4px solid #16a34a; padding:10px 15px; margin:10px 0; border-radius:0 6px 6px 0; }
      .callout-warn { background:#fffbeb; border:1px solid #d97706; border-left:4px solid #d97706; padding:10px 15px; margin:10px 0; border-radius:0 6px 6px 0; }
      .callout-danger { background:#fef2f2; border:1px solid #dc2626; border-left:4px solid #dc2626; padding:10px 15px; margin:10px 0; border-radius:0 6px 6px 0; }
      .callout-info { background:#eff6ff; border:1px solid #2563eb; border-left:4px solid #2563eb; padding:10px 15px; margin:10px 0; border-radius:0 6px 6px 0; }

      /* ===== PRINT OVERRIDES ===== */
      @media print {
        body { background: white !important; padding: 0 !important; }
        .page { 
          box-shadow: none !important; 
          border: none !important; 
          margin: 0 !important; 
          padding: 15px !important; 
          max-width: 100% !important;
          page-break-after: always;
        }
        pre {
          background: #ffffff !important;
          color: #000000 !important;
          border: 1px solid #aaa !important;
          border-left: 3px solid #333 !important;
          page-break-inside: avoid;
        }
        code {
          background: #f5f5f5 !important;
          color: #000000 !important;
        }
        .section-box { page-break-inside: avoid; }
        .mermaid svg { max-width: 100% !important; }
      }
    </style>
"""

# ---------------------------------------------------------------
# Fix dark code block backgrounds that look like black boxes
# ---------------------------------------------------------------
def fix_code_blocks(html):
    # Remove any explicit dark backgrounds on pre/code
    html = re.sub(r'(<pre[^>]*style=["\'][^"\']*)(background[^;]*;)', 
                  lambda m: m.group(1) + 'background:#ffffff;color:#1e293b;', html)
    html = re.sub(r'background:\s*#[0-9a-fA-F]{3,6}\s*;([^"\']*)(font-family:[^;]*monospace)', 
                  r'background:#ffffff;\1\2', html)
    # Replace common dark code BG colors
    for dark_bg in ['#0f172a', '#1e1e2e', '#282c34', '#1a1a2e', '#0d0d0d', '#111827', '#1f2937', '#2d2d2d', '#333333']:
        html = html.replace(dark_bg, '#ffffff')
    # Replace green/white text colors on code
    for green_text in ['#4ade80', '#22c55e', '#86efac', '#a3e635']:
        html = html.replace(green_text, '#1e3a8a')
    return html

# ---------------------------------------------------------------
# Inject improved CSS into <head>
# ---------------------------------------------------------------
def inject_css(html, css):
    return html.replace('</head>', css + '\n</head>', 1)

# ---------------------------------------------------------------
# Process each Final HTML file
# ---------------------------------------------------------------
finals = [f for f in os.listdir(src_dir) if f.endswith('_Final.html')]
print(f"Found {len(finals)} Final HTML files to improve:")

for fname in sorted(finals):
    src_path = os.path.join(src_dir, fname)
    dst_path = os.path.join(dst_dir, fname)
    
    with open(src_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Apply fixes
    html = fix_code_blocks(html)
    html = inject_css(html, IMPROVED_CSS)
    
    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    src_size = os.path.getsize(src_path) / 1024
    dst_size = os.path.getsize(dst_path) / 1024
    print(f"  {fname}: {src_size:.1f} KB -> {dst_size:.1f} KB")

print("\nAll files processed and saved to v0/ folder!")
print("Files in v0/:")
for f in sorted(os.listdir(dst_dir)):
    print(f"  {f}")

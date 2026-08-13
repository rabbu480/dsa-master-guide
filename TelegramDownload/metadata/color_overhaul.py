"""
color_overhaul.py
-----------------
Completely rewrites the CSS in all v0 files with a new professional palette:

NEW DESIGN PHILOSOPHY:
- Section headers: Deep charcoal (#1a1a2a) with WHITE text — crisp, readable
- Accent color: Warm amber/orange (#f59e0b) for highlights — pops on screen AND xerox
- Code blocks: Light cream (#fffef7) with dark charcoal text — never dark bg
- Tables: Alternating white / very light gray — reads clearly on xerox
- Green/Red: Darker shades that xerox to visible grays (NOT light pastels)
- All backgrounds: white or near-white — safe for B&W printing
- Contrast ratios: All text >4.5:1 WCAG AA compliant
"""

import os
import re

v0_dir = r"C:\Users\rabba\Downloads\TelegramDownload\metadata\v0"

# ======================================================
# NEW MASTER CSS – replaces the old one entirely
# ======================================================
NEW_MASTER_CSS = """<style id="master-v1">
    /* =====================================================
       FAANG CHEAT SHEET — v1 Color Palette
       Tested for: Screen color | B&W xerox | PDF export
    ====================================================== */
    :root {
        /* Primary: Deep charcoal (NOT blue) — xerox safe, clean */
        --primary: #1c1c2e;
        --primary-soft: #2d2d44;
        
        /* Accent: Warm amber — visible on both color & xerox */
        --accent: #d97706;
        --accent-light: #fef3c7;
        --accent-border: #f59e0b;
        
        /* Section header backgrounds — each topic gets a distinct tone */
        --hdr-1: #1c1c2e;  /* charcoal (default) */
        --hdr-2: #164e63;  /* deep teal */
        --hdr-3: #14532d;  /* deep green */
        --hdr-4: #7c2d12;  /* deep orange-red */
        --hdr-5: #312e81;  /* deep indigo */
        
        /* Status colors — dark enough to xerox */
        --ok:   #15803d;  /* dark green */
        --warn: #b45309;  /* dark amber */
        --err:  #b91c1c;  /* dark red */
        
        /* Text */
        --text-body:    #111827;  /* near black */
        --text-sub:     #374151;  /* dark gray */
        --text-muted:   #6b7280;  /* mid gray */
        
        /* Backgrounds */
        --bg-page:      #f1f5f9;  /* light blue-gray page bg */
        --bg-card:      #ffffff;
        --bg-code:      #f8f8f2;  /* warm off-white for code */
        --bg-table-alt: #f9fafb;
        --bg-tip:       #f0fdf4;
        --bg-warn:      #fffbeb;
        --bg-danger:    #fef2f2;
        --bg-info:      #eff6ff;
        
        /* Borders */
        --border:       #d1d5db;
        --border-strong:#6b7280;
    }

    * { box-sizing: border-box; }

    body {
        font-family: 'Inter', system-ui, sans-serif;
        background-color: var(--bg-page);
        color: var(--text-body);
        margin: 0;
        padding: 24px;
        font-size: 13.5px;
        line-height: 1.5;
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
    }

    /* ---- PAGE CARD ---- */
    .page {
        background: var(--bg-card);
        max-width: 1120px;
        margin: 0 auto 48px auto;
        padding: 36px 40px;
        box-shadow: 0 2px 16px rgba(0,0,0,0.08), 0 0 0 1px rgba(0,0,0,0.04);
        border-radius: 10px;
        page-break-after: always;
        border-top: 4px solid var(--accent);
    }

    /* ---- PAGE HEADER ---- */
    .header-top {
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 2px solid var(--primary);
        padding-bottom: 12px;
        margin-bottom: 22px;
    }
    .header-top h1 {
        margin: 0;
        font-size: 2.2rem;
        color: var(--primary);
        font-weight: 900;
        letter-spacing: -0.5px;
    }
    .header-top .subtitle {
        font-size: 1rem;
        font-weight: 500;
        color: var(--text-sub);
        margin-top: 4px;
    }
    .header-top .page-number {
        background: var(--primary);
        color: white;
        padding: 6px 18px;
        border-radius: 20px;
        font-weight: 700;
        font-size: 0.9rem;
        letter-spacing: 1px;
    }

    /* ---- GRID ---- */
    .grid-container {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 18px;
    }
    .col-left, .col-right { min-width: 0; }

    /* ---- SECTION BOX ---- */
    .section-box {
        border: 1px solid var(--border);
        border-radius: 8px;
        overflow: hidden;
        margin-bottom: 18px;
        background: var(--bg-card);
        box-shadow: 0 1px 4px rgba(0,0,0,0.05);
    }
    .section-box:hover { box-shadow: 0 2px 8px rgba(0,0,0,0.1); }

    /* ---- SECTION HEADERS — charcoal by default, accent left border ---- */
    .section-header {
        background: var(--primary);
        color: #ffffff;
        padding: 9px 14px;
        font-weight: 700;
        font-size: 0.82rem;
        letter-spacing: 0.8px;
        text-transform: uppercase;
        display: flex;
        align-items: center;
        border-left: 4px solid var(--accent);
    }
    .section-header span.num {
        background: var(--accent);
        color: var(--primary);
        border-radius: 50%;
        width: 22px; height: 22px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        margin-right: 10px;
        font-size: 0.78rem;
        font-weight: 900;
        flex-shrink: 0;
    }

    /* Override inline bg colors that subagents set on section-header */
    .section-header[style*="background"] { background: var(--primary) !important; color: white !important; }

    /* ---- SECTION CONTENT ---- */
    .section-content { padding: 14px 16px; }

    /* ---- LISTS ---- */
    ul, ol { margin: 6px 0; padding-left: 20px; }
    li { margin-bottom: 6px; color: var(--text-body); }

    /* ---- TABLES ---- */
    table { width: 100%; border-collapse: collapse; font-size: 0.85rem; margin: 8px 0; }
    table th {
        background: var(--primary) !important;
        color: #ffffff !important;
        padding: 8px 10px;
        font-weight: 600;
        font-size: 0.8rem;
        text-align: left;
        letter-spacing: 0.4px;
    }
    table td {
        border: 1px solid var(--border);
        padding: 7px 10px;
        text-align: left;
        vertical-align: top;
    }
    table tr:nth-child(even) td { background: var(--bg-table-alt); }
    table tr:nth-child(odd) td { background: #ffffff; }
    table tbody tr:hover td { background: var(--accent-light); }

    /* ---- CODE BLOCKS — cream bg, charcoal text — ALWAYS printable ---- */
    pre {
        background: var(--bg-code) !important;
        color: var(--text-body) !important;
        border: 1px solid var(--border) !important;
        border-left: 4px solid var(--accent) !important;
        padding: 12px 14px !important;
        border-radius: 6px !important;
        font-family: 'Fira Code', 'Courier New', monospace !important;
        font-size: 0.8rem !important;
        margin: 10px 0 !important;
        overflow-x: auto;
        white-space: pre-wrap;
        word-break: break-word;
        line-height: 1.6;
        box-shadow: none !important;
    }
    /* Inline code */
    code {
        background: #f3f4f6 !important;
        color: #1c1c2e !important;
        border: 1px solid var(--border) !important;
        padding: 1px 5px !important;
        border-radius: 4px !important;
        font-family: 'Fira Code', 'Courier New', monospace !important;
        font-size: 0.85em !important;
        box-shadow: none !important;
    }
    pre code {
        background: transparent !important;
        color: inherit !important;
        border: none !important;
        padding: 0 !important;
    }

    /* ---- FLEX UTILS ---- */
    .flex-row { display: flex; gap: 16px; }
    .flex-col { flex: 1; text-align: center; min-width: 0; }

    /* ---- BADGES (status) ---- */
    .bg-green { background: var(--ok); color: white; padding: 4px 10px; border-radius: 4px; font-weight: 700; font-size: 0.82rem; display: inline-block; }
    .bg-red   { background: var(--err); color: white; padding: 4px 10px; border-radius: 4px; font-weight: 700; font-size: 0.82rem; display: inline-block; }
    .bg-amber { background: var(--warn); color: white; padding: 4px 10px; border-radius: 4px; font-weight: 700; font-size: 0.82rem; display: inline-block; }

    /* Difficulty badges */
    .diff-easy   { color: var(--ok); font-weight: 700; }
    .diff-medium { color: var(--warn); font-weight: 700; }
    .diff-hard   { color: var(--err); font-weight: 700; }

    /* Complexity badges */
    .badge-o1   { display:inline-block; background:#dcfce7; color:#14532d; padding:2px 7px; border-radius:4px; font-weight:700; font-size:0.75rem; border:1px solid #15803d; }
    .badge-olog { display:inline-block; background:#e0f2fe; color:#164e63; padding:2px 7px; border-radius:4px; font-weight:700; font-size:0.75rem; border:1px solid #0369a1; }
    .badge-on   { display:inline-block; background:var(--accent-light); color:#92400e; padding:2px 7px; border-radius:4px; font-weight:700; font-size:0.75rem; border:1px solid var(--warn); }
    .badge-on2  { display:inline-block; background:#fee2e2; color:#7f1d1d; padding:2px 7px; border-radius:4px; font-weight:700; font-size:0.75rem; border:1px solid var(--err); }

    /* ---- CALLOUT / RULE BOXES ---- */
    .rule-box, .callout-warn {
        background: var(--bg-warn);
        border: 1px solid var(--accent-border);
        border-left: 5px solid var(--accent-border);
        padding: 10px 14px;
        margin: 10px 0;
        border-radius: 0 6px 6px 0;
        font-size: 0.88rem;
    }
    .callout-tip {
        background: var(--bg-tip);
        border: 1px solid #16a34a;
        border-left: 5px solid #16a34a;
        padding: 10px 14px;
        margin: 10px 0;
        border-radius: 0 6px 6px 0;
        font-size: 0.88rem;
    }
    .callout-danger {
        background: var(--bg-danger);
        border: 1px solid var(--err);
        border-left: 5px solid var(--err);
        padding: 10px 14px;
        margin: 10px 0;
        border-radius: 0 6px 6px 0;
        font-size: 0.88rem;
    }
    .callout-info {
        background: var(--bg-info);
        border: 1px solid #2563eb;
        border-left: 5px solid #2563eb;
        padding: 10px 14px;
        margin: 10px 0;
        border-radius: 0 6px 6px 0;
        font-size: 0.88rem;
    }

    /* ---- MERMAID ---- */
    .mermaid { display: flex; justify-content: center; margin: 12px 0; }

    /* ---- FULL-WIDTH ELEMENTS ---- */
    .full-width { grid-column: 1 / -1; }

    /* ---- SUPPRESS INVISIBLE COMBOS ----
       Yellow on white = invisible. Force dark text on any yellow/light bg */
    [style*="color: yellow"], [style*="color:yellow"],
    [style*="color: #ffff"], [style*="color:#ffff"],
    [style*="color: #fff0"], [style*="color:#fff0"],
    [style*="color: #ffd"], [style*="color:#ffd"] {
        color: var(--warn) !important;
    }
    /* White text on white bg = invisible. Override */
    [style*="color: white"][style*="background: white"],
    [style*="color: #fff"][style*="background: #fff"],
    [style*="color:white"][style*="background:white"] {
        color: var(--text-body) !important;
    }
    /* Light text that subagents set inline */
    [style*="color: #94a3b8"], [style*="color:#94a3b8"],
    [style*="color: #cbd5e1"], [style*="color:#cbd5e1"],
    [style*="color: #e2e8f0"], [style*="color:#e2e8f0"] {
        color: var(--text-sub) !important;
    }

    /* ---- PRINT / XEROX SAFE ---- */
    @media print {
        body {
            background: white !important;
            padding: 0 !important;
            font-size: 11px !important;
        }
        .page {
            box-shadow: none !important;
            border: none !important;
            border-top: 3px solid #000 !important;
            margin: 0 !important;
            padding: 12px !important;
            max-width: 100% !important;
            page-break-after: always;
        }
        .section-header {
            background: #000000 !important;
            color: #ffffff !important;
            border-left: 4px solid #666 !important;
            -webkit-print-color-adjust: exact;
            print-color-adjust: exact;
        }
        table th {
            background: #000000 !important;
            color: #ffffff !important;
            -webkit-print-color-adjust: exact;
            print-color-adjust: exact;
        }
        table tr:nth-child(even) td {
            background: #f0f0f0 !important;
        }
        pre {
            background: #f8f8f8 !important;
            color: #000000 !important;
            border: 1px solid #aaa !important;
            border-left: 3px solid #000 !important;
            page-break-inside: avoid;
        }
        code {
            background: #eeeeee !important;
            color: #000000 !important;
        }
        .callout-tip, .callout-warn, .callout-danger, .callout-info, .rule-box {
            border-left-width: 3px !important;
            border-color: #555 !important;
            background: #f5f5f5 !important;
        }
        .section-box { page-break-inside: avoid; }
        .mermaid svg { max-width: 100% !important; }
        a { color: inherit; text-decoration: none; }
    }
</style>"""

# =====================================================
# Fix problematic inline color combinations
# =====================================================
def fix_inline_colors(html):
    # 1. Fix inline dark section headers set by subagents
    # Pattern: style="background: #1e3a8a; color: white;" or similar
    # We want to KEEP these dark headers since they look good with our new CSS
    
    # 2. Fix any yellow/light text on light backgrounds (invisible combos)
    # Yellow text → amber
    html = re.sub(r'color:\s*#[fF]{3,4}[dDeE][dDeE][dDeE]', 'color:#92400e', html)  # yellow shades → dark amber
    html = re.sub(r'color:\s*yellow', 'color:#92400e', html)
    
    # 3. Fix very light gray text (invisible on screen & xerox)
    # #94a3b8, #cbd5e1, #e2e8f0 → darker
    html = html.replace('color: #94a3b8', 'color: #4b5563')
    html = html.replace('color:#94a3b8', 'color:#4b5563')
    html = html.replace('color: #cbd5e1', 'color: #374151')
    html = html.replace('color:#cbd5e1', 'color:#374151')
    html = html.replace('color: #e2e8f0', 'color: #374151')
    html = html.replace('color:#e2e8f0', 'color:#374151')
    
    # 4. Fix green text on white (often bad contrast)
    # #4ade80, #86efac, #a3e635 → dark green
    for light_green in ['#4ade80', '#86efac', '#a3e635', '#bbf7d0']:
        html = html.replace(f'color: {light_green}', 'color: #15803d')
        html = html.replace(f'color:{light_green}', 'color:#15803d')
    
    # 5. Fix light blue text (invisible on white)
    for light_blue in ['#93c5fd', '#bfdbfe', '#dbeafe']:
        html = html.replace(f'color: {light_blue}', 'color: #1d4ed8')
        html = html.replace(f'color:{light_blue}', 'color:#1d4ed8')
    
    # 6. Fix code dark backgrounds (inline style on pre/code)
    dark_code_bgs = ['#1e1e2e', '#0f172a', '#282c34', '#1a1a2e', '#111827', 
                     '#0d0d0d', '#1f2937', '#2d2d2d', '#333333', '#272822',
                     '#1e293b']  # near-black bg
    for bg in dark_code_bgs:
        html = html.replace(f'background:{bg}', 'background:#f8f8f2')
        html = html.replace(f'background: {bg}', 'background: #f8f8f2')
        html = html.replace(f'background-color:{bg}', 'background-color:#f8f8f2')
        html = html.replace(f'background-color: {bg}', 'background-color: #f8f8f2')
    
    # 7. Fix green code text (was for dark bg, bad on light bg)
    code_green_texts = ['#4ade80', '#22c55e', '#86efac', '#a3e635', 
                        '#00ff00', '#39ff14', '#00e600']
    for green in code_green_texts:
        html = html.replace(f'color:{green}', 'color:#111827')
        html = html.replace(f'color: {green}', 'color: #111827')
    
    return html

# =====================================================
# Replace old master CSS block with new one
# =====================================================
def replace_css(html, new_css):
    # Remove old <style> blocks (keep only the first one and replace it)
    # The original CSS is between first <style> and </style>
    first_style_start = html.find('<style>')
    if first_style_start == -1:
        first_style_start = html.find('<style id=')
    
    # Find the end of the FIRST style block
    first_style_end = html.find('</style>', first_style_start) + len('</style>')
    
    if first_style_start == -1 or first_style_end < len('</style>'):
        print("WARNING: Could not find style block!")
        return html
    
    # Replace just the first CSS block
    html = html[:first_style_start] + new_css + html[first_style_end:]
    
    # Now remove the second style block added by improve_and_copy.py (the v0 improvements)
    # Find <!-- v0 Improvements --> block
    v0_comment = '<!-- v0 Improvements: FAANG-ready, print-friendly -->'
    v0_start = html.find(v0_comment)
    if v0_start > 0:
        # Find the style tag before the comment
        style_tag_start = html.rfind('<style', 0, v0_start)
        if style_tag_start > 0:
            v0_style_end = html.find('</style>', v0_start) + len('</style>')
            html = html[:style_tag_start] + html[v0_style_end:]
    
    return html

# =====================================================
# Process all v0 files
# =====================================================
files = [f for f in os.listdir(v0_dir) if f.endswith('_Final.html')]
print(f"Processing {len(files)} files in v0/...")

for fname in sorted(files):
    fpath = os.path.join(v0_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Step 1: Fix inline color issues
    html = fix_inline_colors(html)
    
    # Step 2: Replace CSS
    html = replace_css(html, NEW_MASTER_CSS)
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(html)
    
    size_kb = os.path.getsize(fpath) / 1024
    print(f"  OK [{size_kb:.1f} KB] {fname}")

print("\nColor overhaul complete!")
print("\nNew palette summary:")
print("  Section headers: Deep charcoal #1c1c2e (prints solid black on xerox)")
print("  Accent/highlight: Warm amber #d97706 (visible on color AND xerox)")
print("  Table headers: Black bg / white text (xerox safe)")
print("  Code blocks: Cream #f8f8f2 / charcoal text (never dark bg)")
print("  Text: Near-black #111827 on white (max contrast)")
print("  Callout boxes: Light tinted bg / dark border (distinct on xerox)")

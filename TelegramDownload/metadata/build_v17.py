import os
import re
from bs4 import BeautifulSoup
import glob

v10_dir = r"C:\Users\rabba\Downloads\TelegramDownload\metadata\v10"
v17_dir = r"C:\Users\rabba\Downloads\TelegramDownload\metadata\v17"
os.makedirs(v17_dir, exist_ok=True)

THEME_COLORS = [
    ('#059669', '#d1fae5'), # Emerald Green
    ('#2563eb', '#dbeafe'), # Royal Blue
    ('#7c3aed', '#ede9fe'), # Violet
    ('#ea580c', '#ffedd5'), # Orange
    ('#db2777', '#fce7f3'), # Pink
    ('#0284c7', '#e0f2fe'), # Light Blue
    ('#16a34a', '#dcfce7')  # Bright Green
]

def is_dark(color_str):
    color_str = color_str.strip().lower()
    if color_str in ['black', 'darkblue', 'navy', 'purple']: return True
    if color_str in ['white', 'yellow', 'transparent', 'none']: return False
    
    if color_str.startswith('#'):
        c = color_str.lstrip('#')
        if len(c) == 3: c = ''.join([x*2 for x in c])
        if len(c) == 6:
            try:
                r, g, b = int(c[0:2], 16), int(c[2:4], 16), int(c[4:6], 16)
                hsp = (0.299 * (r * r) + 0.587 * (g * g) + 0.114 * (b * b))**0.5
                return hsp < 127.5
            except:
                pass
    
    rgb_match = re.search(r'rgba?\s*\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)', color_str)
    if rgb_match:
        r, g, b = map(int, rgb_match.groups())
        hsp = (0.299 * (r * r) + 0.587 * (g * g) + 0.114 * (b * b))**0.5
        return hsp < 127.5
        
    return False

def clean_styles(soup):
    for tag in soup.find_all(True):
        if not tag.has_attr('style'): continue
        
        style = tag['style']
        new_style = []
        for prop in style.split(';'):
            prop = prop.strip()
            if not prop: continue
            if ':' not in prop:
                new_style.append(prop)
                continue
                
            key, val = [x.strip() for x in prop.split(':', 1)]
            key_lower = key.lower()
            
            # Remove explicit heights that cause overlapping
            if key_lower == 'height' or key_lower == 'max-height':
                continue
            
            if key_lower in ['background', 'background-color']:
                color_match = re.search(r'(#[a-fA-F0-9]+|rgba?\([^)]+\)|[a-zA-Z]+)', val)
                if color_match and is_dark(color_match.group(1)):
                    new_style.append('color: #0f172a !important')
                    new_style.append('background-color: #f8fafc !important')
                    continue
            
            if key_lower == 'color':
                color_match = re.search(r'(#[a-fA-F0-9]+|rgba?\([^)]+\)|[a-zA-Z]+)', val)
                if color_match and not is_dark(color_match.group(1)):
                    if color_match.group(1) not in ['#fbbf24', 'yellow', 'gold']:
                        val = '#0f172a !important'
                    
            new_style.append(f"{key}: {val}")
            
        tag['style'] = '; '.join(new_style)

def inject_multicolor(soup):
    boxes = soup.find_all('div', class_='section-box')
    for i, box in enumerate(boxes):
        border_color, bg_color = THEME_COLORS[i % len(THEME_COLORS)]
        box['style'] = box.get('style', '') + f'; border: 2px solid {border_color} !important;'
        hdr = box.find('div', class_='section-header')
        if hdr:
            hdr['style'] = hdr.get('style', '') + f'; background-color: {bg_color} !important; color: {border_color} !important; font-weight: 900 !important; border-bottom: 2px solid {border_color};'

def add_faang_patterns(fname, soup):
    if "Array" in fname:
        tbl = soup.find('table')
        if tbl:
            tbl.append(BeautifulSoup("""
            <tr style="border-bottom: 1px solid #e2e8f0;">
                <td style="padding: 8px 0; font-weight:bold;">🪟</td>
                <td style="padding: 8px 0;">Contiguous Subarray?</td>
                <td style="padding: 8px 0; font-weight: bold;">Sliding Window</td>
            </tr>
            <tr style="border-bottom: 1px solid #e2e8f0;">
                <td style="padding: 8px 0; font-weight:bold;">➕🗺️</td>
                <td style="padding: 8px 0;">Subarray Sum = K?</td>
                <td style="padding: 8px 0; font-weight: bold;">Prefix Sum + HashMap</td>
            </tr>
            """, 'html.parser'))
            
def fix_sudoku(html):
    return re.sub(r'36\.\s*Valid Sudoku.*?</tr>', 
                  r'''36. Valid Sudoku</td>
                  <td>Validate rows, cols, and 3x3 grids</td>
                  <td>Use HashSet to track seen numbers</td>
                  <td>
                    <strong>Row/Col/Box:</strong><br>
                    <pre style="white-space: pre-wrap !important;">for(int i=0;i<9;i++)
  for(int j=0;j<9;j++)
    if(!set.add(board[i][j])) return false;</pre>
                  </td></tr>''', 
                  html, flags=re.DOTALL)

def fix_heaps_order(soup):
    pages = soup.find_all('div', class_='page')
    if len(pages) >= 3:
        seen_texts = set()
        for p in pages:
            txt = p.text[:500]
            if txt in seen_texts:
                p.decompose()
            else:
                seen_texts.add(txt)

def process_file(fname):
    src_path = os.path.join(v10_dir, fname)
    dst_path = os.path.join(v17_dir, fname)
    
    with open(src_path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    if "Array" in fname:
        html = fix_sudoku(html)
        
    soup = BeautifulSoup(html, 'html.parser')
    
    # Core V14 Logic
    clean_styles(soup)
    
    # FAANG Patterns
    add_faang_patterns(fname, soup)
    
    # Extra V17 Fixes
    if "Heap" in fname:
        fix_heaps_order(soup)
        
    if "Tree" in fname or "Graph" in fname:
        inject_multicolor(soup)
    
    # Global Screen/Print CSS to fix Code Blocks (mixes/overlaps) and PDF gaps
    style_tag = soup.find('style')
    if style_tag:
        style_tag.append("""
        /* FIX CODE BLOCKS MIXING / NO NEWLINES */
        pre, code {
            white-space: pre-wrap !important;
            word-wrap: break-word !important;
            display: block !important;
            line-height: 1.5 !important;
        }
        
        /* HARDCORE PRINT SETTINGS (Keep Colors, Prevent 24 pages) */
        @media print {
            body { padding: 0 !important; margin: 0 !important; -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
            .page { 
                page-break-after: auto !important; 
                page-break-inside: avoid !important;
                margin-bottom: 20px !important; 
                box-shadow: none !important; 
                zoom: 0.72; 
            }
            .section-box, .content-grid {
                page-break-inside: avoid !important;
                break-inside: avoid !important;
            }
            th { background-color: #e2e8f0 !important; font-size: 14px !important; color: #000 !important; }
        }
        """)

    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"Generated V17: {fname}")

for fname in os.listdir(v10_dir):
    if fname.endswith('_Final.html'):
        process_file(fname)

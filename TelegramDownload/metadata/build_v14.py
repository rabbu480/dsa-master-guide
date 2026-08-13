import os
import re
from bs4 import BeautifulSoup
import glob

v10_dir = r"C:\Users\rabba\Downloads\TelegramDownload\metadata\v10" # Let's go back to v10 which was the clean base before I started messing with headers and backgrounds
v14_dir = r"C:\Users\rabba\Downloads\TelegramDownload\metadata\v14"
os.makedirs(v14_dir, exist_ok=True)

# Helper to check if a color is dark
def is_dark(color_str):
    color_str = color_str.strip().lower()
    # Handle named colors
    if color_str in ['black', 'darkblue', 'navy', 'purple']: return True
    if color_str in ['white', 'yellow', 'transparent', 'none']: return False
    
    # Handle hex
    if color_str.startswith('#'):
        c = color_str.lstrip('#')
        if len(c) == 3: c = ''.join([x*2 for x in c])
        if len(c) == 6:
            try:
                r, g, b = int(c[0:2], 16), int(c[2:4], 16), int(c[4:6], 16)
                # HSP equation
                hsp = (0.299 * (r * r) + 0.587 * (g * g) + 0.114 * (b * b))**0.5
                return hsp < 127.5
            except:
                pass
    
    # Handle rgb/rgba
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
            
            # If it's a background color and it's dark, strip it
            if key_lower in ['background', 'background-color']:
                # Extract color value (naive extraction, works for simple styles)
                color_match = re.search(r'(#[a-fA-F0-9]+|rgba?\([^)]+\)|[a-zA-Z]+)', val)
                if color_match and is_dark(color_match.group(1)):
                    # Don't add this property (we strip it)
                    # And force text color to dark so it's readable
                    new_style.append('color: #0f172a !important')
                    # Give it a very light background so it's not totally transparent if it was a box
                    new_style.append('background-color: #f8fafc !important')
                    continue
            
            # If it's a text color and it's light, and we are not keeping a dark background
            if key_lower == 'color':
                color_match = re.search(r'(#[a-fA-F0-9]+|rgba?\([^)]+\)|[a-zA-Z]+)', val)
                if color_match and not is_dark(color_match.group(1)):
                    # Check if the parent has a dark background we are keeping. 
                    # But wait, we are stripping ALL dark backgrounds. So light text is ALWAYS bad.
                    # Convert light text to dark text!
                    if color_match.group(1) not in ['#fbbf24', 'yellow', 'gold']: # Keep yellows since they contrast okayish on white
                        val = '#0f172a !important'
                    
            new_style.append(f"{key}: {val}")
            
        tag['style'] = '; '.join(new_style)

# Apply FAANG patterns from v12 directly
def add_faang_patterns(fname, soup):
    if "Array" in fname:
        tbl = soup.find('table') # Naive append for array
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
            
def process_file(fname):
    src_path = os.path.join(v10_dir, fname)
    dst_path = os.path.join(v14_dir, fname)
    
    with open(src_path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    
    # 1. Smart Clean Styles
    clean_styles(soup)
    
    # 2. Add FAANG
    add_faang_patterns(fname, soup)
    
    # 3. Global print CSS
    style_tag = soup.find('style')
    if style_tag:
        style_tag.append("""
        /* Hardcore Print Optimizations */
        @media print {
            body { padding: 0 !important; margin: 0 !important; background: white !important; }
            * { color: #0f172a !important; text-shadow: none !important; }
            .page { page-break-after: always; margin-bottom: 0 !important; padding: 10px !important; box-shadow: none !important; border: none !important; zoom: 0.72; }
            .section-box { page-break-inside: avoid; }
            pre, code { background: #f1f5f9 !important; color: #b91c1c !important; }
            th { background: #e2e8f0 !important; font-size: 14px !important; color: #000 !important; }
        }
        """)

    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"Generated V14 {fname}")

for fname in os.listdir(v10_dir):
    if fname.endswith('_Final.html'):
        process_file(fname)

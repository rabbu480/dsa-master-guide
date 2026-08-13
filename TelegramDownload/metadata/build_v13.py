import os
import re
from bs4 import BeautifulSoup

src_dir = r"C:\Users\rabba\Downloads\TelegramDownload\metadata\v12" # Read from v12 since it has Array FAANG updates
v13_dir = r"C:\Users\rabba\Downloads\TelegramDownload\metadata\v13"
os.makedirs(v13_dir, exist_ok=True)

# Rainbow colors for Trees and Graphs
THEME_COLORS = [
    ('#059669', '#d1fae5'), # Emerald Green
    ('#2563eb', '#dbeafe'), # Royal Blue
    ('#7c3aed', '#ede9fe'), # Violet
    ('#ea580c', '#ffedd5'), # Orange
    ('#db2777', '#fce7f3'), # Pink
    ('#0284c7', '#e0f2fe'), # Light Blue
    ('#16a34a', '#dcfce7')  # Bright Green
]

def clean_dark_backgrounds(soup):
    for tag in soup.find_all(True):
        if not tag.has_attr('style'): continue
        
        style = tag['style']
        # Remove any dark background colors entirely
        # 1e1e1e (dark gray/black), 1a365d (dark blue), black, 000000
        style = re.sub(r'background-color:\s*(#1e1e1e|#1a365d|black|#000000);?', '', style, flags=re.IGNORECASE)
        style = re.sub(r'background:\s*(#1e1e1e|#1a365d|black|#000000);?', '', style, flags=re.IGNORECASE)
        
        # If the tag's color was forced to white, but we just removed the dark bg, the text will be invisible on white paper!
        # So we must also remove color: white if we removed a dark background, OR force it to black/primary.
        style = re.sub(r'color:\s*(white|#fff|#ffffff);?', 'color: #0f172a;', style, flags=re.IGNORECASE)
        
        tag['style'] = style

def fix_array_sudoku(soup):
    sudoku = soup.find(string=re.compile('36\. Valid Sudoku'))
    if sudoku:
        box = sudoku.find_parent('div', class_='section-box')
        if box:
            tbl = box.find('table')
            if tbl:
                for row in tbl.find_all('tr'):
                    if '36. Valid Sudoku' in row.text:
                        # Fix the code cell
                        tds = row.find_all('td')
                        if len(tds) >= 4:
                            # It's usually the 3rd or 4th column that holds code
                            tds[3].clear()
                            tds[3].append(BeautifulSoup("<div><strong>Row/Col/Box:</strong></div><pre>for(int i=0;i<9;i++)\n  for(int j=0;j<9;j++)\n    if(!set.add(board[i][j])) return false;</pre>", 'html.parser'))

def inject_multicolor(soup):
    boxes = soup.find_all('div', class_='section-box')
    for i, box in enumerate(boxes):
        border_color, bg_color = THEME_COLORS[i % len(THEME_COLORS)]
        
        # Set border color for the box
        box['style'] = box.get('style', '') + f'; border: 2px solid {border_color} !important;'
        
        # Set header color
        hdr = box.find('div', class_='section-header')
        if hdr:
            hdr['style'] = hdr.get('style', '') + f'; background-color: {bg_color} !important; color: {border_color} !important; font-weight: 900 !important; border-bottom: 2px solid {border_color};'

def fix_graph_zigzag(soup):
    # Ensure all grids flow sequentially
    for grid in soup.find_all(style=re.compile(r'display:\s*grid')):
        # Remove weird grid templates that might force column flows
        style = grid['style']
        style = re.sub(r'grid-template-columns:[^;]+;', 'grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));', style)
        grid['style'] = style

def add_faang_concepts(fname, soup):
    if "Heap" in fname:
        # Check if Median from Data Stream is mentioned
        if "Median from Data Stream" not in soup.text:
            # Find a place to append Two Heaps
            hdr = soup.find(string=re.compile('PATTERN'))
            if hdr:
                box = hdr.find_parent('div', class_='section-box')
                if box:
                    parent = box.parent
                    parent.append(BeautifulSoup(f"""
                    <div class="section-box" style="border: 2px solid #db2777; margin-top: 15px;">
                        <div class="section-header" style="background-color: #fce7f3; color: #db2777; padding: 8px; font-weight: bold;">TWO HEAPS PATTERN (FAANG TRAP)</div>
                        <div class="section-content" style="padding: 10px;">
                            <p><strong>Problem:</strong> Find Median from Data Stream (LC 295)</p>
                            <p><strong>Key Idea:</strong> Maintain a Max Heap for the lower half of numbers, and a Min Heap for the upper half. Keep them balanced (size difference <= 1).</p>
                        </div>
                    </div>
                    """, 'html.parser'))
                    
    if "Tree" in fname:
        if "Lowest Common Ancestor" not in soup.text:
            hdr = soup.find(string=re.compile('ADVANCED'))
            if hdr:
                box = hdr.find_parent('div', class_='section-box')
                if box:
                    content = box.find('div', class_='section-content')
                    if content:
                        content.append(BeautifulSoup("""
                        <div style="margin-top:10px; border-top: 1px solid #ccc; padding-top: 10px;">
                            <strong>Lowest Common Ancestor (LCA)</strong>: Very common FAANG question. If both nodes are smaller than root, go left. If both larger, go right. Else, root is LCA.
                        </div>
                        """, 'html.parser'))

def process_file(fname):
    src_path = os.path.join(src_dir, fname)
    dst_path = os.path.join(v13_dir, fname)
    
    with open(src_path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    
    # 1. Strip dark backgrounds and fix text colors
    clean_dark_backgrounds(soup)
    
    # Also fix header-top backgrounds that were explicitly added in v11
    for hdr_top in soup.find_all('div', class_='header-top'):
        hdr_top['style'] = hdr_top.get('style', '').replace('background-color: #1a365d;', '').replace('color: white;', 'color: #0f172a;')
    
    # 2. Add FAANG missing concepts
    add_faang_concepts(fname, soup)
    
    if "Array" in fname:
        fix_array_sudoku(soup)
        
    if "Tree" in fname or "Graph" in fname:
        inject_multicolor(soup)
        
    if "Graph" in fname:
        fix_graph_zigzag(soup)
        
    # Global print adjustments
    style_tag = soup.find('style')
    if style_tag:
        style_tag.append("""
        /* V13 Print Optimizations */
        @media print {
            body { padding: 0 !important; margin: 0 !important; background: white !important; }
            /* Use a safer zoom to ensure no massive blank spaces, and allow flexible heights */
            .page { page-break-after: always; margin-bottom: 0 !important; padding: 10px !important; box-shadow: none !important; border: none !important; }
            .section-box { page-break-inside: avoid; }
        }
        """)

    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"[{os.path.getsize(dst_path)//1024}KB] {fname} -> V13 FAANG Cleaned")

for fname in os.listdir(src_dir):
    if fname.endswith('_Final.html'):
        process_file(fname)

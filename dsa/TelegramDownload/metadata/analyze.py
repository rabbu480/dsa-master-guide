import os, glob
from bs4 import BeautifulSoup

def analyze(fname):
    print(f'\\n--- {os.path.basename(fname)} ---')
    with open(fname, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    # Check dark backgrounds
    dark_boxes = soup.find_all(style=lambda v: v and ('#1e1e1e' in v.lower() or '#1a365d' in v.lower() or 'black' in v.lower() or '#000000' in v.lower()))
    print(f'Dark boxes found: {len(dark_boxes)}')
    
    # Check Sudoku Code
    sudoku = soup.find(string=lambda t: t and '36. Valid Sudoku' in t)
    if sudoku:
        parent = sudoku.find_parent('tr')
        if parent:
            print('Sudoku table row found.')
        else:
            print('Sudoku not in a tr.')
            
    # Check tree/graph colors
    headers = soup.find_all('div', class_='section-header')
    colors = set()
    for h in headers:
        if h.has_attr('style'):
            # Extract background-color using regex
            import re
            match = re.search(r'background-color:\s*(#[a-fA-F0-9]+)', h['style'])
            if match:
                colors.add(match.group(1))
    print(f'Unique header styles: {len(colors)}')

for f in glob.glob(r'C:\\Users\\rabba\\Downloads\\TelegramDownload\\metadata\\v12\\*_Final.html'):
    analyze(f)

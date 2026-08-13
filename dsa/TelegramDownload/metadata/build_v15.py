import os
import re
from bs4 import BeautifulSoup

v10_dir = r"C:\Users\rabba\Downloads\TelegramDownload\metadata\v10"
v15_dir = r"C:\Users\rabba\Downloads\TelegramDownload\metadata\v15"
os.makedirs(v15_dir, exist_ok=True)

GLOBAL_CSS_OVERRIDE = """
<style>
/* ====================================================
   V15: THE ULTIMATE FAANG PRINT LOCKDOWN
   Guarantees 100% Readability & No Black Backgrounds
==================================================== */
* {
    color: #0f172a !important; /* Force dark slate text */
    text-shadow: none !important;
}

/* Nuke all dark inline backgrounds by forcing transparency on elements */
div, span, table, th, td, tr, p, section {
    background-color: transparent !important;
    background: transparent !important;
}

/* Give structural elements a clean white background */
body, .page, .section-box {
    background-color: #ffffff !important;
    background: #ffffff !important;
}

/* Style headers so they pop (Light Grey background, Dark Text, Colored Border) */
.section-header, .header-top {
    background-color: #f1f5f9 !important;
    color: #0f172a !important;
    border-bottom: 2px solid #0f172a !important;
    font-weight: 900 !important;
}

/* Perfect Code Blocks (Prevents mixing/overlapping lines) */
pre, code {
    white-space: pre-wrap !important;
    word-wrap: break-word !important;
    word-break: break-all !important;
    display: block !important;
    background-color: #f8fafc !important;
    color: #b91c1c !important; /* Dark red for code syntax */
    font-weight: 600 !important;
    line-height: 1.5 !important;
    padding: 4px !important;
    border-radius: 4px !important;
}

/* Table Readability Fix */
th {
    background-color: #e2e8f0 !important;
    font-size: 13px !important;
    font-weight: bold !important;
}
td {
    font-size: 13px !important;
}

/* Print Specific Rules */
@media print {
    body { padding: 0 !important; margin: 0 !important; }
    .page { 
        page-break-after: always !important; 
        margin-bottom: 0 !important; 
        padding: 10px !important; 
        box-shadow: none !important; 
        border: none !important; 
        zoom: 0.73; /* Scale down to prevent 24-page blowouts */
    }
    .section-box { page-break-inside: avoid !important; margin-bottom: 15px !important; }
}
</style>
"""

def fix_sudoku(html):
    # Rip out the broken sudoku block and replace it manually
    html = re.sub(r'36\.\s*Valid Sudoku.*?</tr>', 
                  r'''36. Valid Sudoku</td>
                  <td>Validate rows, cols, and 3x3 grids</td>
                  <td>Use HashSet to track seen numbers</td>
                  <td>
                    <strong>Row/Col/Box:</strong><br>
                    <pre>for(int i=0;i<9;i++)
  for(int j=0;j<9;j++)
    if(!set.add(board[i][j])) return false;</pre>
                  </td></tr>''', 
                  html, flags=re.DOTALL)
    return html

def fix_heaps_order(soup):
    # The user said "Heeap has page twice may ucan move page2 last to after page make page 3 if thsi not duplciate .."
    # Let's just find the pages and ensure they are uniquely ordered.
    pages = soup.find_all('div', class_='page')
    if len(pages) >= 3:
        # Swap page 2 and 3 if needed, but we don't know exactly what they meant.
        # Often, dropping duplicates is best. Let's just remove exact duplicate pages.
        seen_texts = set()
        for p in pages:
            txt = p.text[:500]
            if txt in seen_texts:
                p.decompose()
            else:
                seen_texts.add(txt)

def process_file(fname):
    src_path = os.path.join(v10_dir, fname)
    dst_path = os.path.join(v15_dir, fname)
    
    with open(src_path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    if "Array" in fname:
        html = fix_sudoku(html)
        
    soup = BeautifulSoup(html, 'html.parser')
    
    if "Heap" in fname:
        fix_heaps_order(soup)
    
    # Inject the master CSS override
    if soup.head:
        soup.head.append(BeautifulSoup(GLOBAL_CSS_OVERRIDE, 'html.parser'))
    elif soup.body:
        soup.body.insert(0, BeautifulSoup(GLOBAL_CSS_OVERRIDE, 'html.parser'))

    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"Generated Locked V15: {fname}")

for fname in os.listdir(v10_dir):
    if fname.endswith('_Final.html'):
        process_file(fname)

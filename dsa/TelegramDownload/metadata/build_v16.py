import os
import re
from bs4 import BeautifulSoup
import glob

v10_dir = r"C:\Users\rabba\Downloads\TelegramDownload\metadata\v10"
v16_dir = r"C:\Users\rabba\Downloads\TelegramDownload\metadata\v16"
os.makedirs(v16_dir, exist_ok=True)

def fix_array_bugs(html):
    # 1. Valid Sudoku Code Block Fix
    html = re.sub(r'36\.\s*Valid Sudoku.*?</tr>', 
                  r'''36. Valid Sudoku</td>
                  <td>Validate rows, cols, and 3x3 grids</td>
                  <td>Use HashSet to track seen numbers</td>
                  <td>
                    <strong>Row/Col/Box:</strong><br>
                    <pre style="white-space: pre-wrap !important; word-break: break-word !important;">for(int i=0;i<9;i++)
  for(int j=0;j<9;j++)
    if(!set.add(board[i][j])) return false;</pre>
                  </td></tr>''', 
                  html, flags=re.DOTALL)
                  
    # 2. Fix the Table Header readability (PROBLEM | KEY IDEA | APPROACH)
    # The user complained it was unreadable. Let's ensure it has a light background and dark text.
    html = re.sub(r'(<th[^>]*>)\s*PROBLEM\s*(</th>)', r'\1<span style="color:#0f172a!important; font-size:14px;">PROBLEM</span>\2', html)
    html = re.sub(r'(<th[^>]*>)\s*KEY IDEA\s*(</th>)', r'\1<span style="color:#0f172a!important; font-size:14px;">KEY IDEA</span>\2', html)
    html = re.sub(r'(<th[^>]*>)\s*APPROACH / FORMULA / PATTERN\s*(</th>)', r'\1<span style="color:#0f172a!important; font-size:14px;">APPROACH / FORMULA / PATTERN</span>\2', html)
    
    # 3. Fix "TIPS & REMINDERS" and "COMMON HASHMAP METHODS" invisible text
    # In v10 they had color: #1e3a8a (dark blue). If the background is dark, we need to make it bright white/yellow!
    # Let's just force the text color to white with a text-shadow so it's readable on ANY background.
    html = html.replace('⭐ TIPS &amp; REMINDERS', '<span style="color:white !important; text-shadow: 1px 1px 2px black;">⭐ TIPS &amp; REMINDERS</span>')
    html = html.replace('⚙️ COMMON HASHMAP METHODS (JAVA)', '<span style="color:white !important; text-shadow: 1px 1px 2px black;">⚙️ COMMON HASHMAP METHODS (JAVA)</span>')
    html = html.replace('🕒 COMPLEXITY REFERENCE', '<span style="color:white !important; text-shadow: 1px 1px 2px black;">🕒 COMPLEXITY REFERENCE</span>')
    
    # 4. Fix List <-> Array mixed code
    # We just need to make sure all <pre> tags don't mix lines
    return html

def process_file(fname):
    src_path = os.path.join(v10_dir, fname)
    dst_path = os.path.join(v16_dir, fname)
    
    with open(src_path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    if "Array" in fname:
        html = fix_array_bugs(html)
        
    soup = BeautifulSoup(html, 'html.parser')
    
    # Fix dark text on dark backgrounds by ensuring dark mode boxes have white text
    for box in soup.find_all(True):
        if not box.has_attr('style'): continue
        style = box['style'].lower()
        if '#1e1e1e' in style or '#0f172a' in style or '#1e293b' in style or 'black' in style:
            # It's a dark background box, explicitly force the text to be white!
            box['style'] = box['style'] + '; color: #ffffff !important;'
            # And force all spans inside it to inherit white text unless it's syntax highlighting
            for child in box.find_all(['div', 'span', 'p', 'li']):
                if child.has_attr('style') and 'color' in child['style']:
                    # if it's already explicitly colored, we might keep it if it's a bright color
                    child_color = re.search(r'color:\s*(#[a-fA-F0-9]+)', child['style'])
                    if child_color and child_color.group(1).lower() in ['#1e3a8a', '#0f172a', '#000000', 'black']:
                        # It's explicitly dark text, override to white
                        child['style'] = child['style'].replace(child_color.group(0), 'color: #ffffff')
                else:
                    child['style'] = child.get('style', '') + '; color: #ffffff !important;'

    # Global CSS to fix layout, PDF spaces, and code overlapping
    style_tag = soup.find('style')
    if style_tag:
        style_tag.append("""
        /* FIX CODE OVERLAPPING AND MIXING */
        pre, code {
            white-space: pre-wrap !important;
            word-wrap: break-word !important;
            word-break: break-all !important;
            line-height: 1.5 !important;
        }
        
        /* FIX HUGE BLANK SPACES IN PDF (IPAD VIEW) */
        @media print {
            body { padding: 0 !important; margin: 0 !important; -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
            .page { 
                page-break-after: auto !important; /* Allow continuous flow */
                page-break-inside: avoid !important;
                margin-bottom: 20px !important; 
                box-shadow: none !important; 
                zoom: 0.75; 
            }
            .section-box, .content-grid {
                page-break-inside: avoid !important;
                break-inside: avoid !important;
            }
        }
        """)

    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"Generated V16 (Identical to HTML, Nice Look, No Blank Spaces): {fname}")

for fname in os.listdir(v10_dir):
    if fname.endswith('_Final.html'):
        process_file(fname)

import os
import re
from bs4 import BeautifulSoup

v11_dir = r"C:\Users\rabba\Downloads\TelegramDownload\metadata\v11"
v12_dir = r"C:\Users\rabba\Downloads\TelegramDownload\metadata\v12"
os.makedirs(v12_dir, exist_ok=True)

def get_box(header_text_element):
    if not header_text_element: return None
    parent = header_text_element.parent
    while parent:
        if parent.name == 'div' and 'section-box' in parent.get('class', []):
            return parent
        parent = parent.parent
    return None

def process_file(fname):
    src_path = os.path.join(v11_dir, fname)
    dst_path = os.path.join(v12_dir, fname)
    
    with open(src_path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    
    if "Array" in fname:
        pattern_header = soup.find(string=re.compile('2. PATTERN RECOGNITION'))
        box = get_box(pattern_header)
        if box:
            tbl = box.find('table')
            if tbl:
                tbl.append(BeautifulSoup("""
                <tr style="border-bottom: 1px solid #e2e8f0;">
                    <td style="padding: 8px 0; color: #f43f5e; font-weight:bold;">🪟</td>
                    <td style="padding: 8px 0;">Contiguous Subarray?</td>
                    <td style="padding: 8px 0; font-weight: bold;">Sliding Window</td>
                </tr>
                <tr style="border-bottom: 1px solid #e2e8f0;">
                    <td style="padding: 8px 0; color: #8b5cf6; font-weight:bold;">👉👈</td>
                    <td style="padding: 8px 0;">Sorted Array Search?</td>
                    <td style="padding: 8px 0; font-weight: bold;">Two Pointers</td>
                </tr>
                <tr style="border-bottom: 1px solid #e2e8f0;">
                    <td style="padding: 8px 0; color: #0ea5e9; font-weight:bold;">➕🗺️</td>
                    <td style="padding: 8px 0;">Subarray Sum = K?</td>
                    <td style="padding: 8px 0; font-weight: bold;">Prefix Sum + HashMap</td>
                </tr>
                """, 'html.parser'))
                    
        tips_header = soup.find(string=re.compile('11. TIPS & TRICKS'))
        box = get_box(tips_header)
        if box:
            content = box.find('div', class_='section-content')
            if content:
                content.append(BeautifulSoup("""
                <div style="display: flex; margin-bottom: 8px;">
                    <div style="color: #22c55e; margin-right: 8px; font-weight:bold;">✔️</div>
                    <div><strong>Prefix Sum + HashMap</strong> is the ultimate FAANG trap for Subarray Sum problems.</div>
                </div>
                """, 'html.parser'))
                    
        patterns_header = soup.find(string=re.compile('3. COMMON PATTERNS'))
        box = get_box(patterns_header)
        if box:
            content = box.find('div', class_='section-content')
            if content:
                content.append(BeautifulSoup("""
                <div style="display: flex; margin-top: 8px;">
                    <div style="color: #22c55e; margin-right: 8px; font-weight:bold;">✅</div>
                    <div>Subarray Sum = K → <strong>Prefix Sum + Map</strong></div>
                </div>
                """, 'html.parser'))

    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"[{os.path.getsize(dst_path)//1024}KB] {fname} -> V12 FAANG Updated")

for fname in os.listdir(v11_dir):
    if fname.endswith('_Final.html'):
        process_file(fname)

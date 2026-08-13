import os
import re
from bs4 import BeautifulSoup

src_dir = r"C:\Users\rabba\Downloads\TelegramDownload\metadata"
v10_dir = r"C:\Users\rabba\Downloads\TelegramDownload\metadata\v10"
os.makedirs(v10_dir, exist_ok=True)

def get_box(header_text_element):
    if not header_text_element: return None
    parent = header_text_element.parent
    while parent:
        if parent.name == 'div' and 'section-box' in parent.get('class', []):
            return parent
        parent = parent.parent
    return None

def process_file(fname):
    src_path = os.path.join(src_dir, fname)
    dst_path = os.path.join(v10_dir, fname)
    
    with open(src_path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    
    style_tag = soup.find('style')
    if style_tag:
        extra_css = """
        /* Fix code overflowing */
        pre { white-space: pre-wrap !important; word-break: break-word !important; }
        code { word-break: break-word !important; }
        /* Ensure dark mode boxes have white text */
        .section-box[style*="background-color: #1e1e1e"] { color: white !important; }
        .section-box[style*="background-color: #1e1e1e"] * { color: white !important; }
        .section-box[style*="background-color: #1e1e1e"] code { color: #38bdf8 !important; }
        
        @media print {
            body { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
            .page { page-break-after: always; box-shadow: none !important; margin: 0 !important; }
        }
        """
        style_tag.append(extra_css)
        
    if "Array" in fname:
        h1 = soup.find(string=re.compile('VOLUME 1: ARRAYS & HASHING'))
        if h1 and h1.parent.name == 'h1':
            h1.parent['style'] = h1.parent.get('style', '') + '; font-size: 18px !important;'
            
        h1_2 = soup.find(string=re.compile('ARRAYS & HASHING CHEAT SHEET ✅'))
        if h1_2 and h1_2.parent.name == 'h1':
            h1_2.parent['style'] = h1_2.parent.get('style', '').replace('#fbbf24', '#b45309')
            
        problems_header = soup.find(string=re.compile('3. PROBLEMS COVERED'))
        box = get_box(problems_header)
        if box:
            tbl = box.find('table')
            if tbl:
                rows = tbl.find_all('tr')
                for row in rows:
                    cols = row.find_all('td')
                    if len(cols) >= 4:
                        if 'Valid Anagram' in cols[1].text:
                            cols[3].append(BeautifulSoup("<br><code style='color:#ef4444;font-size:0.8em;'>freq[c-'a']++</code>", 'html.parser'))
                        elif 'Group Anagrams' in cols[1].text:
                            cols[3].append(BeautifulSoup("<br><code style='color:#ef4444;font-size:0.8em;'>Arrays.toString(freq)</code>", 'html.parser'))
                            
        aha_header = soup.find(string=re.compile('4. BIGGEST AHA MOMENTS'))
        box = get_box(aha_header)
        if box:
            ga = box.find(string=re.compile('Group Anagrams'))
            if ga:
                ga.parent.insert_after(BeautifulSoup("<div style='color:#059669; font-weight:bold; font-size:0.9em;'>Key: Arrays.toString(freq)</div>", 'html.parser'))

        api_header = soup.find(string=re.compile('7. JAVA APIS USED'))
        box = get_box(api_header)
        if box:
            hm = box.find(string=re.compile('HashMap'))
            if hm:
                p = hm.parent.parent
                p.append(BeautifulSoup("<div>⮑ putIfAbsent(k,v) → V</div>", 'html.parser'))
                p.append(BeautifulSoup("<div>⮑ compute(k,fn) → V</div>", 'html.parser'))

        conv_header = soup.find(string=re.compile('8. COMMON CONVERSIONS'))
        box = get_box(conv_header)
        if box:
            content = box.find('div', class_='section-content')
            if content:
                content.clear()
                content.append(BeautifulSoup("""
                <table style="width: 100%; border-collapse: collapse;">
                    <tr><td style="color:var(--primary);font-weight:bold;padding:4px;">String → Primitive</td><td style="padding:4px;"><code>Integer.parseInt(s)</code></td></tr>
                    <tr><td style="color:var(--primary);font-weight:bold;padding:4px;">Primitive → String</td><td style="padding:4px;"><code>String.valueOf(p)</code></td></tr>
                    <tr><td style="color:var(--primary);font-weight:bold;padding:4px;">String → Wrapper</td><td style="padding:4px;"><code>Integer.valueOf(s)</code></td></tr>
                    <tr><td style="color:var(--primary);font-weight:bold;padding:4px;">Wrapper → String</td><td style="padding:4px;"><code>w.toString()</code></td></tr>
                    <tr><td style="color:var(--primary);font-weight:bold;padding:4px;">Primitive → Wrapper</td><td style="padding:4px;"><code>Integer.valueOf(p)</code></td></tr>
                    <tr><td style="color:var(--primary);font-weight:bold;padding:4px;">Wrapper → Primitive</td><td style="padding:4px;"><code>w.intValue()</code></td></tr>
                    <tr><td style="color:var(--primary);font-weight:bold;padding:4px;">String ↔ char[]</td><td style="padding:4px;"><code>s.toCharArray()</code> / <code>new String(arr)</code></td></tr>
                </table>
                """, 'html.parser'))

        when_header = soup.find(string=re.compile('10. WHEN TO USE WHAT'))
        box = get_box(when_header)
        if box:
            tbl = box.find('table')
            if tbl:
                tbl.append(BeautifulSoup("<tr><td style='padding:4px;font-weight:bold;'>int[128]</td><td style='padding:4px;'>ASCII chars</td></tr>", 'html.parser'))

        box11 = soup.find(string=re.compile('11. TIPS & TRICKS'))
        if box11:
            box = get_box(box11)
            if box:
                grid_container = box.parent
                if grid_container and 'display: grid' in grid_container.get('style', ''):
                    grid_container['style'] = grid_container['style'].replace('1fr 1fr 2fr', '1fr 1fr')
                
        comp_header = soup.find(string=re.compile('14. COMPLEXITY SUMMARY TABLE'))
        box = get_box(comp_header)
        if box:
            tbl = box.find('table')
            if tbl:
                tbl['style'] = tbl.get('style', '') + '; font-size: 10px;'
                
    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"[{os.path.getsize(dst_path)//1024}KB] {fname} -> V10 Restored")

for fname in os.listdir(src_dir):
    if fname.endswith('_Final.html'):
        process_file(fname)

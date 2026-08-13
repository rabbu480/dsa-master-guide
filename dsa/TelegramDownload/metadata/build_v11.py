import os
import re
from bs4 import BeautifulSoup

src_dir = r"C:\Users\rabba\Downloads\TelegramDownload\metadata"
v11_dir = r"C:\Users\rabba\Downloads\TelegramDownload\metadata\v11"
os.makedirs(v11_dir, exist_ok=True)

def process_file(fname):
    src_path = os.path.join(src_dir, fname)
    dst_path = os.path.join(v11_dir, fname)
    
    with open(src_path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    
    # --- FIX 1: The CSS & Print Engine ---
    style_tag = soup.find('style')
    if style_tag:
        extra_css = """
        /* Fix code overflowing */
        pre { white-space: pre-wrap !important; word-break: break-word !important; }
        code { word-break: break-word !important; }
        
        /* Ensure dark mode boxes have white text and nice blue code */
        .section-box[style*="background-color: #1e1e1e"] { color: white !important; }
        .section-box[style*="background-color: #1e1e1e"] * { color: white !important; }
        .section-box[style*="background-color: #1e1e1e"] code { color: #38bdf8 !important; }
        
        @media print {
            /* Force exact colors and no margins */
            body { 
                -webkit-print-color-adjust: exact !important; 
                print-color-adjust: exact !important; 
                padding: 0 !important;
                margin: 0 !important;
                background: white !important;
            }
            @page { margin: 0.5cm; } /* Maximize printable area */
            
            /* Shrink content slightly to prevent 24-page blowouts */
            .page { 
                page-break-after: always !important; 
                page-break-inside: avoid !important;
                break-inside: avoid !important;
                box-shadow: none !important; 
                margin: 0 !important; 
                padding: 0 !important;
                max-width: 100% !important;
                border: none !important;
                zoom: 0.72; /* The magic number to fit 1100px wide pages perfectly onto A4 without spilling */
            }
            
            /* Allow grid items to print smoothly without forcing page breaks if not needed */
            .section-box {
                page-break-inside: avoid !important;
                break-inside: avoid !important;
            }
        }
        """
        style_tag.append(extra_css)
        
    # --- FIX 2: Specific Text & Layout Fixes ---
    if "Array" in fname:
        # A. Make headers match Volume 1 style (dark blue background, white text)
        for h1 in soup.find_all('h1'):
            text = h1.get_text()
            if 'VOLUME 1: ARRAYS & HASHING' in text:
                # Shrink it slightly so it doesn't take up the whole page
                h1.parent['style'] = h1.parent.get('style', '') + '; font-size: 18px !important;'
            elif 'ARRAYS & HASHING CHEAT SHEET' in text and 'VOLUME 1' not in text:
                # The user HATED the yellow-on-white. Let's give it the dark blue header background!
                parent_div = h1.parent
                if parent_div and parent_div.name == 'div':
                    parent_div['style'] = 'background-color: #1a365d; color: white; padding: 15px; border-radius: 8px; margin-bottom: 20px; text-align: center;'
                    h1['style'] = h1.get('style', '').replace('#fbbf24', '#fbbf24') # Keep text yellow, but now on dark blue!
                    
        # B. Make all .header-top divs (which hold titles) have the nice dark blue theme
        for header_top in soup.find_all('div', class_='header-top'):
            if 'background-color' not in header_top.get('style', ''):
                header_top['style'] = header_top.get('style', '') + '; background-color: #1a365d; color: white; padding: 15px; border-radius: 8px; margin-bottom: 20px;'
            
        # C. Problems Covered (Add code snippets to the table safely)
        for box in soup.find_all('div', class_='section-box'):
            hdr = box.find('div', class_='section-header')
            if not hdr: continue
            hdr_text = hdr.get_text()
            
            if '3. PROBLEMS COVERED' in hdr_text:
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
                                
            elif '4. BIGGEST AHA MOMENTS' in hdr_text:
                ga = box.find(string=re.compile('Group Anagrams'))
                if ga:
                    ga.parent.insert_after(BeautifulSoup("<div style='color:#059669; font-weight:bold; font-size:0.9em;'>Key: Arrays.toString(freq)</div>", 'html.parser'))

            elif '7. JAVA APIS USED' in hdr_text:
                hm = box.find(string=re.compile('HashMap'))
                if hm:
                    p = hm.parent.parent
                    p.append(BeautifulSoup("<div>⮑ putIfAbsent(k,v) → V</div>", 'html.parser'))
                    p.append(BeautifulSoup("<div>⮑ compute(k,fn) → V</div>", 'html.parser'))

            elif '8. COMMON CONVERSIONS' in hdr_text:
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

            elif '10. WHEN TO USE WHAT' in hdr_text:
                tbl = box.find('table')
                if tbl:
                    tbl.append(BeautifulSoup("<tr><td style='padding:4px;font-weight:bold;'>int[128]</td><td style='padding:4px;'>ASCII chars</td></tr>", 'html.parser'))

            elif '11. TIPS & TRICKS' in hdr_text:
                grid_container = box.parent
                if grid_container and 'display: grid' in grid_container.get('style', ''):
                    grid_container['style'] = grid_container['style'].replace('1fr 1fr 2fr', '1fr 1fr')
                    
            elif '14. COMPLEXITY SUMMARY TABLE' in hdr_text:
                tbl = box.find('table')
                if tbl:
                    tbl['style'] = tbl.get('style', '') + '; font-size: 10px;'
                
    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"[{os.path.getsize(dst_path)//1024}KB] {fname} -> V11 Printed Fixed")

for fname in os.listdir(src_dir):
    if fname.endswith('_Final.html'):
        process_file(fname)

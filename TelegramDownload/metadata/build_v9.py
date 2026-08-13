import os
import re
from bs4 import BeautifulSoup

src_dir = r"C:\Users\rabba\Downloads\TelegramDownload\metadata"
v9_dir = r"C:\Users\rabba\Downloads\TelegramDownload\metadata\v9"
os.makedirs(v9_dir, exist_ok=True)

LC_DESCRIPTIONS = {
    # Heaps
    "LC 215 Kth Largest Element in Array": "LC 215 Kth Largest (Find kth largest using Min Heap of size k)",
    "LC 347 Top K Frequent Elements": "LC 347 Top K Frequent (Count freqs, then use Min Heap of size k)",
    "LC 973 K Closest Points to Origin": "LC 973 K Closest (Use Max Heap of size k to discard farthest)",
    "LC 692 Top K Frequent Words": "LC 692 Top K Frequent Words (Min Heap with custom string comparator)",
    "LeetCode 1046": "LC 1046 Last Stone Weight<br><span style='color:var(--text-muted);font-size:0.85em;'>(Repeatedly smash 2 heaviest using Max Heap)</span>",
    "Last Stone Weight": "", 
    "LeetCode 23": "LC 23 Merge K Sorted Lists<br><span style='color:var(--text-muted);font-size:0.85em;'>(Min Heap tracks smallest head across k lists)</span>",
    "Merge K Sorted Lists": "",
    "LeetCode 373": "LC 373 K Pairs Smallest Sums<br><span style='color:var(--text-muted);font-size:0.85em;'>(Min heap to explore smallest combinations)</span>",
    "Find K Pairs with": "",
    "Smallest Sums": "",
    "LeetCode 295": "LC 295 Median from Data Stream<br><span style='color:var(--text-muted);font-size:0.85em;'>(Max Heap for left half, Min Heap for right)</span>",
    "Find Median from": "",
    "Data Stream": "",
    # Arrays
    "1. Two Sum": "1. Two Sum (Find 2 numbers that add to target using HashMap complement)",
    "128. Longest Consecutive Sequence": "128. Longest Consecutive (HashSet, check sequence start if n-1 absent)",
    "242. Valid Anagram": "242. Valid Anagram (Count char freqs: freq[c-'a']++ / --)",
    "217. Contains Duplicate": "217. Contains Duplicate (!set.add(num))",
    "49. Group Anagrams": "49. Group Anagrams (Use Arrays.toString(freq) as HashMap key)",
    "347. Top K Frequent Elements": "347. Top K Frequent (Freq map -> Min Heap)",
    # Binary Search
    "704. Binary Search": "704. Binary Search (Classic O(log n) search on sorted array)",
    "74. Search a 2D Matrix": "74. Search a 2D Matrix (Treat matrix as flat 1D array: mid/cols, mid%cols)",
    "875. Koko Eating Bananas": "875. Koko Eating Bananas (Binary Search on Answer: rate k from 1 to max(piles))",
    "153. Find Minimum in Rotated Sorted Array": "153. Find Min in Rotated Array (If mid > right, min is in right half)",
    "33. Search in Rotated Sorted Array": "33. Search in Rotated Array (Determine which half is sorted first)",
    # Trees
    "226. Invert Binary Tree": "226. Invert Binary Tree (Swap left and right children recursively)",
    "104. Maximum Depth of Binary Tree": "104. Max Depth of Binary Tree (1 + max(left, right))",
    "100. Same Tree": "100. Same Tree (Check if p.val == q.val and recurse left/right)",
    "543. Diameter of Binary Tree": "543. Diameter of Binary Tree (Max of left_height + right_height updated globally)",
    "110. Balanced Binary Tree": "110. Balanced Binary Tree (Check if abs(left - right) <= 1)",
    "235. LCA of a Binary Search Tree": "235. LCA of BST (If p and q are > root, go right. If < root, go left. Else root)",
    "102. Binary Tree Level Order Traversal": "102. Level Order Traversal (BFS using Queue, iterate layer by layer)",
    "199. Binary Tree Right Side View": "199. Right Side View (BFS, add last node of each level to result)",
    "1448. Count Good Nodes in Binary Tree": "1448. Count Good Nodes (DFS, track max value seen along path)",
    "98. Validate Binary Search Tree": "98. Validate BST (DFS with valid min and max range bounds)",
    "230. Kth Smallest Element in a BST": "230. Kth Smallest in BST (Inorder traversal gives sorted order)",
    "105. Construct Tree from Preorder and Inorder": "105. Construct Tree (Preorder gives root, Inorder gives left/right subtree sizes)",
    # Graphs
    "200. Number of Islands": "200. Number of Islands (DFS/BFS to sink '1's when found)",
    "695. Max Area of Island": "695. Max Area of Island (Return 1 + DFS(neighbors) and track global max)",
    "133. Clone Graph": "133. Clone Graph (HashMap to map original nodes to cloned nodes)",
    "994. Rotting Oranges": "994. Rotting Oranges (Multi-source BFS from all rotten oranges)",
    "417. Pacific Atlantic Water Flow": "417. Pacific Atlantic (DFS/BFS from oceans inwards to find peaks)",
    "207. Course Schedule": "207. Course Schedule (Detect cycle in directed graph / topological sort)",
    "210. Course Schedule II": "210. Course Schedule II (Return topological sort order)",
    "684. Redundant Connection": "684. Redundant Connection (Union-Find to detect cycle in undirected graph)"
}

THEMES = {
    "1.Array&Hashing_Final.html": {"primary": "#3730a3", "secondary": "#4f46e5", "bg": "#f8fafc"}, # Indigo, lighter bg
    "6.Binary_Search_Final.html": {"primary": "#0f766e", "secondary": "#0d9488", "bg": "#f8fafc"}, # Teal
    "8.Trees_Final.html": {"primary": "#047857", "secondary": "#059669", "bg": "#f8fafc"},       # Emerald
    "9.Graphs_Final.html": {"primary": "#5b21b6", "secondary": "#7c3aed", "bg": "#f8fafc"},      # Violet
    "10.Heaps_Final.html": {"primary": "#be123c", "secondary": "#e11d48", "bg": "#f8fafc"}       # Rose
}

def get_v9_css(theme):
    return f"""
<style id="faang-v9">
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Fira+Code:wght@500;600;700&display=swap');

:root {{
    --primary: {theme['primary']}; 
    --secondary: {theme['secondary']}; 
    --green: #059669;
    --green-dark: #047857;
    --red: #dc2626;
    --red-dark: #b91c1c;
    --yellow: #d97706;
    --yellow-dark: #b45309;
    --purple: #7c3aed;
    --purple-dark: #5b21b6;
    --orange: #ea580c;
    --orange-dark: #c2410c;
    
    --text-dark: #0f172a;
    --text-muted: #334155;
    --bg-light: #ffffff;
    --border-color: #cbd5e1;
}}

body {{
    font-family: 'Inter', sans-serif;
    background-color: {theme['bg']};
    color: var(--text-dark);
    margin: 0;
    padding: 10px 20px;
    font-size: 11.5px; /* Compact */
    line-height: 1.45;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
}}

/* FLEX UTILITIES */
.flex-row {{ display: flex; flex-direction: row; gap: 15px; align-items: stretch; justify-content: space-around; width: 100%; }}
.flex-col {{ display: flex; flex-direction: column; flex: 1; min-width: 0; gap: 15px; }}
.bg-green {{ background-color: var(--green); color: white; padding: 3px 8px; border-radius: 4px; font-weight: bold; margin-bottom: 5px; text-align: center; font-size: 0.85em; display: inline-block; }}
.bg-red {{ background-color: var(--red); color: white; padding: 3px 8px; border-radius: 4px; font-weight: bold; margin-bottom: 5px; text-align: center; font-size: 0.85em; display: inline-block; }}

/* HORIZONTAL INTERVIEW FLOW */
.horizontal-flow {{ display: flex; flex-direction: row; align-items: flex-start; gap: 8px; flex-wrap: wrap; justify-content: center; width: 100%; }}
.flow-step {{ background: #ffffff; border: 2px solid var(--primary); border-radius: 6px; padding: 8px; width: 110px; text-align: center; position: relative; box-shadow: 0 2px 4px rgba(0,0,0,0.05); flex-grow: 1; min-width: 100px; }}
.flow-step-num {{ background: var(--primary); color: white; width: 20px; height: 20px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 900; font-size: 0.75rem; position: absolute; top: -10px; left: 50%; transform: translateX(-50%); box-shadow: 0 2px 4px rgba(0,0,0,0.2); }}
.flow-step-title {{ font-weight: 900; color: var(--primary); margin-top: 4px; font-size: 0.8rem; text-transform: uppercase; }}
.flow-step-desc {{ font-size: 0.75rem; color: var(--text-dark); line-height: 1.2; margin-top: 3px; font-weight: 500; }}
.flow-arrow {{ color: var(--primary); font-size: 1.2rem; font-weight: bold; align-self: center; }}

/* CSS GRID - Master layout */
.master-container {{ max-width: 1150px; margin: 0 auto; }}
.content-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 15px; align-items: start; width: 100%; margin-top: 15px; }}
.span-all {{ grid-column: 1 / -1 !important; }}

.main-header {{ text-align: center; border-bottom: 3px solid var(--primary); padding-bottom: 10px; margin-bottom: 15px; display: flex; align-items: center; justify-content: center; gap: 15px; background: white; padding: 15px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }}
.main-header h1 {{ margin: 0; font-size: 1.8rem; color: var(--primary); font-weight: 900; letter-spacing: 0.5px; text-transform: uppercase; }}

.section-box {{ border: 2px solid var(--primary); border-radius: 8px; overflow: hidden; background: white; box-shadow: 0 3px 8px rgba(0,0,0,0.05); break-inside: avoid; page-break-inside: avoid; }}
.section-header {{ background: var(--primary); color: white; padding: 8px 12px; font-weight: 800; font-size: 0.9rem; display: flex; align-items: center; text-transform: uppercase; letter-spacing: 0.5px; }}
.section-box.color-green {{ border-color: var(--green-dark); }} .section-box.color-green .section-header {{ background: var(--green-dark); }} .section-box.color-green .section-header span.num {{ color: var(--green-dark); }}
.section-box.color-purple {{ border-color: var(--purple-dark); }} .section-box.color-purple .section-header {{ background: var(--purple-dark); }} .section-box.color-purple .section-header span.num {{ color: var(--purple-dark); }}
.section-box.color-orange {{ border-color: var(--orange-dark); }} .section-box.color-orange .section-header {{ background: var(--orange-dark); }} .section-box.color-orange .section-header span.num {{ color: var(--orange-dark); }}
.section-box.color-red {{ border-color: var(--red-dark); }} .section-box.color-red .section-header {{ background: var(--red-dark); }} .section-box.color-red .section-header span.num {{ color: var(--red-dark); }}

.section-header span.num {{ background: white; color: var(--primary); border-radius: 50%; width: 22px; height: 22px; display: inline-flex; align-items: center; justify-content: center; margin-right: 10px; font-size: 0.8rem; font-weight: 900; box-shadow: 0 1px 3px rgba(0,0,0,0.2); }}
.section-content {{ padding: 12px; font-weight: 500; }}
.section-content p, .section-content li, .section-content div:not([class]) {{ color: var(--text-dark); }}

.box-aha {{ background-color: #f0fdf4; border: 2px solid #22c55e; border-radius: 6px; padding: 18px 12px 10px; position: relative; break-inside: avoid; page-break-inside: avoid; font-weight: 600; margin-bottom: 12px; }}
.box-aha-title {{ background-color: #22c55e; color: white; padding: 3px 10px; border-radius: 12px; font-weight: 800; position: absolute; top: -12px; left: 10px; font-size: 0.75rem; letter-spacing: 0.5px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }}
.box-tip {{ background-color: #fffbeb; border: 2px solid #f59e0b; border-radius: 6px; padding: 18px 12px 10px; position: relative; break-inside: avoid; page-break-inside: avoid; font-weight: 600; margin-bottom: 12px; }}
.box-tip-title {{ background-color: #f59e0b; color: white; padding: 3px 10px; border-radius: 12px; font-weight: 800; position: absolute; top: -12px; left: 10px; font-size: 0.75rem; letter-spacing: 0.5px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }}
.box-mistake {{ background-color: #fef2f2; border: 2px solid #ef4444; border-radius: 6px; padding: 18px 12px 10px; position: relative; break-inside: avoid; page-break-inside: avoid; font-weight: 600; margin-bottom: 12px; }}
.box-mistake-title {{ background-color: #ef4444; color: white; padding: 3px 10px; border-radius: 12px; font-weight: 800; position: absolute; top: -12px; left: 10px; font-size: 0.75rem; letter-spacing: 0.5px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }}

pre {{ background: #f8fafc !important; color: #0f172a !important; border: 1px solid var(--border-color) !important; border-left: 4px solid var(--secondary) !important; padding: 10px 12px !important; border-radius: 6px !important; font-family: 'Fira Code', monospace !important; font-size: 0.8rem !important; margin: 8px 0 !important; white-space: pre-wrap !important; word-break: break-word !important; word-wrap: break-word !important; line-height: 1.5; font-weight: 600 !important; overflow: hidden !important; }}
code {{ background: #f1f5f9; color: var(--secondary); padding: 1px 4px; border-radius: 3px; font-family: 'Fira Code', monospace; font-size: 0.9em; font-weight: 700; border: 1px solid #e2e8f0; word-break: break-word; }}
pre code {{ background: transparent !important; color: inherit !important; padding: 0 !important; border: none !important; }}

table {{ width: 100%; border-collapse: separate; border-spacing: 0; font-size: 0.8rem; margin: 10px 0; border-radius: 6px; overflow: hidden; border: 1px solid var(--border-color); }}
table th {{ background: var(--primary) !important; color: white !important; padding: 6px 8px; text-align: left; font-weight: 800; text-transform: uppercase; font-size: 0.75rem; letter-spacing: 0.5px; }}
table td {{ border-bottom: 1px solid var(--border-color); border-right: 1px solid var(--border-color); padding: 6px 8px; line-height: 1.4; font-weight: 500; }}
table tr td:last-child {{ border-right: none; }}
table tr:last-child td {{ border-bottom: none; }}
table tr:nth-child(even) td {{ background: #f8fafc; }}

ul, ol {{ margin: 0; padding-left: 18px; }} li {{ margin-bottom: 4px; line-height: 1.4; }}

.mermaid svg {{ max-width: 100% !important; height: auto !important; max-height: 200px !important; display: block; margin: 0 auto; }}

/* Enhanced Syntax Colors for Light Mode */
[style*="color: #569cd6"] {{ color: #2563eb !important; font-weight: 800; }} 
[style*="color: #c586c0"] {{ color: #7e22ce !important; font-weight: 800; }} 
[style*="color: #b5cea8"] {{ color: #b91c1c !important; font-weight: 700; }} 
[style*="color: #6a9955"] {{ color: #475569 !important; font-style: italic; font-weight: 500; }} 

@media print {{
    body {{ background: white !important; padding: 0 !important; font-size: 10px !important; zoom: 0.85; }}
    .master-container {{ margin: 0 !important; max-width: 100% !important; }}
    .content-grid {{ display: grid !important; grid-template-columns: 1fr 1fr !important; gap: 10px !important; }}
    .section-box {{ break-inside: auto; page-break-inside: auto; margin-bottom: 10px; }}
    .box-aha, .box-tip, .box-mistake, tr, pre {{ page-break-inside: avoid !important; break-inside: avoid !important; }}
    @page {{ margin: 0.5cm; }}
}}
</style>
"""

JS_SYNTAX = """
<script type="module">
    import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
    mermaid.initialize({ 
        startOnLoad: true, 
        theme: 'base',
        themeVariables: {
            primaryColor: '#f1f5f9',
            primaryTextColor: '#0f172a',
            primaryBorderColor: '#0f172a',
            lineColor: '#334155',
            fontFamily: 'Inter',
            fontSize: '14px',
            nodeBorder: '#0f172a',
            mainBkg: '#ffffff',
            edgeLabelBackground: '#ffffff'
        }
    });
</script>
"""

APPENDICES = {
    "1.Array&Hashing_Final.html": [
        ("color-purple", "TWO POINTER TEMPLATES", "<pre>// Opposite ends\nint lo = 0, hi = n - 1;\nwhile (lo < hi) {\n    int sum = arr[lo] + arr[hi];\n    if (sum == target) return true;\n    else if (sum < target) lo++;\n    else hi--;\n}</pre>"),
        ("color-orange", "SLIDING WINDOW TEMPLATE", "<pre>// Variable window\nint lo = 0, maxLen = 0;\nfor (int hi = 0; hi < n; hi++) {\n    // add arr[hi] to window state\n    while (!validWindow) {\n        // remove arr[lo] from state\n        lo++;\n    }\n    maxLen = Math.max(maxLen, hi - lo + 1);\n}</pre>"),
        ("color-green", "PREFIX SUM HASHMAP (FAANG TRAP)", "<pre>// Subarray Sum Equals K\nint sum = 0, count = 0;\nMap&lt;Integer,Integer&gt; pCount = new HashMap&lt;&gt;();\npCount.put(0, 1);\nfor (int num : nums) {\n    sum += num;\n    count += pCount.getOrDefault(sum - k, 0);\n    pCount.merge(sum, 1, Integer::sum);\n}</pre>")
    ],
    # ... Add others if needed
}

def clean_mermaid(soup):
    for mermaid in soup.find_all('div', class_='mermaid'):
        text = mermaid.get_text()
        text = text.replace('\xa0', ' ')
        mermaid.string = text

def strip_inline_colors(soup):
    for tag in soup.find_all(True):
        if tag.name not in ['pre', 'code'] and not tag.find_parent('pre') and not tag.find_parent('code'):
            style = tag.get('style', '')
            if style:
                # Aggressively remove all color/background hardcodes except some structure
                style = re.sub(r'background-color:\s*#[a-fA-F0-9]{3,6};?', '', style, flags=re.IGNORECASE)
                style = re.sub(r'background:\s*#[a-fA-F0-9]{3,6};?', '', style, flags=re.IGNORECASE)
                style = re.sub(r'color:\s*#[a-fA-F0-9]{3,6};?', '', style, flags=re.IGNORECASE)
                style = re.sub(r'color:\s*white;?', '', style, flags=re.IGNORECASE)
                style = re.sub(r'color:\s*black;?', '', style, flags=re.IGNORECASE)
                
                if not any(c in style for c in ['width', 'flex', 'text-align', 'padding', 'margin', 'border']):
                    del tag['style']
                else:
                    tag['style'] = style

def enrich_arrays_specific(soup):
    # Fix Big O Rules layout (make them side-by-side)
    for box in soup.find_all('div', class_='section-box'):
        header = box.find('div', class_='section-header')
        if not header: continue
        title = header.get_text(strip=True).upper()
        
        if 'BIG-O RULES' in title:
            content = box.find('div', class_='section-content')
            if content:
                content['class'] = content.get('class', []) + ['flex-row']
                for hr in content.find_all('hr'): hr.decompose() # Remove hr
                
        elif 'JAVA APIS USED' in title:
            # Add compute and putIfAbsent
            content = box.find('div', class_='section-content')
            if content:
                hm_div = content.find(string=re.compile('HashMap'))
                if hm_div:
                    parent = hm_div.parent.parent
                    new_api1 = soup.new_tag('div')
                    new_api1.string = "⮑ putIfAbsent(k, v) → returns v (or null)"
                    new_api2 = soup.new_tag('div')
                    new_api2.string = "⮑ compute(k, (k,v)->...) → returns new v"
                    parent.append(new_api1)
                    parent.append(new_api2)

        elif 'COMMON CONVERSIONS' in title:
            # Completely rewrite this table based on the images
            content = box.find('div', class_='section-content')
            if content:
                content.clear()
                table = BeautifulSoup("""
                <table style="width: 100%;">
                    <tr><td style="color:var(--primary);font-weight:bold;">String → Primitive</td><td><code>Integer.parseInt(s)</code></td></tr>
                    <tr><td style="color:var(--primary);font-weight:bold;">Primitive → String</td><td><code>String.valueOf(p)</code></td></tr>
                    <tr><td style="color:var(--primary);font-weight:bold;">String → Wrapper</td><td><code>Integer.valueOf(s)</code></td></tr>
                    <tr><td style="color:var(--primary);font-weight:bold;">Wrapper → String</td><td><code>w.toString()</code></td></tr>
                    <tr><td style="color:var(--primary);font-weight:bold;">Primitive → Wrapper</td><td><code>Integer.valueOf(p)</code> (Autoboxing)</td></tr>
                    <tr><td style="color:var(--primary);font-weight:bold;">Wrapper → Primitive</td><td><code>w.intValue()</code> (Unboxing)</td></tr>
                    <tr><td style="color:var(--primary);font-weight:bold;">String → char[]</td><td><code>s.toCharArray()</code></td></tr>
                    <tr><td style="color:var(--primary);font-weight:bold;">char[] → String</td><td><code>new String(arr)</code></td></tr>
                </table>
                """, 'html.parser')
                content.append(table)
                
        elif 'WHEN TO USE WHAT?' in title:
            content = box.find('div', class_='section-content')
            if content:
                tbl = content.find('table')
                if tbl:
                    tbl.append(BeautifulSoup("<tr><td style='font-weight:bold;'>int[128] / int[256]</td><td>When dealing with all ASCII characters</td></tr>", 'html.parser'))
                    
        elif 'BIGGEST AHA MOMENTS' in title:
            content = box.find('div', class_='section-content')
            if content:
                # Rewrite group anagrams Aha moment
                ga = content.find(string=re.compile('Group Anagrams'))
                if ga:
                    p = ga.parent
                    p.insert_after(BeautifulSoup("""
                    <div style="margin-bottom:8px;">
                        <div>Map characters to array: <code>freq[c-'a']++</code></div>
                        <div>Create key: <code>Arrays.toString(freq)</code></div>
                        <div style="color:var(--text-muted);font-size:0.9em;">Use this string as the HashMap key!</div>
                    </div>
                    """, 'html.parser'))

def build_v9():
    finals = [f for f in os.listdir(src_dir) if f.endswith('_Final.html')]
    print(f"Building v9 FINAL (Ultra Compact Print Optimization)...")
    
    for fname in sorted(finals):
        src_path = os.path.join(src_dir, fname)
        dst_path = os.path.join(v9_dir, fname)
        
        with open(src_path, 'r', encoding='utf-8') as f:
            raw_html = f.read()
            
        for key, val in LC_DESCRIPTIONS.items():
            if val != "": raw_html = raw_html.replace(key, val)
            
        raw_html = raw_html.replace("LeetCode 1046<br>Last Stone Weight", LC_DESCRIPTIONS["LeetCode 1046"])
        raw_html = raw_html.replace("LeetCode 23<br>Merge K Sorted Lists", LC_DESCRIPTIONS["LeetCode 23"])
        
        soup = BeautifulSoup(raw_html, 'html.parser')
        
        # 1. Clean Mermaid
        clean_mermaid(soup)
        
        # 2. Strip inline colors that break light mode (black on black fixes)
        strip_inline_colors(soup)
        
        # 3. Apply Array Specific Content changes
        if 'Array' in fname:
            enrich_arrays_specific(soup)
            
        # 4. Extract all .section-box, .box-aha, .box-tip, .box-mistake globally
        all_boxes = []
        for box in soup.find_all(class_=lambda x: x and any(cls in x for cls in ['section-box', 'box-aha', 'box-tip', 'box-mistake'])):
            is_nested = False
            parent = box.parent
            while parent:
                if any(cls in parent.get('class', []) for cls in ['section-box', 'box-aha', 'box-tip', 'box-mistake']):
                    is_nested = True
                    break
                parent = parent.parent
            if not is_nested:
                all_boxes.append(box.extract())
                
        # Handle 11, 12, 13 Stacking specifically for Array&Hashing
        stack_col = soup.new_tag('div', attrs={'class': 'flex-col'})
        boxes_to_grid = []
        
        for box in all_boxes:
            title = ''
            header = box.find('div', class_='section-header')
            if header: title = header.get_text(strip=True).upper()
            
            # Remove giant header spans to let them sit side-by-side
            if box.get('class') and 'span-all' in box['class']:
                box['class'].remove('span-all')
            
            if 'TEMPLATE' in title or 'ROADMAP' in title or 'INTERVIEW FLOW' in title or 'KEY PROBLEMS' in title:
                box['class'] = box.get('class', []) + ['span-all']
                
            if 'TIPS & TRICKS' in title or 'COMMON PITFALLS' in title or 'MEMORY TRICKS' in title:
                stack_col.append(box)
            else:
                boxes_to_grid.append(box)
                
        # 5. Clear body completely and rebuild single page flow
        body = soup.find('body')
        body.clear()
        
        master_container = soup.new_tag('div', attrs={'class': 'master-container'})
        
        # Create minimal sleek header
        topic_name = fname.replace('_Final.html', '').replace('.', ' ').strip().upper()
        main_header = soup.new_tag('div', attrs={'class': 'main-header'})
        h1 = soup.new_tag('h1')
        h1.string = f"{topic_name} CHEAT SHEET"
        subtitle = soup.new_tag('div', attrs={'class': 'bg-green', 'style': 'margin:0;'})
        subtitle.string = "FAANG Prep"
        main_header.append(h1)
        main_header.append(subtitle)
        master_container.append(main_header)
        
        grid_container = soup.new_tag('div', attrs={'class': 'content-grid'})
        
        # Add normal boxes to grid
        for box in boxes_to_grid:
            grid_container.append(box)
            
        # Add the stacked column to grid (takes up one grid cell, stacking contents vertically)
        if len(stack_col.contents) > 0:
            grid_container.append(stack_col)
            
        # Append appendices for this file if exist
        if fname in APPENDICES:
            for color_class, title, content in APPENDICES[fname]:
                new_sec = soup.new_tag('div', attrs={'class': f'section-box {color_class}'})
                new_hdr = soup.new_tag('div', attrs={'class': 'section-header'})
                new_hdr.string = title
                new_cnt = soup.new_tag('div', attrs={'class': 'section-content'})
                cnt_soup = BeautifulSoup(content, 'html.parser')
                new_cnt.append(cnt_soup)
                new_sec.append(new_hdr)
                new_sec.append(new_cnt)
                grid_container.append(new_sec)
                
        master_container.append(grid_container)
        body.append(master_container)
        
        # Renumber headers sequentially
        counter = 1
        for box in soup.find_all('div', class_='section-box'):
            header = box.find('div', class_='section-header')
            if header:
                existing_num = header.find('span', class_='num')
                if existing_num: existing_num.decompose()
                
                # clean leading numbers from title text
                txt = header.get_text(strip=True)
                txt = re.sub(r'^[0-9]+\.\s*', '', txt)
                header.string = txt
                
                num_span = soup.new_tag('span', attrs={'class': 'num'})
                num_span.string = str(counter)
                header.insert(0, num_span)
                counter += 1

        # Final CSS/JS injection
        theme = THEMES.get(fname, {"primary": "#1e3a8a", "secondary": "#2563eb", "bg": "#f8fafc"})
        head = soup.find('head')
        for style in head.find_all('style'): style.decompose()
        head.append(BeautifulSoup(get_v9_css(theme), 'html.parser'))
        
        old_script = soup.find('script', type='module')
        if old_script: old_script.decompose()
        body.append(BeautifulSoup(JS_SYNTAX, 'html.parser'))
        
        title_tag = soup.find('title')
        if title_tag: title_tag.string = f"{topic_name} (FAANG Cheat Sheet)"
            
        with open(dst_path, 'w', encoding='utf-8') as f: f.write(str(soup))
        size_kb = os.path.getsize(dst_path) / 1024
        print(f"  [{size_kb:.0f}KB] {fname} - Finalized V9 (Print fixed).")

if __name__ == '__main__':
    build_v9()

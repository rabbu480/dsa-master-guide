import os
import re
from bs4 import BeautifulSoup

src_dir = r"C:\Users\rabba\Downloads\TelegramDownload\metadata"
v7_dir = r"C:\Users\rabba\Downloads\TelegramDownload\metadata\v7"
os.makedirs(v7_dir, exist_ok=True)

# LC Descriptions for enrichment
LC_DESCRIPTIONS = {
    # Heaps
    "LC 215 Kth Largest Element in Array": "LC 215 Kth Largest Element (Find kth largest using Min Heap of size k)",
    "LC 347 Top K Frequent Elements": "LC 347 Top K Frequent (Count freqs, then use Min Heap of size k)",
    "LC 973 K Closest Points to Origin": "LC 973 K Closest Points (Use Max Heap of size k to discard farthest)",
    "LC 692 Top K Frequent Words": "LC 692 Top K Frequent Words (Min Heap with custom string comparator)",
    "LeetCode 1046": "LC 1046 Last Stone Weight<br><span style='color:var(--text-muted);font-size:0.85em;'>(Repeatedly smash 2 heaviest stones using Max Heap)</span>",
    "Last Stone Weight": "", 
    "LeetCode 23": "LC 23 Merge K Sorted Lists<br><span style='color:var(--text-muted);font-size:0.85em;'>(Min Heap to track smallest head across k lists)</span>",
    "Merge K Sorted Lists": "",
    "LeetCode 373": "LC 373 K Pairs with Smallest Sums<br><span style='color:var(--text-muted);font-size:0.85em;'>(Min heap to explore smallest combinations)</span>",
    "Find K Pairs with": "",
    "Smallest Sums": "",
    "LeetCode 295": "LC 295 Median from Data Stream<br><span style='color:var(--text-muted);font-size:0.85em;'>(Balance Max Heap for left half, Min Heap for right half)</span>",
    "Find Median from": "",
    "Data Stream": "",
    # Arrays
    "1. Two Sum": "1. Two Sum (Find 2 numbers that add to target using HashMap complement lookup)",
    "128. Longest Consecutive Sequence": "128. Longest Consecutive Sequence (Add all to HashSet, check sequence start if n-1 doesn't exist)",
    "242. Valid Anagram": "242. Valid Anagram (Count char frequencies, must be identical)",
    "217. Contains Duplicate": "217. Contains Duplicate (Check if length of HashSet equals length of array)",
    "49. Group Anagrams": "49. Group Anagrams (Sort string or count chars to use as HashMap key)",
    "347. Top K Frequent Elements": "347. Top K Frequent Elements (Bucket sort frequencies or Min Heap)",
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
    "1.Array&Hashing_Final.html": {"primary": "#3730a3", "secondary": "#4f46e5", "bg": "#eef2ff"}, # Indigo
    "6.Binary_Search_Final.html": {"primary": "#0f766e", "secondary": "#0d9488", "bg": "#f0fdfa"}, # Teal
    "8.Trees_Final.html": {"primary": "#047857", "secondary": "#059669", "bg": "#ecfdf5"},       # Emerald
    "9.Graphs_Final.html": {"primary": "#5b21b6", "secondary": "#7c3aed", "bg": "#f5f3ff"},      # Violet
    "10.Heaps_Final.html": {"primary": "#be123c", "secondary": "#e11d48", "bg": "#fff1f2"}       # Rose
}

def get_v7_css(theme):
    return f"""
<style id="faang-v7">
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Fira+Code:wght@500;600&display=swap');

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
    --text-muted: #475569;
    --bg-light: #f8fafc;
    --border-color: #cbd5e1;
}}

body {{
    font-family: 'Inter', sans-serif;
    background-color: {theme['bg']};
    color: var(--text-dark);
    margin: 0;
    padding: 20px;
    font-size: 13.5px;
    line-height: 1.55;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
}}

/* FLEX UTILITIES */
.flex-row {{
    display: flex;
    flex-direction: row;
    gap: 15px;
    align-items: flex-start;
    justify-content: space-around;
    width: 100%;
}}
.flex-col {{ display: flex; flex-direction: column; flex: 1; min-width: 0; }}
.bg-green {{ background-color: var(--green); color: white; padding: 4px 10px; border-radius: 4px; font-weight: bold; margin-bottom: 5px; text-align: center; font-size: 0.9em; }}
.bg-red {{ background-color: var(--red); color: white; padding: 4px 10px; border-radius: 4px; font-weight: bold; margin-bottom: 5px; text-align: center; font-size: 0.9em; }}

/* HORIZONTAL INTERVIEW FLOW */
.horizontal-flow {{ display: flex; flex-direction: row; align-items: flex-start; gap: 10px; flex-wrap: wrap; justify-content: center; width: 100%; }}
.flow-step {{ background: #ffffff; border: 2px solid var(--primary); border-radius: 8px; padding: 10px; width: 130px; text-align: center; position: relative; box-shadow: 0 4px 6px rgba(0,0,0,0.05); flex-grow: 1; min-width: 120px; }}
.flow-step-num {{ background: var(--primary); color: white; width: 22px; height: 22px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 900; font-size: 0.8rem; position: absolute; top: -11px; left: 50%; transform: translateX(-50%); box-shadow: 0 2px 4px rgba(0,0,0,0.2); }}
.flow-step-title {{ font-weight: 900; color: var(--primary); margin-top: 5px; font-size: 0.85rem; text-transform: uppercase; }}
.flow-step-desc {{ font-size: 0.8rem; color: var(--text-dark); line-height: 1.3; margin-top: 4px; font-weight: 500; }}
.flow-arrow {{ color: var(--primary); font-size: 1.5rem; font-weight: bold; align-self: center; }}

.page {{ background: white; max-width: 1100px; margin: 0 auto 40px auto; padding: 40px 50px; box-shadow: 0 15px 35px rgba(0,0,0,0.1); border-radius: 12px; page-break-after: always; border-top: 8px solid var(--primary); position: relative; overflow: hidden; }}

.header-top {{ display: flex; justify-content: space-between; align-items: center; border-bottom: 3px solid var(--primary); padding-bottom: 12px; margin-bottom: 25px; }}
.header-title-box {{ display: flex; align-items: baseline; gap: 15px; }}
.header-title-box h1 {{ margin: 0; font-size: 2.6rem; color: var(--primary); font-weight: 900; letter-spacing: 0.5px; text-transform: uppercase; }}
.header-title-box .subtitle {{ background-color: var(--secondary); color: white; padding: 5px 14px; border-radius: 20px; font-weight: 800; font-size: 0.9rem; box-shadow: 0 2px 4px rgba(0,0,0,0.2); }}

/* CSS GRID */
.content-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 25px; align-items: start; width: 100%; }}
.span-all {{ grid-column: 1 / -1 !important; }}

.section-box {{ border: 2px solid var(--primary); border-radius: 10px; overflow: hidden; background: white; box-shadow: 0 4px 10px rgba(0,0,0,0.05); break-inside: avoid; page-break-inside: avoid; }}
.section-header {{ background: var(--primary); color: white; padding: 12px 16px; font-weight: 800; font-size: 1rem; display: flex; align-items: center; text-transform: uppercase; letter-spacing: 0.5px; }}
.section-box.color-green {{ border-color: var(--green-dark); }} .section-box.color-green .section-header {{ background: var(--green-dark); }} .section-box.color-green .section-header span.num {{ color: var(--green-dark); }}
.section-box.color-purple {{ border-color: var(--purple-dark); }} .section-box.color-purple .section-header {{ background: var(--purple-dark); }} .section-box.color-purple .section-header span.num {{ color: var(--purple-dark); }}
.section-box.color-orange {{ border-color: var(--orange-dark); }} .section-box.color-orange .section-header {{ background: var(--orange-dark); }} .section-box.color-orange .section-header span.num {{ color: var(--orange-dark); }}
.section-box.color-red {{ border-color: var(--red-dark); }} .section-box.color-red .section-header {{ background: var(--red-dark); }} .section-box.color-red .section-header span.num {{ color: var(--red-dark); }}

.section-header span.num {{ background: white; color: var(--primary); border-radius: 50%; width: 26px; height: 26px; display: inline-flex; align-items: center; justify-content: center; margin-right: 14px; font-size: 0.9rem; font-weight: 900; box-shadow: 0 2px 4px rgba(0,0,0,0.2); }}
.section-content {{ padding: 18px; font-weight: 500; }}
.section-content p, .section-content li, .section-content div:not([class]) {{ color: var(--text-dark); }}

.box-aha {{ background-color: #f0fdf4; border: 2px solid #22c55e; border-radius: 8px; padding: 22px 18px 15px; position: relative; box-shadow: 0 4px 6px rgba(34,197,94,0.1); break-inside: avoid; page-break-inside: avoid; font-weight: 600; margin-bottom: 10px; }}
.box-aha-title {{ background-color: #22c55e; color: white; padding: 4px 14px; border-radius: 20px; font-weight: 800; position: absolute; top: -14px; left: 15px; font-size: 0.85rem; letter-spacing: 0.5px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
.box-tip {{ background-color: #fffbeb; border: 2px solid #f59e0b; border-radius: 8px; padding: 22px 18px 15px; position: relative; box-shadow: 0 4px 6px rgba(245,158,11,0.1); break-inside: avoid; page-break-inside: avoid; font-weight: 600; margin-bottom: 10px; }}
.box-tip-title {{ background-color: #f59e0b; color: white; padding: 4px 14px; border-radius: 20px; font-weight: 800; position: absolute; top: -14px; left: 15px; font-size: 0.85rem; letter-spacing: 0.5px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
.box-mistake {{ background-color: #fef2f2; border: 2px solid #ef4444; border-radius: 8px; padding: 22px 18px 15px; position: relative; box-shadow: 0 4px 6px rgba(239,68,68,0.1); break-inside: avoid; page-break-inside: avoid; font-weight: 600; margin-bottom: 10px; }}
.box-mistake-title {{ background-color: #ef4444; color: white; padding: 4px 14px; border-radius: 20px; font-weight: 800; position: absolute; top: -14px; left: 15px; font-size: 0.85rem; letter-spacing: 0.5px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}

pre {{ background: #f8fafc !important; color: #0f172a !important; border: 1px solid var(--border-color) !important; border-left: 5px solid var(--secondary) !important; padding: 15px 18px !important; border-radius: 8px !important; font-family: 'Fira Code', monospace !important; font-size: 0.85rem !important; margin: 12px 0 !important; overflow-x: auto; white-space: pre-wrap; line-height: 1.6; box-shadow: inset 0 2px 4px rgba(0,0,0,0.02) !important; font-weight: 600 !important; }}
code {{ background: #f1f5f9; color: var(--secondary); padding: 2px 6px; border-radius: 4px; font-family: 'Fira Code', monospace; font-size: 0.9em; font-weight: 700; border: 1px solid #e2e8f0; }}
pre code {{ background: transparent !important; color: inherit !important; padding: 0 !important; border: none !important; }}

table {{ width: 100%; border-collapse: separate; border-spacing: 0; font-size: 0.9rem; margin: 15px 0; border-radius: 8px; overflow: hidden; border: 1px solid var(--border-color); box-shadow: 0 4px 6px rgba(0,0,0,0.03); }}
table th {{ background: var(--primary) !important; color: white !important; padding: 10px 14px; text-align: left; font-weight: 800; white-space: nowrap; text-transform: uppercase; font-size: 0.85rem; letter-spacing: 0.5px; border-bottom: 2px solid rgba(0,0,0,0.2); }}
table td {{ border-bottom: 1px solid var(--border-color); border-right: 1px solid var(--border-color); padding: 10px 14px; line-height: 1.5; font-weight: 500; }}
table tr td:last-child {{ border-right: none; }}
table tr:last-child td {{ border-bottom: none; }}
table tr:nth-child(even) td {{ background: #f8fafc; }}
table tr:hover td {{ background: #f1f5f9; }}

ul, ol {{ margin: 0; padding-left: 22px; }} li {{ margin-bottom: 8px; line-height: 1.5; }}

.mermaid svg {{ max-width: 100% !important; height: auto !important; max-height: 240px !important; display: block; margin: 0 auto; }}

[style*="color: #569cd6"] {{ color: #2563eb !important; font-weight: 800; }} 
[style*="color: #c586c0"] {{ color: #7e22ce !important; font-weight: 800; }} 
[style*="color: #b5cea8"] {{ color: #b91c1c !important; font-weight: 700; }} 
[style*="color: #6a9955"] {{ color: #475569 !important; font-style: italic; font-weight: 500; }} 

@media print {{
    body {{ background: white !important; padding: 0 !important; }}
    .page {{ box-shadow: none !important; margin: 0 !important; padding: 25px 0 !important; border: none !important; border-top: 6px solid var(--primary) !important; border-radius: 0 !important; }}
    .section-box, .box-aha, .box-tip, .box-mistake, tr {{ page-break-inside: avoid !important; break-inside: avoid !important; }}
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
            fontSize: '15px',
            nodeBorder: '#0f172a',
            mainBkg: '#f8fafc',
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
    "6.Binary_Search_Final.html": [
        ("color-purple", "UNIVERSAL TEMPLATE (Leftmost)", "<pre>// Find LEFTMOST position where condition is true\nint lo = 0, hi = n;\nwhile (lo < hi) {\n    int mid = lo + (hi - lo) / 2;\n    if (condition(mid)) hi = mid;\n    else lo = mid + 1;\n}\nreturn lo;</pre>"),
        ("color-orange", "SEARCH ON ANSWER PATTERN", "<pre>// Minimize the maximum\nlong lo = minPossible, hi = maxPossible;\nwhile (lo < hi) {\n    long mid = lo + (hi - lo) / 2;\n    if (canAchieve(mid)) hi = mid;\n    else lo = mid + 1;\n}\nreturn lo;</pre>"),
        ("color-green", "ROTATED ARRAY TRICK", "<pre>// Which half is sorted?\nif (nums[lo] <= nums[mid]) {\n    // Left is sorted. Is target inside?\n    if (target >= nums[lo] && target < nums[mid]) hi = mid - 1;\n    else lo = mid + 1;\n} else {\n    // Right is sorted...\n}</pre>")
    ],
    "8.Trees_Final.html": [
        ("color-purple", "UNIVERSAL DFS (Bottom-Up)", "<pre>int dfs(TreeNode node) {\n    if (node == null) return 0;\n    int left = dfs(node.left);\n    int right = dfs(node.right);\n    ans = Math.max(ans, left + right + node.val);\n    return Math.max(left, right) + 1;\n}</pre>"),
        ("color-orange", "LEVEL ORDER BFS", "<pre>Queue&lt;TreeNode&gt; q = new LinkedList&lt;&gt;();\nq.offer(root);\nwhile (!q.isEmpty()) {\n    int size = q.size(); // MUST snapshot size\n    for (int i = 0; i < size; i++) {\n        TreeNode curr = q.poll();\n        if (curr.left != null) q.offer(curr.left);\n        if (curr.right != null) q.offer(curr.right);\n    }\n}</pre>"),
        ("color-green", "BST CRITICAL OPERATIONS", "<pre>// Validate BST\nboolean isValid(TreeNode n, long min, long max) {\n    if (n == null) return true;\n    if (n.val <= min || n.val >= max) return false;\n    return isValid(n.left, min, n.val) && isValid(n.right, n.val, max);\n}</pre>")
    ],
    "10.Heaps_Final.html": [
        ("color-purple", "TOP-K ELEMENTS PATTERN", "<p><strong>Rule:</strong> K Largest → Min Heap of size K. K Smallest → Max Heap of size K.</p><pre>PriorityQueue&lt;Integer&gt; minHeap = new PriorityQueue&lt;&gt;();\nfor (int num : nums) {\n    minHeap.offer(num);\n    if (minHeap.size() > k) minHeap.poll();\n}</pre>"),
        ("color-orange", "COMPARATOR GUIDE (FAANG Trap)", "<table><tr><th>Goal</th><th>Comparator</th></tr><tr><td>Min Heap</td><td><code>new PriorityQueue&lt;&gt;()</code></td></tr><tr><td>Max Heap</td><td><code>Collections.reverseOrder()</code></td></tr><tr><td>Safe</td><td><code>(a,b) -> Integer.compare(a, b)</code></td></tr></table>")
    ],
    "9.Graphs_Final.html": [
        ("color-purple", "STANDARD BFS SHORTEST PATH", "<pre>int dist = 0;\nwhile (!q.isEmpty()) {\n    for (int sz = q.size(); sz > 0; sz--) {\n        int node = q.poll();\n        if (node == target) return dist;\n        for (int nei : adj.get(node))\n            if (!vis[nei]) { q.offer(nei); vis[nei]=true; }\n    }\n    dist++;\n}</pre>"),
        ("color-orange", "UNION-FIND (DSU)", "<pre>int find(int x) {\n    return parent[x] == x ? x : (parent[x] = find(parent[x]));\n}\nboolean union(int x, int y) {\n    int px = find(x), py = find(y);\n    if (px == py) return false;\n    if (rank[px] < rank[py]) parent[px] = py;\n    else if (rank[px] > rank[py]) parent[py] = px;\n    else { parent[py] = px; rank[px]++; }\n    return true;\n}</pre>"),
        ("color-green", "DIJKSTRA TEMPLATE", "<pre>PriorityQueue&lt;int[]&gt; pq = new PriorityQueue&lt;&gt;((a,b)->a[0]-b[0]);\npq.offer(new int[]{0, src});\nwhile (!pq.isEmpty()) {\n    int[] cur = pq.poll();\n    int d=cur[0], u=cur[1];\n    if (d > dist[u]) continue; // stale\n    for (int[] e : adj[u]) {\n        if (dist[u] + e[1] < dist[e[0]]) {\n            dist[e[0]] = dist[u] + e[1];\n            pq.offer(new int[]{dist[e[0]], e[0]});\n        }\n    }\n}</pre>")
    ]
}

def transform_interview_flow(soup, box):
    content_div = box.find('div', class_='section-content')
    if not content_div: return
    text = content_div.get_text()
    if 'Clarify' in text and 'Constraints' in text and 'Brute Force' in text:
        steps = [
            ("1", "Clarify", "Constraints, edge cases, input range, duplicates?"),
            ("2", "Brute Force", "Write simple solution"),
            ("3", "Better", "Optimize Time & Space"),
            ("4", "Optimal", "Best approach"),
            ("5", "Complexity", "Time & Space analysis"),
            ("6", "Code", "Clean & bug free"),
            ("7", "Explain", "Walk through execution")
        ]
        content_div.clear()
        flex_container = soup.new_tag('div', attrs={'class': 'horizontal-flow'})
        for i, (num, title, desc) in enumerate(steps):
            step_div = soup.new_tag('div', attrs={'class': 'flow-step'})
            num_div = soup.new_tag('div', attrs={'class': 'flow-step-num'})
            num_div.string = num
            title_div = soup.new_tag('div', attrs={'class': 'flow-step-title'})
            title_div.string = title
            desc_div = soup.new_tag('div', attrs={'class': 'flow-step-desc'})
            desc_div.string = desc
            step_div.append(num_div)
            step_div.append(title_div)
            step_div.append(desc_div)
            flex_container.append(step_div)
            if i < len(steps) - 1:
                arrow_div = soup.new_tag('div', attrs={'class': 'flow-arrow'})
                arrow_div.string = "→"
                flex_container.append(arrow_div)
        content_div.append(flex_container)
        box['class'] = box.get('class', []) + ['span-all']

def should_span_all(box):
    header = box.find('div', class_='section-header')
    if header:
        title = header.get_text(strip=True).upper()
        if 'TEMPLATE COMPARISON' in title: return True
        if 'ROADMAP' in title: return True
        if 'INTERVIEW FLOW' in title: return True 
        if 'ARRAY REPRESENTATION' in title: return False
        if 'IMPORTANT TERMINOLOGY' in title: return False
    return False

def clean_mermaid(soup):
    for mermaid in soup.find_all('div', class_='mermaid'):
        text = mermaid.get_text()
        text = text.replace('\xa0', ' ')
        mermaid.string = text

def deduplicate_and_restructure(soup):
    seen_titles = set()
    boxes_to_remove = []
    term_box = None
    points_box = None
    mistakes_box = None
    
    for box in soup.find_all('div', class_='section-box'):
        header = box.find('div', class_='section-header')
        if not header: continue
        title = header.get_text(strip=True).upper()
        if 'IMPORTANT TERMINOLOGY' in title: term_box = box
        elif 'KEY POINTS TO REMEMBER' in title: points_box = box
        elif 'COMMON MISTAKES' in title: mistakes_box = box
            
    if term_box and points_box and mistakes_box:
        term_content = term_box.find('div', class_='section-content')
        if term_content:
            p_content = points_box.find('div', class_='section-content')
            if p_content:
                new_div = soup.new_tag('div', style='margin-top: 15px; border-top: 1px dashed #cbd5e1; padding-top: 10px;')
                new_div.append(soup.new_tag('strong', style='color: var(--green); display: block; margin-bottom: 5px;'))
                new_div.find('strong').string = "Key Points to Remember"
                for el in p_content.contents: new_div.append(el)
                term_content.append(new_div)
            m_content = mistakes_box.find('div', class_='section-content')
            if m_content:
                new_div2 = soup.new_tag('div', style='margin-top: 15px; border-top: 1px dashed #cbd5e1; padding-top: 10px;')
                new_div2.append(soup.new_tag('strong', style='color: var(--red); display: block; margin-bottom: 5px;'))
                new_div2.find('strong').string = "Common Mistakes"
                for el in m_content.contents: new_div2.append(el)
                term_content.append(new_div2)
        points_box.decompose()
        mistakes_box.decompose()

    for box in soup.find_all('div', class_='section-box'):
        header = box.find('div', class_='section-header')
        if header:
            num_span = header.find('span', class_='num')
            if num_span: num_span.extract()
            title = header.get_text(strip=True).upper()
            title = re.sub(r'[^A-Z0-9 ]', '', title)
            title = re.sub(r'\s+', ' ', title).strip()
            if 'INTERVIEW FLOW' in title: 
                title = 'INTERVIEW FLOW'
                transform_interview_flow(soup, box)
            if 'PATTERN RECOGNITION' in title: title = 'PATTERN RECOGNITION'
            if 'DUPLICATE DETECTION' in title: title = 'DUPLICATE DETECTION'
            if 'COMPLEXITY' in title: title = 'COMPLEXITY'
            if title not in seen_titles:
                seen_titles.add(title)
            else:
                boxes_to_remove.append(box)

    for b in boxes_to_remove: b.decompose()

    for div in soup.find_all('div'):
        style = div.get('style', '')
        if 'background-color: #f0fdf4' in style and 'border: 2px solid #22c55e' in style:
            div['class'] = div.get('class', []) + ['box-aha']
            del div['style']
            t_div = div.find('div', style=lambda s: s and 'background-color: #22c55e' in s)
            if t_div:
                t_div['class'] = ['box-aha-title']
                del t_div['style']
        elif 'background-color: #fffbeb' in style and 'border: 2px solid #fbbf24' in style:
            div['class'] = div.get('class', []) + ['box-tip']
            del div['style']
            t_div = div.find('div', style=lambda s: s and 'background-color: #fbbf24' in s)
            if t_div:
                t_div['class'] = ['box-tip-title']
                del t_div['style']
        elif 'background-color: #fef2f2' in style and 'border: 2px solid #ef4444' in style:
            div['class'] = div.get('class', []) + ['box-mistake']
            del div['style']
            t_div = div.find('div', style=lambda s: s and 'background-color: #ef4444' in s)
            if t_div:
                t_div['class'] = ['box-mistake-title']
                del t_div['style']
    return seen_titles

def enrich_leetcode_statements(html_str):
    for key, val in LC_DESCRIPTIONS.items():
        if val != "":
            html_str = html_str.replace(key, val)
    html_str = html_str.replace("LeetCode 1046<br>Last Stone Weight", "LC 1046 Last Stone Weight<br><span style='color:var(--text-muted);font-size:0.85em;'>(Repeatedly smash 2 heaviest stones using Max Heap)</span>")
    html_str = html_str.replace("LeetCode 23<br>Merge K Sorted Lists", "LC 23 Merge K Sorted Lists<br><span style='color:var(--text-muted);font-size:0.85em;'>(Min Heap to track smallest head across k lists)</span>")
    html_str = html_str.replace("LeetCode 373<br>Find K Pairs with<br>Smallest Sums", "LC 373 K Pairs with Smallest Sums<br><span style='color:var(--text-muted);font-size:0.85em;'>(Min heap to explore smallest combinations)</span>")
    html_str = html_str.replace("LeetCode 295<br>Find Median from<br>Data Stream", "LC 295 Median from Data Stream<br><span style='color:var(--text-muted);font-size:0.85em;'>(Balance Max Heap for left half, Min Heap for right half)</span>")
    return html_str

def build_v7():
    finals = [f for f in os.listdir(src_dir) if f.endswith('_Final.html')]
    print(f"Building v7 FINAL (Premium Printing Edition without TOC)...")
    
    for fname in sorted(finals):
        src_path = os.path.join(src_dir, fname)
        dst_path = os.path.join(v7_dir, fname)
        
        with open(src_path, 'r', encoding='utf-8') as f:
            raw_html = f.read()
            
        raw_html = enrich_leetcode_statements(raw_html)
        raw_html = re.sub(r'<div class="header-top">.*?FAANG Quick Reference.*?</div>\s*</div>\s*</div>', '', raw_html, flags=re.DOTALL)
        soup = BeautifulSoup(raw_html, 'html.parser')
        
        clean_mermaid(soup)
        
        for tree_box in soup.find_all(string=re.compile('COMPLETE BINARY TREE')):
            header = tree_box.find_parent('div', class_='section-header')
            if header:
                box = header.parent
                content = box.find('div', class_='section-content')
                if content:
                    flex_row = content.find('div', style=lambda s: s and 'display: flex' in s)
                    if flex_row:
                        flex_row['class'] = flex_row.get('class', []) + ['flex-row']
                        del flex_row['style']
        
        for tag in soup.find_all(True):
            if tag.name not in ['pre', 'code'] and not tag.find_parent('pre') and not tag.find_parent('code'):
                style = tag.get('style', '')
                if style:
                    style = re.sub(r'color\s*:\s*#ffffff;?', '', style, flags=re.IGNORECASE)
                    style = re.sub(r'color\s*:\s*#fff;?', '', style, flags=re.IGNORECASE)
                    style = re.sub(r'color\s*:\s*white;?', '', style, flags=re.IGNORECASE)
                    style = re.sub(r'color\s*:\s*#e2e8f0;?', '', style, flags=re.IGNORECASE)
                    if not any(c in style for c in ['color', 'background', 'width', 'flex', 'text-align', 'padding']):
                        del tag['style']
                    else:
                        tag['style'] = style
        
        seen_titles = deduplicate_and_restructure(soup)
        
        if fname in APPENDICES:
            pages = soup.find_all('div', class_='page')
            if pages:
                last_page = pages[-1]
                for color_class, title, content in APPENDICES[fname]:
                    norm_title = re.sub(r'[^A-Z0-9 ]', '', title.upper()).strip()
                    if norm_title not in seen_titles:
                        new_sec = soup.new_tag('div', attrs={'class': f'section-box {color_class}'})
                        new_hdr = soup.new_tag('div', attrs={'class': 'section-header'})
                        new_hdr.string = title
                        new_cnt = soup.new_tag('div', attrs={'class': 'section-content'})
                        cnt_soup = BeautifulSoup(content, 'html.parser')
                        new_cnt.append(cnt_soup)
                        new_sec.append(new_hdr)
                        new_sec.append(new_cnt)
                        last_page.append(new_sec)
        
        for page in soup.find_all('div', class_='page'):
            if not page.get_text(strip=True): page.decompose()

        pages = soup.find_all('div', class_='page')
        for page in pages:
            boxes_to_move = []
            for box in page.find_all('div', class_=lambda x: x and any(cls in x for cls in ['section-box', 'box-aha', 'box-tip', 'box-mistake'])):
                is_nested = False
                parent = box.parent
                while parent and parent != page:
                    p_classes = parent.get('class', [])
                    if any(cls in p_classes for cls in ['section-box', 'box-aha', 'box-tip', 'box-mistake']):
                        is_nested = True
                        break
                    parent = parent.parent
                if not is_nested:
                    boxes_to_move.append(box)
            grid_container = soup.new_tag('div', attrs={'class': 'content-grid'})
            for box in boxes_to_move:
                if should_span_all(box): box['class'] = box.get('class', []) + ['span-all']
                extracted = box.extract()
                grid_container.append(extracted)
            for grid in page.find_all('div', class_='grid-container'): grid.decompose()
            page.append(grid_container)

        # Generate numbers for headers sequentially across ALL pages, but NO TOC PAGE.
        counter = 1
        for i, page in enumerate(pages):
            for box in page.find_all('div', class_=lambda x: x and 'section-box' in x):
                header = box.find('div', class_='section-header')
                if header:
                    num_span = soup.new_tag('span', attrs={'class': 'num'})
                    num_span.string = str(counter)
                    header.insert(0, num_span)
                    counter += 1

        for style in soup.find_all('style'):
            # clean up old styles
            style.decompose()
            
        head = soup.find('head')
        if head:
            theme = THEMES.get(fname, {"primary": "#1e3a8a", "secondary": "#2563eb", "bg": "#f8fafc"})
            head.append(BeautifulSoup(get_v7_css(theme), 'html.parser'))
            
        body = soup.find('body')
        if body:
            old_script = soup.find('script', type='module')
            if old_script: old_script.decompose()
            body.append(BeautifulSoup(JS_SYNTAX, 'html.parser'))
            
        title_tag = soup.find('title')
        topic_name = fname.replace('_Final.html', '').replace('.', ' ').strip()
        if title_tag: title_tag.string = f"{topic_name} (FAANG Cheat Sheet)"
            
        with open(dst_path, 'w', encoding='utf-8') as f: f.write(str(soup))
        size_kb = os.path.getsize(dst_path) / 1024
        print(f"  [{size_kb:.0f}KB] {fname} - Finalized without TOC.")

if __name__ == '__main__':
    build_v7()

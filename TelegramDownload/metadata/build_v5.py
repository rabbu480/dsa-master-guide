import os
import re
from bs4 import BeautifulSoup

src_dir = r"C:\Users\rabba\Downloads\TelegramDownload\metadata"
v5_dir = r"C:\Users\rabba\Downloads\TelegramDownload\metadata\v5"
os.makedirs(v5_dir, exist_ok=True)

V5_CSS = """
<style id="faang-v5">
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Fira+Code:wght@400;500&display=swap');

:root {
    --primary: #1e3a8a; 
    --secondary: #2563eb; 
    --green: #10b981;
    --green-dark: #15803d;
    --red: #ef4444;
    --red-dark: #b91c1c;
    --yellow: #f59e0b;
    --yellow-dark: #b45309;
    --purple: #8b5cf6;
    --purple-dark: #5b21b6;
    --orange: #f97316;
    --orange-dark: #c2410c;
    
    --text-dark: #0f172a;
    --text-muted: #64748b;
    --bg-light: #f8fafc;
    --border-color: #cbd5e1;
}

body {
    font-family: 'Inter', sans-serif;
    background-color: #e2e8f0;
    color: var(--text-dark);
    margin: 0;
    padding: 20px;
    font-size: 13.5px;
    line-height: 1.5;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
}

/* FLEX UTILITIES FOR SIDE-BY-SIDE CONTENT (LIKE HEAPS DIAGRAM) */
.flex-row {
    display: flex;
    flex-direction: row;
    gap: 15px;
    align-items: stretch;
    justify-content: space-between;
    width: 100%;
}
.flex-col {
    display: flex;
    flex-direction: column;
    flex: 1;
    min-width: 0; /* Prevent flex overflow */
}
.bg-green { background-color: var(--green); color: white; padding: 4px 10px; border-radius: 4px; font-weight: bold; margin-bottom: 5px; text-align: center; }
.bg-red { background-color: var(--red); color: white; padding: 4px 10px; border-radius: 4px; font-weight: bold; margin-bottom: 5px; text-align: center; }

/* HORIZONTAL INTERVIEW FLOW */
.horizontal-flow {
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    gap: 10px;
    flex-wrap: wrap;
    justify-content: center;
    width: 100%;
}
.flow-step {
    background: #f1f5f9;
    border: 1px solid var(--primary);
    border-radius: 8px;
    padding: 8px;
    width: 130px;
    text-align: center;
    position: relative;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    flex-grow: 1;
    min-width: 120px;
}
.flow-step-num {
    background: var(--primary);
    color: white;
    width: 20px;
    height: 20px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 800;
    font-size: 0.75rem;
    position: absolute;
    top: -10px;
    left: 50%;
    transform: translateX(-50%);
}
.flow-step-title {
    font-weight: 800;
    color: var(--primary);
    margin-top: 5px;
    font-size: 0.85rem;
    text-transform: uppercase;
}
.flow-step-desc {
    font-size: 0.75rem;
    color: var(--text-dark);
    line-height: 1.2;
    margin-top: 4px;
}
.flow-arrow {
    color: var(--primary);
    font-size: 1.5rem;
    font-weight: bold;
    align-self: center;
}

.page {
    background: white;
    max-width: 1100px; 
    margin: 0 auto 40px auto;
    padding: 40px 50px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
    border-radius: 12px;
    page-break-after: always;
    border-top: 6px solid var(--primary);
    position: relative;
    overflow: hidden;
}

.header-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 3px solid var(--primary);
    padding-bottom: 12px;
    margin-bottom: 25px;
}
.header-title-box { display: flex; align-items: baseline; gap: 15px; }
.header-title-box h1 {
    margin: 0; font-size: 2.4rem; color: var(--primary);
    font-weight: 900; letter-spacing: 0.5px; text-transform: uppercase;
}
.header-title-box .subtitle {
    background-color: var(--secondary); color: white;
    padding: 5px 14px; border-radius: 20px; font-weight: 800; font-size: 0.85rem;
    box-shadow: 0 2px 4px rgba(37,99,235,0.2);
}

.toc-box {
    background-color: #f8fafc;
    border: 2px dashed var(--secondary);
    border-radius: 10px;
    padding: 20px 25px;
    margin-bottom: 30px;
    break-inside: avoid;
    page-break-inside: avoid;
}
.toc-header {
    color: var(--primary);
    font-size: 1.3rem;
    font-weight: 900;
    margin-bottom: 20px;
    text-transform: uppercase;
    display: flex;
    align-items: center;
    gap: 10px;
    letter-spacing: 0.5px;
}
.toc-masonry {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 25px;
}
.toc-page-col {
    break-inside: avoid;
    page-break-inside: avoid;
    background: white;
    border: 1px solid var(--border-color);
    padding: 15px;
    border-radius: 8px;
    box-sizing: border-box;
    box-shadow: 0 2px 5px rgba(0,0,0,0.02);
}
.toc-page-title {
    font-weight: 900;
    color: white;
    background-color: var(--secondary);
    padding: 5px 12px;
    border-radius: 6px;
    font-size: 0.9rem;
    display: inline-block;
    margin-bottom: 12px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}
.toc-item {
    font-size: 0.85rem;
    font-weight: 600;
    color: var(--text-dark);
    display: flex;
    align-items: flex-start;
    gap: 10px;
    margin-bottom: 8px;
    line-height: 1.4;
}
.toc-num {
    background-color: var(--primary);
    color: white;
    border-radius: 4px;
    padding: 2px 6px;
    font-size: 0.75rem;
    font-weight: 800;
    min-width: 18px;
    text-align: center;
    flex-shrink: 0;
}

/* CSS GRID FOR PERFECT SIDE-BY-SIDE READING ORDER */
.content-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 25px;
    align-items: start; /* Don't stretch rows */
    width: 100%;
}

.span-all {
    grid-column: 1 / -1 !important;
}

.section-box {
    border: 1px solid var(--primary);
    border-radius: 8px; 
    overflow: hidden; 
    background: white;
    box-shadow: 0 3px 8px rgba(0,0,0,0.04);
    break-inside: avoid;
    page-break-inside: avoid;
}
.section-header {
    background: var(--primary); color: white;
    padding: 10px 14px; font-weight: 800; font-size: 0.95rem;
    display: flex; align-items: center; text-transform: uppercase;
    letter-spacing: 0.5px;
}
.section-box.color-green { border-color: var(--green-dark); }
.section-box.color-green .section-header { background: var(--green-dark); }
.section-box.color-green .section-header span.num { color: var(--green-dark); }
.section-box.color-purple { border-color: var(--purple-dark); }
.section-box.color-purple .section-header { background: var(--purple-dark); }
.section-box.color-purple .section-header span.num { color: var(--purple-dark); }
.section-box.color-orange { border-color: var(--orange-dark); }
.section-box.color-orange .section-header { background: var(--orange-dark); }
.section-box.color-orange .section-header span.num { color: var(--orange-dark); }
.section-box.color-red { border-color: var(--red-dark); }
.section-box.color-red .section-header { background: var(--red-dark); }
.section-box.color-red .section-header span.num { color: var(--red-dark); }

.section-header span.num {
    background: white; color: var(--primary);
    border-radius: 50%; width: 24px; height: 24px;
    display: inline-flex; align-items: center; justify-content: center;
    margin-right: 12px; font-size: 0.85rem; font-weight: 900;
    box-shadow: 0 1px 3px rgba(0,0,0,0.2);
}
.section-content { padding: 15px; }

/* FIX INVISIBLE TEXT: Force defaults */
.section-content p, .section-content li, .section-content div:not([class]) {
    color: var(--text-dark);
}

.box-aha { background-color: #f0fdf4; border: 2px solid #22c55e; border-radius: 8px; padding: 20px 15px 15px; position: relative; box-shadow: 0 2px 5px rgba(34,197,94,0.1); break-inside: avoid; page-break-inside: avoid; }
.box-aha-title { background-color: #22c55e; color: white; padding: 4px 14px; border-radius: 20px; font-weight: bold; position: absolute; top: -14px; left: 15px; font-size: 0.85rem; letter-spacing: 0.5px; }
.box-tip { background-color: #fffbeb; border: 2px solid #f59e0b; border-radius: 8px; padding: 20px 15px 15px; position: relative; box-shadow: 0 2px 5px rgba(245,158,11,0.1); break-inside: avoid; page-break-inside: avoid; }
.box-tip-title { background-color: #f59e0b; color: white; padding: 4px 14px; border-radius: 20px; font-weight: bold; position: absolute; top: -14px; left: 15px; font-size: 0.85rem; letter-spacing: 0.5px; }
.box-mistake { background-color: #fef2f2; border: 2px solid #ef4444; border-radius: 8px; padding: 20px 15px 15px; position: relative; box-shadow: 0 2px 5px rgba(239,68,68,0.1); break-inside: avoid; page-break-inside: avoid; }
.box-mistake-title { background-color: #ef4444; color: white; padding: 4px 14px; border-radius: 20px; font-weight: bold; position: absolute; top: -14px; left: 15px; font-size: 0.85rem; letter-spacing: 0.5px; }

pre {
    background: #f8fafc !important; color: #0f172a !important;
    border: 1px solid var(--border-color) !important; border-left: 4px solid var(--secondary) !important;
    padding: 12px 15px !important; border-radius: 6px !important;
    font-family: 'Fira Code', monospace !important; font-size: 0.85rem !important;
    margin: 10px 0 !important; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; 
    box-shadow: inset 0 0 8px rgba(0,0,0,0.01) !important;
}
code { background: #f1f5f9; color: var(--secondary); padding: 2px 6px; border-radius: 4px; font-family: 'Fira Code', monospace; font-size: 0.9em; font-weight: 700; }
pre code { background: transparent !important; color: inherit !important; padding: 0 !important; font-weight: 500; }

table { width: 100%; border-collapse: separate; border-spacing: 0; font-size: 0.85rem; margin: 10px 0; border-radius: 6px; overflow: hidden; border: 1px solid var(--border-color); box-shadow: 0 2px 4px rgba(0,0,0,0.02); }
table th { background: var(--primary) !important; color: white !important; padding: 8px 12px; text-align: left; font-weight: 700; white-space: nowrap; text-transform: uppercase; font-size: 0.8rem; letter-spacing: 0.5px; border-bottom: 2px solid rgba(0,0,0,0.1); }
table td { border-bottom: 1px solid var(--border-color); border-right: 1px solid var(--border-color); padding: 8px 12px; line-height: 1.4; }
table tr td:last-child { border-right: none; }
table tr:last-child td { border-bottom: none; }
table tr:nth-child(even) td { background: #f8fafc; }
table tr:hover td { background: #f1f5f9; }

ul, ol { margin: 0; padding-left: 20px; } li { margin-bottom: 6px; line-height: 1.5; }

.diff-easy { color: #16a34a; font-weight: 800; background: #dcfce7; padding: 2px 8px; border-radius: 12px; font-size: 0.8em; text-transform: uppercase; }
.diff-med { color: #d97706; font-weight: 800; background: #fef3c7; padding: 2px 8px; border-radius: 12px; font-size: 0.8em; text-transform: uppercase; }
.diff-hard { color: #dc2626; font-weight: 800; background: #fee2e2; padding: 2px 8px; border-radius: 12px; font-size: 0.8em; text-transform: uppercase; }

/* FIX MERMAID SIZING SO IT DOESN'T BECOME ENORMOUS */
.mermaid svg {
    max-width: 100% !important;
    height: auto !important;
    max-height: 220px !important;
    display: block;
    margin: 0 auto;
}

[style*="background-color: #1e1e1e"],[style*="background-color:#1e1e1e"],[style*="background: #1e1e2e"] { background: transparent !important; }
[style*="color: #d4d4d4"],[style*="color:#d4d4d4"],[style*="color: #e2e8f0"] { color: #0f172a !important; }
[style*="color: #569cd6"] { color: #2563eb !important; font-weight: 700; } 
[style*="color: #c586c0"] { color: #7e22ce !important; font-weight: 700; } 
[style*="color: #b5cea8"] { color: #b91c1c !important; font-weight: 600; } 
[style*="color: #6a9955"] { color: #64748b !important; font-style: italic; } 

@media print {
    body { background: white !important; padding: 0 !important; }
    .page { box-shadow: none !important; margin: 0 !important; padding: 20px 0 !important; border: none !important; border-top: 4px solid var(--primary) !important; border-radius: 0 !important; }
    .section-box, .box-aha, .box-tip, .box-mistake, .toc-box, .toc-page-col { 
        page-break-inside: avoid !important;
        break-inside: avoid !important; 
    }
}
</style>
"""

JS_SYNTAX = """
<script type="module">
    import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
    mermaid.initialize({ 
        startOnLoad: true, 
        theme: 'base',
        themeVariables: {
            primaryColor: '#f8fafc',
            primaryTextColor: '#0f172a',
            primaryBorderColor: '#3b82f6',
            lineColor: '#94a3b8',
            fontFamily: 'Inter',
            fontSize: '14px',
            nodeBorder: '#3b82f6'
        }
    });

    document.addEventListener('DOMContentLoaded', function() {
        document.querySelectorAll('pre').forEach(pre => {
            let code = pre.innerHTML;
            if (code.indexOf('\\n') === -1 && code.length > 60) {
                code = code.replace(/; /g, ';\\n    ');
                code = code.replace(/{ /g, '{\\n    ');
                code = code.replace(/ }/g, '\\n}');
                pre.innerHTML = code;
            }
        });
    });
</script>
"""

APPENDICES = {
    "1.Array&Hashing_Final.html": [
        ("color-purple", "TWO POINTER TEMPLATES", "<pre>// Opposite ends\nint lo = 0, hi = n - 1;\nwhile (lo < hi) {\n    int sum = arr[lo] + arr[hi];\n    if (sum == target) return true;\n    else if (sum < target) lo++;\n    else hi--;\n}</pre>"),
        ("color-orange", "SLIDING WINDOW TEMPLATE", "<pre>// Variable window\nint lo = 0, maxLen = 0;\nfor (int hi = 0; hi < n; hi++) {\n    // add arr[hi] to window state\n    while (!validWindow) {\n        // remove arr[lo] from state\n        lo++;\n    }\n    maxLen = Math.max(maxLen, hi - lo + 1);\n}</pre>"),
        ("color-green", "PREFIX SUM HASHMAP (FAANG TRAP)", "<pre>// Subarray Sum Equals K\nint sum = 0, count = 0;\nMap&lt;Integer,Integer&gt; pCount = new HashMap&lt;&gt;();\npCount.put(0, 1);\nfor (int num : nums) {\n    sum += num;\n    count += pCount.getOrDefault(sum - k, 0);\n    pCount.merge(sum, 1, Integer::sum);\n}</pre>"),
        ("color-red", "TOP ARRAYS PROBLEMS", "<table><tr><th>#</th><th>Problem</th><th>Pattern</th><th>Level</th></tr><tr><td>1</td><td>Two Sum</td><td>HashMap</td><td><span class='diff-easy'>Easy</span></td></tr><tr><td>128</td><td>Longest Consecutive</td><td>HashSet</td><td><span class='diff-med'>Med</span></td></tr><tr><td>560</td><td>Subarray Sum = K</td><td>Prefix+Map</td><td><span class='diff-med'>Med</span></td></tr><tr><td>76</td><td>Min Window Substring</td><td>Sliding Window</td><td><span class='diff-hard'>Hard</span></td></tr></table>")
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
        ("color-orange", "COMPARATOR GUIDE (FAANG Trap)", "<table><tr><th>Goal</th><th>Comparator</th></tr><tr><td>Min Heap</td><td><code>new PriorityQueue&lt;&gt;()</code></td></tr><tr><td>Max Heap</td><td><code>Collections.reverseOrder()</code></td></tr><tr><td>Safe</td><td><code>(a,b) -> Integer.compare(a, b)</code></td></tr></table>"),
        ("color-red", "TOP HEAPS PROBLEMS", "<table><tr><th>#</th><th>Problem</th><th>Pattern</th><th>Level</th></tr><tr><td>215</td><td>Kth Largest Element</td><td>Min Heap</td><td><span class='diff-med'>Med</span></td></tr><tr><td>347</td><td>Top K Frequent</td><td>Map + Min Heap</td><td><span class='diff-med'>Med</span></td></tr><tr><td>295</td><td>Median Data Stream</td><td>Two Heaps</td><td><span class='diff-hard'>Hard</span></td></tr></table>")
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

def deduplicate_sections(soup):
    seen_titles = set()
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
                box.decompose()

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

def should_span_all(box):
    header = box.find('div', class_='section-header')
    if header:
        title = header.get_text(strip=True).upper()
        if 'TEMPLATE COMPARISON' in title: return True
        if 'ROADMAP' in title: return True
        if 'INTERVIEW FLOW' in title: return True 
        
    table = box.find('table')
    if table:
        first_row = table.find('tr')
        if first_row:
            if len(first_row.find_all(['td', 'th'])) >= 4:
                return True
    return False

def build_v5():
    finals = [f for f in os.listdir(src_dir) if f.endswith('_Final.html')]
    print(f"Building v5 with CSS GRID (Left-to-Right Ordering) + MAX-WIDTH FIXES...")
    
    for fname in sorted(finals):
        src_path = os.path.join(src_dir, fname)
        dst_path = os.path.join(v5_dir, fname)
        
        with open(src_path, 'r', encoding='utf-8') as f:
            raw_html = f.read()
            
        raw_html = re.sub(r'<div class="header-top">.*?FAANG Quick Reference.*?</div>\s*</div>\s*</div>', '', raw_html, flags=re.DOTALL)
        soup = BeautifulSoup(raw_html, 'html.parser')
        
        # AGGRESSIVELY STRIP INLINE COLORS THAT RUIN LIGHT MODE VISIBILITY
        for tag in soup.find_all(True):
            if tag.name not in ['pre', 'code'] and not tag.find_parent('pre') and not tag.find_parent('code'):
                style = tag.get('style', '')
                if style:
                    # Remove "color: white", "color: #fff", "color: #ffffff", "color: #e2e8f0" (light slate)
                    style = re.sub(r'color\s*:\s*#ffffff;?', '', style, flags=re.IGNORECASE)
                    style = re.sub(r'color\s*:\s*#fff;?', '', style, flags=re.IGNORECASE)
                    style = re.sub(r'color\s*:\s*white;?', '', style, flags=re.IGNORECASE)
                    style = re.sub(r'color\s*:\s*#e2e8f0;?', '', style, flags=re.IGNORECASE)
                    tag['style'] = style
                    if not tag['style'].strip():
                        del tag['style']
        
        # Strip all inline styles EXCEPT essential layouts
        for tag in soup.find_all(True):
            if tag.get('style'):
                if not any(c in tag['style'] for c in ['color', 'background', 'width', 'flex']):
                    del tag['style']
        
        seen_titles = deduplicate_sections(soup)
        
        # APPENDICES (Now properly flowing into the grid!)
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
            if not page.get_text(strip=True):
                page.decompose()

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
            
            # USE content-grid instead of content-masonry!
            grid_container = soup.new_tag('div', attrs={'class': 'content-grid'})
            
            for box in boxes_to_move:
                if should_span_all(box):
                    box['class'] = box.get('class', []) + ['span-all']
                extracted = box.extract()
                grid_container.append(extracted)
                
            for grid in page.find_all('div', class_='grid-container'):
                grid.decompose()
                
            page.append(grid_container)

        counter = 1
        toc_by_page = []
        for i, page in enumerate(pages):
            page_sections = []
            for box in page.find_all('div', class_=lambda x: x and 'section-box' in x):
                header = box.find('div', class_='section-header')
                if header:
                    title_text = header.get_text(strip=True)
                    page_sections.append((counter, title_text))
                    num_span = soup.new_tag('span', attrs={'class': 'num'})
                    num_span.string = str(counter)
                    header.insert(0, num_span)
                    counter += 1
            if page_sections:
                toc_by_page.append((i + 1, page_sections))
                
        if toc_by_page:
            toc_div = soup.new_tag('div', attrs={'class': 'toc-box'})
            toc_hdr = soup.new_tag('div', attrs={'class': 'toc-header'})
            toc_hdr.string = "📖 WHAT'S INSIDE THIS CHEAT SHEET"
            toc_div.append(toc_hdr)
            toc_masonry = soup.new_tag('div', attrs={'class': 'toc-masonry'})
            for page_num, sections in toc_by_page:
                page_col = soup.new_tag('div', attrs={'class': 'toc-page-col'})
                page_title = soup.new_tag('div', attrs={'class': 'toc-page-title'})
                page_title.string = f"PAGE {page_num}"
                page_col.append(page_title)
                for num, title in sections:
                    item = soup.new_tag('div', attrs={'class': 'toc-item'})
                    num_span = soup.new_tag('div', attrs={'class': 'toc-num'})
                    num_span.string = str(num)
                    item.append(num_span)
                    item.append(soup.new_string(title))
                    page_col.append(item)
                toc_masonry.append(page_col)
            toc_div.append(toc_masonry)
            
            first_page = soup.find('div', class_='page')
            if first_page:
                header_top = first_page.find('div', class_='header-top')
                if header_top:
                    header_top.insert_after(toc_div)
                else:
                    first_page.insert(0, toc_div)

        for style in soup.find_all('style'):
            if not style.get('id') == 'faang-v5':
                style.decompose()
            
        head = soup.find('head')
        if head:
            head.append(BeautifulSoup(V5_CSS, 'html.parser'))
            
        body = soup.find('body')
        if body:
            old_script = soup.find('script', type='module')
            if old_script: old_script.decompose()
            body.append(BeautifulSoup(JS_SYNTAX, 'html.parser'))
            
        title_tag = soup.find('title')
        topic_name = fname.replace('_Final.html', '').replace('.', ' ').strip()
        if title_tag:
            title_tag.string = f"{topic_name} (FAANG Cheat Sheet)"
            
        with open(dst_path, 'w', encoding='utf-8') as f:
            f.write(str(soup))
            
        size_kb = os.path.getsize(dst_path) / 1024
        print(f"  [{size_kb:.0f}KB] {fname} - Added CSS Grid v5.")

if __name__ == '__main__':
    build_v5()

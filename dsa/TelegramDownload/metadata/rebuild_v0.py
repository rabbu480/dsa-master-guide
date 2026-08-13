"""
rebuild_v0.py
--------------
Rebuilds all v0 files from scratch from the original Final HTML files.
Applies:
  1. New master CSS (charcoal + amber palette, xerox-safe)
  2. Code block fixes (white bg, black text)
  3. Invisible color fixes
  4. FAANG appendix pages
"""

import os
import re

src_dir = r"C:\Users\rabba\Downloads\TelegramDownload\metadata"
v0_dir = r"C:\Users\rabba\Downloads\TelegramDownload\metadata\v0"
os.makedirs(v0_dir, exist_ok=True)

# =====================================================
# New Master CSS
# =====================================================
NEW_MASTER_CSS = """<style id="master-v1">
    /* =====================================================
       FAANG CHEAT SHEET — v1 Color Palette
       Palette: Charcoal + Amber accent
       Tested for: Screen color | B&W xerox | PDF export
    ====================================================== */
    :root {
        --primary: #1c1c2e;
        --accent:  #d97706;
        --accent-light: #fef3c7;
        --accent-border: #f59e0b;
        --ok:   #15803d;
        --warn: #b45309;
        --err:  #b91c1c;
        --text-body:  #111827;
        --text-sub:   #374151;
        --text-muted: #6b7280;
        --bg-page:    #f1f5f9;
        --bg-card:    #ffffff;
        --bg-code:    #f8f8f2;
        --bg-table-alt: #f9fafb;
        --bg-tip:    #f0fdf4;
        --bg-warn:   #fffbeb;
        --bg-danger: #fef2f2;
        --bg-info:   #eff6ff;
        --border:    #d1d5db;
    }
    * { box-sizing: border-box; }
    body {
        font-family: 'Inter', system-ui, sans-serif;
        background-color: var(--bg-page);
        color: var(--text-body);
        margin: 0; padding: 24px;
        font-size: 13.5px; line-height: 1.5;
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
    }
    .page {
        background: var(--bg-card);
        max-width: 1120px;
        margin: 0 auto 48px auto;
        padding: 36px 40px;
        box-shadow: 0 2px 16px rgba(0,0,0,0.08);
        border-radius: 10px;
        page-break-after: always;
        border-top: 4px solid var(--accent);
    }
    .header-top {
        display: flex;
        justify-content: space-between; align-items: center;
        border-bottom: 2px solid var(--primary);
        padding-bottom: 12px; margin-bottom: 22px;
    }
    .header-top h1 {
        margin: 0; font-size: 2.2rem; color: var(--primary);
        font-weight: 900; letter-spacing: -0.5px;
    }
    .header-top .subtitle { font-size: 1rem; font-weight: 500; color: var(--text-sub); margin-top: 4px; }
    .header-top .page-number {
        background: var(--primary); color: white;
        padding: 6px 18px; border-radius: 20px;
        font-weight: 700; font-size: 0.9rem; letter-spacing: 1px;
    }
    .grid-container { display: grid; grid-template-columns: 1fr 1fr; gap: 18px; }
    .col-left, .col-right { min-width: 0; }
    .full-width { grid-column: 1 / -1; }
    .section-box {
        border: 1px solid var(--border); border-radius: 8px;
        overflow: hidden; margin-bottom: 18px;
        background: var(--bg-card);
        box-shadow: 0 1px 4px rgba(0,0,0,0.05);
    }
    /* SECTION HEADERS: charcoal bg + amber left accent + WHITE text */
    .section-header {
        background: var(--primary) !important;
        color: #ffffff !important;
        padding: 9px 14px;
        font-weight: 700; font-size: 0.82rem;
        letter-spacing: 0.8px; text-transform: uppercase;
        display: flex; align-items: center;
        border-left: 4px solid var(--accent) !important;
    }
    .section-header span.num {
        background: var(--accent); color: var(--primary);
        border-radius: 50%; width: 22px; height: 22px;
        display: inline-flex; align-items: center; justify-content: center;
        margin-right: 10px; font-size: 0.78rem; font-weight: 900; flex-shrink: 0;
    }
    .section-content { padding: 14px 16px; }
    ul, ol { margin: 6px 0; padding-left: 20px; }
    li { margin-bottom: 6px; }
    /* TABLES: black header, alternating rows */
    table { width: 100%; border-collapse: collapse; font-size: 0.85rem; margin: 8px 0; }
    table th {
        background: var(--primary) !important; color: #ffffff !important;
        padding: 8px 10px; font-weight: 600; font-size: 0.8rem;
        text-align: left; letter-spacing: 0.4px;
        -webkit-print-color-adjust: exact; print-color-adjust: exact;
    }
    table td { border: 1px solid var(--border); padding: 7px 10px; vertical-align: top; }
    table tr:nth-child(even) td { background: var(--bg-table-alt); }
    table tr:nth-child(odd) td { background: #ffffff; }
    /* CODE BLOCKS: cream bg, near-black text — ALWAYS PRINTABLE */
    pre {
        background: var(--bg-code) !important;
        color: var(--text-body) !important;
        border: 1px solid var(--border) !important;
        border-left: 4px solid var(--accent) !important;
        padding: 12px 14px !important; border-radius: 6px !important;
        font-family: 'Fira Code', 'Courier New', monospace !important;
        font-size: 0.8rem !important; margin: 10px 0 !important;
        overflow-x: auto; white-space: pre-wrap; word-break: break-word;
        line-height: 1.6; box-shadow: none !important;
    }
    code {
        background: #f3f4f6 !important; color: #1c1c2e !important;
        border: 1px solid var(--border) !important;
        padding: 1px 5px !important; border-radius: 4px !important;
        font-family: 'Fira Code', 'Courier New', monospace !important;
        font-size: 0.85em !important; box-shadow: none !important;
    }
    pre code { background: transparent !important; color: inherit !important; border: none !important; padding: 0 !important; }
    .flex-row { display: flex; gap: 16px; }
    .flex-col { flex: 1; text-align: center; min-width: 0; }
    .bg-green { background: var(--ok); color: white; padding: 4px 10px; border-radius: 4px; font-weight: 700; font-size: 0.82rem; display: inline-block; }
    .bg-red   { background: var(--err); color: white; padding: 4px 10px; border-radius: 4px; font-weight: 700; font-size: 0.82rem; display: inline-block; }
    .badge-o1   { display:inline-block; background:#dcfce7; color:#14532d; padding:2px 7px; border-radius:4px; font-weight:700; font-size:0.75rem; border:1px solid #15803d; }
    .badge-olog { display:inline-block; background:#e0f2fe; color:#164e63; padding:2px 7px; border-radius:4px; font-weight:700; font-size:0.75rem; border:1px solid #0369a1; }
    .badge-on   { display:inline-block; background:var(--accent-light); color:#92400e; padding:2px 7px; border-radius:4px; font-weight:700; font-size:0.75rem; border:1px solid var(--warn); }
    .badge-on2  { display:inline-block; background:#fee2e2; color:#7f1d1d; padding:2px 7px; border-radius:4px; font-weight:700; font-size:0.75rem; border:1px solid var(--err); }
    .rule-box, .callout-warn {
        background: var(--bg-warn); border: 1px solid var(--accent-border);
        border-left: 5px solid var(--accent-border); padding: 10px 14px;
        margin: 10px 0; border-radius: 0 6px 6px 0; font-size: 0.88rem;
    }
    .callout-tip {
        background: var(--bg-tip); border: 1px solid #16a34a;
        border-left: 5px solid #16a34a; padding: 10px 14px;
        margin: 10px 0; border-radius: 0 6px 6px 0; font-size: 0.88rem;
    }
    .callout-danger {
        background: var(--bg-danger); border: 1px solid var(--err);
        border-left: 5px solid var(--err); padding: 10px 14px;
        margin: 10px 0; border-radius: 0 6px 6px 0; font-size: 0.88rem;
    }
    .callout-info {
        background: var(--bg-info); border: 1px solid #2563eb;
        border-left: 5px solid #2563eb; padding: 10px 14px;
        margin: 10px 0; border-radius: 0 6px 6px 0; font-size: 0.88rem;
    }
    .mermaid { display: flex; justify-content: center; margin: 12px 0; }
    /* FIX INVISIBLE COLORS from subagent inline styles */
    [style*="color: #94a3b8"], [style*="color:#94a3b8"] { color: #4b5563 !important; }
    [style*="color: #cbd5e1"], [style*="color:#cbd5e1"] { color: #374151 !important; }
    [style*="color: #e2e8f0"], [style*="color:#e2e8f0"] { color: #374151 !important; }
    @media print {
        body { background: white !important; padding: 0 !important; font-size: 11px !important; }
        .page {
            box-shadow: none !important; border: none !important;
            border-top: 3px solid #000 !important;
            margin: 0 !important; padding: 12px !important;
            max-width: 100% !important; page-break-after: always;
        }
        .section-header {
            background: #111 !important; color: #fff !important;
            -webkit-print-color-adjust: exact; print-color-adjust: exact;
        }
        table th { background: #111 !important; color: #fff !important; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
        table tr:nth-child(even) td { background: #f0f0f0 !important; }
        pre { background: #f8f8f8 !important; color: #000 !important; border: 1px solid #aaa !important; border-left: 3px solid #333 !important; page-break-inside: avoid; }
        code { background: #eee !important; color: #000 !important; }
        .callout-tip, .callout-warn, .callout-danger, .callout-info, .rule-box { border-left-width: 3px !important; background: #f5f5f5 !important; }
        .section-box { page-break-inside: avoid; }
        a { color: inherit; text-decoration: none; }
    }
</style>"""

# =====================================================
# FAANG Appendix pages (one per topic)
# =====================================================
APPENDICES = {
    "10.Heaps_Final.html": """
<div class="page">
  <div class="header-top"><div><h1>HEAP &mdash; FAANG Quick Reference</h1><div class="subtitle">&#x2B50; Must-Know Patterns &amp; Critical Code Templates</div></div><div class="page-number">APPENDIX</div></div>
  <div class="grid-container">
    <div>
      <div class="section-box"><div class="section-header"><span class="num">A</span> TOP-K ELEMENTS (Most Common FAANG Pattern)</div><div class="section-content">
        <p><strong>Rule:</strong> K Largest → Min Heap of size K. K Smallest → Max Heap of size K.</p>
        <pre>// K Largest Elements — O(n log k)
PriorityQueue&lt;Integer&gt; minHeap = new PriorityQueue&lt;&gt;();
for (int num : nums) {
    minHeap.offer(num);
    if (minHeap.size() > k) minHeap.poll();
}
// minHeap contains K largest elements</pre>
        <pre>// K Most Frequent — O(n log k)
Map&lt;Integer, Integer&gt; freq = new HashMap&lt;&gt;();
for (int n : nums) freq.merge(n, 1, Integer::sum);
PriorityQueue&lt;int[]&gt; pq = new PriorityQueue&lt;&gt;((a,b)->a[1]-b[1]);
for (var e : freq.entrySet()) {
    pq.offer(new int[]{e.getKey(), e.getValue()});
    if (pq.size() > k) pq.poll();
}</pre>
      </div></div>
      <div class="section-box"><div class="section-header"><span class="num">B</span> TWO-HEAP MEDIAN PATTERN</div><div class="section-content">
        <pre>// MedianFinder — O(log n) add, O(1) findMedian
PriorityQueue&lt;Integer&gt; lo = new PriorityQueue&lt;&gt;(Collections.reverseOrder());
PriorityQueue&lt;Integer&gt; hi = new PriorityQueue&lt;&gt;();
void addNum(int n) {
    lo.offer(n);
    hi.offer(lo.poll());       // balance max to hi
    if (hi.size() > lo.size()) lo.offer(hi.poll()); // rebalance
}
double findMedian() {
    return lo.size() > hi.size() ? lo.peek() : (lo.peek()+hi.peek())/2.0;
}</pre>
      </div></div>
      <div class="section-box"><div class="section-header"><span class="num">C</span> K-WAY MERGE</div><div class="section-content">
        <pre>// Merge K sorted lists — O(n log k)
PriorityQueue&lt;int[]&gt; pq = new PriorityQueue&lt;&gt;((a,b)->a[0]-b[0]);
for (int i = 0; i &lt; lists.length; i++)
    if (!lists[i].isEmpty())
        pq.offer(new int[]{lists[i].get(0), i, 0});
while (!pq.isEmpty()) {
    int[] cur = pq.poll(); result.add(cur[0]);
    int ni = cur[2]+1;
    if (ni &lt; lists[cur[1]].size())
        pq.offer(new int[]{lists[cur[1]].get(ni), cur[1], ni});
}</pre>
      </div></div>
    </div>
    <div>
      <div class="section-box"><div class="section-header"><span class="num">D</span> COMPARATOR GUIDE (FAANG Trap)</div><div class="section-content">
        <table><tr><th>Goal</th><th>Comparator</th></tr>
        <tr><td>Min Heap (default)</td><td><code>new PriorityQueue&lt;&gt;()</code></td></tr>
        <tr><td>Max Heap</td><td><code>Collections.reverseOrder()</code></td></tr>
        <tr><td>By field ascending</td><td><code>(a,b) -> Integer.compare(a.val, b.val)</code></td></tr>
        <tr><td>By 2nd col desc</td><td><code>(a,b) -> b[1] - a[1]</code></td></tr>
        <tr><td>Multi-key</td><td><code>(a,b) -> a[0]==b[0] ? a[1]-b[1] : a[0]-b[0]</code></td></tr></table>
        <div class="callout-danger" style="margin-top:10px;"><strong>&#x26A0; Overflow Trap:</strong> Never use <code>b - a</code> if values near Integer.MAX_VALUE. Use <code>Integer.compare(b, a)</code>.</div>
      </div></div>
      <div class="section-box"><div class="section-header"><span class="num">E</span> DECISION TABLE</div><div class="section-content">
        <table><tr><th>Trigger Keywords</th><th>Use</th></tr>
        <tr><td>K largest / K smallest</td><td>Min/Max Heap size K</td></tr>
        <tr><td>Most frequent K</td><td>HashMap + Min Heap</td></tr>
        <tr><td>Running median</td><td>Two Heaps</td></tr>
        <tr><td>Merge K sorted</td><td>K-Way Merge (Min Heap)</td></tr>
        <tr><td>Reorganize / Rearrange</td><td>Max Heap greedy</td></tr>
        <tr><td>Task Scheduler</td><td>Max Heap + cooldown</td></tr>
        <tr><td>Shortest path (weighted)</td><td>Dijkstra + Min Heap</td></tr></table>
      </div></div>
      <div class="section-box"><div class="section-header"><span class="num">F</span> TOP LEETCODE PROBLEMS</div><div class="section-content">
        <table><tr><th>#</th><th>Problem</th><th>Pattern</th><th>Level</th></tr>
        <tr><td>215</td><td>Kth Largest Element</td><td>Top-K</td><td><span style="color:#b45309;font-weight:700;">Med</span></td></tr>
        <tr><td>347</td><td>Top K Frequent</td><td>HashMap+Heap</td><td><span style="color:#b45309;font-weight:700;">Med</span></td></tr>
        <tr><td>295</td><td>Median Data Stream</td><td>Two Heap</td><td><span style="color:#b91c1c;font-weight:700;">Hard</span></td></tr>
        <tr><td>23</td><td>Merge K Sorted Lists</td><td>K-Way Merge</td><td><span style="color:#b91c1c;font-weight:700;">Hard</span></td></tr>
        <tr><td>621</td><td>Task Scheduler</td><td>Max Heap greedy</td><td><span style="color:#b45309;font-weight:700;">Med</span></td></tr>
        <tr><td>767</td><td>Reorganize String</td><td>Max Heap greedy</td><td><span style="color:#b45309;font-weight:700;">Med</span></td></tr>
        <tr><td>1046</td><td>Last Stone Weight</td><td>Max Heap basic</td><td><span style="color:#15803d;font-weight:700;">Easy</span></td></tr></table>
      </div></div>
    </div>
  </div>
</div>
""",

    "6.Binary_Search_Final.html": """
<div class="page">
  <div class="header-top"><div><h1>BINARY SEARCH &mdash; FAANG Quick Reference</h1><div class="subtitle">&#x2B50; Universal Template &amp; All Variants</div></div><div class="page-number">APPENDIX</div></div>
  <div class="grid-container">
    <div>
      <div class="section-box"><div class="section-header"><span class="num">A</span> UNIVERSAL TEMPLATE (Covers 99% of problems)</div><div class="section-content">
        <pre>// Find LEFTMOST position where condition is true
int lo = 0, hi = n;  // hi=n for "first position satisfying"
while (lo &lt; hi) {
    int mid = lo + (hi - lo) / 2;  // no overflow
    if (condition(mid)) hi = mid;   // could be answer
    else lo = mid + 1;              // too small
}
return lo; // check if lo is valid answer</pre>
        <pre>// Find RIGHTMOST satisfying position
while (lo &lt; hi) {
    int mid = lo + (hi - lo + 1) / 2; // +1 avoids infinite loop
    if (condition(mid)) lo = mid;
    else hi = mid - 1;
}</pre>
        <div class="callout-tip"><strong>Key Insight:</strong> Define a monotone boolean function. BS finds the boundary.</div>
      </div></div>
      <div class="section-box"><div class="section-header"><span class="num">B</span> ROTATED SORTED ARRAY</div><div class="section-content">
        <pre>// #33 Search in Rotated Sorted Array
int lo = 0, hi = nums.length - 1;
while (lo &lt;= hi) {
    int mid = lo + (hi - lo) / 2;
    if (nums[mid] == target) return mid;
    if (nums[lo] &lt;= nums[mid]) { // LEFT half sorted
        if (target >= nums[lo] && target &lt; nums[mid]) hi = mid-1;
        else lo = mid+1;
    } else { // RIGHT half sorted
        if (target > nums[mid] && target &lt;= nums[hi]) lo = mid+1;
        else hi = mid-1;
    }
}
return -1;</pre>
      </div></div>
    </div>
    <div>
      <div class="section-box"><div class="section-header"><span class="num">C</span> SEARCH ON ANSWER PATTERN</div><div class="section-content">
        <pre>// "Minimize the maximum" or "Maximize the minimum"
// Search the ANSWER SPACE, not the array
long lo = minPossible, hi = maxPossible;
while (lo &lt; hi) {
    long mid = lo + (hi - lo) / 2;
    if (canAchieve(mid)) hi = mid;   // mid works, try smaller
    else lo = mid + 1;               // mid too small
}
return lo;</pre>
        <div class="callout-info">Examples: Koko Eating Bananas (#875), Ship Packages (#1011), Split Array (#410)</div>
      </div></div>
      <div class="section-box"><div class="section-header"><span class="num">D</span> COMMON PITFALLS</div><div class="section-content">
        <table><tr><th>Pitfall</th><th>Fix</th></tr>
        <tr><td><code>(lo+hi)/2</code> overflow</td><td><code>lo + (hi-lo)/2</code></td></tr>
        <tr><td>Infinite loop lo=mid</td><td>Use <code>mid = lo+(hi-lo+1)/2</code> when lo=mid</td></tr>
        <tr><td>Off-by-one</td><td>Dry-run with 2-element array</td></tr>
        <tr><td>Wrong boundary</td><td>Draw timeline: "what's the first mid that satisfies?"</td></tr></table>
      </div></div>
      <div class="section-box"><div class="section-header"><span class="num">E</span> TOP LEETCODE PROBLEMS</div><div class="section-content">
        <table><tr><th>#</th><th>Problem</th><th>Level</th></tr>
        <tr><td>704</td><td>Binary Search (classic)</td><td><span style="color:#15803d;font-weight:700;">Easy</span></td></tr>
        <tr><td>33</td><td>Search Rotated Array</td><td><span style="color:#b45309;font-weight:700;">Med</span></td></tr>
        <tr><td>153</td><td>Find Min in Rotated</td><td><span style="color:#b45309;font-weight:700;">Med</span></td></tr>
        <tr><td>875</td><td>Koko Eating Bananas</td><td><span style="color:#b45309;font-weight:700;">Med</span></td></tr>
        <tr><td>1011</td><td>Capacity to Ship</td><td><span style="color:#b45309;font-weight:700;">Med</span></td></tr>
        <tr><td>4</td><td>Median Two Sorted Arrays</td><td><span style="color:#b91c1c;font-weight:700;">Hard</span></td></tr>
        <tr><td>410</td><td>Split Array Largest Sum</td><td><span style="color:#b91c1c;font-weight:700;">Hard</span></td></tr></table>
      </div></div>
    </div>
  </div>
</div>
""",

    "1.Array&Hashing_Final.html": """
<div class="page">
  <div class="header-top"><div><h1>ARRAYS &amp; HASHING &mdash; FAANG Quick Reference</h1><div class="subtitle">&#x2B50; Core Patterns — Two Pointer, Sliding Window, Prefix Sum</div></div><div class="page-number">APPENDIX</div></div>
  <div class="grid-container">
    <div>
      <div class="section-box"><div class="section-header"><span class="num">A</span> TWO POINTERS</div><div class="section-content">
        <pre>// Opposite ends (sorted array — Two Sum, 3Sum)
int lo = 0, hi = n - 1;
while (lo &lt; hi) {
    int s = arr[lo] + arr[hi];
    if (s == target) { /* found */ lo++; hi--; }
    else if (s &lt; target) lo++;
    else hi--;
}</pre>
        <pre>// Same direction slow/fast (remove duplicates)
int slow = 0;
for (int fast = 0; fast &lt; n; fast++)
    if (arr[fast] != arr[slow]) arr[++slow] = arr[fast];</pre>
      </div></div>
      <div class="section-box"><div class="section-header"><span class="num">B</span> SLIDING WINDOW</div><div class="section-content">
        <pre>// Fixed window size K (max sum of K elements)
int sum = 0, max = 0;
for (int i = 0; i &lt; n; i++) {
    sum += arr[i];
    if (i >= k) sum -= arr[i-k];
    if (i >= k-1) max = Math.max(max, sum);
}</pre>
        <pre>// Variable window (longest substring without repeat)
int lo = 0, maxLen = 0;
Map&lt;Character,Integer&gt; map = new HashMap&lt;&gt;();
for (int hi = 0; hi &lt; n; hi++) {
    map.merge(s.charAt(hi), 1, Integer::sum);
    while (map.get(s.charAt(hi)) > 1) {
        map.merge(s.charAt(lo), -1, Integer::sum);
        lo++;
    }
    maxLen = Math.max(maxLen, hi - lo + 1);
}</pre>
      </div></div>
      <div class="section-box"><div class="section-header"><span class="num">C</span> PREFIX SUM + HASHMAP</div><div class="section-content">
        <pre>// Subarray Sum Equals K (#560) — O(n)
int sum = 0, count = 0;
Map&lt;Integer,Integer&gt; pCount = new HashMap&lt;&gt;();
pCount.put(0, 1);
for (int num : nums) {
    sum += num;
    count += pCount.getOrDefault(sum - k, 0);
    pCount.merge(sum, 1, Integer::sum);
}</pre>
      </div></div>
    </div>
    <div>
      <div class="section-box"><div class="section-header"><span class="num">D</span> HASHMAP PATTERNS</div><div class="section-content">
        <pre>// Two Sum — O(n)
Map&lt;Integer,Integer&gt; seen = new HashMap&lt;&gt;();
for (int i = 0; i &lt; n; i++) {
    if (seen.containsKey(target - nums[i]))
        return new int[]{seen.get(target-nums[i]), i};
    seen.put(nums[i], i);
}</pre>
        <pre>// Frequency count (concise)
Map&lt;T,Integer&gt; freq = new HashMap&lt;&gt;();
freq.merge(key, 1, Integer::sum);</pre>
        <pre>// Group anagrams key
char[] chars = s.toCharArray();
Arrays.sort(chars);
String key = new String(chars);</pre>
      </div></div>
      <div class="section-box"><div class="section-header"><span class="num">E</span> TOP LEETCODE PROBLEMS</div><div class="section-content">
        <table><tr><th>#</th><th>Problem</th><th>Pattern</th><th>Level</th></tr>
        <tr><td>1</td><td>Two Sum</td><td>HashMap</td><td><span style="color:#15803d;font-weight:700;">Easy</span></td></tr>
        <tr><td>49</td><td>Group Anagrams</td><td>Sort key</td><td><span style="color:#b45309;font-weight:700;">Med</span></td></tr>
        <tr><td>128</td><td>Longest Consecutive</td><td>HashSet</td><td><span style="color:#b45309;font-weight:700;">Med</span></td></tr>
        <tr><td>560</td><td>Subarray Sum = K</td><td>Prefix+Map</td><td><span style="color:#b45309;font-weight:700;">Med</span></td></tr>
        <tr><td>3</td><td>Longest No-Repeat</td><td>Sliding window</td><td><span style="color:#b45309;font-weight:700;">Med</span></td></tr>
        <tr><td>76</td><td>Min Window Substring</td><td>Sliding window</td><td><span style="color:#b91c1c;font-weight:700;">Hard</span></td></tr>
        <tr><td>15</td><td>3Sum</td><td>Sort+Two pointer</td><td><span style="color:#b45309;font-weight:700;">Med</span></td></tr>
        <tr><td>42</td><td>Trapping Rain Water</td><td>Two pointer</td><td><span style="color:#b91c1c;font-weight:700;">Hard</span></td></tr></table>
      </div></div>
    </div>
  </div>
</div>
""",

    "8.Trees_Final.html": """
<div class="page">
  <div class="header-top"><div><h1>TREES &mdash; FAANG Quick Reference</h1><div class="subtitle">&#x2B50; DFS/BFS Templates &amp; BST Patterns</div></div><div class="page-number">APPENDIX</div></div>
  <div class="grid-container">
    <div>
      <div class="section-box"><div class="section-header"><span class="num">A</span> ITERATIVE INORDER (BST sorted order)</div><div class="section-content">
        <pre>List&lt;Integer&gt; inorder(TreeNode root) {
    List&lt;Integer&gt; res = new ArrayList&lt;&gt;();
    Deque&lt;TreeNode&gt; stack = new ArrayDeque&lt;&gt;();
    TreeNode curr = root;
    while (curr != null || !stack.isEmpty()) {
        while (curr != null) { stack.push(curr); curr = curr.left; }
        curr = stack.pop();
        res.add(curr.val);
        curr = curr.right;
    }
    return res;
}</pre>
      </div></div>
      <div class="section-box"><div class="section-header"><span class="num">B</span> LEVEL ORDER BFS</div><div class="section-content">
        <pre>List&lt;List&lt;Integer&gt;&gt; levelOrder(TreeNode root) {
    List&lt;List&lt;Integer&gt;&gt; res = new ArrayList&lt;&gt;();
    if (root == null) return res;
    Queue&lt;TreeNode&gt; q = new LinkedList&lt;&gt;();
    q.offer(root);
    while (!q.isEmpty()) {
        List&lt;Integer&gt; level = new ArrayList&lt;&gt;();
        int size = q.size(); // snapshot — critical!
        for (int i = 0; i &lt; size; i++) {
            TreeNode node = q.poll();
            level.add(node.val);
            if (node.left != null) q.offer(node.left);
            if (node.right != null) q.offer(node.right);
        }
        res.add(level);
    }
    return res;
}</pre>
      </div></div>
      <div class="section-box"><div class="section-header"><span class="num">C</span> UNIVERSAL DFS (Bottom-Up)</div><div class="section-content">
        <pre>// Used for: height, diameter, max path sum, etc.
int dfs(TreeNode node) {
    if (node == null) return 0;     // base case
    int left  = dfs(node.left);    // get from left
    int right = dfs(node.right);   // get from right
    // update global answer if needed
    ans = Math.max(ans, left + right + node.val);
    return Math.max(left, right) + 1; // return to parent
}</pre>
        <div class="callout-tip"><strong>Key:</strong> "What do I need from subtrees to compute my answer?"</div>
      </div></div>
    </div>
    <div>
      <div class="section-box"><div class="section-header"><span class="num">D</span> BST OPERATIONS</div><div class="section-content">
        <pre>// Validate BST — pass min/max bounds
boolean isValid(TreeNode n, long min, long max) {
    if (n == null) return true;
    if (n.val <= min || n.val >= max) return false;
    return isValid(n.left, min, n.val)
        && isValid(n.right, n.val, max);
}
// Call: isValid(root, Long.MIN_VALUE, Long.MAX_VALUE)</pre>
        <pre>// LCA of BST (use BST property — no extra space)
TreeNode lca(TreeNode root, TreeNode p, TreeNode q) {
    if (p.val < root.val && q.val < root.val) return lca(root.left, p, q);
    if (p.val > root.val && q.val > root.val) return lca(root.right, p, q);
    return root; // split point = LCA
}</pre>
      </div></div>
      <div class="section-box"><div class="section-header"><span class="num">E</span> TOP LEETCODE PROBLEMS</div><div class="section-content">
        <table><tr><th>#</th><th>Problem</th><th>Pattern</th><th>Level</th></tr>
        <tr><td>104</td><td>Max Depth</td><td>DFS</td><td><span style="color:#15803d;font-weight:700;">Easy</span></td></tr>
        <tr><td>102</td><td>Level Order</td><td>BFS</td><td><span style="color:#b45309;font-weight:700;">Med</span></td></tr>
        <tr><td>543</td><td>Diameter</td><td>DFS bottom-up</td><td><span style="color:#15803d;font-weight:700;">Easy</span></td></tr>
        <tr><td>124</td><td>Max Path Sum</td><td>DFS bottom-up</td><td><span style="color:#b91c1c;font-weight:700;">Hard</span></td></tr>
        <tr><td>235</td><td>LCA of BST</td><td>BST property</td><td><span style="color:#b45309;font-weight:700;">Med</span></td></tr>
        <tr><td>98</td><td>Validate BST</td><td>BST bounds</td><td><span style="color:#b45309;font-weight:700;">Med</span></td></tr>
        <tr><td>199</td><td>Right Side View</td><td>BFS level order</td><td><span style="color:#b45309;font-weight:700;">Med</span></td></tr>
        <tr><td>297</td><td>Serialize BT</td><td>DFS/BFS</td><td><span style="color:#b91c1c;font-weight:700;">Hard</span></td></tr></table>
      </div></div>
    </div>
  </div>
</div>
""",

    "9.Graphs_Final.html": """
<div class="page">
  <div class="header-top"><div><h1>GRAPHS &mdash; FAANG Quick Reference</h1><div class="subtitle">&#x2B50; Algorithm Templates &amp; Decision Table</div></div><div class="page-number">APPENDIX</div></div>
  <div class="grid-container">
    <div>
      <div class="section-box"><div class="section-header"><span class="num">A</span> BFS (Shortest path unweighted)</div><div class="section-content">
        <pre>int bfs(int src, int tgt, List&lt;List&lt;Integer&gt;&gt; adj) {
    boolean[] vis = new boolean[n];
    Queue&lt;Integer&gt; q = new LinkedList&lt;&gt;();
    q.offer(src); vis[src] = true;
    int dist = 0;
    while (!q.isEmpty()) {
        for (int sz = q.size(); sz > 0; sz--) {
            int node = q.poll();
            if (node == tgt) return dist;
            for (int nei : adj.get(node))
                if (!vis[nei]) { q.offer(nei); vis[nei]=true; }
        }
        dist++;
    }
    return -1;
}</pre>
      </div></div>
      <div class="section-box"><div class="section-header"><span class="num">B</span> UNION-FIND (DSU)</div><div class="section-content">
        <pre>int[] parent, rank;
void init(int n) {
    parent = new int[n]; rank = new int[n];
    for (int i=0;i&lt;n;i++) parent[i]=i;
}
int find(int x) {
    if (parent[x]!=x) parent[x]=find(parent[x]); // path compression
    return parent[x];
}
boolean union(int x, int y) {
    int px=find(x), py=find(y);
    if (px==py) return false;
    if (rank[px]&lt;rank[py]) { int t=px;px=py;py=t; }
    parent[py]=px;
    if (rank[px]==rank[py]) rank[px]++;
    return true;
}
// O(alpha(n)) ≈ O(1) amortized</pre>
      </div></div>
    </div>
    <div>
      <div class="section-box"><div class="section-header"><span class="num">C</span> DIJKSTRA (Weighted shortest path)</div><div class="section-content">
        <pre>int[] dijkstra(int src, List&lt;int[]&gt;[] adj, int n) {
    int[] dist = new int[n];
    Arrays.fill(dist, Integer.MAX_VALUE);
    dist[src] = 0;
    PriorityQueue&lt;int[]&gt; pq = new PriorityQueue&lt;&gt;((a,b)->a[0]-b[0]);
    pq.offer(new int[]{0, src});
    while (!pq.isEmpty()) {
        int[] cur = pq.poll();
        int d=cur[0], node=cur[1];
        if (d > dist[node]) continue; // stale
        for (int[] e : adj[node]) {
            if (dist[node]+e[1] &lt; dist[e[0]]) {
                dist[e[0]] = dist[node]+e[1];
                pq.offer(new int[]{dist[e[0]], e[0]});
            }
        }
    }
    return dist; // O((V+E)logV)
}</pre>
      </div></div>
      <div class="section-box"><div class="section-header"><span class="num">D</span> TOPOLOGICAL SORT (Kahn's BFS)</div><div class="section-content">
        <pre>List&lt;Integer&gt; topo(int n, int[][] edges) {
    List&lt;List&lt;Integer&gt;&gt; adj = new ArrayList&lt;&gt;();
    int[] inDeg = new int[n];
    for (int i=0;i&lt;n;i++) adj.add(new ArrayList&lt;&gt;());
    for (int[] e : edges) { adj.get(e[0]).add(e[1]); inDeg[e[1]]++; }
    Queue&lt;Integer&gt; q = new LinkedList&lt;&gt;();
    for (int i=0;i&lt;n;i++) if (inDeg[i]==0) q.offer(i);
    List&lt;Integer&gt; order = new ArrayList&lt;&gt;();
    while (!q.isEmpty()) {
        int node = q.poll(); order.add(node);
        for (int nei : adj.get(node))
            if (--inDeg[nei]==0) q.offer(nei);
    }
    return order.size()==n ? order : new ArrayList&lt;&gt;(); // empty=cycle
}</pre>
      </div></div>
      <div class="section-box"><div class="section-header"><span class="num">E</span> ALGORITHM DECISION TABLE</div><div class="section-content">
        <table><tr><th>Problem Type</th><th>Algorithm</th><th>Time</th></tr>
        <tr><td>Shortest path (unweighted)</td><td>BFS</td><td>O(V+E)</td></tr>
        <tr><td>Shortest path (weighted, +ve)</td><td>Dijkstra</td><td>O((V+E)logV)</td></tr>
        <tr><td>Shortest path (neg weights)</td><td>Bellman-Ford</td><td>O(VE)</td></tr>
        <tr><td>All pairs shortest path</td><td>Floyd-Warshall</td><td>O(V³)</td></tr>
        <tr><td>Cycle detection (directed)</td><td>DFS (colors)</td><td>O(V+E)</td></tr>
        <tr><td>Connected components</td><td>Union-Find / BFS</td><td>O(V+E)</td></tr>
        <tr><td>Topological order</td><td>Kahn's / DFS</td><td>O(V+E)</td></tr>
        <tr><td>Min spanning tree</td><td>Prim's / Kruskal</td><td>O(E logV)</td></tr></table>
      </div></div>
    </div>
  </div>
</div>
"""
}

# =====================================================
# Fix bad inline colors from subagents
# =====================================================
def fix_inline_colors(html):
    # Dark code backgrounds → cream
    dark_bgs = ['#1e1e2e','#0f172a','#282c34','#1a1a2e','#111827',
                '#0d0d0d','#1f2937','#2d2d2d','#333333','#272822','#1e293b']
    for bg in dark_bgs:
        html = html.replace(f'background:{bg}', 'background:#f8f8f2')
        html = html.replace(f'background: {bg}', 'background: #f8f8f2')
        html = html.replace(f'background-color:{bg}', 'background-color:#f8f8f2')
        html = html.replace(f'background-color: {bg}', 'background-color: #f8f8f2')
    
    # Green text (for dark bg) → dark text
    green_txts = ['#4ade80','#22c55e','#86efac','#a3e635','#39ff14','#00ff00']
    for g in green_txts:
        html = html.replace(f'color:{g}', 'color:#111827')
        html = html.replace(f'color: {g}', 'color: #111827')
    
    # Light gray text → readable
    html = html.replace('color: #94a3b8','color: #4b5563')
    html = html.replace('color:#94a3b8','color:#4b5563')
    html = html.replace('color: #cbd5e1','color: #374151')
    html = html.replace('color:#cbd5e1','color:#374151')
    
    # Yellow text → amber (visible)
    html = html.replace('color: yellow','color: #92400e')
    html = html.replace('color:yellow','color:#92400e')
    
    return html

# =====================================================
# Main rebuild
# =====================================================
finals = [f for f in os.listdir(src_dir) if f.endswith('_Final.html')]
print(f"Rebuilding {len(finals)} v0 files from originals...")

for fname in sorted(finals):
    src_path = os.path.join(src_dir, fname)
    dst_path = os.path.join(v0_dir, fname)
    
    with open(src_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Fix inline colors first
    html = fix_inline_colors(html)
    
    # Inject new CSS into head
    if '</head>' in html:
        html = html.replace('</head>', NEW_MASTER_CSS + '\n</head>', 1)
    else:
        # Prepend CSS before first <body> tag
        html = html.replace('<body>', NEW_MASTER_CSS + '\n<body>', 1)
    
    # Inject FAANG appendix before </body>
    appendix = APPENDICES.get(fname, '')
    if appendix and '</body>' in html:
        html = html.replace('</body>', appendix + '\n</body>', 1)
    
    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    size_kb = os.path.getsize(dst_path) / 1024
    has_new_css = '#1c1c2e' in html  # charcoal primary
    has_appendix = 'FAANG Quick Reference' in html
    print(f"  OK [{size_kb:.1f} KB] {fname} | NewCSS={has_new_css} | Appendix={has_appendix}")

print("\nRebuild complete!")

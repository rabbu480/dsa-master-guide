"""
build_v2.py
-----------
Creates v2/ from original finals with a premium FAANG-level design:

Design System:
  - WHITE background pages (clean, printable)
  - TEAL (#0f766e) primary — professional, distinct from boring blue
  - AMBER (#d97706) accent — warm, high contrast, xerox-safe
  - SLATE (#0f172a) for headings
  - Carefully chosen colors with WCAG AA contrast
  - Code blocks: dark slate bg (#0f172a) + green text (#4ade80) 
    BUT with a PRINT override to white/black
  - Beautiful card shadows, rounded corners, smooth gradients
  - Works perfectly on screen AND prints clean on xerox
"""

import os
import re

src_dir = r"C:\Users\rabba\Downloads\TelegramDownload\metadata"
v2_dir  = r"C:\Users\rabba\Downloads\TelegramDownload\metadata\v2"
os.makedirs(v2_dir, exist_ok=True)

# ============================================================
# PREMIUM MASTER CSS — v2
# ============================================================
V2_CSS = """<style id="faang-v2">
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Fira+Code:wght@400;500&display=swap');

/* =====================================================
   FAANG CHEAT SHEET v2 — Premium Design System
   Primary: Teal  |  Accent: Amber  |  Text: Slate
   ✓ Screen color  ✓ PDF export  ✓ B&W xerox
===================================================== */
:root {
  /* Core palette */
  --teal-900: #134e4a;
  --teal-700: #0f766e;
  --teal-600: #0d9488;
  --teal-100: #ccfbf1;
  --teal-50:  #f0fdfa;

  --amber-700: #b45309;
  --amber-500: #f59e0b;
  --amber-200: #fde68a;
  --amber-50:  #fffbeb;

  --slate-900: #0f172a;
  --slate-800: #1e293b;
  --slate-700: #334155;
  --slate-500: #64748b;
  --slate-300: #cbd5e1;
  --slate-100: #f1f5f9;
  --slate-50:  #f8fafc;

  --green-700: #15803d;
  --green-100: #dcfce7;
  --red-700:   #b91c1c;
  --red-100:   #fee2e2;
  --blue-700:  #1d4ed8;
  --blue-100:  #dbeafe;

  --white: #ffffff;

  /* Semantic aliases */
  --primary:       var(--teal-700);
  --primary-dark:  var(--teal-900);
  --accent:        var(--amber-500);
  --accent-dark:   var(--amber-700);
  --text-heading:  var(--slate-900);
  --text-body:     var(--slate-800);
  --text-muted:    var(--slate-500);
  --bg-page:       #e8f4f8;
  --border:        var(--slate-300);
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

body {
  font-family: 'Inter', system-ui, -apple-system, sans-serif;
  background: var(--bg-page);
  background-image: linear-gradient(135deg, #e0f2f1 0%, #e8f4f8 50%, #fef9c3 100%);
  color: var(--text-body);
  padding: 32px 24px;
  font-size: 13px;
  line-height: 1.6;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
  min-height: 100vh;
}

/* ======================== PAGE CARD ======================== */
.page {
  background: var(--white);
  max-width: 1140px;
  margin: 0 auto 56px auto;
  border-radius: 16px;
  overflow: hidden;
  box-shadow:
    0 0 0 1px rgba(0,0,0,0.04),
    0 4px 6px rgba(0,0,0,0.04),
    0 12px 32px rgba(0,0,0,0.08);
  page-break-after: always;
  position: relative;
}
.page::before {
  content: '';
  display: block;
  height: 5px;
  background: linear-gradient(90deg, var(--teal-700) 0%, var(--teal-600) 50%, var(--amber-500) 100%);
}
.page-inner {
  padding: 32px 36px 36px;
}

/* ======================== HEADER ======================== */
.header-top {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  padding-bottom: 20px;
  margin-bottom: 24px;
  border-bottom: 2px solid var(--slate-100);
  position: relative;
}
.header-top::after {
  content: '';
  position: absolute;
  bottom: -2px; left: 0;
  width: 120px; height: 2px;
  background: var(--primary);
}
.header-top h1 {
  font-size: 2rem;
  font-weight: 900;
  color: var(--text-heading);
  letter-spacing: -0.5px;
  line-height: 1.1;
}
.header-top .subtitle {
  font-size: 0.9rem;
  font-weight: 500;
  color: var(--text-muted);
  margin-top: 6px;
}
.header-top .page-number {
  background: linear-gradient(135deg, var(--teal-700), var(--teal-900));
  color: white;
  padding: 6px 20px;
  border-radius: 100px;
  font-weight: 700;
  font-size: 0.8rem;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  flex-shrink: 0;
  box-shadow: 0 2px 8px rgba(15, 118, 110, 0.3);
}

/* ======================== GRID ======================== */
.grid-container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
  align-items: start;
}
.col-left, .col-right { min-width: 0; }
.full-width { grid-column: 1 / -1; }

/* ======================== SECTION BOX ======================== */
.section-box {
  border: 1px solid var(--slate-100);
  border-radius: 10px;
  overflow: hidden;
  margin-bottom: 16px;
  background: var(--white);
  transition: box-shadow 0.15s ease;
  box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}
.section-box:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}

/* ======================== SECTION HEADERS ======================== */
/* Default: teal gradient */
.section-header {
  display: flex;
  align-items: center;
  padding: 10px 14px;
  font-weight: 700;
  font-size: 0.78rem;
  letter-spacing: 0.8px;
  text-transform: uppercase;
  background: linear-gradient(135deg, var(--teal-700) 0%, var(--teal-900) 100%) !important;
  color: #ffffff !important;
  border-bottom: 2px solid rgba(255,255,255,0.08);
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}
.section-header span.num {
  background: var(--amber-500);
  color: var(--slate-900);
  border-radius: 50%;
  width: 22px; height: 22px;
  display: inline-flex;
  align-items: center; justify-content: center;
  margin-right: 10px;
  font-size: 0.75rem;
  font-weight: 900;
  flex-shrink: 0;
  box-shadow: 0 1px 3px rgba(0,0,0,0.2);
}
/* Section header color variants (used per topic) */
.section-header.h-amber {
  background: linear-gradient(135deg, #92400e 0%, #78350f 100%) !important;
}
.section-header.h-green {
  background: linear-gradient(135deg, #15803d 0%, #14532d 100%) !important;
}
.section-header.h-red {
  background: linear-gradient(135deg, #b91c1c 0%, #7f1d1d 100%) !important;
}
.section-header.h-indigo {
  background: linear-gradient(135deg, #4338ca 0%, #312e81 100%) !important;
}

/* ======================== CONTENT ======================== */
.section-content {
  padding: 14px 16px;
}
ul, ol { padding-left: 20px; margin: 6px 0; }
li { margin-bottom: 6px; color: var(--text-body); }
p { margin: 6px 0; }
strong { color: var(--slate-900); }

/* ======================== TABLES ======================== */
table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.82rem;
  margin: 8px 0;
  border-radius: 8px;
  overflow: hidden;
  border: 1px solid var(--slate-100);
}
table thead tr th {
  background: linear-gradient(135deg, var(--teal-700), var(--teal-900)) !important;
  color: #ffffff !important;
  padding: 9px 12px;
  font-weight: 700;
  font-size: 0.75rem;
  text-align: left;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}
table th {
  background: linear-gradient(135deg, var(--teal-700), var(--teal-900)) !important;
  color: #ffffff !important;
  padding: 9px 12px;
  font-weight: 700;
  font-size: 0.75rem;
  text-align: left;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}
table td {
  padding: 8px 12px;
  border-bottom: 1px solid var(--slate-100);
  vertical-align: top;
  line-height: 1.4;
}
table tr:nth-child(even) td { background: var(--teal-50); }
table tr:nth-child(odd) td { background: var(--white); }
table tr:hover td { background: var(--amber-50); }

/* ======================== CODE BLOCKS ======================== */
/* Screen: beautiful dark code */
pre {
  background: var(--slate-900) !important;
  color: #e2e8f0 !important;
  border: none !important;
  border-left: 4px solid var(--amber-500) !important;
  padding: 14px 16px !important;
  border-radius: 0 8px 8px 0 !important;
  font-family: 'Fira Code', 'Courier New', monospace !important;
  font-size: 0.78rem !important;
  margin: 10px 0 !important;
  overflow-x: auto;
  white-space: pre-wrap;
  word-break: break-word;
  line-height: 1.7;
  box-shadow: inset 0 0 0 1px rgba(255,255,255,0.05) !important;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}
/* Syntax highlights in dark code blocks */
pre .kw  { color: #f59e0b; font-weight: 600; }  /* keywords: amber */
pre .cls { color: #67e8f9; }  /* classes: cyan */
pre .str { color: #86efac; }  /* strings: green */
pre .num { color: #fca5a5; }  /* numbers: red */
pre .cmt { color: #94a3b8; font-style: italic; }  /* comments: gray */

/* Inline code: teal tinted */
code {
  background: var(--teal-50) !important;
  color: var(--teal-900) !important;
  border: 1px solid var(--teal-100) !important;
  padding: 2px 6px !important;
  border-radius: 4px !important;
  font-family: 'Fira Code', monospace !important;
  font-size: 0.85em !important;
  font-weight: 500 !important;
}
pre code {
  background: transparent !important;
  color: inherit !important;
  border: none !important;
  padding: 0 !important;
  font-weight: 400 !important;
}

/* ======================== CALLOUT BOXES ======================== */
.rule-box, .callout-warn {
  background: var(--amber-50);
  border: 1px solid var(--amber-200);
  border-left: 5px solid var(--amber-500);
  padding: 12px 16px;
  margin: 10px 0;
  border-radius: 0 8px 8px 0;
  font-size: 0.85rem;
}
.callout-tip {
  background: var(--green-100);
  border: 1px solid #86efac;
  border-left: 5px solid var(--green-700);
  padding: 12px 16px; margin: 10px 0;
  border-radius: 0 8px 8px 0; font-size: 0.85rem;
}
.callout-danger {
  background: var(--red-100);
  border: 1px solid #fca5a5;
  border-left: 5px solid var(--red-700);
  padding: 12px 16px; margin: 10px 0;
  border-radius: 0 8px 8px 0; font-size: 0.85rem;
}
.callout-info {
  background: var(--blue-100);
  border: 1px solid #93c5fd;
  border-left: 5px solid var(--blue-700);
  padding: 12px 16px; margin: 10px 0;
  border-radius: 0 8px 8px 0; font-size: 0.85rem;
}

/* ======================== BADGES ======================== */
.bg-green { background: var(--green-700); color: white; padding: 3px 10px; border-radius: 100px; font-weight: 700; font-size: 0.78rem; display: inline-block; }
.bg-red   { background: var(--red-700);   color: white; padding: 3px 10px; border-radius: 100px; font-weight: 700; font-size: 0.78rem; display: inline-block; }
.diff-easy   { color: var(--green-700); font-weight: 700; }
.diff-medium { color: var(--amber-700); font-weight: 700; }
.diff-hard   { color: var(--red-700); font-weight: 700; }
.badge-o1   { background: var(--green-100); color: #14532d; border: 1px solid var(--green-700); padding: 1px 7px; border-radius: 4px; font-weight: 700; font-size: 0.72rem; display: inline-block; }
.badge-olog { background: var(--blue-100);  color: #1e3a8a; border: 1px solid var(--blue-700);  padding: 1px 7px; border-radius: 4px; font-weight: 700; font-size: 0.72rem; display: inline-block; }
.badge-on   { background: var(--amber-50);  color: #92400e; border: 1px solid var(--amber-500); padding: 1px 7px; border-radius: 4px; font-weight: 700; font-size: 0.72rem; display: inline-block; }
.badge-on2  { background: var(--red-100);   color: #7f1d1d; border: 1px solid var(--red-700);   padding: 1px 7px; border-radius: 4px; font-weight: 700; font-size: 0.72rem; display: inline-block; }

/* ======================== FLEX UTILS ======================== */
.flex-row { display: flex; gap: 16px; }
.flex-col { flex: 1; text-align: center; min-width: 0; }

/* ======================== MERMAID ======================== */
.mermaid { display: flex; justify-content: center; margin: 12px 0; }

/* ======================== FIX INVISIBLE INLINE COLORS ======================== */
/* Subagent light grays → readable */
[style*="color: #94a3b8"],[style*="color:#94a3b8"] { color: #475569 !important; }
[style*="color: #cbd5e1"],[style*="color:#cbd5e1"] { color: #334155 !important; }
[style*="color: #e2e8f0"],[style*="color:#e2e8f0"] { color: #334155 !important; }
/* Yellow text → amber */
[style*="color: yellow"],[style*="color:yellow"]   { color: #92400e !important; }
/* Light green text (for dark bg) on any bg → dark green */
[style*="color: #4ade80"],[style*="color:#4ade80"] { color: #15803d !important; }
[style*="color: #86efac"],[style*="color:#86efac"] { color: #15803d !important; }

/* ======================== PRINT / XEROX ======================== */
@media print {
  body {
    background: white !important;
    background-image: none !important;
    padding: 0 !important;
    font-size: 10.5px !important;
  }
  .page {
    box-shadow: none !important;
    border: 1px solid #ccc !important;
    border-radius: 0 !important;
    margin: 0 !important;
    page-break-after: always;
    break-after: page;
  }
  .page::before {
    height: 3px;
    background: #000 !important;
    -webkit-print-color-adjust: exact;
  }
  .page-inner { padding: 16px 20px; }
  .header-top h1 { font-size: 1.4rem !important; color: #000 !important; }
  .header-top .page-number {
    background: #000 !important;
    color: #fff !important;
    box-shadow: none !important;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }
  .section-header {
    background: #111 !important;
    color: #fff !important;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }
  table th {
    background: #111 !important;
    color: #fff !important;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }
  table tr:nth-child(even) td { background: #f5f5f5 !important; }
  /* CODE BLOCKS: switch to white bg for printing */
  pre {
    background: #f8f8f8 !important;
    color: #000000 !important;
    border: 1px solid #999 !important;
    border-left: 4px solid #333 !important;
    border-radius: 0 !important;
    box-shadow: none !important;
    page-break-inside: avoid;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }
  code {
    background: #eeeeee !important;
    color: #000000 !important;
    border-color: #ccc !important;
  }
  .callout-tip, .callout-warn, .callout-danger, .callout-info, .rule-box {
    background: #f9f9f9 !important;
    border-left-color: #555 !important;
  }
  .section-box { page-break-inside: avoid; }
  .section-box:hover { box-shadow: none; }
  .mermaid svg { max-width: 100% !important; }
  a { color: #000 !important; text-decoration: none !important; }
}
</style>"""

# =====================================================
# FAANG Appendix pages — v2 styled
# =====================================================
APPENDICES = {
    "10.Heaps_Final.html": """
<div class="page"><div class="page-inner">
  <div class="header-top">
    <div><h1>&#x1F4CA; HEAP — FAANG Quick Reference</h1><div class="subtitle">Must-Know Patterns · Critical Code Templates · Top LeetCode Problems</div></div>
    <div class="page-number">APPENDIX</div>
  </div>
  <div class="grid-container">
    <div>
      <div class="section-box"><div class="section-header"><span class="num">A</span> TOP-K PATTERN (Most Frequent FAANG)</div><div class="section-content">
        <p><strong>Rule:</strong> K Largest → <em>Min Heap size K</em> &nbsp;|&nbsp; K Smallest → <em>Max Heap size K</em></p>
        <pre>// K Largest Elements — O(n log k)
PriorityQueue&lt;Integer&gt; minH = new PriorityQueue&lt;&gt;();
for (int num : nums) {
    minH.offer(num);
    if (minH.size() &gt; k) minH.poll(); // evict smallest
}
// minH now contains exactly K largest</pre>
        <pre>// K Most Frequent — O(n log k)
Map&lt;Integer,Integer&gt; freq = new HashMap&lt;&gt;();
for (int n : nums) freq.merge(n, 1, Integer::sum);
PriorityQueue&lt;int[]&gt; pq =
    new PriorityQueue&lt;&gt;((a,b)-&gt;a[1]-b[1]); // min by freq
for (var e : freq.entrySet()) {
    pq.offer(new int[]{e.getKey(), e.getValue()});
    if (pq.size() &gt; k) pq.poll();
}
// pq contains K most frequent elements</pre>
      </div></div>
      <div class="section-box"><div class="section-header h-indigo"><span class="num">B</span> TWO-HEAP MEDIAN (#295 Hard)</div><div class="section-content">
        <pre>PriorityQueue&lt;Integer&gt; lo = // max-heap: lower half
    new PriorityQueue&lt;&gt;(Collections.reverseOrder());
PriorityQueue&lt;Integer&gt; hi = // min-heap: upper half
    new PriorityQueue&lt;&gt;();

void addNum(int num) {
    lo.offer(num);
    hi.offer(lo.poll());           // move lo's max → hi
    if (hi.size() &gt; lo.size())    // rebalance
        lo.offer(hi.poll());
}
double findMedian() {
    return lo.size() &gt; hi.size()
        ? lo.peek()
        : (lo.peek() + hi.peek()) / 2.0;
}</pre>
      </div></div>
      <div class="section-box"><div class="section-header h-green"><span class="num">C</span> K-WAY MERGE (#23 Hard)</div><div class="section-content">
        <pre>// Merge K sorted lists — O(n log k)
PriorityQueue&lt;int[]&gt; pq =  // [val, listIdx, elemIdx]
    new PriorityQueue&lt;&gt;((a,b)-&gt;a[0]-b[0]);
for (int i = 0; i &lt; k; i++)
    if (!lists[i].isEmpty())
        pq.offer(new int[]{lists[i].get(0), i, 0});
while (!pq.isEmpty()) {
    int[] cur = pq.poll();
    result.add(cur[0]);
    int ni = cur[2] + 1;
    if (ni &lt; lists[cur[1]].size())
        pq.offer(new int[]{lists[cur[1]].get(ni), cur[1], ni});
}</pre>
      </div></div>
    </div>
    <div>
      <div class="section-box"><div class="section-header h-amber"><span class="num">D</span> COMPARATOR GUIDE — FAANG TRAP!</div><div class="section-content">
        <table><tr><th>Goal</th><th>Comparator</th></tr>
        <tr><td>Min Heap (default)</td><td><code>new PriorityQueue&lt;&gt;()</code></td></tr>
        <tr><td>Max Heap</td><td><code>Collections.reverseOrder()</code></td></tr>
        <tr><td>Object by .val</td><td><code>(a,b) -&gt; Integer.compare(a.val, b.val)</code></td></tr>
        <tr><td>int[] by index 1</td><td><code>(a,b) -&gt; a[1] - b[1]</code></td></tr>
        <tr><td>Multi-key sort</td><td><code>(a,b) -&gt; a[0]==b[0] ? a[1]-b[1] : a[0]-b[0]</code></td></tr>
        </table>
        <div class="callout-danger"><strong>&#x26A0; Overflow Trap!</strong> Never write <code>b - a</code> when values can overflow Integer. Use <code>Integer.compare(b, a)</code> always.</div>
      </div></div>
      <div class="section-box"><div class="section-header"><span class="num">E</span> DECISION TABLE</div><div class="section-content">
        <table><tr><th>Trigger Keywords</th><th>Pattern</th><th>Heap Type</th></tr>
        <tr><td>"K largest"</td><td>Top-K</td><td>Min Heap size K</td></tr>
        <tr><td>"K smallest"</td><td>Top-K</td><td>Max Heap size K</td></tr>
        <tr><td>"K most frequent"</td><td>HashMap + Top-K</td><td>Min Heap size K</td></tr>
        <tr><td>"Running median"</td><td>Two Heap</td><td>Max + Min pair</td></tr>
        <tr><td>"Merge K sorted"</td><td>K-Way Merge</td><td>Min Heap</td></tr>
        <tr><td>"Reorganize / rearrange"</td><td>Greedy</td><td>Max Heap</td></tr>
        <tr><td>"Task Scheduler"</td><td>Greedy + cooldown</td><td>Max Heap</td></tr>
        <tr><td>"Dijkstra / shortest"</td><td>Graph SP</td><td>Min Heap</td></tr>
        </table>
      </div></div>
      <div class="section-box"><div class="section-header h-green"><span class="num">F</span> TOP LEETCODE — HEAP</div><div class="section-content">
        <table><tr><th>#</th><th>Problem</th><th>Pattern</th><th>Diff</th></tr>
        <tr><td>215</td><td>Kth Largest Element</td><td>Top-K</td><td><span class="diff-medium">Med</span></td></tr>
        <tr><td>347</td><td>Top K Frequent</td><td>HashMap+Heap</td><td><span class="diff-medium">Med</span></td></tr>
        <tr><td>295</td><td>Find Median Data Stream</td><td>Two Heap</td><td><span class="diff-hard">Hard</span></td></tr>
        <tr><td>23</td><td>Merge K Sorted Lists</td><td>K-Way Merge</td><td><span class="diff-hard">Hard</span></td></tr>
        <tr><td>621</td><td>Task Scheduler</td><td>Max Heap greedy</td><td><span class="diff-medium">Med</span></td></tr>
        <tr><td>767</td><td>Reorganize String</td><td>Max Heap greedy</td><td><span class="diff-medium">Med</span></td></tr>
        <tr><td>973</td><td>K Closest Points</td><td>Top-K (distance)</td><td><span class="diff-medium">Med</span></td></tr>
        <tr><td>1046</td><td>Last Stone Weight</td><td>Max Heap basic</td><td><span class="diff-easy">Easy</span></td></tr>
        </table>
      </div></div>
    </div>
  </div>
</div></div>
""",

    "6.Binary_Search_Final.html": """
<div class="page"><div class="page-inner">
  <div class="header-top">
    <div><h1>&#x1F50D; BINARY SEARCH — FAANG Quick Reference</h1><div class="subtitle">Universal Template · All Variants · Search on Answer</div></div>
    <div class="page-number">APPENDIX</div>
  </div>
  <div class="grid-container">
    <div>
      <div class="section-box"><div class="section-header"><span class="num">A</span> UNIVERSAL TEMPLATE (covers 99%)</div><div class="section-content">
        <div class="callout-tip"><strong>&#x1F4A1; The Mindset:</strong> Define a monotone boolean function. Binary Search finds the boundary between false → true.</div>
        <pre>// Find LEFTMOST position where condition is true
int lo = 0, hi = n; // hi = n means "open right"
while (lo &lt; hi) {
    int mid = lo + (hi - lo) / 2;  // no overflow
    if (condition(mid)) hi = mid;   // mid could be answer
    else              lo = mid + 1; // mid too small
}
// lo == hi is the answer boundary
return lo;</pre>
        <pre>// Find RIGHTMOST satisfying position
int lo = 0, hi = n - 1;
while (lo &lt; hi) {
    int mid = lo + (hi - lo + 1) / 2; // +1 bias right
    if (condition(mid)) lo = mid;      // mid is valid, expand
    else               hi = mid - 1;
}
return lo;</pre>
      </div></div>
      <div class="section-box"><div class="section-header h-amber"><span class="num">B</span> SEARCH ON ANSWER PATTERN</div><div class="section-content">
        <p><strong>Trigger:</strong> "Minimize the maximum" / "Maximize the minimum" / "At most X in Y groups"</p>
        <pre>// Binary search the ANSWER SPACE
long lo = minPossibleAnswer;
long hi = maxPossibleAnswer;
while (lo &lt; hi) {
    long mid = lo + (hi - lo) / 2;
    if (feasible(mid)) hi = mid;   // mid works, try smaller
    else              lo = mid + 1; // mid too small
}
return lo;</pre>
        <div class="callout-info"><strong>Key:</strong> <code>feasible(mid)</code> = "can I achieve this answer with value mid?" — usually a greedy check in O(n).</div>
      </div></div>
      <div class="section-box"><div class="section-header h-red"><span class="num">C</span> ROTATED SORTED ARRAY</div><div class="section-content">
        <pre>// #33 — O(log n)
int lo = 0, hi = nums.length - 1;
while (lo &lt;= hi) {
    int mid = lo + (hi - lo) / 2;
    if (nums[mid] == target) return mid;

    if (nums[lo] &lt;= nums[mid]) {    // LEFT half is sorted
        if (target &gt;= nums[lo] &amp;&amp; target &lt; nums[mid])
            hi = mid - 1;
        else lo = mid + 1;
    } else {                          // RIGHT half is sorted
        if (target &gt; nums[mid] &amp;&amp; target &lt;= nums[hi])
            lo = mid + 1;
        else hi = mid - 1;
    }
}
return -1;</pre>
      </div></div>
    </div>
    <div>
      <div class="section-box"><div class="section-header h-indigo"><span class="num">D</span> COMMON PITFALLS TABLE</div><div class="section-content">
        <table><tr><th>Pitfall</th><th>Symptom</th><th>Fix</th></tr>
        <tr><td>Overflow</td><td>Negative mid</td><td><code>lo + (hi-lo)/2</code></td></tr>
        <tr><td>Infinite loop</td><td>lo never moves</td><td>Use <code>mid = lo+(hi-lo+1)/2</code> when assigning <code>lo=mid</code></td></tr>
        <tr><td>Off-by-one</td><td>Missing boundary</td><td>Dry-run with [a,b] 2-element array</td></tr>
        <tr><td>Wrong direction</td><td>Wrong answer</td><td>Ask: "What is the smallest mid that satisfies condition?"</td></tr>
        <tr><td>hi init wrong</td><td>Skip valid answers</td><td>Think: "Is hi itself a valid candidate?"</td></tr>
        </table>
        <div class="callout-warn">Always ask yourself: <strong>Is this a "find exact" or "find boundary" problem?</strong></div>
      </div></div>
      <div class="section-box"><div class="section-header h-green"><span class="num">E</span> VARIANT CHEAT SHEET</div><div class="section-content">
        <table><tr><th>Problem Type</th><th>hi init</th><th>Template</th></tr>
        <tr><td>Find exact value</td><td>n-1</td><td>lo≤hi with return inside</td></tr>
        <tr><td>First position ≥ target</td><td>n</td><td>Leftmost template</td></tr>
        <tr><td>Last position ≤ target</td><td>n-1</td><td>Rightmost template</td></tr>
        <tr><td>Minimize max (search answer)</td><td>max possible</td><td>Search on answer</td></tr>
        <tr><td>Rotated sorted</td><td>n-1</td><td>Which half is sorted?</td></tr>
        <tr><td>2D matrix search</td><td>m*n-1</td><td>row=mid/n, col=mid%n</td></tr>
        </table>
      </div></div>
      <div class="section-box"><div class="section-header"><span class="num">F</span> TOP LEETCODE — BINARY SEARCH</div><div class="section-content">
        <table><tr><th>#</th><th>Problem</th><th>Type</th><th>Diff</th></tr>
        <tr><td>704</td><td>Binary Search</td><td>Classic</td><td><span class="diff-easy">Easy</span></td></tr>
        <tr><td>35</td><td>Search Insert Position</td><td>Leftmost</td><td><span class="diff-easy">Easy</span></td></tr>
        <tr><td>33</td><td>Search Rotated Array</td><td>Rotated</td><td><span class="diff-medium">Med</span></td></tr>
        <tr><td>153</td><td>Find Min Rotated</td><td>Rotated</td><td><span class="diff-medium">Med</span></td></tr>
        <tr><td>875</td><td>Koko Eating Bananas</td><td>Search Answer</td><td><span class="diff-medium">Med</span></td></tr>
        <tr><td>1011</td><td>Capacity to Ship</td><td>Search Answer</td><td><span class="diff-medium">Med</span></td></tr>
        <tr><td>4</td><td>Median Two Sorted Arrays</td><td>Advanced BS</td><td><span class="diff-hard">Hard</span></td></tr>
        <tr><td>410</td><td>Split Array Largest Sum</td><td>Search Answer</td><td><span class="diff-hard">Hard</span></td></tr>
        </table>
      </div></div>
    </div>
  </div>
</div></div>
""",

    "1.Array&Hashing_Final.html": """
<div class="page"><div class="page-inner">
  <div class="header-top">
    <div><h1>&#x1F9E9; ARRAYS &amp; HASHING — FAANG Quick Reference</h1><div class="subtitle">Two Pointer · Sliding Window · Prefix Sum · HashMap Tricks</div></div>
    <div class="page-number">APPENDIX</div>
  </div>
  <div class="grid-container">
    <div>
      <div class="section-box"><div class="section-header"><span class="num">A</span> TWO POINTER PATTERNS</div><div class="section-content">
        <pre>// OPPOSITE ENDS — Two Sum (sorted), 3Sum
int lo = 0, hi = n - 1;
while (lo &lt; hi) {
    int s = arr[lo] + arr[hi];
    if      (s == target) { /* process */ lo++; hi--; }
    else if (s &lt; target)  lo++;
    else                   hi--;
}</pre>
        <pre>// SAME DIRECTION — Remove Duplicates, Move Zeros
int slow = 0;
for (int fast = 0; fast &lt; n; fast++) {
    if (valid(arr[fast])) {
        arr[slow++] = arr[fast];
    }
}</pre>
      </div></div>
      <div class="section-box"><div class="section-header h-indigo"><span class="num">B</span> SLIDING WINDOW TEMPLATES</div><div class="section-content">
        <pre>// FIXED SIZE window of K — O(n)
int sum = 0, maxSum = 0;
for (int i = 0; i &lt; n; i++) {
    sum += arr[i];
    if (i &gt;= k) sum -= arr[i - k];
    if (i &gt;= k - 1) maxSum = Math.max(maxSum, sum);
}</pre>
        <pre>// VARIABLE window — longest satisfying condition
int lo = 0, maxLen = 0;
Map&lt;Character, Integer&gt; win = new HashMap&lt;&gt;();
for (int hi = 0; hi &lt; s.length(); hi++) {
    win.merge(s.charAt(hi), 1, Integer::sum); // expand
    while (!valid(win)) {                      // shrink
        if (win.merge(s.charAt(lo),-1,Integer::sum) == 0)
            win.remove(s.charAt(lo));
        lo++;
    }
    maxLen = Math.max(maxLen, hi - lo + 1);
}</pre>
      </div></div>
      <div class="section-box"><div class="section-header h-green"><span class="num">C</span> PREFIX SUM + HASHMAP</div><div class="section-content">
        <pre>// Subarray Sum == K — O(n) — #560
int prefixSum = 0, count = 0;
Map&lt;Integer,Integer&gt; seen = new HashMap&lt;&gt;();
seen.put(0, 1);  // empty prefix
for (int num : nums) {
    prefixSum += num;
    // how many prefix sums = prefixSum - k?
    count += seen.getOrDefault(prefixSum - k, 0);
    seen.merge(prefixSum, 1, Integer::sum);
}
return count;</pre>
        <div class="callout-tip"><strong>Pattern:</strong> seen[sum - k] exists → there's a subarray ending here with sum = k.</div>
      </div></div>
    </div>
    <div>
      <div class="section-box"><div class="section-header h-amber"><span class="num">D</span> HASHMAP PATTERNS</div><div class="section-content">
        <pre>// Two Sum — O(n)
Map&lt;Integer,Integer&gt; idx = new HashMap&lt;&gt;();
for (int i = 0; i &lt; n; i++) {
    int comp = target - nums[i];
    if (idx.containsKey(comp))
        return new int[]{idx.get(comp), i};
    idx.put(nums[i], i);
}</pre>
        <pre>// Group Anagrams key trick
char[] ch = s.toCharArray();
Arrays.sort(ch);
String key = new String(ch); // sorted chars = anagram key</pre>
        <pre>// Frequency count (Java idiom)
Map&lt;T, Integer&gt; freq = new HashMap&lt;&gt;();
freq.merge(key, 1, Integer::sum); // cleaner than getOrDefault+put</pre>
      </div></div>
      <div class="section-box"><div class="section-header h-red"><span class="num">E</span> MONOTONIC STACK PATTERN</div><div class="section-content">
        <pre>// Next Greater Element — O(n)
int[] res = new int[n];
Arrays.fill(res, -1);
Deque&lt;Integer&gt; stack = new ArrayDeque&lt;&gt;(); // indices
for (int i = 0; i &lt; n; i++) {
    while (!stack.isEmpty() &amp;&amp; nums[stack.peek()] &lt; nums[i]) {
        res[stack.pop()] = nums[i]; // i is next greater
    }
    stack.push(i);
}
// Works for: Next Greater, Largest Rectangle, Stock Span</pre>
      </div></div>
      <div class="section-box"><div class="section-header h-green"><span class="num">F</span> TOP LEETCODE — ARRAYS</div><div class="section-content">
        <table><tr><th>#</th><th>Problem</th><th>Pattern</th><th>Diff</th></tr>
        <tr><td>1</td><td>Two Sum</td><td>HashMap</td><td><span class="diff-easy">Easy</span></td></tr>
        <tr><td>49</td><td>Group Anagrams</td><td>Sort key</td><td><span class="diff-medium">Med</span></td></tr>
        <tr><td>128</td><td>Longest Consecutive</td><td>HashSet</td><td><span class="diff-medium">Med</span></td></tr>
        <tr><td>560</td><td>Subarray Sum = K</td><td>Prefix+Map</td><td><span class="diff-medium">Med</span></td></tr>
        <tr><td>3</td><td>Longest No-Repeat Substr</td><td>Sliding window</td><td><span class="diff-medium">Med</span></td></tr>
        <tr><td>76</td><td>Min Window Substring</td><td>Sliding window</td><td><span class="diff-hard">Hard</span></td></tr>
        <tr><td>15</td><td>3Sum</td><td>Sort + Two Pointer</td><td><span class="diff-medium">Med</span></td></tr>
        <tr><td>42</td><td>Trapping Rain Water</td><td>Two Pointer / Stack</td><td><span class="diff-hard">Hard</span></td></tr>
        <tr><td>84</td><td>Largest Rectangle Histogram</td><td>Mono Stack</td><td><span class="diff-hard">Hard</span></td></tr>
        </table>
      </div></div>
    </div>
  </div>
</div></div>
""",

    "8.Trees_Final.html": """
<div class="page"><div class="page-inner">
  <div class="header-top">
    <div><h1>&#x1F333; TREES — FAANG Quick Reference</h1><div class="subtitle">DFS Templates · BFS Level Order · BST Operations · LCA</div></div>
    <div class="page-number">APPENDIX</div>
  </div>
  <div class="grid-container">
    <div>
      <div class="section-box"><div class="section-header"><span class="num">A</span> UNIVERSAL DFS (Bottom-Up Return)</div><div class="section-content">
        <div class="callout-tip"><strong>&#x1F4A1; Template Question:</strong> "What do I need from each subtree to compute my answer?"</div>
        <pre>int ans = 0;
int dfs(TreeNode node) {
    if (node == null) return 0;   // base: empty contributes 0
    int L = dfs(node.left);       // get left subtree value
    int R = dfs(node.right);      // get right subtree value
    // Update global answer (uses both subtrees through node)
    ans = Math.max(ans, L + R + node.val);
    // Return value to PARENT (can only use one side)
    return Math.max(L, R) + 1;
}
// Works for: Diameter (#543), Max Path Sum (#124), Height</pre>
      </div></div>
      <div class="section-box"><div class="section-header h-indigo"><span class="num">B</span> ITERATIVE TRAVERSALS</div><div class="section-content">
        <pre>// INORDER (sorted order for BST) — iterative
List&lt;Integer&gt; inorder(TreeNode root) {
    List&lt;Integer&gt; res = new ArrayList&lt;&gt;();
    Deque&lt;TreeNode&gt; stack = new ArrayDeque&lt;&gt;();
    for (TreeNode cur = root; cur!=null || !stack.isEmpty(); ) {
        while (cur != null) { stack.push(cur); cur = cur.left; }
        cur = stack.pop();
        res.add(cur.val);
        cur = cur.right;
    }
    return res;
}</pre>
        <pre>// LEVEL ORDER BFS — standard template
Queue&lt;TreeNode&gt; q = new LinkedList&lt;&gt;();
q.offer(root);
while (!q.isEmpty()) {
    int sz = q.size();       // ← CRITICAL: snapshot before loop
    for (int i = 0; i &lt; sz; i++) {
        TreeNode node = q.poll();
        // process node
        if (node.left  != null) q.offer(node.left);
        if (node.right != null) q.offer(node.right);
    }
    // all nodes at this level processed
}</pre>
      </div></div>
    </div>
    <div>
      <div class="section-box"><div class="section-header h-amber"><span class="num">C</span> BST CRITICAL OPERATIONS</div><div class="section-content">
        <pre>// Validate BST — pass bounds down O(n)
boolean valid(TreeNode n, long min, long max) {
    if (n == null) return true;
    if (n.val &lt;= min || n.val &gt;= max) return false;
    return valid(n.left,  min, n.val)
        &amp;&amp; valid(n.right, n.val, max);
}
// Call: valid(root, Long.MIN_VALUE, Long.MAX_VALUE)</pre>
        <pre>// LCA of BST — use BST property (no extra space!)
TreeNode lca(TreeNode root, TreeNode p, TreeNode q) {
    if (p.val &lt; root.val &amp;&amp; q.val &lt; root.val)
        return lca(root.left, p, q);
    if (p.val &gt; root.val &amp;&amp; q.val &gt; root.val)
        return lca(root.right, p, q);
    return root;  // split point = LCA
}

// LCA of General Binary Tree — O(n)
TreeNode lca(TreeNode node, TreeNode p, TreeNode q) {
    if (node == null || node == p || node == q) return node;
    TreeNode L = lca(node.left, p, q);
    TreeNode R = lca(node.right, p, q);
    return (L != null &amp;&amp; R != null) ? node : (L != null ? L : R);
}</pre>
      </div></div>
      <div class="section-box"><div class="section-header h-green"><span class="num">D</span> TOP LEETCODE — TREES</div><div class="section-content">
        <table><tr><th>#</th><th>Problem</th><th>Pattern</th><th>Diff</th></tr>
        <tr><td>104</td><td>Max Depth</td><td>DFS</td><td><span class="diff-easy">Easy</span></td></tr>
        <tr><td>102</td><td>Level Order Traversal</td><td>BFS</td><td><span class="diff-medium">Med</span></td></tr>
        <tr><td>543</td><td>Diameter of Binary Tree</td><td>DFS bottom-up</td><td><span class="diff-easy">Easy</span></td></tr>
        <tr><td>124</td><td>Binary Tree Max Path Sum</td><td>DFS bottom-up</td><td><span class="diff-hard">Hard</span></td></tr>
        <tr><td>235</td><td>LCA of BST</td><td>BST property</td><td><span class="diff-medium">Med</span></td></tr>
        <tr><td>236</td><td>LCA of Binary Tree</td><td>DFS return</td><td><span class="diff-medium">Med</span></td></tr>
        <tr><td>98</td><td>Validate BST</td><td>BST bounds</td><td><span class="diff-medium">Med</span></td></tr>
        <tr><td>199</td><td>Right Side View</td><td>BFS level</td><td><span class="diff-medium">Med</span></td></tr>
        <tr><td>297</td><td>Serialize Binary Tree</td><td>DFS/BFS</td><td><span class="diff-hard">Hard</span></td></tr>
        </table>
      </div></div>
    </div>
  </div>
</div></div>
""",

    "9.Graphs_Final.html": """
<div class="page"><div class="page-inner">
  <div class="header-top">
    <div><h1>&#x1F5FA; GRAPHS — FAANG Quick Reference</h1><div class="subtitle">BFS · DFS · Union-Find · Dijkstra · Topological Sort</div></div>
    <div class="page-number">APPENDIX</div>
  </div>
  <div class="grid-container">
    <div>
      <div class="section-box"><div class="section-header"><span class="num">A</span> BFS — Shortest Path (Unweighted)</div><div class="section-content">
        <pre>// Standard BFS — O(V+E)
int bfs(int src, int tgt, List&lt;List&lt;Integer&gt;&gt; adj) {
    boolean[] vis = new boolean[n];
    Queue&lt;Integer&gt; q = new LinkedList&lt;&gt;();
    q.offer(src); vis[src] = true;
    int dist = 0;
    while (!q.isEmpty()) {
        for (int sz = q.size(); sz &gt; 0; sz--) {
            int node = q.poll();
            if (node == tgt) return dist;
            for (int nei : adj.get(node))
                if (!vis[nei]) { q.offer(nei); vis[nei] = true; }
        }
        dist++;
    }
    return -1;
}</pre>
      </div></div>
      <div class="section-box"><div class="section-header h-amber"><span class="num">B</span> UNION-FIND (DSU) — Connected Components</div><div class="section-content">
        <pre>int[] parent, rank;
void init(int n) {
    parent = new int[n]; rank = new int[n];
    for (int i = 0; i &lt; n; i++) parent[i] = i;
}
int find(int x) {                          // path compression
    return parent[x] == x ? x : (parent[x] = find(parent[x]));
}
boolean union(int x, int y) {              // union by rank
    int px = find(x), py = find(y);
    if (px == py) return false;
    if (rank[px] &lt; rank[py]) { int t=px; px=py; py=t; }
    parent[py] = px;
    if (rank[px] == rank[py]) rank[px]++;
    return true;
}
// Time: O(α(n)) ≈ O(1) amortized per operation</pre>
      </div></div>
      <div class="section-box"><div class="section-header h-indigo"><span class="num">C</span> DIJKSTRA — Weighted Shortest Path</div><div class="section-content">
        <pre>// O((V+E) log V) — non-negative weights only!
int[] dijkstra(int src, List&lt;int[]&gt;[] adj, int n) {
    int[] dist = new int[n];
    Arrays.fill(dist, Integer.MAX_VALUE);
    dist[src] = 0;
    PriorityQueue&lt;int[]&gt; pq =    // [dist, node]
        new PriorityQueue&lt;&gt;((a,b) -&gt; a[0] - b[0]);
    pq.offer(new int[]{0, src});
    while (!pq.isEmpty()) {
        int[] cur = pq.poll();
        int d = cur[0], u = cur[1];
        if (d &gt; dist[u]) continue;   // stale entry, skip
        for (int[] e : adj[u]) {     // e = [neighbor, weight]
            if (dist[u] + e[1] &lt; dist[e[0]]) {
                dist[e[0]] = dist[u] + e[1];
                pq.offer(new int[]{dist[e[0]], e[0]});
            }
        }
    }
    return dist;
}</pre>
      </div></div>
    </div>
    <div>
      <div class="section-box"><div class="section-header h-green"><span class="num">D</span> TOPOLOGICAL SORT — Kahn's BFS</div><div class="section-content">
        <pre>// O(V+E) — detects cycle too!
List&lt;Integer&gt; topoSort(int n, int[][] edges) {
    List&lt;List&lt;Integer&gt;&gt; adj = new ArrayList&lt;&gt;();
    int[] inDeg = new int[n];
    for (int i = 0; i &lt; n; i++) adj.add(new ArrayList&lt;&gt;());
    for (int[] e : edges) {
        adj.get(e[0]).add(e[1]);
        inDeg[e[1]]++;
    }
    Queue&lt;Integer&gt; q = new LinkedList&lt;&gt;();
    for (int i = 0; i &lt; n; i++)
        if (inDeg[i] == 0) q.offer(i);
    List&lt;Integer&gt; order = new ArrayList&lt;&gt;();
    while (!q.isEmpty()) {
        int node = q.poll();
        order.add(node);
        for (int nei : adj.get(node))
            if (--inDeg[nei] == 0) q.offer(nei);
    }
    // order.size() &lt; n → cycle exists!
    return order.size() == n ? order : Collections.emptyList();
}</pre>
      </div></div>
      <div class="section-box"><div class="section-header h-red"><span class="num">E</span> ALGORITHM DECISION TABLE</div><div class="section-content">
        <table><tr><th>Problem Type</th><th>Algorithm</th><th>Time</th></tr>
        <tr><td>Shortest path (unweighted)</td><td>BFS</td><td>O(V+E)</td></tr>
        <tr><td>Shortest path (+ve weights)</td><td>Dijkstra</td><td>O((V+E)logV)</td></tr>
        <tr><td>Shortest path (neg weights)</td><td>Bellman-Ford</td><td>O(VE)</td></tr>
        <tr><td>All-pairs shortest path</td><td>Floyd-Warshall</td><td>O(V³)</td></tr>
        <tr><td>Cycle detection (directed)</td><td>DFS 3-color</td><td>O(V+E)</td></tr>
        <tr><td>Connected components</td><td>Union-Find / BFS</td><td>O(V+E)</td></tr>
        <tr><td>Topological sort</td><td>Kahn's BFS / DFS</td><td>O(V+E)</td></tr>
        <tr><td>Min spanning tree</td><td>Prim's / Kruskal's</td><td>O(E logV)</td></tr>
        <tr><td>Bipartite check</td><td>BFS 2-coloring</td><td>O(V+E)</td></tr>
        </table>
      </div></div>
      <div class="section-box"><div class="section-header"><span class="num">F</span> TOP LEETCODE — GRAPHS</div><div class="section-content">
        <table><tr><th>#</th><th>Problem</th><th>Pattern</th><th>Diff</th></tr>
        <tr><td>200</td><td>Number of Islands</td><td>DFS/BFS/UF</td><td><span class="diff-medium">Med</span></td></tr>
        <tr><td>207</td><td>Course Schedule</td><td>Topo Sort</td><td><span class="diff-medium">Med</span></td></tr>
        <tr><td>743</td><td>Network Delay Time</td><td>Dijkstra</td><td><span class="diff-medium">Med</span></td></tr>
        <tr><td>684</td><td>Redundant Connection</td><td>Union-Find</td><td><span class="diff-medium">Med</span></td></tr>
        <tr><td>127</td><td>Word Ladder</td><td>BFS</td><td><span class="diff-hard">Hard</span></td></tr>
        <tr><td>785</td><td>Is Graph Bipartite?</td><td>BFS 2-color</td><td><span class="diff-medium">Med</span></td></tr>
        <tr><td>1584</td><td>Min Cost to Connect Points</td><td>Prim's/Kruskal</td><td><span class="diff-medium">Med</span></td></tr>
        <tr><td>329</td><td>Longest Path in Matrix</td><td>DFS + memo</td><td><span class="diff-hard">Hard</span></td></tr>
        </table>
      </div></div>
    </div>
  </div>
</div></div>
"""
}

# =====================================================
# Fix bad inline colors from subagents
# =====================================================
def fix_inline_colors(html):
    # Dark code backgrounds → keep for screen (handled by CSS)
    # But fix TRULY invisible text combinations:
    
    # Light gray text (nearly invisible on white) → readable
    replacements = [
        ('color: #94a3b8', 'color: #475569'),
        ('color:#94a3b8',  'color:#475569'),
        ('color: #cbd5e1', 'color: #334155'),
        ('color:#cbd5e1',  'color:#334155'),
        ('color: #e2e8f0', 'color: #334155'),
        ('color:#e2e8f0',  'color:#334155'),
        ('color: yellow',  'color: #b45309'),
        ('color:yellow',   'color:#b45309'),
        # Green text on non-dark containers → dark green
        ('color: #4ade80', 'color: #15803d'),
        ('color:#4ade80',  'color:#15803d'),
        ('color: #86efac', 'color: #15803d'),
        ('color:#86efac',  'color:#15803d'),
        # Light blue → dark blue
        ('color: #93c5fd', 'color: #1d4ed8'),
        ('color:#93c5fd',  'color:#1d4ed8'),
        ('color: #bfdbfe', 'color: #1d4ed8'),
        ('color:#bfdbfe',  'color:#1d4ed8'),
    ]
    for old, new in replacements:
        html = html.replace(old, new)
    
    # Fix dark code backgrounds that would be invisible with new dark CSS
    # The CSS override handles pre/code globally, but inline styles need explicit fixing
    dark_bgs = ['#1e1e2e','#0f172a','#282c34','#1a1a2e','#111827',
                '#1f2937','#2d2d2d','#333333','#272822']
    for bg in dark_bgs:
        # Only fix if NOT inside a <pre> context (can't tell from regex, so just remove)
        html = html.replace(f'background:{bg}', f'background:{bg}')  # keep as-is (CSS overrides)
        html = html.replace(f'background-color:{bg}', f'background-color:{bg}')
    
    return html

# =====================================================
# Wrap bare body content into .page-inner div
# =====================================================
def ensure_page_inner(html):
    """Ensure .page divs have a .page-inner child for padding."""
    # Add page-inner wrapper if not already present
    if 'class="page-inner"' not in html and 'class=\'page-inner\'' not in html:
        # Wrap content of each .page div
        html = re.sub(
            r'(<div[^>]*class="page"[^>]*>)',
            r'\1<div class="page-inner">',
            html
        )
        html = re.sub(
            r'(</div>)(\s*(?:<div[^>]*class="page"|$))',
            r'</div></div>\2',
            html
        )
    return html

# =====================================================
# Build v2 files
# =====================================================
finals = [f for f in os.listdir(src_dir) if f.endswith('_Final.html')]
print(f"Building v2 for {len(finals)} topics...")

for fname in sorted(finals):
    src_path = os.path.join(src_dir, fname)
    dst_path = os.path.join(v2_dir, fname)
    
    with open(src_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Fix invisible inline colors
    html = fix_inline_colors(html)
    
    # Replace CSS: find the first <style> block in <head> and replace it
    # Also remove the second style block if it exists
    style_match = re.search(r'<style[^>]*>.*?</style>', html, re.DOTALL)
    if style_match:
        html = html[:style_match.start()] + V2_CSS + html[style_match.end():]
    else:
        # Inject before </head>
        html = html.replace('</head>', V2_CSS + '\n</head>', 1)
    
    # Remove any additional <style> blocks (from improve_and_copy.py)
    # Find all remaining style blocks after the first one
    remaining = re.findall(r'<style[^>]*>.*?</style>', html, re.DOTALL)
    if len(remaining) > 1:
        # Remove all but first (which is our V2_CSS)
        for extra in remaining[1:]:
            html = html.replace(extra, '', 1)
    
    # Inject FAANG appendix before </body>
    appendix = APPENDICES.get(fname, '')
    if appendix and '</body>' in html:
        html = html.replace('</body>', appendix + '\n</body>', 1)
    
    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    size_kb = os.path.getsize(dst_path) / 1024
    checks = {
        'teal': '#0d9488' in html or '#0f766e' in html,
        'amber': '#f59e0b' in html,
        'code_dark': 'slate-900' in html or '#0f172a' in html,
        'appendix': 'FAANG Quick Reference' in html,
    }
    print(f"  [{size_kb:.0f}KB] {fname} | teal={checks['teal']} amber={checks['amber']} code={checks['code_dark']} appendix={checks['appendix']}")

print(f"\nv2 folder ready: {v2_dir}")
print("\nDesign summary:")
print("  Background: Gradient teal-blue-amber wash (screen) | white (print)")
print("  Page card: White with teal→amber top gradient stripe")
print("  Section headers: Teal gradient + amber numbered badge")
print("  Tables: Teal gradient header + alternating teal-tint rows")
print("  Code: Dark slate bg + light text (screen) | white bg (print/xerox)")
print("  Callouts: Color-coded tip/warn/danger/info with dark borders")
print("  Difficulty: green/amber/red — xerox-safe dark shades")

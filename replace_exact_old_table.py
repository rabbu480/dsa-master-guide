import os, sys, subprocess, fitz

sys.stdout.reconfigure(encoding='utf-8')

# Read pristine v4 Topic11_Trie.html
v4_file = r"F:\dsa\bookfinal - Copy\v4\bookfinal\Topic11_Trie.html"
with open(v4_file, "r", encoding="utf-8", errors="ignore") as f:
    html = f.read()

# Add print fix CSS inside <head>
print_fix_css = """
pre {
  background: #f8fafc !important;
  color: #0f172a !important;
  border: 1.5px solid #cbd5e1 !important;
  font-family: 'Fira Code', monospace !important;
  font-size: 0.72rem !important;
  line-height: 1.25 !important;
  padding: 8px 10px !important;
  border-radius: 6px !important;
  margin: 4px 0 !important;
  white-space: pre-wrap !important;
}
@media print {
  body { background: white !important; padding: 0 !important; margin: 0 !important; color: black !important; -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
  .top-nav, .toc-sidebar { display: none !important; }
  .app-layout { display: block !important; }
  .page { box-shadow: none !important; border: none !important; margin: 0 !important; padding: 4px 6px !important; width: 100% !important; page-break-after: always !important; break-after: page !important; page-break-inside: avoid !important; break-inside: avoid !important; zoom: 0.82; }
  .page:last-child { page-break-after: avoid !important; break-after: avoid !important; }
  table, tr, td, th { page-break-inside: avoid !important; break-inside: avoid !important; }
  pre {
    background: #f8fafc !important;
    color: #0f172a !important;
    border: 1.5px solid #cbd5e1 !important;
    font-size: 0.68rem !important;
    line-height: 1.18 !important;
  }
}
"""

head_end = html.find('</head>')
style_part = html[:head_end]
style_part = style_part.replace('</style>', print_fix_css + '\n</style>')
html_mod = style_part + html[head_end:]

# Replace LaTeX $ \rightarrow $ with clean unicode arrows →
html_mod = html_mod.replace(r'$\rightarrow$', '→').replace(r'\rightarrow', '→').replace('$ \rightarrow $', '→')

# Replace the table on Page 9 of v4 with an Enriched Problem Ladder Table containing Sample Input & Sample Output!
old_table_pos = html_mod.find('<table style="font-size:0.75rem">')
if old_table_pos == -1:
    old_table_pos = html_mod.find('<th>LC #</th>')
    old_table_pos = html_mod.rfind('<table', 0, old_table_pos)

table_end_pos = html_mod.find('</table>', old_table_pos) + len('</table>')

new_table_html = """<table>
      <tr>
        <th style="width:4%">#</th>
        <th style="width:20%">Problem &amp; LeetCode ID</th>
        <th style="width:26%">Sample Input</th>
        <th style="width:18%">Sample Output</th>
        <th style="width:22%">Key Technique &amp; Pattern</th>
        <th style="width:10%">Complexity</th>
      </tr>
      <tr>
        <td>1</td>
        <td><strong>Implement Trie</strong><br/><span style="font-size:0.7rem;color:var(--sub)">LC 208 · Easy</span></td>
        <td><code>insert("apple"), search("app")</code></td>
        <td><code>false</code></td>
        <td>26-element array TrieNode tree</td>
        <td>$O(L)$</td>
      </tr>
      <tr>
        <td>2</td>
        <td><strong>Longest Common Prefix</strong><br/><span style="font-size:0.7rem;color:var(--sub)">LC 14 · Easy</span></td>
        <td><code>strs = ["flower","flow","flight"]</code></td>
        <td><code>"fl"</code></td>
        <td>Traverse single path until childCount > 1</td>
        <td>$O(N \cdot L)$</td>
      </tr>
      <tr>
        <td>3</td>
        <td><strong>Replace Words</strong><br/><span style="font-size:0.7rem;color:var(--sub)">LC 648 · Medium</span></td>
        <td><code>dict=["cat","bat"], sentence="cattle battery"</code></td>
        <td><code>"cat bat"</code></td>
        <td>Break loop early when <code>isWord == true</code></td>
        <td>$O(S + N \cdot L)$</td>
      </tr>
      <tr>
        <td>4</td>
        <td><strong>Design Add &amp; Search Words</strong><br/><span style="font-size:0.7rem;color:var(--sub)">LC 211 · Medium</span></td>
        <td><code>addWord("bad"), search(".ad")</code></td>
        <td><code>true</code></td>
        <td>Branch into all 26 children on wildcard <code>'.'</code></td>
        <td>$O(26^L)$</td>
      </tr>
      <tr>
        <td>5</td>
        <td><strong>Search Suggestions System</strong><br/><span style="font-size:0.7rem;color:var(--sub)">LC 1268 · Medium</span></td>
        <td><code>products=["mobile","mouse"], search="mouse"</code></td>
        <td><code>[["mobile","mouse"],...]</code></td>
        <td>Store pre-sorted Top-3 product list in node</td>
        <td>$O(N \log N + L)$</td>
      </tr>
      <tr>
        <td>6</td>
        <td><strong>Map Sum Pairs</strong><br/><span style="font-size:0.7rem;color:var(--sub)">LC 677 · Medium</span></td>
        <td><code>insert("apple", 3), sum("ap")</code></td>
        <td><code>3</code></td>
        <td>Update running delta score at prefix nodes</td>
        <td>$O(L)$</td>
      </tr>
      <tr>
        <td>7</td>
        <td><strong>Word Search II</strong><br/><span style="font-size:0.7rem;color:var(--sub)">LC 212 · Hard</span></td>
        <td><code>board=[['o','a'],['t','h']], words=["oath"]</code></td>
        <td><code>["oath"]</code></td>
        <td>2D Grid DFS with Trie node pruning</td>
        <td>$O(M \cdot N \cdot 3^L)$</td>
      </tr>
      <tr>
        <td>8</td>
        <td><strong>Maximum XOR Pair</strong><br/><span style="font-size:0.7rem;color:var(--sub)">LC 421 · Medium</span></td>
        <td><code>nums = [3, 10, 5, 25, 2, 8]</code></td>
        <td><code>28</code> (5 ^ 25)</td>
        <td>31-bit Binary Trie with greedy opposite bit <code>1^b</code></td>
        <td>$O(31 \cdot N)$</td>
      </tr>
      <tr>
        <td>9</td>
        <td><strong>Palindrome Pairs</strong><br/><span style="font-size:0.7rem;color:var(--sub)">LC 336 · Hard</span></td>
        <td><code>words = ["abcd","dcba","lls","s"]</code></td>
        <td><code>[[0,1],[1,0],[3,2]]</code></td>
        <td>Reverse word insertion with palindrome split checks</td>
        <td>$O(N \cdot L^2)$</td>
      </tr>
      <tr>
        <td>10</td>
        <td><strong>Stream of Characters</strong><br/><span style="font-size:0.7rem;color:var(--sub)">LC 1032 · Hard</span></td>
        <td><code>words=["cd","f"], stream='a','b','c','d'</code></td>
        <td><code>[false, false, false, true]</code></td>
        <td>Insert reversed words; search stream backwards</td>
        <td>$O(L)$ per char</td>
      </tr>
    </table>"""

html_mod = html_mod[:old_table_pos] + new_table_html + html_mod[table_end_pos:]

# Consolidate 10 pages into 6 dense pages by merging adjacent light pages
import re
pages_raw = re.split(r'<!-- PAGE \d+:', html_mod)[1:]

def count_open_divs(snippet):
    return len(re.findall(r'<div[\s>]', snippet)) - len(re.findall(r'</div>', snippet))

pages_clean = []
for p in pages_raw:
    ph_start = p.find('<div class="ph">')
    if ph_start != -1:
        ph_end = p.find('</div>\n</div>', ph_start)
        if ph_end == -1: ph_end = p.find('</div></div>', ph_start)
        body = p[ph_end+12:] if ph_end != -1 else p
    else:
        body = p
        
    diff = count_open_divs(body)
    if diff > 0: body += '</div>' * diff
    elif diff < 0: body = ('<div>' * abs(diff)) + body
    pages_clean.append(body)

body_start = html_mod.find('<div class="main-content">') + len('<div class="main-content">')
head_and_main = html_mod[:body_start]

topic_title = "TRIE (PREFIX TREE)"

p1 = f"""\n<!-- PAGE 1: DISCOVERY & TOOLKIT -->\n<div class="page"><div class="ph"><div><h1>{topic_title}</h1><div class="sub">Discovery &amp; Base Toolkit</div></div><div style="text-align:right"><div class="pn">PAGE 1 OF 6</div></div></div>{pages_clean[0]}<div style="margin-top:4px"></div>{pages_clean[1]}</div>"""
p2 = f"""\n<!-- PAGE 2: CORE PATTERNS (WILDCARD & REPLACE WORDS) -->\n<div class="page"><div class="ph"><div><h1>{topic_title}</h1><div class="sub">Core Patterns — Part 1 &amp; Part 2</div></div><div style="text-align:right"><div class="pn">PAGE 2 OF 6</div></div></div>{pages_clean[2]}<div style="margin-top:4px"></div>{pages_clean[3]}</div>"""
p3 = f"""\n<!-- PAGE 3: CORE PATTERNS (GRID DFS & BITWISE TRIE) -->\n<div class="page"><div class="ph"><div><h1>{topic_title}</h1><div class="sub">Core Patterns — Part 3 &amp; Part 4</div></div><div style="text-align:right"><div class="pn">PAGE 3 OF 6</div></div></div>{pages_clean[4]}<div style="margin-top:4px"></div>{pages_clean[5]}</div>"""
p4 = f"""\n<!-- PAGE 4: DECISION TREE & TRIGGER WORDS -->\n<div class="page"><div class="ph"><div><h1>{topic_title}</h1><div class="sub">Decision Tree &amp; Trigger Words</div></div><div style="text-align:right"><div class="pn">PAGE 4 OF 6</div></div></div>{pages_clean[6]}</div>"""
p5 = f"""\n<!-- PAGE 5: PROBLEM LADDER (ALL 10 PROBLEMS WITH SAMPLE INPUT & OUTPUT) -->\n<div class="page"><div class="ph"><div><h1>{topic_title}</h1><div class="sub">FAANG Problem Ladder (All 10 Problems with Inputs &amp; Outputs)</div></div><div style="text-align:right"><div class="pn">PAGE 5 OF 6</div></div></div>{pages_clean[7]}<div style="margin-top:4px"></div>{pages_clean[8]}</div>"""
p6 = f"""\n<!-- PAGE 6: DRY RUN & CHEAT SHEET -->\n<div class="page"><div class="ph"><div><h1>{topic_title}</h1><div class="sub">Dry Run, Proofs &amp; Cheat Sheet</div></div><div style="text-align:right"><div class="pn">PAGE 6 OF 6</div></div></div>{pages_clean[9]}</div>"""

full_html = head_and_main + p1 + p2 + p3 + p4 + p5 + p6 + '\n</div>\n</div>\n</div>\n</body>\n</html>'

dst_html = r"F:\dsa\bookfinal\Topic11_Trie.html"
with open(dst_html, "w", encoding="utf-8") as f:
    f.write(full_html)

print("Saved Restored v4 Topic11_Trie.html with Enriched Problem Ladder Table to", dst_html)

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
pdf_out = r"F:\dsa\bookfinal\Topic11_Trie.pdf"

if os.path.exists(pdf_out): os.remove(pdf_out)

cmd = [chrome_path, '--headless', '--disable-gpu', '--no-pdf-header-footer', f'--print-to-pdf={pdf_out}', dst_html]
subprocess.run(cmd, check=True)

doc = fitz.open(pdf_out)
print("==========================================")
print(f"Generated Topic 11 PDF Page Count: {len(doc)} pages")
print("==========================================")
for i in range(len(doc)):
    page = doc[i]
    text = page.get_text()
    t_clean = text[:70].replace('\n', ' ')
    print(f"Page {i+1} has {len(text)} chars: {t_clean}")
doc.close()

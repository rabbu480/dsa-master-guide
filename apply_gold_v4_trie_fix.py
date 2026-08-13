import os, sys, re, subprocess, fitz

sys.stdout.reconfigure(encoding='utf-8')

v4_file = r"F:\dsa\bookfinal - Copy\v4\bookfinal\Topic11_Trie.html"
with open(v4_file, "r", encoding="utf-8", errors="ignore") as f:
    html = f.read()

# Fix CSS: Light background for ALL code blocks <pre> on screen and in print mode (NO BLACK BACKGROUND!)
light_code_css = """
pre {
  background: #f8fafc !important;
  color: #0f172a !important;
  border: 1.5px solid #cbd5e1 !important;
  font-family: 'Fira Code', monospace !important;
  font-size: 0.70rem !important;
  line-height: 1.2 !important;
  padding: 6px 8px !important;
  border-radius: 5px !important;
  margin: 3px 0 !important;
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
style_part = re.sub(r'@page\s*\{[^}]*\}[\s\S]*?(?=</style>)', '', style_part)
html_mod = style_part.replace('</style>', light_code_css + '\n</style>') + html[head_end:]

# Replace LaTeX $ \rightarrow $ with clean unicode arrows →
html_mod = html_mod.replace(r'$\rightarrow$', '→').replace(r'\rightarrow', '→').replace('$ \rightarrow $', '→')

# Update pattern 2 (Replace Words LC 648) left box with clean format
lc648_old = r'<div class="pc-head">When to Use</div>\s*<div style="font-size:0.78rem">Replace each word in a sentence with the shortest matching root in dictionary.</div>'
lc648_new = """<div class="pc-head">Problem Statement &amp; Mechanics</div>
      <div style="font-size:0.75rem;margin-bottom:3px">Given a dictionary of root words and a sentence, replace every word in the sentence with the shortest root that matches its prefix. If no root matches, keep original word.</div>
      <div class="io-box" style="background:#f1f5f9;border:1px solid #cbd5e1;border-left:3px solid #2563eb;padding:3px 5px;margin:3px 0;border-radius:3px;font-family:'Fira Code',monospace;font-size:0.71rem"><strong>Input:</strong> dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"<br/><strong>Output:</strong> "the cat was rat by the bat"</div>
      <div class="dry-box" style="background:#fefce8;border:1px solid #fef08a;border-left:3px solid #d97706;padding:3px 5px;margin:3px 0;border-radius:3px;font-size:0.72rem"><strong>🔍 Step-by-Step Manual Dry Run:</strong><br/>1. Build Trie with roots: <code>"cat"</code>, <code>"bat"</code>, <code>"rat"</code>.<br/>2. Process <code>"cattle"</code>: Walk Trie <code>c → a → t</code> (isWord = true) → return <strong>"cat"</strong>.<br/>3. Process <code>"rattled"</code>: Walk Trie <code>r → a → t</code> (isWord = true) → return <strong>"rat"</strong>.<br/>4. Process <code>"battery"</code>: Walk Trie <code>b → a → t</code> (isWord = true) → return <strong>"bat"</strong>.</div>"""

html_mod = re.sub(lc648_old, lc648_new, html_mod)

# Update pattern 1 (Wildcard Dot LC 211) left box with clean format
lc211_old = r'<div class="pc-head">Wildcard Dot Mechanics</div>\s*<div style="font-size:0.78rem">\s*When character is \., loop through ALL 26 children\. If ANY child branch matches the remaining string, return true!\s*</div>'
lc211_new = """<div class="pc-head">Problem Statement &amp; Mechanics</div>
      <div style="font-size:0.75rem;margin-bottom:3px">Design a data structure supporting <code>addWord(word)</code> and <code>search(word)</code>, where <code>'.'</code> matches any letter.</div>
      <div class="io-box" style="background:#f1f5f9;border:1px solid #cbd5e1;border-left:3px solid #2563eb;padding:3px 5px;margin:3px 0;border-radius:3px;font-family:'Fira Code',monospace;font-size:0.71rem"><strong>Input:</strong> addWord("bad"), addWord("dad"), addWord("mad"), search("pad"), search(".ad"), search("b..")<br/><strong>Output:</strong> [false, true, true]</div>
      <div class="dry-box" style="background:#fefce8;border:1px solid #fef08a;border-left:3px solid #d97706;padding:3px 5px;margin:3px 0;border-radius:3px;font-size:0.72rem"><strong>🔍 Step-by-Step Manual Dry Run:</strong><br/>1. <code>search(".ad")</code>: First char <code>'.'</code> → DFS branches into all 26 children. 'b' branch checks <code>"ad"</code> → matches <code>"bad"</code>! Returns <strong>true</strong>.<br/>2. <code>search("b..")</code>: 'b' branch exists → 2nd char <code>'.'</code> checks 'a' → 3rd char <code>'.'</code> checks 'd' (isWord = true) → Returns <strong>true</strong>.</div>"""

html_mod = re.sub(lc211_old, lc211_new, html_mod)

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
p5 = f"""\n<!-- PAGE 5: PROBLEM LADDER (ALL 10 PROBLEMS) -->\n<div class="page"><div class="ph"><div><h1>{topic_title}</h1><div class="sub">FAANG Problem Ladder (All 10 Problems)</div></div><div style="text-align:right"><div class="pn">PAGE 5 OF 6</div></div></div>{pages_clean[7]}<div style="margin-top:4px"></div>{pages_clean[8]}</div>"""
p6 = f"""\n<!-- PAGE 6: DRY RUN & CHEAT SHEET -->\n<div class="page"><div class="ph"><div><h1>{topic_title}</h1><div class="sub">Dry Run, Proofs &amp; Cheat Sheet</div></div><div style="text-align:right"><div class="pn">PAGE 6 OF 6</div></div></div>{pages_clean[9]}</div>"""

full_html = head_and_main + p1 + p2 + p3 + p4 + p5 + p6 + '\n</div>\n</div>\n</div>\n</body>\n</html>'

dst_html = r"F:\dsa\bookfinal\Topic11_Trie.html"
with open(dst_html, "w", encoding="utf-8") as f:
    f.write(full_html)

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

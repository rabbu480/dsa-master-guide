import os, sys, subprocess, fitz

sys.stdout.reconfigure(encoding='utf-8')

# Read current Topic11_Trie.html
html_file = r"F:\dsa\bookfinal\Topic11_Trie.html"
with open(html_file, "r", encoding="utf-8", errors="ignore") as f:
    html = f.read()

# Locate the Problem Ladder table box on Page 5
start_marker = '<div class="box grn">'
start_pos = html.find(start_marker, html.find('<!-- PAGE 5'))
if start_pos == -1:
    start_pos = html.find(start_marker)

end_pos = html.find('</div>\n</div>', start_pos) + len('</div>\n</div>')

old_table_block = html[start_pos:end_pos]

new_table_block = """<div class="box grn" style="margin-bottom:8px">
  <div class="bh">🚀 FAANG TRIE PROBLEM LADDER (ALL 10 PROBLEMS WITH SAMPLE INPUT &amp; OUTPUT)</div>
  <div class="bc">
    <table>
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
    </table>
  </div>
</div>"""

html_updated = html[:start_pos] + new_table_block + html[end_pos:]

dst_html = r"F:\dsa\bookfinal\Topic11_Trie.html"
with open(dst_html, "w", encoding="utf-8") as f:
    f.write(html_updated)

print("Updated Page 5 Problem Ladder Table with explicit Inputs & Outputs!")

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

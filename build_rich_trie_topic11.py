import os, sys, subprocess, fitz

sys.stdout.reconfigure(encoding='utf-8')

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Topic 11: Trie (Prefix Tree) Masterclass — FAANG Edition</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Fira+Code:wght@400;500;600&display=swap" rel="stylesheet"/>
<style>
:root {
  --pri: #1e3a8a; --sec: #2563eb; --grn: #059669; --red: #dc2626;
  --pur: #7c3aed; --org: #ea580c; --amb: #d97706; --sky: #0284c7;
  --txt: #0f172a; --sub: #475569; --bdr: #cbd5e1; --bg: #f8fafc;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: 'Inter', sans-serif; background: #e2e8f0; color: var(--txt); font-size: 10.5px; line-height: 1.34; padding: 15px; }

.page {
  background: white; max-width: 1100px; margin: 0 auto 20px auto;
  padding: 10px 14px; border-radius: 8px;
  box-shadow: 0 6px 20px rgba(0,0,0,0.08);
  page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;
}

.ph { display:flex; justify-content:space-between; align-items:center;
  border-bottom: 2.5px solid var(--pri); padding-bottom: 4px; margin-bottom: 8px; }
.ph h1 { font-size: 1.45rem; font-weight: 900; color: var(--pri); letter-spacing: 0.5px; }
.ph .sub { font-size: 0.8rem; font-weight: 600; color: var(--sub); margin-top: 1px; }
.ph .pn { background: var(--pri); color: white; padding: 2px 10px; border-radius: 12px;
  font-weight: 800; font-size: 0.78rem; text-align: right; }
.ph .ptag { font-size: 0.7rem; color: var(--sub); font-weight: 600; margin-top: 2px; }

.g2 { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
.g3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; }

.box { border: 1.5px solid var(--pri); border-radius: 6px; overflow: hidden; margin-bottom: 8px; background: white; }
.box.pur { border-color: var(--pur); }
.box.grn { border-color: var(--grn); }
.box.amb { border-color: var(--amb); }
.box.red { border-color: var(--red); }
.box.sky { border-color: var(--sky); }

.bh { background: var(--pri); color: white; padding: 4px 8px; font-weight: 800; font-size: 0.82rem; display: flex; justify-content: space-between; align-items: center; }
.box.pur .bh { background: var(--pur); }
.box.grn .bh { background: var(--grn); }
.box.amb .bh { background: var(--amb); }
.box.red .bh { background: var(--red); }
.box.sky .bh { background: var(--sky); }

.bc { padding: 6px 8px; font-size: 0.78rem; color: var(--txt); }

.prob-card { border: 1.5px solid var(--pri); border-radius: 6px; margin-bottom: 10px; background: white; overflow: hidden; }
.prob-header { background: #f1f5f9; padding: 6px 10px; border-bottom: 1.5px solid var(--bdr); display: flex; justify-content: space-between; align-items: center; }
.prob-title { font-weight: 800; font-size: 0.88rem; color: var(--pri); }
.prob-badge { background: var(--sec); color: white; padding: 2px 8px; border-radius: 10px; font-size: 0.72rem; font-weight: 700; }

.prob-body { padding: 8px 10px; }
.io-box { background: #f8fafc; border: 1px solid var(--bdr); border-left: 3.5px solid var(--sec); padding: 5px 8px; margin: 4px 0; border-radius: 4px; font-family: 'Fira Code', monospace; font-size: 0.74rem; }
.dry-box { background: #fefce8; border: 1px solid #fef08a; border-left: 3.5px solid var(--amb); padding: 5px 8px; margin: 4px 0; border-radius: 4px; font-size: 0.76rem; }

pre { font-family: 'Fira Code', monospace; font-size: 0.72rem; line-height: 1.25; background: #0f172a; color: #f8fafc; padding: 6px 8px; border-radius: 4px; margin: 4px 0; overflow-x: auto; }
table { font-size: 0.74rem; border-collapse: collapse; width: 100%; margin: 4px 0; }
th, td { padding: 4px 6px; border: 1px solid var(--bdr); text-align: left; }
th { background: #f1f5f9; font-weight: 700; color: var(--pri); }

.aha { background: #eff6ff; border-left: 3.5px solid var(--sec); padding: 5px 8px; margin: 4px 0; font-size: 0.76rem; border-radius: 0 4px 4px 0; }
.aha-t { font-weight: 800; color: var(--sec); margin-bottom: 2px; }

@page { size: A4 portrait; margin: 3mm; }
@media print {
  body { background: white !important; padding: 0 !important; margin: 0 !important; color: black !important; -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
  .top-nav, .toc-sidebar { display: none !important; }
  .app-layout { display: block !important; }
  .page { box-shadow: none !important; border: none !important; margin: 0 !important; padding: 4px 6px !important; width: 100% !important; page-break-after: always !important; break-after: page !important; page-break-inside: avoid !important; break-inside: avoid !important; zoom: 0.85; }
  .page:last-child { page-break-after: avoid !important; break-after: avoid !important; }
  table, tr, td, th { page-break-inside: avoid !important; break-inside: avoid !important; }
}
</style>
</head>
<body>

<div class="container">
<div class="app-layout">
<div class="main-content">

<!-- PAGE 1: FOUNDATION & IMPLEMENT TRIE (LC 208) -->
<div class="page">
<div class="ph">
  <div><h1>TRIE DATA STRUCTURE</h1><div class="sub">FAANG Master Guide — Foundation &amp; Base Implementation</div></div>
  <div style="text-align:right"><div class="pn">PAGE 1 OF 6</div><div class="ptag">PREFIX TREE · O(L) SEARCH · LC 208</div></div>
</div>

<div class="g2" style="margin-bottom:8px">
  <div class="box pur">
    <div class="bh">🎬 THE REAL-WORLD STORY</div>
    <div class="bc">
      Imagine a dictionary search bar. Typing <strong>"app"</strong> instantly suggests <em>"apple"</em>, <em>"application"</em>, <em>"applet"</em>.
      <div class="aha" style="margin-top:4px">
        <div class="aha-t">💡 THE TRIE AHA MOMENT</div>
        Instead of searching N words in O(N × L) time, a Trie shares common prefix nodes! Search time is strictly <strong>O(L)</strong> (where L = length of word), completely independent of dictionary size N!
      </div>
    </div>
  </div>

  <div class="box sky">
    <div class="bh">⚡ WHY NOT HASH MAP?</div>
    <div class="bc">
      <ul style="padding-left:12px;font-size:0.75rem">
        <li><strong>HashMap:</strong> Exact match $O(L)$ lookup, but CANNOT do prefix search $O(L)$! Finding words starting with `"app"` requires scanning all N keys $O(N \cdot L)$!</li>
        <li><strong>Trie (Prefix Tree):</strong> Both exact lookup AND prefix matching run in <strong>$O(L)$ time</strong>!</li>
      </ul>
    </div>
  </div>
</div>

<div class="prob-card">
  <div class="prob-header">
    <div class="prob-title">1. IMPLEMENT TRIE (PREFIX TREE) — LC 208</div>
    <div class="prob-badge">CORE FOUNDATION</div>
  </div>
  <div class="prob-body">
    <div style="font-weight:700;color:var(--sub)">Problem Statement:</div>
    <div>Implement a Trie with <code>insert(word)</code>, <code>search(word)</code>, and <code>startsWith(prefix)</code> methods.</div>
    <div class="io-box">
      <strong>Input:</strong> insert("apple"), search("apple"), search("app"), startsWith("app"), insert("app"), search("app")<br/>
      <strong>Output:</strong> [true, false, true, true]
    </div>
    <div class="dry-box">
      <strong>🔍 Step-by-Step Manual Dry Run:</strong><br/>
      1. <code>insert("apple")</code>: Root → 'a' → 'p' → 'p' → 'l' → 'e' (Mark <code>isEnd = true</code> at 'e').<br/>
      2. <code>search("app")</code>: Traverse 'a'→'p'→'p'. Node exists, but <code>isEnd == false</code> → Return <strong>false</strong>.<br/>
      3. <code>startsWith("app")</code>: Traverse 'a'→'p'→'p'. Node exists → Return <strong>true</strong>.<br/>
      4. <code>insert("app")</code>: Traverse 'a'→'p'→'p', set <code>isEnd = true</code> at 2nd 'p'.<br/>
      5. <code>search("app")</code>: Traverse 'a'→'p'→'p'. <code>isEnd == true</code> → Return <strong>true</strong>.
    </div>
<pre>class Trie {
    private class TrieNode {
        TrieNode[] children = new TrieNode[26];
        boolean isEnd = false;
    }
    private final TrieNode root = new TrieNode();

    public void insert(String word) {
        TrieNode curr = root;
        for (char ch : word.toCharArray()) {
            int idx = ch - 'a';
            if (curr.children[idx] == null) curr.children[idx] = new TrieNode();
            curr = curr.children[idx];
        }
        curr.isEnd = true;
    }

    public boolean search(String word) {
        TrieNode node = execSearch(word);
        return node != null && node.isEnd;
    }

    public boolean startsWith(String prefix) {
        return execSearch(prefix) != null;
    }

    private TrieNode execSearch(String str) {
        TrieNode curr = root;
        for (char ch : str.toCharArray()) {
            curr = curr.children[ch - 'a'];
            if (curr == null) return null;
        }
        return curr;
    }
}</pre>
    <div style="font-size:0.72rem;color:var(--sub);margin-top:2px">
      <strong>Complexity:</strong> Time: $O(L)$ for insert/search/startsWith | Space: $O(N \cdot L)$ total nodes stored.
    </div>
  </div>
</div>
</div>

<!-- PAGE 2: LC 648 (REPLACE WORDS) & LC 211 (WILDCARD SEARCH) -->
<div class="page">
<div class="ph">
  <div><h1>TRIE DATA STRUCTURE</h1><div class="sub">Core Patterns — Shortest Root &amp; Wildcard Search</div></div>
  <div style="text-align:right"><div class="pn">PAGE 2 OF 6</div><div class="ptag">LC 648 · LC 211 · PREFIX ROOT MATCH</div></div>
</div>

<div class="prob-card">
  <div class="prob-header">
    <div class="prob-title">2. REPLACE WORDS (SHORTEST ROOT MATCH) — LC 648</div>
    <div class="prob-badge">PREFIX MATCHING</div>
  </div>
  <div class="prob-body">
    <div style="font-weight:700;color:var(--sub)">Problem Statement:</div>
    <div>Given a dictionary of root words and a sentence, replace every word in the sentence with the shortest root that matches its prefix. If no root matches, keep the original word.</div>
    <div class="io-box">
      <strong>Input:</strong> dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"<br/>
      <strong>Output:</strong> "the cat was rat by the bat"
    </div>
    <div class="dry-box">
      <strong>🔍 Step-by-Step Manual Dry Run:</strong><br/>
      1. Build Trie with roots: <code>"cat"</code>, <code>"bat"</code>, <code>"rat"</code>.<br/>
      2. Process <code>"cattle"</code>: Walk Trie <code>c → a → t</code>. Node at <code>'t'</code> has <code>isEnd = true</code> → Return root <strong>"cat"</strong>.<br/>
      3. Process <code>"rattled"</code>: Walk Trie <code>r → a → t</code>. Node at <code>'t'</code> has <code>isEnd = true</code> → Return root <strong>"rat"</strong>.<br/>
      4. Process <code>"battery"</code>: Walk Trie <code>b → a → t</code>. Node at <code>'t'</code> has <code>isEnd = true</code> → Return root <strong>"bat"</strong>.<br/>
      5. Reassemble sentence: <code>"the cat was rat by the bat"</code>.
    </div>
<pre>public String replaceWords(List&lt;String&gt; dictionary, String sentence) {
    TrieNode root = new TrieNode();
    for (String d : dictionary) { // Build Trie
        TrieNode curr = root;
        for (char c : d.toCharArray()) {
            if (curr.children[c - 'a'] == null) curr.children[c - 'a'] = new TrieNode();
            curr = curr.children[c - 'a'];
        }
        curr.isEnd = true;
    }
    StringBuilder res = new StringBuilder();
    for (String word : sentence.split(" ")) {
        if (res.length() > 0) res.append(" ");
        res.append(findShortestRoot(root, word));
    }
    return res.toString();
}

private String findShortestRoot(TrieNode root, String word) {
    TrieNode curr = root;
    StringBuilder prefix = new StringBuilder();
    for (char c : word.toCharArray()) {
        if (curr.children[c - 'a'] == null || curr.isEnd) break;
        prefix.append(c);
        curr = curr.children[c - 'a'];
    }
    return curr.isEnd ? prefix.toString() : word;
}</pre>
    <div style="font-size:0.72rem;color:var(--sub);margin-top:2px">
      <strong>Complexity:</strong> Time: $O(N \cdot L + S)$ (N roots of length L, S = sentence chars) | Space: $O(N \cdot L)$ for Trie.
    </div>
  </div>
</div>

<div class="prob-card">
  <div class="prob-header">
    <div class="prob-title">3. DESIGN ADD AND SEARCH WORDS (WILDCARD '.') — LC 211</div>
    <div class="prob-badge">TRIE + DFS</div>
  </div>
  <div class="prob-body">
    <div style="font-weight:700;color:var(--sub)">Problem Statement:</div>
    <div>Design a data structure supporting <code>addWord(word)</code> and <code>search(word)</code>, where <code>'.'</code> matches any letter.</div>
    <div class="io-box">
      <strong>Input:</strong> addWord("bad"), addWord("dad"), addWord("mad"), search("pad"), search(".ad"), search("b..")<br/>
      <strong>Output:</strong> [false, true, true]
    </div>
    <div class="dry-box">
      <strong>🔍 Step-by-Step Manual Dry Run:</strong><br/>
      1. <code>search(".ad")</code>: First char <code>'.'</code> → DFS branches into all 26 children. 'b' branch checks <code>"ad"</code> → matches <code>"bad"</code>! Returns <strong>true</strong>.<br/>
      2. <code>search("b..")</code>: 'b' branch exists → 2nd char <code>'.'</code> checks 'a' → 3rd char <code>'.'</code> checks 'd' (<code>isEnd = true</code>) → Returns <strong>true</strong>.
    </div>
<pre>public boolean search(String word) {
    return dfsSearch(root, word, 0);
}

private boolean dfsSearch(TrieNode node, String word, int idx) {
    if (node == null) return false;
    if (idx == word.length()) return node.isEnd;
    char ch = word.charAt(idx);
    if (ch == '.') {
        for (TrieNode child : node.children) {
            if (child != null && dfsSearch(child, word, idx + 1)) return true;
        }
        return false;
    }
    return dfsSearch(node.children[ch - 'a'], word, idx + 1);
}</pre>
  </div>
</div>
</div>

<!-- PAGE 3: LC 1268 (SEARCH SUGGESTIONS) & LC 212 (WORD SEARCH II) -->
<div class="page">
<div class="ph">
  <div><h1>TRIE DATA STRUCTURE</h1><div class="sub">Core Patterns — Autocomplete &amp; 2D Grid DFS Pruning</div></div>
  <div style="text-align:right"><div class="pn">PAGE 3 OF 6</div><div class="ptag">LC 1268 · LC 212 · GRID DFS PRUNING</div></div>
</div>

<div class="prob-card">
  <div class="prob-header">
    <div class="prob-title">4. SEARCH SUGGESTIONS SYSTEM — LC 1268</div>
    <div class="prob-badge">AUTOCOMPLETE</div>
  </div>
  <div class="prob-body">
    <div style="font-weight:700;color:var(--sub)">Problem Statement:</div>
    <div>Given products array and searchWord, return top 3 lexicographically smallest product suggestions after each character of searchWord is typed.</div>
    <div class="io-box">
      <strong>Input:</strong> products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"<br/>
      <strong>Output:</strong> [["mobile","moneypot","monitor"], ["mobile","moneypot","monitor"], ["mouse","mousepad"], ["mouse","mousepad"], ["mouse","mousepad"]]
    </div>
<pre>public List&lt;List&lt;String&gt;&gt; suggestedProducts(String[] products, String searchWord) {
    Arrays.sort(products); // Keep lexicographical order
    TrieNode root = new TrieNode();
    for (String p : products) {
        TrieNode curr = root;
        for (char c : p.toCharArray()) {
            if (curr.children[c - 'a'] == null) curr.children[c - 'a'] = new TrieNode();
            curr = curr.children[c - 'a'];
            if (curr.suggestions.size() < 3) curr.suggestions.add(p); // Store top 3
        }
    }
    List&lt;List&lt;String&gt;&gt; res = new ArrayList&lt;&gt;();
    TrieNode curr = root;
    for (char c : searchWord.toCharArray()) {
        if (curr != null) curr = curr.children[c - 'a'];
        res.add(curr == null ? new ArrayList&lt;&gt;() : curr.suggestions);
    }
    return res;
}</pre>
  </div>
</div>

<div class="prob-card">
  <div class="prob-header">
    <div class="prob-title">5. WORD SEARCH II (GRID DFS + TRIE PRUNING) — LC 212</div>
    <div class="prob-badge">HARD · GRID DFS</div>
  </div>
  <div class="prob-body">
    <div style="font-weight:700;color:var(--sub)">Problem Statement:</div>
    <div>Given an $M \times N$ board of characters and a list of words, return all words present in the grid. Words are formed from sequentially adjacent cells.</div>
    <div class="io-box">
      <strong>Input:</strong> board = [['o','a','a','n'],['e','t','a','e'],['i','h','k','r'],['i','f','l','v']], words = ["oath","pea","eat","rain"]<br/>
      <strong>Output:</strong> ["oath", "eat"]
    </div>
    <div class="dry-box">
      <strong>🔍 Step-by-Step Manual Dry Run:</strong><br/>
      1. Build Trie from words: `"oath"`, `"pea"`, `"eat"`, `"rain"`. Store full word string at leaf nodes (<code>node.word = "oath"</code>).<br/>
      2. DFS from cell (0,0)='o': Moves to (0,1)='a' → (1,1)='t' → (2,1)='h'. Matches <code>"oath"</code> in Trie! Add `"oath"` to result and prune (set <code>node.word = null</code> to avoid duplicate adds).
    </div>
<pre>public List&lt;String&gt; findWords(char[][] board, String[] words) {
    TrieNode root = new TrieNode();
    for (String w : words) {
        TrieNode curr = root;
        for (char c : w.toCharArray()) {
            if (curr.children[c - 'a'] == null) curr.children[c - 'a'] = new TrieNode();
            curr = curr.children[c - 'a'];
        }
        curr.word = w; // Store word at leaf
    }
    List&lt;String&gt; res = new ArrayList&lt;&gt;();
    for (int r = 0; r < board.length; r++) {
        for (int c = 0; c < board[0].length; c++) {
            dfs(board, r, c, root, res);
        }
    }
    return res;
}

private void dfs(char[][] board, int r, int c, TrieNode node, List&lt;String&gt; res) {
    char ch = board[r][c];
    if (ch == '#' || node.children[ch - 'a'] == null) return;
    node = node.children[ch - 'a'];
    if (node.word != null) {
        res.add(node.word);
        node.word = null; // Prevent duplicate entries
    }
    board[r][c] = '#'; // Mark visited
    int[] dr = {-1, 1, 0, 0}, dc = {0, 0, -1, 1};
    for (int i = 0; i < 4; i++) {
        int nr = r + dr[i], nc = c + dc[i];
        if (nr >= 0 && nr < board.length && nc >= 0 && nc < board[0].length) {
            dfs(board, nr, nc, node, res);
        }
    }
    board[r][c] = ch; // Backtrack
}</pre>
  </div>
</div>
</div>

<!-- PAGE 4: LC 421 (MAX XOR 31-BIT TRIE) & DECISION TREE -->
<div class="page">
<div class="ph">
  <div><h1>TRIE DATA STRUCTURE</h1><div class="sub">Advanced Patterns — Bitwise Binary Trie &amp; Decision Tree</div></div>
  <div style="text-align:right"><div class="pn">PAGE 4 OF 6</div><div class="ptag">LC 421 · BITWISE XOR · DECISION TREE</div></div>
</div>

<div class="prob-card">
  <div class="prob-header">
    <div class="prob-title">6. MAXIMUM XOR OF TWO NUMBERS IN AN ARRAY — LC 421</div>
    <div class="prob-badge">BITWISE TRIE</div>
  </div>
  <div class="prob-body">
    <div style="font-weight:700;color:var(--sub)">Problem Statement:</div>
    <div>Given an integer array nums, return the maximum result of <code>nums[i] XOR nums[j]</code>.</div>
    <div class="io-box">
      <strong>Input:</strong> nums = [3, 10, 5, 25, 2, 8]<br/>
      <strong>Output:</strong> 28 (5 XOR 25 = 00101^11001 = 11100 = 28)
    </div>
    <div class="dry-box">
      <strong>🔍 Step-by-Step Manual Dry Run:</strong><br/>
      1. Represent each number as a 31-bit binary path in a Binary Trie (children array of size 2: `[0]` and `[1]`).<br/>
      2. For number 25 (`11001`), to maximize XOR, at bit position $b$, we greedily pick the opposite bit `1 - b`. If opposite branch exists, bit $b$ contributes $2^b$ to max XOR!
    </div>
<pre>class BitTrieNode { BitTrieNode[] child = new BitTrieNode[2]; }

public int findMaximumXOR(int[] nums) {
    BitTrieNode root = new BitTrieNode();
    for (int num : nums) { // Insert all 31-bit integers
        BitTrieNode curr = root;
        for (int i = 30; i >= 0; i--) {
            int bit = (num >> i) & 1;
            if (curr.child[bit] == null) curr.child[bit] = new BitTrieNode();
            curr = curr.child[bit];
        }
    }
    int maxXor = 0;
    for (int num : nums) { // Greedily find opposite bit
        BitTrieNode curr = root;
        int currXor = 0;
        for (int i = 30; i >= 0; i--) {
            int bit = (num >> i) & 1;
            int oppBit = 1 - bit;
            if (curr.child[oppBit] != null) {
                currXor |= (1 << i);
                curr = curr.child[oppBit];
            } else {
                curr = curr.child[bit];
            }
        }
        maxXor = Math.max(maxXor, currXor);
    }
    return maxXor;
}</pre>
  </div>
</div>

<div class="box amb" style="margin-top:6px">
  <div class="bh">🌳 TRIE PATTERN DECISION TREE &amp; TRIGGER WORDS</div>
  <div class="bc">
    <table>
      <tr><th>Trigger Keywords in Problem</th><th>Optimal Pattern</th><th>Key Technical Trick</th></tr>
      <tr><td>"Find shortest prefix root", "Replace words"</td><td>Shortest Root Match (LC 648)</td><td>Stop at first node where <code>isEnd == true</code></td></tr>
      <tr><td>"Wildcard matching '.'", "Dictionary search"</td><td>Trie + DFS Backtracking (LC 211)</td><td>Branch into all 26 children on <code>'.'</code></td></tr>
      <tr><td>"Autocomplete", "Top 3 search suggestions"</td><td>Trie + Top-K Bucket (LC 1268)</td><td>Store sorted Top-3 List directly inside TrieNode</td></tr>
      <tr><td>"Find words in 2D grid", "Boggle board"</td><td>Trie + 2D Grid DFS Pruning (LC 212)</td><td>Store full word at leaf; set <code>node.word = null</code> upon match</td></tr>
      <tr><td>"Maximum XOR pair", "Bitwise range XOR"</td><td>31-Bit Binary Trie (LC 421)</td><td>Greedily walk opposite bit branch <code>1 - bit</code></td></tr>
    </table>
  </div>
</div>
</div>

<!-- PAGE 5: PROBLEM LADDER & SUMMARY TABLE -->
<div class="page">
<div class="ph">
  <div><h1>TRIE DATA STRUCTURE</h1><div class="sub">FAANG Problem Ladder &amp; Pattern Summary</div></div>
  <div style="text-align:right"><div class="pn">PAGE 5 OF 6</div><div class="ptag">PROBLEM LADDER · PRACTICE STRATEGY</div></div>
</div>

<div class="box grn">
  <div class="bh">🚀 FAANG TRIE PROBLEM LADDER</div>
  <div class="bc">
    <table>
      <tr><th>#</th><th>Problem</th><th>Difficulty</th><th>Key Concept &amp; Pattern</th><th>Time Complexity</th></tr>
      <tr><td>1</td><td>Implement Trie (Prefix Tree) — LC 208</td><td><span style="color:var(--grn);font-weight:700">Easy</span></td><td>Node class with 26-element TrieNode array</td><td>$O(L)$ per op</td></tr>
      <tr><td>2</td><td>Longest Common Prefix — LC 14</td><td><span style="color:var(--grn);font-weight:700">Easy</span></td><td>Single path traversal until branching factor > 1</td><td>$O(N \cdot L)$</td></tr>
      <tr><td>3</td><td>Replace Words — LC 648</td><td><span style="color:var(--amb);font-weight:700">Medium</span></td><td>Early exit on first prefix node with <code>isEnd = true</code></td><td>$O(S + N \cdot L)$</td></tr>
      <tr><td>4</td><td>Design Add and Search Words — LC 211</td><td><span style="color:var(--amb);font-weight:700">Medium</span></td><td>Recursive DFS search on wildcard character <code>'.'</code></td><td>$O(26^L)$ worst</td></tr>
      <tr><td>5</td><td>Search Suggestions System — LC 1268</td><td><span style="color:var(--amb);font-weight:700">Medium</span></td><td>Store pre-sorted Top-3 product list inside each node</td><td>$O(N \log N + L)$</td></tr>
      <tr><td>6</td><td>Map Sum Pairs — LC 677</td><td><span style="color:var(--amb);font-weight:700">Medium</span></td><td>Store running sum of values at prefix node</td><td>$O(L)$</td></tr>
      <tr><td>7</td><td>Word Search II — LC 212</td><td><span style="color:var(--red);font-weight:700">Hard</span></td><td>Grid DFS with Trie node pruning and path backtrack</td><td>$O(M \cdot N \cdot 3^L)$</td></tr>
      <tr><td>8</td><td>Maximum XOR of Two Numbers — LC 421</td><td><span style="color:var(--amb);font-weight:700">Medium</span></td><td>31-bit Binary Trie with greedy opposite bit navigation</td><td>$O(31 \cdot N)$</td></tr>
      <tr><td>9</td><td>Palindrome Pairs — LC 336</td><td><span style="color:var(--red);font-weight:700">Hard</span></td><td>Reverse word insertion with palindrome suffix checks</td><td>$O(N \cdot L^2)$</td></tr>
      <tr><td>10</td><td>Stream of Characters — LC 1032</td><td><span style="color:var(--red);font-weight:700">Hard</span></td><td>Reverse Trie with stream history buffer</td><td>$O(L)$ per char</td></tr>
    </table>
  </div>
</div>

<div class="box">
  <div class="bh">📊 TRIE TIME &amp; SPACE COMPLEXITY CHEAT SHEET</div>
  <div class="bc">
    <table>
      <tr><th>Operation</th><th>Time Complexity</th><th>Space Complexity</th><th>Why Trie Beats HashMap</th></tr>
      <tr><td>Insert Word</td><td>$O(L)$</td><td>$O(L)$ per new chars</td><td>Creates shared prefix nodes automatically</td></tr>
      <tr><td>Exact Search</td><td>$O(L)$</td><td>$O(1)$ auxiliary</td><td>Direct pointer hops, zero string hashing cost</td></tr>
      <tr><td>Prefix Search</td><td>$O(L)$</td><td>$O(1)$ auxiliary</td><td>HashMap requires $O(N \cdot L)$ key scan!</td></tr>
      <tr><td>Wildcard Search</td><td>$O(26^K \cdot L)$</td><td>$O(L)$ call stack</td><td>DFS explores only valid tree branches</td></tr>
      <tr><td>Max XOR Search</td><td>$O(31) = O(1)$</td><td>$O(31 \cdot N)$</td><td>Greedily evaluates highest bit contribution</td></tr>
    </table>
  </div>
</div>
</div>

<!-- PAGE 6: DRY RUN, MATH PROOFS & CHEAT SHEET -->
<div class="page">
<div class="ph">
  <div><h1>TRIE DATA STRUCTURE</h1><div class="sub">Dry Run Walkthroughs &amp; FAANG Interview Cheat Sheet</div></div>
  <div style="text-align:right"><div class="pn">PAGE 6 OF 6</div><div class="ptag">DRY RUN · INTERVIEW PROOFS · CHEAT SHEET</div></div>
</div>

<div class="g2" style="margin-bottom:8px">
  <div class="box sky">
    <div class="bh">🧠 MEMORY OPTIMIZATION TRICKS</div>
    <div class="bc">
      <ul style="padding-left:12px;font-size:0.75rem">
        <li><strong>Array vs Map:</strong> Use <code>TrieNode[26]</code> for lowercase English. Use <code>Map&lt;Character, TrieNode&gt;</code> for arbitrary Unicode/ASCII.</li>
        <li><strong>Leaf Storage:</strong> Store the full word string directly in leaf nodes (<code>node.word = word</code>) during Word Search II (LC 212) to avoid string reconstruction!</li>
        <li><strong>Node Pruning:</strong> In grid search, decrement child count or set <code>node.word = null</code> upon finding a word to avoid re-searching duplicate words!</li>
      </ul>
    </div>
  </div>

  <div class="box amb">
    <div class="bh">⚡ INTERVIEW EDGE CASES &amp; BUGS</div>
    <div class="bc">
      <ul style="padding-left:12px;font-size:0.75rem">
        <li><strong>Prefix vs Full Word:</strong> Always distinguish between <code>startsWith()</code> and <code>search()</code>. <code>search()</code> MUST check <code>curr.isEnd == true</code>!</li>
        <li><strong>Empty Strings:</strong> Handle empty string insertion gracefully (root node's <code>isEnd</code> becomes <code>true</code>).</li>
        <li><strong>Single Character Words:</strong> Ensure array indexing <code>ch - 'a'</code> handles bounds properly without throwing <code>ArrayIndexOutOfBoundsException</code>.</li>
      </ul>
    </div>
  </div>
</div>

<div class="box red">
  <div class="bh">📌 TOP 5 FAANG TRIE INTERVIEW RULES</div>
  <div class="bc">
    <ol style="padding-left:14px;font-size:0.76rem">
      <li><strong>Always define TrieNode cleanly:</strong> Keep <code>children</code> array/map and <code>isEnd</code> boolean encapsulated inside the class.</li>
      <li><strong>Prefix Search Signal:</strong> If a problem mentions <em>"starts with"</em>, <em>"autocomplete"</em>, or <em>"common prefix"</em>, reach for Trie immediately!</li>
      <li><strong>Combine with DFS for Grids:</strong> For Boggle / Word Search II, build the Trie from dictionary words first, then DFS the 2D grid while walking Trie pointers simultaneously!</li>
      <li><strong>Bitwise XOR Signal:</strong> For <em>"maximum XOR pair"</em>, use a 31-bit Binary Trie!</li>
      <li><strong>Time Complexity Clarity:</strong> In interviews, clearly state L = max word length and N = number of words. Trie operations are $O(L)$, NOT $O(N)$!</li>
    </ol>
  </div>
</div>
</div>

</div>
</div>
</div>
</body>
</html>"""

dst_html = r"F:\dsa\bookfinal\Topic11_Trie.html"
with open(dst_html, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Saved high-density readable HTML to", dst_html)

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
pdf_out = r"F:\dsa\bookfinal\Topic11_Trie.pdf"

if os.path.exists(pdf_out):
    os.remove(pdf_out)

cmd = [chrome_path, '--headless', '--disable-gpu', '--no-pdf-header-footer', f'--print-to-pdf={pdf_out}', dst_html]
subprocess.run(cmd, check=True)

doc = fitz.open(pdf_out)
print("==========================================")
print(f"Generated PDF Page Count: {len(doc)} pages")
print("==========================================")

for i in range(len(doc)):
    page = doc[i]
    text = page.get_text()
    t_clean = text[:70].replace('\n', ' ')
    print(f"Page {i+1} has {len(text)} chars: {t_clean}")

doc.close()

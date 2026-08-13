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
body { font-family: 'Inter', sans-serif; background: #e2e8f0; color: var(--txt); font-size: 10.5px; line-height: 1.3; padding: 12px; }

.page {
  background: white; max-width: 1100px; margin: 0 auto 18px auto;
  padding: 8px 12px; border-radius: 8px;
  box-shadow: 0 6px 20px rgba(0,0,0,0.08);
  page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;
}

.ph { display:flex; justify-content:space-between; align-items:center;
  border-bottom: 2.5px solid var(--pri); padding-bottom: 3px; margin-bottom: 6px; }
.ph h1 { font-size: 1.4rem; font-weight: 900; color: var(--pri); letter-spacing: 0.5px; }
.ph .sub { font-size: 0.78rem; font-weight: 600; color: var(--sub); margin-top: 1px; }
.ph .pn { background: var(--pri); color: white; padding: 2px 10px; border-radius: 12px;
  font-weight: 800; font-size: 0.75rem; text-align: right; }
.ph .ptag { font-size: 0.68rem; color: var(--sub); font-weight: 600; margin-top: 2px; }

.g2 { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
.g3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px; }

.box { border: 1.5px solid var(--pri); border-radius: 5px; overflow: hidden; margin-bottom: 6px; background: white; }
.box.pur { border-color: var(--pur); }
.box.grn { border-color: var(--grn); }
.box.amb { border-color: var(--amb); }
.box.red { border-color: var(--red); }
.box.sky { border-color: var(--sky); }

.bh { background: var(--pri); color: white; padding: 3px 6px; font-weight: 800; font-size: 0.8rem; display: flex; justify-content: space-between; align-items: center; }
.box.pur .bh { background: var(--pur); }
.box.grn .bh { background: var(--grn); }
.box.amb .bh { background: var(--amb); }
.box.red .bh { background: var(--red); }
.box.sky .bh { background: var(--sky); }

.bc { padding: 5px 6px; font-size: 0.76rem; color: var(--txt); }

/* PROW SIDE-BY-SIDE DESIGN */
.prow { border: 1.5px solid var(--pri); border-radius: 5px; overflow: hidden; margin-bottom: 6px; background: white; }
.prow-head { background: var(--pri); color: white; padding: 3px 6px; display: flex; align-items: center; gap: 6px; }
.ptag2 { background: rgba(255,255,255,0.2); padding: 1px 5px; border-radius: 6px; font-size: 0.68rem; font-weight: 800; }
.ptitle { font-weight: 800; font-size: 0.85rem; flex: 1; }
.psub { font-size: 0.72rem; opacity: 0.9; }

.prow-body { display: flex; gap: 6px; padding: 5px; background: #fff; }
.pc { border: 1px solid var(--bdr); border-radius: 4px; padding: 5px 6px; background: #f8fafc; }
.pc-head { font-weight: 800; color: var(--pri); font-size: 0.78rem; margin-bottom: 3px; border-bottom: 1px solid var(--bdr); padding-bottom: 2px; }

.io-box { background: #f1f5f9; border: 1px solid var(--bdr); border-left: 3px solid var(--sec); padding: 3px 5px; margin: 3px 0; border-radius: 3px; font-family: 'Fira Code', monospace; font-size: 0.71rem; }
.dry-box { background: #fefce8; border: 1px solid #fef08a; border-left: 3px solid var(--amb); padding: 3px 5px; margin: 3px 0; border-radius: 3px; font-size: 0.72rem; }

pre { font-family: 'Fira Code', monospace; font-size: 0.7rem; line-height: 1.18; background: #0f172a; color: #f8fafc; padding: 4px 6px; border-radius: 4px; margin: 2px 0; overflow-x: auto; }
table { font-size: 0.72rem; border-collapse: collapse; width: 100%; margin: 2px 0; }
th, td { padding: 3px 5px; border: 1px solid var(--bdr); text-align: left; }
th { background: #f1f5f9; font-weight: 700; color: var(--pri); }

.aha { background: #eff6ff; border-left: 3px solid var(--sec); padding: 4px 6px; margin: 3px 0; font-size: 0.74rem; border-radius: 0 3px 3px 0; }
.aha-t { font-weight: 800; color: var(--sec); margin-bottom: 1px; }

@page { size: A4 portrait; margin: 3mm; }
@media print {
  body { background: white !important; padding: 0 !important; margin: 0 !important; color: black !important; -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
  .top-nav, .toc-sidebar { display: none !important; }
  .app-layout { display: block !important; }
  .page { box-shadow: none !important; border: none !important; margin: 0 !important; padding: 4px 6px !important; width: 100% !important; page-break-after: always !important; break-after: page !important; page-break-inside: avoid !important; break-inside: avoid !important; zoom: 0.85; }
  .page:last-child { page-break-after: avoid !important; break-after: avoid !important; }
  table, tr, td, th { page-break-inside: avoid !important; break-inside: avoid !important; }
  
  /* PRINT FRIENDLY CODE BLOCK BACKGROUND */
  pre {
    background: #f8fafc !important;
    color: #0f172a !important;
    border: 1px solid #cbd5e1 !important;
    font-family: 'Fira Code', monospace !important;
    font-size: 0.7rem !important;
    line-height: 1.18 !important;
    padding: 4px 6px !important;
    white-space: pre-wrap !important;
  }
}
</style>
</head>
<body>

<div class="container">
<div class="app-layout">
<div class="main-content">

<!-- PAGE 1: FOUNDATION & PROBLEMS 1 & 2 -->
<div class="page">
<div class="ph">
  <div><h1>TRIE DATA STRUCTURE</h1><div class="sub">FAANG Master Guide — Foundation &amp; Problems 1-2</div></div>
  <div style="text-align:right"><div class="pn">PAGE 1 OF 6</div><div class="ptag">FOUNDATION · LC 208 · LC 14</div></div>
</div>

<div class="g2" style="margin-bottom:6px">
  <div class="box pur">
    <div class="bh">🎬 THE REAL-WORLD STORY</div>
    <div class="bc">
      Imagine a dictionary search bar. Typing <strong>"app"</strong> instantly suggests <em>"apple"</em>, <em>"application"</em>, <em>"applet"</em>.
      <div class="aha" style="margin-top:2px">
        <div class="aha-t">💡 THE TRIE AHA MOMENT</div>
        Search time is strictly <strong>O(L)</strong> (L = word length), independent of dictionary size N!
      </div>
    </div>
  </div>

  <div class="box sky">
    <div class="bh">⚡ WHY NOT HASH MAP?</div>
    <div class="bc">
      <ul style="padding-left:10px;font-size:0.74rem">
        <li><strong>HashMap:</strong> Exact match $O(L)$ lookup, but CANNOT do prefix search $O(L)$! Finding words starting with `"app"` requires scanning all N keys $O(N \cdot L)$!</li>
        <li><strong>Trie (Prefix Tree):</strong> Both exact lookup AND prefix matching run in <strong>$O(L)$ time</strong>!</li>
      </ul>
    </div>
  </div>
</div>

<div class="prow">
  <div class="prow-head">
    <div class="ptag2">PROBLEM 1</div>
    <div class="ptitle">IMPLEMENT TRIE (PREFIX TREE) — LC 208</div>
    <div class="psub">e.g. Implement Trie</div>
  </div>
  <div class="prow-body">
    <div class="pc" style="flex:1">
      <div class="pc-head">Problem Statement &amp; Mechanics</div>
      <div style="font-size:0.74rem;margin-bottom:2px">
        Design a Trie class supporting <code>insert(word)</code>, <code>search(word)</code>, and <code>startsWith(prefix)</code>.
      </div>
      <div class="io-box">
        <strong>Input:</strong> insert("apple"), search("apple"), search("app"), startsWith("app"), insert("app"), search("app")<br/>
        <strong>Output:</strong> [true, false, true, true]
      </div>
      <div class="dry-box">
        <strong>🔍 Step-by-Step Manual Dry Run:</strong><br/>
        1. <code>insert("apple")</code>: Walk Root $\rightarrow$ 'a' $\rightarrow$ 'p' $\rightarrow$ 'p' $\rightarrow$ 'l' $\rightarrow$ 'e' (set <code>isEnd = true</code> at 'e').<br/>
        2. <code>search("app")</code>: Traverse 'a'$\rightarrow$'p'$\rightarrow$'p'. Node exists, but <code>isEnd == false</code> $\rightarrow$ Return <strong>false</strong>.<br/>
        3. <code>startsWith("app")</code>: Traverse 'a'$\rightarrow$'p'$\rightarrow$'p'. Node exists $\rightarrow$ Return <strong>true</strong>.<br/>
        4. <code>insert("app")</code>: Set <code>isEnd = true</code> at 2nd 'p' $\rightarrow$ <code>search("app")</code> now returns <strong>true</strong>.
      </div>
    </div>
    <div class="pc" style="flex:1.4">
      <div class="pc-head">Template Code — LC 208</div>
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
    </div>
  </div>
</div>

<div class="prow">
  <div class="prow-head">
    <div class="ptag2">PROBLEM 2</div>
    <div class="ptitle">LONGEST COMMON PREFIX — LC 14</div>
    <div class="psub">e.g. Longest Common Prefix</div>
  </div>
  <div class="prow-body">
    <div class="pc" style="flex:1">
      <div class="pc-head">Problem Statement &amp; Mechanics</div>
      <div style="font-size:0.74rem;margin-bottom:2px">
        Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return <code>""</code>.
      </div>
      <div class="io-box">
        <strong>Input:</strong> strs = ["flower", "flow", "flight"]<br/>
        <strong>Output:</strong> "fl"
      </div>
      <div class="dry-box">
        <strong>🔍 Step-by-Step Manual Dry Run:</strong><br/>
        1. Insert all words into Trie.<br/>
        2. Walk down from root. At 'f': only 1 child ('l') $\rightarrow$ add 'f' to prefix.<br/>
        3. At 'l': has 2 children ('o' and 'i') $\rightarrow$ branching factor > 1! Stop traversal.<br/>
        4. Longest common prefix is <strong>"fl"</strong>.
      </div>
    </div>
    <div class="pc" style="flex:1.4">
      <div class="pc-head">Solution Code — LC 14</div>
<pre>public String longestCommonPrefix(String[] strs) {
    if (strs == null || strs.length == 0) return "";
    TrieNode root = new TrieNode();
    for (String s : strs) {
        if (s.isEmpty()) return "";
        TrieNode curr = root;
        for (char c : s.toCharArray()) {
            if (curr.children[c - 'a'] == null) {
                curr.children[c - 'a'] = new TrieNode();
                curr.childCount++;
            }
            curr = curr.children[c - 'a'];
        }
        curr.isEnd = true;
    }
    StringBuilder prefix = new StringBuilder();
    TrieNode curr = root;
    while (curr != null && curr.childCount == 1 && !curr.isEnd) {
        for (int i = 0; i < 26; i++) {
            if (curr.children[i] != null) {
                prefix.append((char)('a' + i));
                curr = curr.children[i];
                break;
            }
        }
    }
    return prefix.toString();
}</pre>
    </div>
  </div>
</div>
</div>

<!-- PAGE 2: PROBLEMS 3 & 4 (LC 648 & LC 211) -->
<div class="page">
<div class="ph">
  <div><h1>TRIE DATA STRUCTURE</h1><div class="sub">Core Patterns — Shortest Root &amp; Wildcard Search</div></div>
  <div style="text-align:right"><div class="pn">PAGE 2 OF 6</div><div class="ptag">LC 648 · LC 211 · PREFIX ROOT MATCH</div></div>
</div>

<div class="prow">
  <div class="prow-head">
    <div class="ptag2">PROBLEM 3</div>
    <div class="ptitle">REPLACE WORDS (SHORTEST ROOT PREFIX REPLACEMENT) — LC 648</div>
    <div class="psub">e.g. Replace Words</div>
  </div>
  <div class="prow-body">
    <div class="pc" style="flex:1">
      <div class="pc-head">Problem Statement &amp; Mechanics</div>
      <div style="font-size:0.74rem;margin-bottom:2px">
        Given a dictionary of root words and a sentence, replace every word in the sentence with the shortest root that matches its prefix. If no root matches, keep original word.
      </div>
      <div class="io-box">
        <strong>Input:</strong> dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"<br/>
        <strong>Output:</strong> "the cat was rat by the bat"
      </div>
      <div class="dry-box">
        <strong>🔍 Step-by-Step Manual Dry Run:</strong><br/>
        1. Build Trie with roots: <code>"cat"</code>, <code>"bat"</code>, <code>"rat"</code>.<br/>
        2. Process <code>"cattle"</code>: Walk Trie <code>c → a → t</code>. Node at <code>'t'</code> has <code>isEnd = true</code> $\rightarrow$ Return root <strong>"cat"</strong>.<br/>
        3. Process <code>"rattled"</code>: Walk Trie <code>r → a → t</code>. Node at <code>'t'</code> has <code>isEnd = true</code> $\rightarrow$ Return root <strong>"rat"</strong>.<br/>
        4. Process <code>"battery"</code>: Walk Trie <code>b → a → t</code>. Node at <code>'t'</code> has <code>isEnd = true</code> $\rightarrow$ Return root <strong>"bat"</strong>.<br/>
        5. Reassembled Result: <code>"the cat was rat by the bat"</code>.
      </div>
    </div>
    <div class="pc" style="flex:1.4">
      <div class="pc-head">Solution Code — LC 648</div>
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
    </div>
  </div>
</div>

<div class="prow">
  <div class="prow-head">
    <div class="ptag2">PROBLEM 4</div>
    <div class="ptitle">DESIGN ADD AND SEARCH WORDS (WILDCARD '.') — LC 211</div>
    <div class="psub">e.g. Design Add and Search Words Data Structure</div>
  </div>
  <div class="prow-body">
    <div class="pc" style="flex:1">
      <div class="pc-head">Problem Statement &amp; Mechanics</div>
      <div style="font-size:0.74rem;margin-bottom:2px">
        Design a data structure supporting <code>addWord(word)</code> and <code>search(word)</code>, where <code>'.'</code> matches any letter.
      </div>
      <div class="io-box">
        <strong>Input:</strong> addWord("bad"), addWord("dad"), addWord("mad"), search("pad"), search(".ad"), search("b..")<br/>
        <strong>Output:</strong> [false, true, true]
      </div>
      <div class="dry-box">
        <strong>🔍 Step-by-Step Manual Dry Run:</strong><br/>
        1. <code>search(".ad")</code>: First char <code>'.'</code> $\rightarrow$ DFS branches into all 26 children. 'b' branch checks <code>"ad"</code> $\rightarrow$ matches <code>"bad"</code>! Returns <strong>true</strong>.<br/>
        2. <code>search("b..")</code>: 'b' branch exists $\rightarrow$ 2nd char <code>'.'</code> checks 'a' $\rightarrow$ 3rd char <code>'.'</code> checks 'd' (<code>isEnd = true</code>) $\rightarrow$ Returns <strong>true</strong>.
      </div>
    </div>
    <div class="pc" style="flex:1.4">
      <div class="pc-head">Solution Code — LC 211</div>
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
</div>

<!-- PAGE 3: PROBLEMS 5 & 6 (LC 1268 & LC 677) -->
<div class="page">
<div class="ph">
  <div><h1>TRIE DATA STRUCTURE</h1><div class="sub">Core Patterns — Autocomplete &amp; Map Sum Pairs</div></div>
  <div style="text-align:right"><div class="pn">PAGE 3 OF 6</div><div class="ptag">LC 1268 · LC 677 · PREFIX MAP</div></div>
</div>

<div class="prow">
  <div class="prow-head">
    <div class="ptag2">PROBLEM 5</div>
    <div class="ptitle">SEARCH SUGGESTIONS SYSTEM (AUTOCOMPLETE) — LC 1268</div>
    <div class="psub">e.g. Search Suggestions System</div>
  </div>
  <div class="prow-body">
    <div class="pc" style="flex:1">
      <div class="pc-head">Problem Statement &amp; Mechanics</div>
      <div style="font-size:0.74rem;margin-bottom:2px">
        Given products array and searchWord, return top 3 lexicographically smallest product suggestions after each character of searchWord is typed.
      </div>
      <div class="io-box">
        <strong>Input:</strong> products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"<br/>
        <strong>Output:</strong> [["mobile","moneypot","monitor"], ["mobile","moneypot","monitor"], ["mouse","mousepad"], ["mouse","mousepad"], ["mouse","mousepad"]]
      </div>
      <div class="dry-box">
        <strong>🔍 Step-by-Step Manual Dry Run:</strong><br/>
        1. Sort products lexicographically.<br/>
        2. Insert into Trie. Each TrieNode holds a list <code>suggestions</code> capping at size 3.<br/>
        3. Type 'm' $\rightarrow$ returns ["mobile","moneypot","monitor"]. Type 'm' 'o' $\rightarrow$ returns ["mobile","moneypot","monitor"]. Type 'm' 'o' 'u' $\rightarrow$ returns ["mouse","mousepad"].
      </div>
    </div>
    <div class="pc" style="flex:1.4">
      <div class="pc-head">Solution Code — LC 1268</div>
<pre>public List&lt;List&lt;String&gt;&gt; suggestedProducts(String[] products, String searchWord) {
    Arrays.sort(products);
    TrieNode root = new TrieNode();
    for (String p : products) {
        TrieNode curr = root;
        for (char c : p.toCharArray()) {
            if (curr.children[c - 'a'] == null) curr.children[c - 'a'] = new TrieNode();
            curr = curr.children[c - 'a'];
            if (curr.suggestions.size() < 3) curr.suggestions.add(p);
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
</div>

<div class="prow">
  <div class="prow-head">
    <div class="ptag2">PROBLEM 6</div>
    <div class="ptitle">MAP SUM PAIRS — LC 677</div>
    <div class="psub">e.g. Map Sum Pairs</div>
  </div>
  <div class="prow-body">
    <div class="pc" style="flex:1">
      <div class="pc-head">Problem Statement &amp; Mechanics</div>
      <div style="font-size:0.74rem;margin-bottom:2px">
        Design a MapSum class with <code>insert(key, val)</code> and <code>sum(prefix)</code>. <code>sum(prefix)</code> returns sum of all key values that start with the prefix.
      </div>
      <div class="io-box">
        <strong>Input:</strong> insert("apple", 3), sum("ap"), insert("app", 2), sum("ap")<br/>
        <strong>Output:</strong> [3, 5]
      </div>
      <div class="dry-box">
        <strong>🔍 Step-by-Step Manual Dry Run:</strong><br/>
        1. Store HashMap to track previous key values for delta calculation <code>delta = val - map.getOrDefault(key, 0)</code>.<br/>
        2. Walk Trie along key path and add <code>delta</code> to <code>node.score</code> at every character node.<br/>
        3. <code>sum("ap")</code> $\rightarrow$ walk Trie to 'p' node $\rightarrow$ return <code>node.score</code> in $O(L)$ time!
      </div>
    </div>
    <div class="pc" style="flex:1.4">
      <div class="pc-head">Solution Code — LC 677</div>
<pre>class MapSum {
    private class TrieNode {
        TrieNode[] children = new TrieNode[26];
        int score = 0;
    }
    private final TrieNode root = new TrieNode();
    private final Map&lt;String, Integer&gt; map = new HashMap&lt;&gt;();

    public void insert(String key, int val) {
        int delta = val - map.getOrDefault(key, 0);
        map.put(key, val);
        TrieNode curr = root;
        for (char c : key.toCharArray()) {
            if (curr.children[c - 'a'] == null) curr.children[c - 'a'] = new TrieNode();
            curr = curr.children[c - 'a'];
            curr.score += delta;
        }
    }

    public int sum(String prefix) {
        TrieNode curr = root;
        for (char c : prefix.toCharArray()) {
            curr = curr.children[c - 'a'];
            if (curr == null) return 0;
        }
        return curr.score;
    }
}</pre>
    </div>
  </div>
</div>
</div>

<!-- PAGE 4: PROBLEMS 7 & 8 (LC 212 & LC 421) -->
<div class="page">
<div class="ph">
  <div><h1>TRIE DATA STRUCTURE</h1><div class="sub">Advanced Patterns — Grid DFS Pruning &amp; Bitwise Binary Trie</div></div>
  <div style="text-align:right"><div class="pn">PAGE 4 OF 6</div><div class="ptag">LC 212 · LC 421 · GRID DFS · BITWISE XOR</div></div>
</div>

<div class="prow">
  <div class="prow-head">
    <div class="ptag2">PROBLEM 7</div>
    <div class="ptitle">WORD SEARCH II (GRID DFS + TRIE PRUNING) — LC 212</div>
    <div class="psub">e.g. Word Search II</div>
  </div>
  <div class="prow-body">
    <div class="pc" style="flex:1">
      <div class="pc-head">Problem Statement &amp; Mechanics</div>
      <div style="font-size:0.74rem;margin-bottom:2px">
        Given an $M \times N$ board of characters and a list of words, return all words present in the grid. Words are formed from sequentially adjacent cells.
      </div>
      <div class="io-box">
        <strong>Input:</strong> board = [['o','a','a','n'],['e','t','a','e'],['i','h','k','r'],['i','f','l','v']], words = ["oath","pea","eat","rain"]<br/>
        <strong>Output:</strong> ["oath", "eat"]
      </div>
      <div class="dry-box">
        <strong>🔍 Step-by-Step Manual Dry Run:</strong><br/>
        1. Build Trie from words: `"oath"`, `"pea"`, `"eat"`, `"rain"`. Store full word string at leaf nodes (<code>node.word = "oath"</code>).<br/>
        2. DFS from cell (0,0)='o': Moves to (0,1)='a' $\rightarrow$ (1,1)='t' $\rightarrow$ (2,1)='h'. Matches <code>"oath"</code> in Trie! Add `"oath"` to result and prune (set <code>node.word = null</code> to avoid duplicate adds).
      </div>
    </div>
    <div class="pc" style="flex:1.4">
      <div class="pc-head">Solution Code — LC 212</div>
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
        node.word = null; // Prevent duplicates
    }
    board[r][c] = '#'; // Visited
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

<div class="prow">
  <div class="prow-head">
    <div class="ptag2">PROBLEM 8</div>
    <div class="ptitle">MAXIMUM XOR OF TWO NUMBERS IN AN ARRAY — LC 421</div>
    <div class="psub">e.g. Maximum XOR Pair</div>
  </div>
  <div class="prow-body">
    <div class="pc" style="flex:1">
      <div class="pc-head">Problem Statement &amp; Mechanics</div>
      <div style="font-size:0.74rem;margin-bottom:2px">
        Given an integer array nums, return the maximum result of <code>nums[i] XOR nums[j]</code>.
      </div>
      <div class="io-box">
        <strong>Input:</strong> nums = [3, 10, 5, 25, 2, 8]<br/>
        <strong>Output:</strong> 28 (5 XOR 25 = 00101^11001 = 11100 = 28)
      </div>
      <div class="dry-box">
        <strong>🔍 Step-by-Step Manual Dry Run:</strong><br/>
        1. Represent each number as a 31-bit binary path in a Binary Trie (children array of size 2: <code>[0]</code> and <code>[1]</code>).<br/>
        2. For number 25 (<code>11001</code>), to maximize XOR, at bit position $b$, we greedily pick the opposite bit <code>1 - b</code>. If opposite branch exists, bit $b$ contributes $2^b$ to max XOR!
      </div>
    </div>
    <div class="pc" style="flex:1.4">
      <div class="pc-head">Solution Code — LC 421</div>
<pre>class BitTrieNode { BitTrieNode[] child = new BitTrieNode[2]; }

public int findMaximumXOR(int[] nums) {
    BitTrieNode root = new BitTrieNode();
    for (int num : nums) { // Insert 31-bit binary
        BitTrieNode curr = root;
        for (int i = 30; i >= 0; i--) {
            int bit = (num >> i) & 1;
            if (curr.child[bit] == null) curr.child[bit] = new BitTrieNode();
            curr = curr.child[bit];
        }
    }
    int maxXor = 0;
    for (int num : nums) { // Greedily pick opposite bit
        BitTrieNode curr = root;
        int currXor = 0;
        for (int i = 30; i >= 0; i--) {
            int bit = (num >> i) & 1;
            int oppBit = 1 - bit;
            if (curr.child[oppBit] != null) {
                currXor |= (1 << i);
                curr = curr.child[oppBit];
            } else curr = curr.child[bit];
        }
        maxXor = Math.max(maxXor, currXor);
    }
    return maxXor;
}</pre>
    </div>
  </div>
</div>
</div>

<!-- PAGE 5: PROBLEMS 9 & 10 (LC 336 & LC 1032) -->
<div class="page">
<div class="ph">
  <div><h1>TRIE DATA STRUCTURE</h1><div class="sub">Advanced Patterns — Palindrome Pairs &amp; Stream Trie</div></div>
  <div style="text-align:right"><div class="pn">PAGE 5 OF 6</div><div class="ptag">LC 336 · LC 1032 · REVERSE TRIE</div></div>
</div>

<div class="prow">
  <div class="prow-head">
    <div class="ptag2">PROBLEM 9</div>
    <div class="ptitle">PALINDROME PAIRS — LC 336</div>
    <div class="psub">e.g. Palindrome Pairs</div>
  </div>
  <div class="prow-body">
    <div class="pc" style="flex:1">
      <div class="pc-head">Problem Statement &amp; Mechanics</div>
      <div style="font-size:0.74rem;margin-bottom:2px">
        Given a list of unique words, return all pairs of distinct indices <code>(i, j)</code> such that concatenation <code>words[i] + words[j]</code> is a palindrome.
      </div>
      <div class="io-box">
        <strong>Input:</strong> words = ["abcd","dcba","lls","s","sssll"]<br/>
        <strong>Output:</strong> [[0,1],[1,0],[3,2],[2,4]]
      </div>
      <div class="dry-box">
        <strong>🔍 Step-by-Step Manual Dry Run:</strong><br/>
        1. Insert reversed words into Trie. Store index of word at leaf node.<br/>
        2. For word <code>"abcd"</code>: Search forward in Trie. Traverses <code>'a'→'b'→'c'→'d'</code>, matches reversed <code>"dcba"</code> (index 1) $\rightarrow$ Pair <code>(0, 1)</code> is valid palindrome!<br/>
        3. Check palindrome prefix/suffix splits to find asymmetric pairs like <code>"lls" + "s" = "llss"</code> (not pal) vs <code>"s" + "lls" = "slls"</code> (pal!).
      </div>
    </div>
    <div class="pc" style="flex:1.4">
      <div class="pc-head">Solution Code — LC 336</div>
<pre>public List&lt;List&lt;Integer&gt;&gt; palindromePairs(String[] words) {
    List&lt;List&lt;Integer&gt;&gt; res = new ArrayList&lt;&gt;();
    Map&lt;String, Integer&gt; map = new HashMap&lt;&gt;();
    for (int i = 0; i < words.length; i++) map.put(words[i], i);
    for (int i = 0; i < words.length; i++) {
        String w = words[i];
        for (int j = 0; j <= w.length(); j++) {
            String str1 = w.substring(0, j);
            String str2 = w.substring(j);
            if (isPal(str1)) {
                String revStr2 = new StringBuilder(str2).reverse().toString();
                if (map.containsKey(revStr2) && map.get(revStr2) != i) {
                    res.add(Arrays.asList(map.get(revStr2), i));
                }
            }
            if (isPal(str2) && str2.length() > 0) {
                String revStr1 = new StringBuilder(str1).reverse().toString();
                if (map.containsKey(revStr1) && map.get(revStr1) != i) {
                    res.add(Arrays.asList(i, map.get(revStr1)));
                }
            }
        }
    }
    return res;
}
private boolean isPal(String s) {
    int l = 0, r = s.length() - 1;
    while (l < r) if (s.charAt(l++) != s.charAt(r--)) return false;
    return true;
}</pre>
    </div>
  </div>
</div>

<div class="prow">
  <div class="prow-head">
    <div class="ptag2">PROBLEM 10</div>
    <div class="ptitle">STREAM OF CHARACTERS — LC 1032</div>
    <div class="psub">e.g. Stream of Characters</div>
  </div>
  <div class="prow-body">
    <div class="pc" style="flex:1">
      <div class="pc-head">Problem Statement &amp; Mechanics</div>
      <div style="font-size:0.74rem;margin-bottom:2px">
        Design a StreamChecker class that receives a stream of characters one by one, and returns true if any suffix of the stream matches a word in the dictionary.
      </div>
      <div class="io-box">
        <strong>Input:</strong> words = ["cd", "f", "kl"]. Stream queries: 'a', 'b', 'c', 'd', 'e', 'f'<br/>
        <strong>Output:</strong> [false, false, false, true, false, true]
      </div>
      <div class="dry-box">
        <strong>🔍 Step-by-Step Manual Dry Run:</strong><br/>
        1. Insert all words in REVERSE order into Trie: `"cd"` $\rightarrow$ insert `"dc"`. `"f"` $\rightarrow$ insert `"f"`.<br/>
        2. Keep a StringBuilder stream history. When query char arrives, append to stream history.<br/>
        3. Walk Trie BACKWARDS from newest stream char. Query 'd' after 'c' $\rightarrow$ stream history `"cd"`. Search backwards: 'd' $\rightarrow$ 'c' (matches <code>isEnd = true</code>) $\rightarrow$ Return <strong>true</strong>!
      </div>
    </div>
    <div class="pc" style="flex:1.4">
      <div class="pc-head">Solution Code — LC 1032</div>
<pre>class StreamChecker {
    private class TrieNode {
        TrieNode[] children = new TrieNode[26];
        boolean isEnd = false;
    }
    private final TrieNode root = new TrieNode();
    private final StringBuilder stream = new StringBuilder();

    public StreamChecker(String[] words) {
        for (String w : words) { // Insert reversed
            TrieNode curr = root;
            for (int i = w.length() - 1; i >= 0; i--) {
                char c = w.charAt(i);
                if (curr.children[c - 'a'] == null) curr.children[c - 'a'] = new TrieNode();
                curr = curr.children[c - 'a'];
            }
            curr.isEnd = true;
        }
    }

    public boolean query(char letter) {
        stream.append(letter);
        TrieNode curr = root;
        for (int i = stream.length() - 1; i >= 0; i--) {
            curr = curr.children[stream.charAt(i) - 'a'];
            if (curr == null) return false;
            if (curr.isEnd) return true;
        }
        return false;
    }
}</pre>
    </div>
  </div>
</div>
</div>

<!-- PAGE 6: DECISION TREE, LADDER SUMMARY & CHEAT SHEET -->
<div class="page">
<div class="ph">
  <div><h1>TRIE DATA STRUCTURE</h1><div class="sub">Pattern Decision Tree, Summary &amp; FAANG Cheat Sheet</div></div>
  <div style="text-align:right"><div class="pn">PAGE 6 OF 6</div><div class="ptag">DECISION TREE · SUMMARY · CHEAT SHEET</div></div>
</div>

<div class="box amb" style="margin-bottom:6px">
  <div class="bh">🌳 TRIE PATTERN DECISION TREE &amp; TRIGGER WORDS</div>
  <div class="bc">
    <table>
      <tr><th>Trigger Keywords in Problem</th><th>Optimal Pattern</th><th>Key Technical Trick</th></tr>
      <tr><td>"Find shortest prefix root", "Replace words"</td><td>Shortest Root Match (LC 648)</td><td>Stop at first node where <code>isEnd == true</code></td></tr>
      <tr><td>"Wildcard matching '.'", "Dictionary search"</td><td>Trie + DFS Backtracking (LC 211)</td><td>Branch into all 26 children on <code>'.'</code></td></tr>
      <tr><td>"Autocomplete", "Top 3 search suggestions"</td><td>Trie + Top-K Bucket (LC 1268)</td><td>Store sorted Top-3 List directly inside TrieNode</td></tr>
      <tr><td>"Find words in 2D grid", "Boggle board"</td><td>Trie + 2D Grid DFS Pruning (LC 212)</td><td>Store full word at leaf; set <code>node.word = null</code> upon match</td></tr>
      <tr><td>"Maximum XOR pair", "Bitwise range XOR"</td><td>31-Bit Binary Trie (LC 421)</td><td>Greedily walk opposite bit branch <code>1 - bit</code></td></tr>
      <tr><td>"Stream of chars", "Check matching suffix"</td><td>Reverse Trie Stream (LC 1032)</td><td>Insert words reversed; search stream backwards</td></tr>
    </table>
  </div>
</div>

<div class="box grn" style="margin-bottom:6px">
  <div class="bh">🚀 COMPLETE ALL 10 PROBLEMS SUMMARY</div>
  <div class="bc">
    <table>
      <tr><th>#</th><th>Problem</th><th>Difficulty</th><th>Key Technique</th><th>Time Complexity</th></tr>
      <tr><td>1</td><td>Implement Trie — LC 208</td><td><span style="color:var(--grn);font-weight:700">Easy</span></td><td>26-element array TrieNode pointer tree</td><td>$O(L)$</td></tr>
      <tr><td>2</td><td>Longest Common Prefix — LC 14</td><td><span style="color:var(--grn);font-weight:700">Easy</span></td><td>Traverse single branch until childCount > 1</td><td>$O(N \cdot L)$</td></tr>
      <tr><td>3</td><td>Replace Words — LC 648</td><td><span style="color:var(--amb);font-weight:700">Medium</span></td><td>Early exit on first prefix node with <code>isEnd = true</code></td><td>$O(S + N \cdot L)$</td></tr>
      <tr><td>4</td><td>Design Add/Search Words — LC 211</td><td><span style="color:var(--amb);font-weight:700">Medium</span></td><td>Recursive DFS search on wildcard character <code>'.'</code></td><td>$O(26^L)$ worst</td></tr>
      <tr><td>5</td><td>Search Suggestions — LC 1268</td><td><span style="color:var(--amb);font-weight:700">Medium</span></td><td>Store pre-sorted Top-3 product list inside each node</td><td>$O(N \log N + L)$</td></tr>
      <tr><td>6</td><td>Map Sum Pairs — LC 677</td><td><span style="color:var(--amb);font-weight:700">Medium</span></td><td>Maintain delta score sum at every prefix node</td><td>$O(L)$</td></tr>
      <tr><td>7</td><td>Word Search II — LC 212</td><td><span style="color:var(--red);font-weight:700">Hard</span></td><td>Grid DFS with Trie node pruning and path backtrack</td><td>$O(M \cdot N \cdot 3^L)$</td></tr>
      <tr><td>8</td><td>Maximum XOR Pair — LC 421</td><td><span style="color:var(--amb);font-weight:700">Medium</span></td><td>31-bit Binary Trie with greedy opposite bit navigation</td><td>$O(31 \cdot N)$</td></tr>
      <tr><td>9</td><td>Palindrome Pairs — LC 336</td><td><span style="color:var(--red);font-weight:700">Hard</span></td><td>Reverse word insertion with palindrome split checks</td><td>$O(N \cdot L^2)$</td></tr>
      <tr><td>10</td><td>Stream of Characters — LC 1032</td><td><span style="color:var(--red);font-weight:700">Hard</span></td><td>Reverse Trie with stream history buffer</td><td>$O(L)$ per char</td></tr>
    </table>
  </div>
</div>

<div class="box red">
  <div class="bh">📌 TOP 5 FAANG TRIE INTERVIEW RULES</div>
  <div class="bc">
    <ol style="padding-left:14px;font-size:0.74rem">
      <li><strong>Prefix Search Signal:</strong> If a problem mentions <em>"starts with"</em>, <em>"autocomplete"</em>, or <em>"common prefix"</em>, reach for Trie immediately!</li>
      <li><strong>Combine with DFS for Grids:</strong> For Boggle / Word Search II, build Trie from dictionary words first, then DFS grid while walking Trie pointers!</li>
      <li><strong>Bitwise XOR Signal:</strong> For <em>"maximum XOR pair"</em>, use a 31-bit Binary Trie!</li>
      <li><strong>Reverse Storage:</strong> For suffix matching or stream queries, store words in REVERSE order in the Trie!</li>
      <li><strong>Time Complexity Clarity:</strong> In interviews, state L = max word length and N = number of words. Trie ops are $O(L)$, NOT $O(N)$!</li>
    </ol>
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

print("Saved Ultimate 10-Problem Trie HTML to", dst_html)

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

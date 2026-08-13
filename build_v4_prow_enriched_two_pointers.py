import os, sys, subprocess, fitz

sys.stdout.reconfigure(encoding='utf-8')

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Topic 03: Two Pointers Masterclass — FAANG Edition</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Fira+Code:wght@400;500;600&display=swap" rel="stylesheet"/>
<style>
:root {
  --pri: #1e3a8a; --sec: #2563eb; --grn: #059669; --red: #dc2626;
  --pur: #7c3aed; --org: #ea580c; --amb: #d97706; --sky: #0284c7;
  --txt: #0f172a; --sub: #475569; --bdr: #cbd5e1; --bg: #f8fafc;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: 'Inter', sans-serif; background: #e2e8f0; color: var(--txt); font-size: 10.5px; line-height: 1.32; padding: 15px; }

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

/* PROW ORIGINAL V4 STYLING */
.prow { border: 1.5px solid var(--pri); border-radius: 6px; overflow: hidden; margin-bottom: 8px; background: white; }
.prow-head { background: var(--pri); color: white; padding: 4px 8px; display: flex; align-items: center; gap: 8px; }
.ptag2 { background: rgba(255,255,255,0.2); padding: 2px 6px; border-radius: 8px; font-size: 0.7rem; font-weight: 800; }
.ptitle { font-weight: 800; font-size: 0.88rem; flex: 1; }
.psub { font-size: 0.75rem; opacity: 0.9; }

.prow-body { display: flex; gap: 8px; padding: 6px; background: #fff; }
.pc { border: 1px solid var(--bdr); border-radius: 5px; padding: 6px 8px; background: #f8fafc; }
.pc-head { font-weight: 800; color: var(--pri); font-size: 0.8rem; margin-bottom: 4px; border-bottom: 1px solid var(--bdr); padding-bottom: 3px; }

.io-box { background: #f1f5f9; border: 1px solid var(--bdr); border-left: 3.5px solid var(--sec); padding: 4px 6px; margin: 4px 0; border-radius: 4px; font-family: 'Fira Code', monospace; font-size: 0.73rem; }
.dry-box { background: #fefce8; border: 1px solid #fef08a; border-left: 3.5px solid var(--amb); padding: 4px 6px; margin: 4px 0; border-radius: 4px; font-size: 0.74rem; }

pre { font-family: 'Fira Code', monospace; font-size: 0.72rem; line-height: 1.22; background: #0f172a; color: #f8fafc; padding: 6px 8px; border-radius: 4px; margin: 2px 0; overflow-x: auto; }
table { font-size: 0.74rem; border-collapse: collapse; width: 100%; margin: 2px 0; }
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

<!-- PAGE 1: FOUNDATION & SIDE-BY-SIDE TEMPLATES -->
<div class="page">
<div class="ph">
  <div><h1>TWO POINTERS PATTERN</h1><div class="sub">FAANG Master Guide — Java Edition &amp; Templates</div></div>
  <div style="text-align:right"><div class="pn">PAGE 1 OF 5</div><div class="ptag">FOUNDATION · TEMPLATES · COMPLEXITY</div></div>
</div>

<div class="g3" style="margin-bottom:8px">
  <div class="box pur">
    <div class="bh">🎬 THE REAL-WORLD STORY</div>
    <div class="bc">
      Imagine two people walking from opposite ends of a hallway looking for a pair of numbers that add up to a target.
      <div class="aha" style="margin-top:4px">
        <div class="aha-t">💡 THE TWO POINTERS AHA MOMENT</div>
        If array is sorted: <code>arr[left] + arr[right]</code> tells us which pointer to move! Sum too small $\rightarrow$ <code>left++</code>. Sum too large $\rightarrow$ <code>right--</code>. Replaces $O(N^2)$ loops with <strong>$O(N)$ single pass</strong>!
      </div>
    </div>
  </div>

  <div class="box">
    <div class="bh">🤔 WHY NOT NESTED LOOPS?</div>
    <div class="bc">
      <ul style="padding-left:12px;font-size:0.75rem">
        <li><strong>Nested Loops $O(N^2)$:</strong> Checks every pair $(i, j)$. For $N=100,000$, requires 10 billion ops $\rightarrow$ TLE!</li>
        <li><strong>Two Pointers $O(N)$:</strong> Moves inward deterministically. Steps $\le N$. Runs in 5ms!</li>
        <li><strong>Space $O(1)$:</strong> Reuses array pointers with 0 extra memory allocation.</li>
      </ul>
    </div>
  </div>

  <div class="box sky">
    <div class="bh">📌 2 MAIN POINTER VARIATIONS</div>
    <div class="bc">
      <strong>1. Opposite Direction (Converging):</strong>
<pre>left -> [ 1, 2, 4, 6, 8, 11 ] <- right
sum = 1+11 = 12 > target 10 -> right--
sum = 1+8  = 9  < target 10 -> left++</pre>
      <strong>2. Same Direction (Fast &amp; Slow):</strong>
<pre>[ slow, fast -> ] (In-place array modify)</pre>
    </div>
  </div>
</div>

<div class="g2">
  <div class="box">
    <div class="bh">1. TEMPLATE A: OPPOSITE DIRECTION (CONVERGING)</div>
    <div class="bc">
<pre>public int[] twoSumSorted(int[] nums, int target) {
    int left = 0, right = nums.length - 1;
    while (left < right) {
        int sum = nums[left] + nums[right];
        if (sum == target) return new int[]{left + 1, right + 1};
        else if (sum < target) left++;  // Needs larger value
        else right--;                   // Needs smaller value
    }
    return new int[0];
}</pre>
    </div>
  </div>

  <div class="box pur">
    <div class="bh">2. TEMPLATE B: SAME DIRECTION (FAST &amp; SLOW)</div>
    <div class="bc">
<pre>public int removeDuplicates(int[] nums) {
    if (nums.length == 0) return 0;
    int slow = 0;
    for (int fast = 1; fast < nums.length; fast++) {
        if (nums[fast] != nums[slow]) {
            slow++;
            nums[slow] = nums[fast]; // Overwrite in-place
        }
    }
    return slow + 1; // Unique length
}</pre>
    </div>
  </div>
</div>
</div>

<!-- PAGE 2: CORE PATTERNS (VALID PALINDROME & TWO SUM II & 3SUM) -->
<div class="page">
<div class="ph">
  <div><h1>TWO POINTERS PATTERN</h1><div class="sub">Core Patterns — Valid Palindrome &amp; 3Sum</div></div>
  <div style="text-align:right"><div class="pn">PAGE 2 OF 5</div><div class="ptag">LC 125 · LC 15 · OPPOSITE POINTERS</div></div>
</div>

<div class="prow">
  <div class="prow-head">
    <div class="ptag2">PATTERN 1</div>
    <div class="ptitle">VALID PALINDROME (LC 125)</div>
    <div class="psub">e.g. Valid Palindrome</div>
  </div>
  <div class="prow-body">
    <div class="pc" style="flex:1">
      <div class="pc-head">Problem Statement &amp; Mechanics</div>
      <div style="font-size:0.76rem;margin-bottom:4px">
        Check if a string is a palindrome after converting all uppercase letters to lowercase and removing non-alphanumeric characters.
      </div>
      <div class="io-box">
        <strong>Input:</strong> s = "A man, a plan, a canal: Panama"<br/>
        <strong>Output:</strong> true ("amanaplanacanalpanama" is palindrome)
      </div>
      <div class="dry-box">
        <strong>🔍 Step-by-Step Manual Dry Run:</strong><br/>
        1. Pointers <code>left=0 ('A')</code>, <code>right=30 ('a')</code>. Lowercase matches ('a' == 'a') $\rightarrow$ <code>left++</code>, <code>right--</code>.<br/>
        2. Skip spaces/punctuation using <code>Character.isLetterOrDigit()</code>.<br/>
        3. All corresponding characters match $\rightarrow$ Return <strong>true</strong>.
      </div>
    </div>
    <div class="pc" style="flex:1.4">
      <div class="pc-head">Template — LC 125</div>
<pre>public boolean isPalindrome(String s) {
    int l = 0, r = s.length() - 1;
    while (l < r) {
        while (l < r && !Character.isLetterOrDigit(s.charAt(l))) l++;
        while (l < r && !Character.isLetterOrDigit(s.charAt(r))) r--;
        if (Character.toLowerCase(s.charAt(l)) != Character.toLowerCase(s.charAt(r))) return false;
        l++; r--;
    }
    return true;
}</pre>
    </div>
  </div>
</div>

<div class="prow">
  <div class="prow-head">
    <div class="ptag2">PATTERN 2</div>
    <div class="ptitle">3SUM ZERO SUM TRIPLETS (LC 15)</div>
    <div class="psub">e.g. 3Sum</div>
  </div>
  <div class="prow-body">
    <div class="pc" style="flex:1">
      <div class="pc-head">Problem Statement &amp; Mechanics</div>
      <div style="font-size:0.76rem;margin-bottom:4px">
        Given an integer array nums, return all unique triplets <code>[nums[i], nums[j], nums[k]]</code> such that <code>nums[i] + nums[j] + nums[k] == 0</code>.
      </div>
      <div class="io-box">
        <strong>Input:</strong> nums = [-1, 0, 1, 2, -1, -4]<br/>
        <strong>Output:</strong> [[-1, -1, 2], [-1, 0, 1]]
      </div>
      <div class="dry-box">
        <strong>🔍 Step-by-Step Manual Dry Run:</strong><br/>
        1. Sort array: <code>[-4, -1, -1, 0, 1, 2]</code>.<br/>
        2. Fix <code>i=1 (-1)</code>: Target pair sum = +1. <code>l=2(-1), r=5(2)</code>: sum = 1 == target! Found <code>[-1, -1, 2]</code>. Skip duplicates!<br/>
        3. <code>l=3(0), r=4(1)</code>: sum = 1 == target! Found <code>[-1, 0, 1]</code>.
      </div>
    </div>
    <div class="pc" style="flex:1.4">
      <div class="pc-head">Template — LC 15</div>
<pre>public List&lt;List&lt;Integer&gt;&gt; threeSum(int[] nums) {
    Arrays.sort(nums);
    List&lt;List&lt;Integer&gt;&gt; res = new ArrayList&lt;&gt;();
    for (int i = 0; i < nums.length - 2; i++) {
        if (i > 0 && nums[i] == nums[i - 1]) continue; // Skip duplicate i
        int l = i + 1, r = nums.length - 1, target = -nums[i];
        while (l < r) {
            int sum = nums[l] + nums[r];
            if (sum == target) {
                res.add(Arrays.asList(nums[i], nums[l], nums[r]));
                while (l < r && nums[l] == nums[l + 1]) l++; // Skip dups
                while (l < r && nums[r] == nums[r - 1]) r--;
                l++; r--;
            } else if (sum < target) l++;
            else r--;
        }
    }
    return res;
}</pre>
    </div>
  </div>
</div>
</div>

<!-- PAGE 3: CONTAINER WITH MOST WATER & TRAPPING RAIN WATER -->
<div class="page">
<div class="ph">
  <div><h1>TWO POINTERS PATTERN</h1><div class="sub">Core Patterns — Boundary Water Containers</div></div>
  <div style="text-align:right"><div class="pn">PAGE 3 OF 5</div><div class="ptag">LC 11 · LC 42 · GREEDY BOUNDARY</div></div>
</div>

<div class="prow">
  <div class="prow-head">
    <div class="ptag2">PATTERN 3</div>
    <div class="ptitle">CONTAINER WITH MOST WATER (LC 11)</div>
    <div class="psub">e.g. Container With Most Water</div>
  </div>
  <div class="prow-body">
    <div class="pc" style="flex:1">
      <div class="pc-head">Problem Statement &amp; Mechanics</div>
      <div style="font-size:0.76rem;margin-bottom:4px">
        Given n vertical lines, find two lines that together with x-axis form a container containing the most water.
      </div>
      <div class="io-box">
        <strong>Input:</strong> height = [1,8,6,2,5,4,8,3,7]<br/>
        <strong>Output:</strong> 49 (Index 1 (h=8) &amp; Index 8 (h=7): width=7, minH=7 $\rightarrow$ Area = 49)
      </div>
      <div class="dry-box">
        <strong>🔍 Step-by-Step Manual Dry Run:</strong><br/>
        1. Start <code>l=0 (h=1)</code>, <code>r=8 (h=7)</code>: Area = $\min(1,7) \times 8 = 8$. Move shorter side <code>l++</code>.<br/>
        2. <code>l=1 (h=8)</code>, <code>r=8 (h=7)</code>: Area = $\min(8,7) \times 7 = 49$. Max Area = <strong>49</strong>. Move shorter side <code>r--</code>!
      </div>
    </div>
    <div class="pc" style="flex:1.4">
      <div class="pc-head">Template — LC 11</div>
<pre>public int maxArea(int[] height) {
    int l = 0, r = height.length - 1, maxWater = 0;
    while (l < r) {
        int w = r - l;
        int h = Math.min(height[l], height[r]);
        maxWater = Math.max(maxWater, w * h);
        if (height[l] < height[r]) l++;
        else r--;
    }
    return maxWater;
}</pre>
    </div>
  </div>
</div>

<div class="prow">
  <div class="prow-head">
    <div class="ptag2">PATTERN 4</div>
    <div class="ptitle">TRAPPING RAIN WATER (LC 42)</div>
    <div class="psub">e.g. Trapping Rain Water</div>
  </div>
  <div class="prow-body">
    <div class="pc" style="flex:1">
      <div class="pc-head">Problem Statement &amp; Mechanics</div>
      <div style="font-size:0.76rem;margin-bottom:4px">
        Given n non-negative integers representing elevation map, compute how much water it can trap after raining.
      </div>
      <div class="io-box">
        <strong>Input:</strong> height = [0,1,0,2,1,0,1,3,2,1,2,1]<br/>
        <strong>Output:</strong> 6
      </div>
      <div class="dry-box">
        <strong>🔍 Step-by-Step Manual Dry Run:</strong><br/>
        1. Water at cell $i$ is $\min(\text{lMax}, \text{rMax}) - h[i]$.<br/>
        2. If <code>height[l] < height[r]</code>, water at <code>l</code> is bounded by <code>lMax</code>! Process <code>l++</code>.<br/>
        3. Otherwise, process <code>r--</code>. $O(1)$ space!
      </div>
    </div>
    <div class="pc" style="flex:1.4">
      <div class="pc-head">Template — LC 42</div>
<pre>public int trap(int[] height) {
    int l = 0, r = height.length - 1;
    int lMax = 0, rMax = 0, water = 0;
    while (l < r) {
        if (height[l] < height[r]) {
            if (height[l] >= lMax) lMax = height[l];
            else water += lMax - height[l];
            l++;
        } else {
            if (height[r] >= rMax) rMax = height[r];
            else water += rMax - height[r];
            r--;
        }
    }
    return water;
}</pre>
    </div>
  </div>
</div>
</div>

<!-- PAGE 4: DECISION TREE & PROBLEM LADDER -->
<div class="page">
<div class="ph">
  <div><h1>TWO POINTERS PATTERN</h1><div class="sub">Decision Tree &amp; FAANG Problem Ladder</div></div>
  <div style="text-align:right"><div class="pn">PAGE 4 OF 5</div><div class="ptag">DECISION TREE · PROBLEM LADDER</div></div>
</div>

<div class="box amb">
  <div class="bh">🌳 TWO POINTERS DECISION TREE &amp; TRIGGER WORDS</div>
  <div class="bc">
    <table>
      <tr><th>Trigger Keywords</th><th>Pointer Strategy</th><th>Key Trick</th></tr>
      <tr><td>"Sorted Array", "Find pair sum"</td><td>Opposite Converging (LC 167)</td><td><code>sum < target ? l++ : r--</code></td></tr>
      <tr><td>"In-place duplicate removal", "Move zeros"</td><td>Fast &amp; Slow Same Direction (LC 26)</td><td><code>nums[slow] = nums[fast]</code> when distinct</td></tr>
      <tr><td>"Container water", "Trapping rain"</td><td>Greedy Boundary Convergence (LC 11, 42)</td><td>Advance the pointer with smaller height</td></tr>
      <tr><td>"3Sum", "4Sum", "Triplet sum to zero"</td><td>Sort + Outer Loop + Two Pointers (LC 15)</td><td>Always skip duplicate values for i, l, r!</td></tr>
    </table>
  </div>
</div>

<div class="box grn">
  <div class="bh">🚀 FAANG TWO POINTERS PROBLEM LADDER</div>
  <div class="bc">
    <table>
      <tr><th>#</th><th>Problem</th><th>Difficulty</th><th>Key Concept</th><th>Time Complexity</th></tr>
      <tr><td>1</td><td>Valid Palindrome — LC 125</td><td><span style="color:var(--grn);font-weight:700">Easy</span></td><td>Converging alphanumeric scan</td><td>$O(N)$ time, $O(1)$ space</td></tr>
      <tr><td>2</td><td>Two Sum II (Sorted Array) — LC 167</td><td><span style="color:var(--grn);font-weight:700">Medium</span></td><td>Opposite direction sum search</td><td>$O(N)$ time, $O(1)$ space</td></tr>
      <tr><td>3</td><td>Remove Duplicates from Sorted Array — LC 26</td><td><span style="color:var(--grn);font-weight:700">Easy</span></td><td>Fast &amp; Slow in-place overwrite</td><td>$O(N)$ time, $O(1)$ space</td></tr>
      <tr><td>4</td><td>Container With Most Water — LC 11</td><td><span style="color:var(--amb);font-weight:700">Medium</span></td><td>Greedy boundary inward convergence</td><td>$O(N)$ time, $O(1)$ space</td></tr>
      <tr><td>5</td><td>3Sum — LC 15</td><td><span style="color:var(--amb);font-weight:700">Medium</span></td><td>Sort + 2-pointer inner loop + skip dups</td><td>$O(N^2)$ time, $O(1)$ space</td></tr>
      <tr><td>6</td><td>Trapping Rain Water — LC 42</td><td><span style="color:var(--red);font-weight:700">Hard</span></td><td>Dual peak max boundary pointers</td><td>$O(N)$ time, $O(1)$ space</td></tr>
    </table>
  </div>
</div>
</div>

<!-- PAGE 5: DRY RUN, MATH PROOFS & CHEAT SHEET -->
<div class="page">
<div class="ph">
  <div><h1>TWO POINTERS PATTERN</h1><div class="sub">Dry Run, Math Proofs &amp; FAANG Cheat Sheet</div></div>
  <div style="text-align:right"><div class="pn">PAGE 5 OF 5</div><div class="ptag">DRY RUN · PROOFS · CHEAT SHEET</div></div>
</div>

<div class="g2" style="margin-bottom:8px">
  <div class="box sky">
    <div class="bh">🧠 MATH PROOF: WHY GREEDY WATER WORKS</div>
    <div class="bc">
      Suppose $h[l] < h[r]$. Area is $(r - l) \times h[l]$.<br/>
      If we kept $l$ fixed and moved $r$ to any $r' < r$:
      <ul>
        <li>Width decreases: $(r' - l) < (r - l)$.</li>
        <li>Height is $\min(h[l], h[r']) \le h[l]$.</li>
      </ul>
      Therefore, any container with $l$ fixed and $r' < r$ MUST have area $\le$ current area! Discard pointer $l$ safely!
    </div>
  </div>

  <div class="box amb">
    <div class="bh">⚡ TOP INTERVIEW BUGS TO AVOID</div>
    <div class="bc">
      <ul style="padding-left:12px;font-size:0.75rem">
        <li><strong>Duplicate Triplets in 3Sum:</strong> Always skip duplicates for <code>i</code>, <code>l</code>, and <code>r</code> after finding a valid sum!</li>
        <li><strong>Off-by-one in Fast/Slow:</strong> Remember to return <code>slow + 1</code> for unique array length!</li>
        <li><strong>Pointer Crossover:</strong> Loop condition must be <code>while (l < r)</code>.</li>
      </ul>
    </div>
  </div>
</div>

<div class="box red">
  <div class="bh">📌 TOP 5 FAANG TWO POINTER INTERVIEW RULES</div>
  <div class="bc">
    <ol style="padding-left:16px;font-size:0.78rem">
      <li><strong>Check array sorting:</strong> If array is sorted, 2 Pointers gives $O(N)$ time &amp; $O(1)$ space instantly!</li>
      <li><strong>In-place constraint:</strong> Whenever a problem asks for $O(1)$ space modification, think Fast &amp; Slow pointers!</li>
      <li><strong>Boundary Shrinking:</strong> Shrink from sides inward whenever global max is bounded by outer limits (Container Water).</li>
      <li><strong>Skip Duplicates:</strong> Always handle duplicate elements explicitly when counting unique sets.</li>
      <li><strong>Always state complexities clearly:</strong> Time $O(N)$ or $O(N^2)$, Space $O(1)$!</li>
    </ol>
  </div>
</div>

</div>
</div>
</div>
</body>
</html>"""

dst_html = r"F:\dsa\bookfinal\Topic03_TwoPointers.html"
with open(dst_html, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Saved restored prow layout HTML to", dst_html)

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
pdf_out = r"F:\dsa\bookfinal\Topic03_TwoPointers.pdf"

if os.path.exists(pdf_out):
    os.remove(pdf_out)

cmd = [chrome_path, '--headless', '--disable-gpu', '--no-pdf-header-footer', f'--print-to-pdf={pdf_out}', dst_html]
subprocess.run(cmd, check=True)

doc = fitz.open(pdf_out)
print("==========================================")
print(f"Generated Topic 03 PDF Page Count: {len(doc)} pages")
print("==========================================")

for i in range(len(doc)):
    page = doc[i]
    text = page.get_text()
    t_clean = text[:70].replace('\n', ' ')
    print(f"Page {i+1} has {len(text)} chars: {t_clean}")

doc.close()

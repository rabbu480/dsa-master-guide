"""
faang_enhancer.py
------------------
Reads each v0 Final HTML, searches for common FAANG patterns
that may be missing or incomplete, and injects a FAANG QUICK
REFERENCE appendix page at the end of each file.
"""

import os
import re

v0_dir = r"C:\Users\rabba\Downloads\TelegramDownload\metadata\v0"

# ---------------------------------------------------------------
# FAANG Quick Reference pages – one per topic
# ---------------------------------------------------------------

HEAPS_APPENDIX = """
<div class="page">
  <!-- FAANG QUICK REFERENCE: HEAPS -->
  <div class="header-top">
    <div>
      <h1>HEAP &mdash; FAANG Quick Reference</h1>
      <div class="subtitle" style="color:#334155;">&#x2B50; Must-Know Patterns &amp; Common Mistakes</div>
    </div>
    <div class="page-number">APPENDIX</div>
  </div>

  <div class="grid-container">
    <div>
      <div class="section-box">
        <div class="section-header"><span class="num">A</span> TOP-K ELEMENTS PATTERN</div>
        <div class="section-content">
          <p><strong>When to use:</strong> Find K largest/smallest, K most frequent.</p>
          <p><strong>Strategy:</strong> Use a <em>Min Heap of size K</em> for K largest (counter-intuitive!).</p>
          <pre>
// K Largest Elements
PriorityQueue&lt;Integer&gt; minHeap = new PriorityQueue&lt;&gt;();
for (int num : nums) {
    minHeap.offer(num);
    if (minHeap.size() &gt; k) minHeap.poll(); // evict smallest
}
// minHeap now contains K largest
// Time: O(n log k)  Space: O(k)</pre>
          <pre>
// K Most Frequent (HashMap + MinHeap)
Map&lt;Integer, Integer&gt; freq = new HashMap&lt;&gt;();
for (int n : nums) freq.merge(n, 1, Integer::sum);
PriorityQueue&lt;int[]&gt; pq = new PriorityQueue&lt;&gt;((a,b)-&gt;a[1]-b[1]);
for (var e : freq.entrySet()) {
    pq.offer(new int[]{e.getKey(), e.getValue()});
    if (pq.size() &gt; k) pq.poll();
}
// Time: O(n log k)  Space: O(n)</pre>
        </div>
      </div>

      <div class="section-box">
        <div class="section-header"><span class="num">B</span> TWO-HEAP PATTERN (MEDIAN)</div>
        <div class="section-content">
          <p><strong>When to use:</strong> Dynamic median, sliding window median.</p>
          <p><strong>Strategy:</strong> Keep lower half in Max Heap, upper half in Min Heap. Balance sizes.</p>
          <pre>
PriorityQueue&lt;Integer&gt; lo = new PriorityQueue&lt;&gt;(Collections.reverseOrder());
PriorityQueue&lt;Integer&gt; hi = new PriorityQueue&lt;&gt;();

void addNum(int num) {
    lo.offer(num);
    hi.offer(lo.poll()); // push lo's max to hi
    if (hi.size() &gt; lo.size())
        lo.offer(hi.poll()); // rebalance
}

double findMedian() {
    return lo.size() == hi.size()
        ? (lo.peek() + hi.peek()) / 2.0
        : lo.peek();
}</pre>
        </div>
      </div>

      <div class="section-box">
        <div class="section-header"><span class="num">C</span> K-WAY MERGE PATTERN</div>
        <div class="section-content">
          <p><strong>When to use:</strong> Merge K sorted lists/arrays.</p>
          <pre>
// Each element: [value, listIndex, elementIndex]
PriorityQueue&lt;int[]&gt; pq = new PriorityQueue&lt;&gt;((a,b)-&gt;a[0]-b[0]);
for (int i = 0; i &lt; lists.length; i++)
    if (!lists[i].isEmpty())
        pq.offer(new int[]{lists[i].get(0), i, 0});

while (!pq.isEmpty()) {
    int[] curr = pq.poll();
    result.add(curr[0]);
    int nextIdx = curr[2] + 1;
    if (nextIdx &lt; lists[curr[1]].size())
        pq.offer(new int[]{lists[curr[1]].get(nextIdx), curr[1], nextIdx});
}
// Time: O(n log k)  Space: O(k)</pre>
        </div>
      </div>
    </div>

    <div>
      <div class="section-box">
        <div class="section-header"><span class="num">D</span> CUSTOM COMPARATORS (FAANG TRAP)</div>
        <div class="section-content">
          <table>
            <tr><th>Goal</th><th>Comparator</th></tr>
            <tr><td>Min Heap (default)</td><td><code>new PriorityQueue&lt;&gt;()</code></td></tr>
            <tr><td>Max Heap</td><td><code>Collections.reverseOrder()</code></td></tr>
            <tr><td>Custom object by field</td><td><code>(a,b) -&gt; a.val - b.val</code></td></tr>
            <tr><td>2D array by 2nd col</td><td><code>(a,b) -&gt; a[1] - b[1]</code></td></tr>
            <tr><td>String by length</td><td><code>Comparator.comparingInt(String::length)</code></td></tr>
            <tr><td>Multi-key sort</td><td><code>(a,b) -&gt; a[0]==b[0] ? a[1]-b[1] : a[0]-b[0]</code></td></tr>
          </table>
          <div class="callout-danger" style="margin-top:10px;">
            <strong>&#x26A0; Integer Overflow Trap!</strong><br>
            Never use <code>b - a</code> for comparator if values can exceed Integer.MAX_VALUE/2.<br>
            Use <code>Integer.compare(b, a)</code> instead!
          </div>
        </div>
      </div>

      <div class="section-box">
        <div class="section-header"><span class="num">E</span> HEAP PROBLEM DECISION GUIDE</div>
        <div class="section-content">
          <table>
            <tr><th>Trigger Words</th><th>Pattern</th><th>Heap Type</th></tr>
            <tr><td>"K largest"</td><td>Top-K</td><td>Min Heap (size K)</td></tr>
            <tr><td>"K smallest"</td><td>Top-K</td><td>Max Heap (size K)</td></tr>
            <tr><td>"Most frequent K"</td><td>Top-K + HashMap</td><td>Min Heap (size K)</td></tr>
            <tr><td>"Running median"</td><td>Two Heap</td><td>Max+Min pair</td></tr>
            <tr><td>"Merge K sorted"</td><td>K-Way Merge</td><td>Min Heap</td></tr>
            <tr><td>"Next interval/event"</td><td>Greedy + Heap</td><td>Min Heap</td></tr>
            <tr><td>"Rearrange/reorganize"</td><td>Greedy + Heap</td><td>Max Heap</td></tr>
            <tr><td>"Dijkstra/Prim"</td><td>Graph + Heap</td><td>Min Heap</td></tr>
          </table>
        </div>
      </div>

      <div class="section-box">
        <div class="section-header"><span class="num">F</span> KEY LEETCODE PROBLEMS</div>
        <div class="section-content">
          <table>
            <tr><th>#</th><th>Problem</th><th>Pattern</th><th>Diff</th></tr>
            <tr><td>215</td><td>Kth Largest Element</td><td>Top-K</td><td style="color:#d97706;">Med</td></tr>
            <tr><td>347</td><td>Top K Frequent Elements</td><td>Top-K + HashMap</td><td style="color:#d97706;">Med</td></tr>
            <tr><td>295</td><td>Find Median from Data Stream</td><td>Two Heap</td><td style="color:#dc2626;">Hard</td></tr>
            <tr><td>23</td><td>Merge K Sorted Lists</td><td>K-Way Merge</td><td style="color:#dc2626;">Hard</td></tr>
            <tr><td>621</td><td>Task Scheduler</td><td>Greedy + Max Heap</td><td style="color:#d97706;">Med</td></tr>
            <tr><td>767</td><td>Reorganize String</td><td>Greedy + Max Heap</td><td style="color:#d97706;">Med</td></tr>
            <tr><td>743</td><td>Network Delay Time</td><td>Dijkstra</td><td style="color:#d97706;">Med</td></tr>
            <tr><td>1046</td><td>Last Stone Weight</td><td>Max Heap Basic</td><td style="color:#16a34a;">Easy</td></tr>
          </table>
        </div>
      </div>
    </div>
  </div>
</div>
"""

BINARY_SEARCH_APPENDIX = """
<div class="page">
  <div class="header-top">
    <div>
      <h1>BINARY SEARCH &mdash; FAANG Quick Reference</h1>
      <div class="subtitle" style="color:#334155;">&#x2B50; Universal Template &amp; All Variants</div>
    </div>
    <div class="page-number">APPENDIX</div>
  </div>

  <div class="grid-container">
    <div>
      <div class="section-box">
        <div class="section-header"><span class="num">A</span> UNIVERSAL BINARY SEARCH TEMPLATE</div>
        <div class="section-content">
          <p>One template that covers 99% of binary search problems:</p>
          <pre>
// Find LEFTMOST position satisfying condition
int lo = 0, hi = n - 1;  // adjust hi as needed
while (lo &lt; hi) {
    int mid = lo + (hi - lo) / 2;  // avoids overflow
    if (condition(mid)) {
        hi = mid;        // mid could be answer, keep it
    } else {
        lo = mid + 1;    // mid is not answer
    }
}
return lo; // or check if lo satisfies condition</pre>
          <div class="callout-tip">
            <strong>&#x1F4A1; Key Insight:</strong> Always ask "what condition must mid satisfy?" 
            If satisfied → shrink right. If not → shrink left.
          </div>
        </div>
      </div>

      <div class="section-box">
        <div class="section-header"><span class="num">B</span> VARIANTS &amp; WHEN TO USE</div>
        <div class="section-content">
          <table>
            <tr><th>Variant</th><th>Use Case</th><th>hi init</th></tr>
            <tr><td>Find exact</td><td>Target in sorted array</td><td>n-1</td></tr>
            <tr><td>Find leftmost</td><td>First occurrence, first ≥ target</td><td>n</td></tr>
            <tr><td>Find rightmost</td><td>Last occurrence, last ≤ target</td><td>n-1</td></tr>
            <tr><td>Search on answer</td><td>Minimize max, Maximize min</td><td>max possible</td></tr>
            <tr><td>Rotated array</td><td>Search rotated sorted array</td><td>n-1</td></tr>
          </table>
          <pre style="margin-top:10px;">
// Find RIGHTMOST (last occurrence)
while (lo &lt; hi) {
    int mid = lo + (hi - lo + 1) / 2; // +1 to avoid infinite loop
    if (condition(mid)) lo = mid;
    else hi = mid - 1;
}</pre>
        </div>
      </div>

      <div class="section-box">
        <div class="section-header"><span class="num">C</span> SEARCH ON ANSWER PATTERN</div>
        <div class="section-content">
          <p><strong>When:</strong> "Minimize the maximum" or "Maximize the minimum" in a problem.</p>
          <pre>
// Binary search on the ANSWER SPACE
long lo = minPossible, hi = maxPossible;
while (lo &lt; hi) {
    long mid = lo + (hi - lo) / 2;
    if (canAchieve(mid)) {  // is mid a valid answer?
        hi = mid;           // try smaller
    } else {
        lo = mid + 1;       // need larger
    }
}
return lo;</pre>
          <div class="callout-info">
            Examples: Koko Eating Bananas (#875), Capacity to Ship (#1011), Split Array Largest Sum (#410)
          </div>
        </div>
      </div>
    </div>

    <div>
      <div class="section-box">
        <div class="section-header"><span class="num">D</span> ROTATED SORTED ARRAY</div>
        <div class="section-content">
          <pre>
// #33 Search in Rotated Sorted Array
int lo = 0, hi = nums.length - 1;
while (lo &lt;= hi) {
    int mid = lo + (hi - lo) / 2;
    if (nums[mid] == target) return mid;
    
    if (nums[lo] &lt;= nums[mid]) { // LEFT half is sorted
        if (target &gt;= nums[lo] &amp;&amp; target &lt; nums[mid])
            hi = mid - 1;
        else lo = mid + 1;
    } else { // RIGHT half is sorted
        if (target &gt; nums[mid] &amp;&amp; target &lt;= nums[hi])
            lo = mid + 1;
        else hi = mid - 1;
    }
}
return -1;</pre>
        </div>
      </div>

      <div class="section-box">
        <div class="section-header"><span class="num">E</span> COMMON PITFALLS</div>
        <div class="section-content">
          <table>
            <tr><th>Pitfall</th><th>Fix</th></tr>
            <tr><td>Integer overflow with <code>(lo+hi)/2</code></td><td>Use <code>lo + (hi-lo)/2</code></td></tr>
            <tr><td>Infinite loop with <code>lo=mid</code></td><td>Use <code>mid = lo+(hi-lo+1)/2</code></td></tr>
            <tr><td>Off-by-one on boundary</td><td>Dry-run with 2-element array</td></tr>
            <tr><td>Wrong condition direction</td><td>Ask: "does mid satisfy the minimum valid condition?"</td></tr>
          </table>
        </div>
      </div>

      <div class="section-box">
        <div class="section-header"><span class="num">F</span> KEY LEETCODE PROBLEMS</div>
        <div class="section-content">
          <table>
            <tr><th>#</th><th>Problem</th><th>Pattern</th><th>Diff</th></tr>
            <tr><td>704</td><td>Binary Search</td><td>Classic</td><td style="color:#16a34a;">Easy</td></tr>
            <tr><td>35</td><td>Search Insert Position</td><td>Leftmost</td><td style="color:#16a34a;">Easy</td></tr>
            <tr><td>33</td><td>Search Rotated Array</td><td>Rotated</td><td style="color:#d97706;">Med</td></tr>
            <tr><td>153</td><td>Find Min in Rotated</td><td>Rotated</td><td style="color:#d97706;">Med</td></tr>
            <tr><td>875</td><td>Koko Eating Bananas</td><td>Search on Answer</td><td style="color:#d97706;">Med</td></tr>
            <tr><td>1011</td><td>Capacity to Ship</td><td>Search on Answer</td><td style="color:#d97706;">Med</td></tr>
            <tr><td>4</td><td>Median of Two Sorted Arrays</td><td>Binary Search</td><td style="color:#dc2626;">Hard</td></tr>
            <tr><td>410</td><td>Split Array Largest Sum</td><td>Search on Answer</td><td style="color:#dc2626;">Hard</td></tr>
          </table>
        </div>
      </div>
    </div>
  </div>
</div>
"""

ARRAYS_APPENDIX = """
<div class="page">
  <div class="header-top">
    <div>
      <h1>ARRAYS &amp; HASHING &mdash; FAANG Quick Reference</h1>
      <div class="subtitle" style="color:#334155;">&#x2B50; Core Patterns &amp; Templates</div>
    </div>
    <div class="page-number">APPENDIX</div>
  </div>

  <div class="grid-container">
    <div>
      <div class="section-box">
        <div class="section-header"><span class="num">A</span> TWO POINTER PATTERNS</div>
        <div class="section-content">
          <pre>
// Opposite ends (Two Sum sorted, 3Sum)
int lo = 0, hi = n - 1;
while (lo &lt; hi) {
    int sum = arr[lo] + arr[hi];
    if (sum == target) { /* found */ lo++; hi--; }
    else if (sum &lt; target) lo++;
    else hi--;
}</pre>
          <pre>
// Same direction (Remove Duplicates, Sliding Window)
int slow = 0;
for (int fast = 0; fast &lt; n; fast++) {
    if (condition(arr[fast])) {
        arr[slow++] = arr[fast];
    }
}</pre>
        </div>
      </div>

      <div class="section-box">
        <div class="section-header"><span class="num">B</span> SLIDING WINDOW TEMPLATES</div>
        <div class="section-content">
          <pre>
// Fixed window size K
int sum = 0, maxSum = 0;
for (int i = 0; i &lt; n; i++) {
    sum += arr[i];
    if (i &gt;= k) sum -= arr[i - k];
    if (i &gt;= k - 1) maxSum = Math.max(maxSum, sum);
}</pre>
          <pre>
// Variable window (longest with condition)
int lo = 0, maxLen = 0;
Map&lt;Character, Integer&gt; map = new HashMap&lt;&gt;();
for (int hi = 0; hi &lt; n; hi++) {
    map.merge(s.charAt(hi), 1, Integer::sum); // add
    while (!valid(map)) {                     // shrink
        map.merge(s.charAt(lo), -1, Integer::sum);
        if (map.get(s.charAt(lo)) == 0) map.remove(s.charAt(lo));
        lo++;
    }
    maxLen = Math.max(maxLen, hi - lo + 1);
}</pre>
        </div>
      </div>

      <div class="section-box">
        <div class="section-header"><span class="num">C</span> PREFIX SUM + HASH</div>
        <div class="section-content">
          <pre>
// Subarray sum equals K (#560)
int sum = 0, count = 0;
Map&lt;Integer, Integer&gt; prefixCount = new HashMap&lt;&gt;();
prefixCount.put(0, 1); // empty subarray
for (int num : nums) {
    sum += num;
    count += prefixCount.getOrDefault(sum - k, 0);
    prefixCount.merge(sum, 1, Integer::sum);
}
return count;</pre>
        </div>
      </div>
    </div>

    <div>
      <div class="section-box">
        <div class="section-header"><span class="num">D</span> HASH MAP TRICKS</div>
        <div class="section-content">
          <pre>
// Frequency count
Map&lt;T, Integer&gt; freq = new HashMap&lt;&gt;();
freq.merge(key, 1, Integer::sum); // cleaner than getOrDefault

// Check anagram
int[] count = new int[26];
for (char c : s.toCharArray()) count[c - 'a']++;
for (char c : t.toCharArray()) count[c - 'a']--;
// if all zeros -&gt; anagram

// Two Sum O(n) with HashMap
Map&lt;Integer, Integer&gt; seen = new HashMap&lt;&gt;();
for (int i = 0; i &lt; n; i++) {
    if (seen.containsKey(target - nums[i]))
        return new int[]{seen.get(target - nums[i]), i};
    seen.put(nums[i], i);
}</pre>
        </div>
      </div>

      <div class="section-box">
        <div class="section-header"><span class="num">E</span> KEY LEETCODE PROBLEMS</div>
        <div class="section-content">
          <table>
            <tr><th>#</th><th>Problem</th><th>Pattern</th><th>Diff</th></tr>
            <tr><td>1</td><td>Two Sum</td><td>HashMap</td><td style="color:#16a34a;">Easy</td></tr>
            <tr><td>49</td><td>Group Anagrams</td><td>HashMap + Sort Key</td><td style="color:#d97706;">Med</td></tr>
            <tr><td>128</td><td>Longest Consecutive</td><td>HashSet</td><td style="color:#d97706;">Med</td></tr>
            <tr><td>560</td><td>Subarray Sum Equals K</td><td>Prefix Sum + HashMap</td><td style="color:#d97706;">Med</td></tr>
            <tr><td>3</td><td>Longest Substring No Repeat</td><td>Sliding Window</td><td style="color:#d97706;">Med</td></tr>
            <tr><td>76</td><td>Minimum Window Substring</td><td>Sliding Window</td><td style="color:#dc2626;">Hard</td></tr>
            <tr><td>15</td><td>3Sum</td><td>Two Pointer + Sort</td><td style="color:#d97706;">Med</td></tr>
            <tr><td>42</td><td>Trapping Rain Water</td><td>Two Pointer / Stack</td><td style="color:#dc2626;">Hard</td></tr>
          </table>
        </div>
      </div>
    </div>
  </div>
</div>
"""

TREES_APPENDIX = """
<div class="page">
  <div class="header-top">
    <div>
      <h1>TREES &mdash; FAANG Quick Reference</h1>
      <div class="subtitle" style="color:#334155;">&#x2B50; Traversal Templates &amp; Key Patterns</div>
    </div>
    <div class="page-number">APPENDIX</div>
  </div>

  <div class="grid-container">
    <div>
      <div class="section-box">
        <div class="section-header"><span class="num">A</span> ITERATIVE TRAVERSALS (No Recursion Stack)</div>
        <div class="section-content">
          <pre>
// INORDER (Left-Root-Right) - gives BST in sorted order
List&lt;Integer&gt; inorder(TreeNode root) {
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
          <pre>
// LEVEL ORDER (BFS)
List&lt;List&lt;Integer&gt;&gt; levelOrder(TreeNode root) {
    List&lt;List&lt;Integer&gt;&gt; res = new ArrayList&lt;&gt;();
    if (root == null) return res;
    Queue&lt;TreeNode&gt; q = new LinkedList&lt;&gt;();
    q.offer(root);
    while (!q.isEmpty()) {
        List&lt;Integer&gt; level = new ArrayList&lt;&gt;();
        int size = q.size();  // IMPORTANT: snapshot size!
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
        </div>
      </div>

      <div class="section-box">
        <div class="section-header"><span class="num">B</span> UNIVERSAL DFS TEMPLATE</div>
        <div class="section-content">
          <pre>
// Return value from subtrees (bottom-up)
int dfs(TreeNode node) {
    if (node == null) return BASE_CASE; // 0, null, etc.
    
    int left = dfs(node.left);   // get from left
    int right = dfs(node.right); // get from right
    
    // Compute answer using node.val, left, right
    // Update global answer if needed
    
    return VALUE_TO_PARENT; // what to pass up
}</pre>
          <div class="callout-tip">
            <strong>&#x1F4A1; The key question:</strong> "What do I need from my subtrees to compute my answer?"
          </div>
        </div>
      </div>
    </div>

    <div>
      <div class="section-box">
        <div class="section-header"><span class="num">C</span> BST OPERATIONS</div>
        <div class="section-content">
          <pre>
// Validate BST (pass min/max bounds)
boolean isValid(TreeNode node, long min, long max) {
    if (node == null) return true;
    if (node.val &lt;= min || node.val &gt;= max) return false;
    return isValid(node.left, min, node.val) 
        &amp;&amp; isValid(node.right, node.val, max);
}
// Call: isValid(root, Long.MIN_VALUE, Long.MAX_VALUE)</pre>
          <pre>
// LCA of BST (use BST property!)
TreeNode lca(TreeNode root, TreeNode p, TreeNode q) {
    if (p.val &lt; root.val &amp;&amp; q.val &lt; root.val)
        return lca(root.left, p, q);
    if (p.val &gt; root.val &amp;&amp; q.val &gt; root.val)
        return lca(root.right, p, q);
    return root; // split point = LCA
}</pre>
        </div>
      </div>

      <div class="section-box">
        <div class="section-header"><span class="num">D</span> KEY LEETCODE PROBLEMS</div>
        <div class="section-content">
          <table>
            <tr><th>#</th><th>Problem</th><th>Pattern</th><th>Diff</th></tr>
            <tr><td>104</td><td>Max Depth Binary Tree</td><td>DFS</td><td style="color:#16a34a;">Easy</td></tr>
            <tr><td>102</td><td>Level Order Traversal</td><td>BFS</td><td style="color:#d97706;">Med</td></tr>
            <tr><td>543</td><td>Diameter of Binary Tree</td><td>DFS (bottom-up)</td><td style="color:#16a34a;">Easy</td></tr>
            <tr><td>124</td><td>Binary Tree Max Path Sum</td><td>DFS (bottom-up)</td><td style="color:#dc2626;">Hard</td></tr>
            <tr><td>235</td><td>LCA of BST</td><td>BST property</td><td style="color:#d97706;">Med</td></tr>
            <tr><td>98</td><td>Validate BST</td><td>BST bounds</td><td style="color:#d97706;">Med</td></tr>
            <tr><td>199</td><td>Binary Tree Right Side View</td><td>BFS/DFS</td><td style="color:#d97706;">Med</td></tr>
            <tr><td>297</td><td>Serialize/Deserialize BT</td><td>DFS/BFS</td><td style="color:#dc2626;">Hard</td></tr>
          </table>
        </div>
      </div>
    </div>
  </div>
</div>
"""

GRAPHS_APPENDIX = """
<div class="page">
  <div class="header-top">
    <div>
      <h1>GRAPHS &mdash; FAANG Quick Reference</h1>
      <div class="subtitle" style="color:#334155;">&#x2B50; Algorithm Templates &amp; Complexity</div>
    </div>
    <div class="page-number">APPENDIX</div>
  </div>

  <div class="grid-container">
    <div>
      <div class="section-box">
        <div class="section-header"><span class="num">A</span> BFS + DFS TEMPLATES</div>
        <div class="section-content">
          <pre>
// BFS (shortest path in unweighted graph)
int bfs(int start, int target, List&lt;List&lt;Integer&gt;&gt; adj) {
    boolean[] visited = new boolean[n];
    Queue&lt;Integer&gt; q = new LinkedList&lt;&gt;();
    q.offer(start); visited[start] = true;
    int dist = 0;
    while (!q.isEmpty()) {
        int size = q.size();
        for (int i = 0; i &lt; size; i++) {
            int node = q.poll();
            if (node == target) return dist;
            for (int nei : adj.get(node))
                if (!visited[nei]) { q.offer(nei); visited[nei] = true; }
        }
        dist++;
    }
    return -1;
}</pre>
          <pre>
// DFS (iterative)
void dfs(int start, List&lt;List&lt;Integer&gt;&gt; adj, boolean[] vis) {
    Deque&lt;Integer&gt; stack = new ArrayDeque&lt;&gt;();
    stack.push(start); vis[start] = true;
    while (!stack.isEmpty()) {
        int node = stack.pop();
        for (int nei : adj.get(node))
            if (!vis[nei]) { stack.push(nei); vis[nei] = true; }
    }
}</pre>
        </div>
      </div>

      <div class="section-box">
        <div class="section-header"><span class="num">B</span> UNION-FIND (DSU)</div>
        <div class="section-content">
          <pre>
int[] parent, rank;
void init(int n) {
    parent = new int[n]; rank = new int[n];
    for (int i = 0; i &lt; n; i++) parent[i] = i;
}
int find(int x) {
    if (parent[x] != x) parent[x] = find(parent[x]); // path compression
    return parent[x];
}
boolean union(int x, int y) {
    int px = find(x), py = find(y);
    if (px == py) return false; // already connected
    if (rank[px] &lt; rank[py]) { int t=px;px=py;py=t; }
    parent[py] = px;
    if (rank[px] == rank[py]) rank[px]++;
    return true;
}
// Time: O(α(n)) ≈ O(1) amortized</pre>
        </div>
      </div>
    </div>

    <div>
      <div class="section-box">
        <div class="section-header"><span class="num">C</span> DIJKSTRA (Weighted Shortest Path)</div>
        <div class="section-content">
          <pre>
// Standard Dijkstra
int[] dijkstra(int src, List&lt;int[]&gt;[] adj, int n) {
    int[] dist = new int[n];
    Arrays.fill(dist, Integer.MAX_VALUE);
    dist[src] = 0;
    PriorityQueue&lt;int[]&gt; pq = new PriorityQueue&lt;&gt;((a,b)-&gt;a[0]-b[0]);
    pq.offer(new int[]{0, src}); // [distance, node]
    while (!pq.isEmpty()) {
        int[] curr = pq.poll();
        int d = curr[0], node = curr[1];
        if (d &gt; dist[node]) continue; // stale entry
        for (int[] edge : adj[node]) {
            int next = edge[0], weight = edge[1];
            if (dist[node] + weight &lt; dist[next]) {
                dist[next] = dist[node] + weight;
                pq.offer(new int[]{dist[next], next});
            }
        }
    }
    return dist;
}
// Time: O((V+E) log V)  Space: O(V+E)</pre>
        </div>
      </div>

      <div class="section-box">
        <div class="section-header"><span class="num">D</span> TOPOLOGICAL SORT (Kahn's Algorithm)</div>
        <div class="section-content">
          <pre>
// Kahn's BFS Topo Sort
List&lt;Integer&gt; topoSort(int n, int[][] edges) {
    List&lt;List&lt;Integer&gt;&gt; adj = new ArrayList&lt;&gt;();
    int[] inDegree = new int[n];
    for (int i = 0; i &lt; n; i++) adj.add(new ArrayList&lt;&gt;());
    for (int[] e : edges) { adj.get(e[0]).add(e[1]); inDegree[e[1]]++; }
    
    Queue&lt;Integer&gt; q = new LinkedList&lt;&gt;();
    for (int i = 0; i &lt; n; i++) if (inDegree[i] == 0) q.offer(i);
    
    List&lt;Integer&gt; order = new ArrayList&lt;&gt;();
    while (!q.isEmpty()) {
        int node = q.poll();
        order.add(node);
        for (int nei : adj.get(node))
            if (--inDegree[nei] == 0) q.offer(nei);
    }
    return order.size() == n ? order : new ArrayList&lt;&gt;(); // empty = cycle
}</pre>
        </div>
      </div>

      <div class="section-box">
        <div class="section-header"><span class="num">E</span> ALGORITHM DECISION TABLE</div>
        <div class="section-content">
          <table>
            <tr><th>Problem Type</th><th>Algorithm</th><th>Time</th></tr>
            <tr><td>Shortest path (unweighted)</td><td>BFS</td><td>O(V+E)</td></tr>
            <tr><td>Shortest path (weighted, no neg)</td><td>Dijkstra</td><td>O((V+E)logV)</td></tr>
            <tr><td>Shortest path (with neg weights)</td><td>Bellman-Ford</td><td>O(VE)</td></tr>
            <tr><td>All-pairs shortest path</td><td>Floyd-Warshall</td><td>O(V³)</td></tr>
            <tr><td>Detect cycle (directed)</td><td>DFS (color: white/gray/black)</td><td>O(V+E)</td></tr>
            <tr><td>Detect cycle (undirected)</td><td>Union-Find or DFS</td><td>O(V+E)</td></tr>
            <tr><td>Topological order</td><td>Kahn's BFS or DFS</td><td>O(V+E)</td></tr>
            <tr><td>Connected components</td><td>Union-Find or BFS</td><td>O(V+E)</td></tr>
            <tr><td>Min spanning tree</td><td>Prim's or Kruskal's</td><td>O(E logV)</td></tr>
          </table>
        </div>
      </div>
    </div>
  </div>
</div>
"""

# ---------------------------------------------------------------
# Map each filename to its appendix
# ---------------------------------------------------------------
APPENDIX_MAP = {
    "10.Heaps_Final.html": HEAPS_APPENDIX,
    "6.Binary_Search_Final.html": BINARY_SEARCH_APPENDIX,
    "1.Array&Hashing_Final.html": ARRAYS_APPENDIX,
    "8.Trees_Final.html": TREES_APPENDIX,
    "9.Graphs_Final.html": GRAPHS_APPENDIX,
}

print("Injecting FAANG appendix pages into v0 files...")

for fname, appendix in APPENDIX_MAP.items():
    fpath = os.path.join(v0_dir, fname)
    if not os.path.exists(fpath):
        print(f"  WARNING: {fname} not found in v0/")
        continue
    
    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Inject appendix before </body>
    html = html.replace("</body>", appendix + "\n</body>", 1)
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(html)
    
    size_kb = os.path.getsize(fpath) / 1024
    print(f"  {fname}: {size_kb:.1f} KB (with appendix)")

print("\nAll v0 files enhanced with FAANG Quick Reference pages!")

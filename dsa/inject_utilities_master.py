import os
import re

utils_html_snippets = {
    "Topic01_Foundations_BigO.html": """
            <div class="section-box box-teal" style="margin-top:8px">
                <div class="section-header">🧰 REUSABLE COMPLEXITY &amp; MATH UTILITIES</div>
                <div class="section-content">
                    <p style="font-weight:700;margin:0 0 4px">Common Asymptotic Computation Helpers:</p>
<pre>
// 1. Log2 Computation: log2(N) = log(N) / log(2)
int log2(int n) { return (int)(Math.log(n) / Math.log(2)); }

// 2. Power of 2 Check: n & (n - 1) == 0 (for n > 0)
boolean isPowerOfTwo(int n) { return n > 0 && (n & (n - 1)) == 0; }

// 3. Fast Bitwise Shift for 2^N: (1 << N)
long powerOfTwo(int n) { return 1L << n; }</pre>
                </div>
            </div>""",

    "Topic02_Arrays_Strings_Hashing.html": """
            <div class="section-box box-teal" style="margin-top:8px">
                <div class="section-header">🧰 REUSABLE ARRAYS, STRINGS &amp; HASHING UTILITIES</div>
                <div class="section-content">
                    <div class="grid-2">
                        <div>
                            <p style="font-weight:700;margin:0 0 4px">Array &amp; String Conversions:</p>
<pre>
// int[] ➔ List<Integer>
List&lt;Integer&gt; list = Arrays.stream(arr).boxed().collect(Collectors.toList());
// List<Integer> ➔ int[]
int[] arr = list.stream().mapToInt(i -&gt; i).toArray();
// String ➔ char[] ➔ String
char[] chars = str.toCharArray();
String s = new String(chars);</pre>
                        </div>
                        <div>
                            <p style="font-weight:700;margin:0 0 4px">HashMap &amp; Frequency Utilities:</p>
<pre>
// Character frequency array (a-z)
int[] freq = new int[26];
freq[ch - 'a']++;
// HashMap getOrDefault & computeIfAbsent
map.put(key, map.getOrDefault(key, 0) + 1);
map.computeIfAbsent(key, k -&gt; new ArrayList&lt;&gt;()).add(val);</pre>
                        </div>
                    </div>
                </div>
            </div>""",

    "Topic03_TwoPointers.html": """
            <div class="section-box box-teal" style="margin-top:8px">
                <div class="section-header">🧰 REUSABLE TWO POINTERS UTILITIES</div>
                <div class="section-content">
                    <div class="grid-2">
                        <div>
                            <p style="font-weight:700;margin:0 0 4px">Element Swapping &amp; Reversal:</p>
<pre>
void swap(int[] arr, int i, int j) {
    int temp = arr[i]; arr[i] = arr[j]; arr[j] = temp;
}
void reverse(int[] arr, int left, int right) {
    while (left &lt; right) swap(arr, left++, right--);
}</pre>
                        </div>
                        <div>
                            <p style="font-weight:700;margin:0 0 4px">Array Partition Utility (Lomuto):</p>
<pre>
int partition(int[] arr, int low, int high) {
    int pivot = arr[high], i = low;
    for (int j = low; j &lt; high; j++) {
        if (arr[j] &lt;= pivot) swap(arr, i++, j);
    }
    swap(arr, i, high);
    return i;
}</pre>
                        </div>
                    </div>
                </div>
            </div>""",

    "Topic05_BinarySearch.html": """
            <div class="section-box box-teal" style="margin-top:8px">
                <div class="section-header">🧰 REUSABLE BINARY SEARCH UTILITIES</div>
                <div class="section-content">
                    <div class="grid-2">
                        <div>
                            <p style="font-weight:700;margin:0 0 4px">Safe Mid &amp; Boundary Helpers:</p>
<pre>
// Safe Midpoint calculation (prevents Integer overflow)
int mid = lo + (hi - lo) / 2;

// Lower Bound: First index where arr[i] >= target
int lowerBound(int[] arr, int target) {
    int lo = 0, hi = arr.length;
    while (lo &lt; hi) {
        int mid = lo + (hi - lo) / 2;
        if (arr[mid] &lt; target) lo = mid + 1;
        else hi = mid;
    }
    return lo;
}</pre>
                        </div>
                        <div>
                            <p style="font-weight:700;margin:0 0 4px">Feasibility Check Template (Search on Answer):</p>
<pre>
boolean feasible(int mid, int[] nums, int k) {
    int count = 1, sum = 0;
    for (int num : nums) {
        if (sum + num &gt; mid) {
            count++; sum = num;
        } else sum += num;
    }
    return count &lt;= k;
}</pre>
                        </div>
                    </div>
                </div>
            </div>""",

    "Topic06_LinkedList.html": """
            <div class="section-box box-teal" style="margin-top:8px">
                <div class="section-header">🧰 REUSABLE LINKED LIST UTILITIES</div>
                <div class="section-content">
                    <div class="grid-2">
                        <div>
                            <p style="font-weight:700;margin:0 0 4px">Reverse Linked List Utility:</p>
<pre>
ListNode reverseList(ListNode head) {
    ListNode prev = null, curr = head;
    while (curr != null) {
        ListNode nextTemp = curr.next;
        curr.next = prev;
        prev = curr;
        curr = nextTemp;
    }
    return prev;
}</pre>
                        </div>
                        <div>
                            <p style="font-weight:700;margin:0 0 4px">Find Middle Node (Fast &amp; Slow):</p>
<pre>
ListNode findMiddle(ListNode head) {
    ListNode slow = head, fast = head;
    while (fast != null &amp;&amp; fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;
    }
    return slow;
}</pre>
                        </div>
                    </div>
                </div>
            </div>""",

    "Topic07_Stack.html": """
            <div class="section-box box-teal" style="margin-top:8px">
                <div class="section-header">🧰 REUSABLE STACK UTILITIES &amp; APIS</div>
                <div class="section-content">
                    <div class="grid-2">
                        <div>
                            <p style="font-weight:700;margin:0 0 4px">ArrayDeque as Stack (Fast &amp; Modern):</p>
<pre>
Deque&lt;Integer&gt; stack = new ArrayDeque&lt;&gt;();
stack.push(val); // Push onto top
int top = stack.pop(); // Pop top element
int peek = stack.peek(); // Peek top without popping
boolean empty = stack.isEmpty();</pre>
                        </div>
                        <div>
                            <p style="font-weight:700;margin:0 0 4px">Monotonic Stack Template (Next Greater):</p>
<pre>
int[] nextGreater(int[] nums) {
    int[] res = new int[nums.length];
    Arrays.fill(res, -1);
    Deque&lt;Integer&gt; stack = new ArrayDeque&lt;&gt;(); // stores indices
    for (int i = 0; i &lt; nums.length; i++) {
        while (!stack.isEmpty() &amp;&amp; nums[i] &gt; nums[stack.peek()]) {
            res[stack.pop()] = nums[i];
        }
        stack.push(i);
    }
    return res;
}</pre>
                        </div>
                    </div>
                </div>
            </div>""",

    "Topic08_Queue_Deque.html": """
            <div class="section-box box-teal" style="margin-top:8px">
                <div class="section-header">🧰 REUSABLE QUEUE &amp; DEQUE UTILITIES</div>
                <div class="section-content">
                    <div class="grid-2">
                        <div>
                            <p style="font-weight:700;margin:0 0 4px">Queue &amp; Deque Operation Reference:</p>
<pre>
// Queue (FIFO): offer(), poll(), peek()
Queue&lt;Integer&gt; q = new ArrayDeque&lt;&gt;();
q.offer(val); int front = q.poll();

// Deque (Double Ended): offerFirst(), offerLast(), pollFirst(), pollLast()
Deque&lt;Integer&gt; deque = new ArrayDeque&lt;&gt;();</pre>
                        </div>
                        <div>
                            <p style="font-weight:700;margin:0 0 4px">Circular Queue Modulo Math:</p>
<pre>
// Modulo Arithmetic for Circular Indexing
int nextIndex = (currIndex + 1) % capacity;
int prevIndex = (currIndex - 1 + capacity) % capacity;</pre>
                        </div>
                    </div>
                </div>
            </div>""",

    "Topic09_Heap.html": """
            <div class="section-box box-teal" style="margin-top:8px">
                <div class="section-header">🧰 REUSABLE HEAP (PRIORITYQUEUE) UTILITIES</div>
                <div class="section-content">
                    <div class="grid-2">
                        <div>
                            <p style="font-weight:700;margin:0 0 4px">PriorityQueue Declarations &amp; Comparators:</p>
<pre>
// Min-Heap (default)
PriorityQueue&lt;Integer&gt; minHeap = new PriorityQueue&lt;&gt;();

// Max-Heap
PriorityQueue&lt;Integer&gt; maxHeap = new PriorityQueue&lt;&gt;(Collections.reverseOrder());

// Pair Comparator (a[1] - b[1] with safe Integer.compare)
PriorityQueue&lt;int[]&gt; pairPQ = new PriorityQueue&lt;&gt;((a, b) -&gt; Integer.compare(a[1], b[1]));</pre>
                        </div>
                        <div>
                            <p style="font-weight:700;margin:0 0 4px">Top-K Min-Heap Insertion Template:</p>
<pre>
// Maintain Top K largest elements in O(N log K) time
PriorityQueue&lt;Integer&gt; pq = new PriorityQueue&lt;&gt;();
for (int num : nums) {
    pq.offer(num);
    if (pq.size() &gt; k) pq.poll(); // evict smallest
}</pre>
                        </div>
                    </div>
                </div>
            </div>""",

    "Topic10_Trees.html": """
            <div class="section-box box-teal" style="margin-top:8px">
                <div class="section-header">🧰 REUSABLE TREE &amp; BST UTILITIES</div>
                <div class="section-content">
                    <div class="grid-2">
                        <div>
                            <p style="font-weight:700;margin:0 0 4px">TreeNode Definition &amp; Construction:</p>
<pre>
public class TreeNode {
    public int val;
    public TreeNode left, right;
    public TreeNode(int val) { this.val = val; }
}</pre>
                        </div>
                        <div>
                            <p style="font-weight:700;margin:0 0 4px">Height &amp; Depth Helper Function:</p>
<pre>
int height(TreeNode root) {
    if (root == null) return 0;
    return 1 + Math.max(height(root.left), height(root.right));
}</pre>
                        </div>
                    </div>
                </div>
            </div>""",

    "Topic11_Trie.html": """
            <div class="section-box box-teal" style="margin-top:8px">
                <div class="section-header">🧰 REUSABLE TRIE UTILITIES &amp; NODE CLASS</div>
                <div class="section-content">
<pre>
class TrieNode {
    TrieNode[] children = new TrieNode[26];
    boolean isEnd = false;
}
void insert(TrieNode root, String word) {
    TrieNode curr = root;
    for (char c : word.toCharArray()) {
        int idx = c - 'a';
        if (curr.children[idx] == null) curr.children[idx] = new TrieNode();
        curr = curr.children[idx];
    }
    curr.isEnd = true;
}</pre>
                </div>
            </div>""",

    "Topic13_Backtracking.html": """
            <div class="section-box box-teal" style="margin-top:8px">
                <div class="section-header">🧰 REUSABLE BACKTRACKING UTILITIES &amp; TEMPLATE</div>
                <div class="section-content">
<pre>
// Generic Choose -> Explore -> Undo Skeleton
void backtrack(int start, int[] nums, List&lt;Integer&gt; path, List&lt;List&lt;Integer&gt;&gt; res) {
    res.add(new ArrayList&lt;&gt;(path)); // Add snapshot of valid state
    for (int i = start; i &lt; nums.length; i++) {
        // 1. CHOOSE
        path.add(nums[i]);
        // 2. EXPLORE
        backtrack(i + 1, nums, path, res);
        // 3. UNDO (State Restoration)
        path.remove(path.size() - 1);
    }
}</pre>
                </div>
            </div>""",

    "Topic14_DynamicProgramming.html": """
            <div class="section-box box-teal" style="margin-top:8px">
                <div class="section-header">🧰 REUSABLE DYNAMIC PROGRAMMING UTILITIES</div>
                <div class="section-content">
                    <div class="grid-2">
                        <div>
                            <p style="font-weight:700;margin:0 0 4px">Memoization Table Initialization:</p>
<pre>
// 1D Memo initialization with -1
int[] memo = new int[n + 1];
Arrays.fill(memo, -1);

// 2D Memo initialization with -1
int[][] memo2D = new int[n + 1][m + 1];
for (int[] row : memo2D) Arrays.fill(row, -1);</pre>
                        </div>
                        <div>
                            <p style="font-weight:700;margin:0 0 4px">Space Optimization Row Swap:</p>
<pre>
// 1D DP array space optimization (prev vs curr)
int[] prev = new int[m + 1];
int[] curr = new int[m + 1];
// At end of outer loop step:
prev = curr.clone();</pre>
                        </div>
                    </div>
                </div>
            </div>""",

    "Topic15_Greedy.html": """
            <div class="section-box box-teal" style="margin-top:8px">
                <div class="section-header">🧰 REUSABLE GREEDY UTILITIES</div>
                <div class="section-content">
<pre>
// Interval sorting by end time (Canonical Greedy Choice)
Arrays.sort(intervals, (a, b) -&gt; Integer.compare(a[1], b[1]));

// Max Reach Tracker Pattern (Jump Game / Gas Station)
int maxReach = 0;
for (int i = 0; i &lt; nums.length; i++) {
    if (i &gt; maxReach) return false; // unreachable gap
    maxReach = Math.max(maxReach, i + nums[i]);
}</pre>
                </div>
            </div>""",

    "Topic17_BitManipulation.html": """
            <div class="section-box box-teal" style="margin-top:8px">
                <div class="section-header">🧰 REUSABLE BITWISE UTILITIES</div>
                <div class="section-content">
                    <div class="grid-2">
                        <div>
                            <p style="font-weight:700;margin:0 0 4px">Core Bit Operations:</p>
<pre>
// Clear lowest set bit: n & (n - 1)
n = n & (n - 1);
// Isolate lowest set bit: n & -n
int lowestBit = n & -n;
// Check if i-th bit is set: (n >> i) & 1 == 1
boolean isSet = ((n &gt;&gt; i) &amp; 1) == 1;</pre>
                        </div>
                        <div>
                            <p style="font-weight:700;margin:0 0 4px">Bitmask Subset Enumeration:</p>
<pre>
// Iterate over all submasks of a bitmask
for (int sub = mask; sub &gt; 0; sub = (sub - 1) &amp; mask) {
    // Process submask
}</pre>
                        </div>
                    </div>
                </div>
            </div>""",

    "Topic18_Math.html": """
            <div class="section-box box-teal" style="margin-top:8px">
                <div class="section-header">🧰 REUSABLE MATHEMATICAL UTILITIES</div>
                <div class="section-content">
                    <div class="grid-2">
                        <div>
                            <p style="font-weight:700;margin:0 0 4px">GCD &amp; LCM (Euclidean Algorithm):</p>
<pre>
long gcd(long a, long b) { return b == 0 ? a : gcd(b, a % b); }
long lcm(long a, long b) { return (a / gcd(a, b)) * b; }</pre>
                        </div>
                        <div>
                            <p style="font-weight:700;margin:0 0 4px">Binary Exponentiation O(log N):</p>
<pre>
long power(long base, long exp, long mod) {
    long res = 1; base %= mod;
    while (exp &gt; 0) {
        if ((exp &amp; 1) == 1) res = (res * base) % mod;
        base = (base * base) % mod; exp &gt;&gt;= 1;
    }
    return res;
}</pre>
                        </div>
                    </div>
                </div>
            </div>""",

    "Topic19_AdvancedDS.html": """
            <div class="section-box box-teal" style="margin-top:8px">
                <div class="section-header">🧰 REUSABLE ADVANCED DATA STRUCTURE UTILITIES</div>
                <div class="section-content">
                    <div class="grid-2">
                        <div>
                            <p style="font-weight:700;margin:0 0 4px">Fenwick Tree (BIT) Operations:</p>
<pre>
void update(int[] bit, int i, int val) {
    for (; i &lt; bit.length; i += i &amp; -i) bit[i] += val;
}
int query(int[] bit, int i) {
    int sum = 0;
    for (; i &gt; 0; i -= i &amp; -i) sum += bit[i];
    return sum;
}</pre>
                        </div>
                        <div>
                            <p style="font-weight:700;margin:0 0 4px">Segment Tree Array Size Rule:</p>
<pre>
// Always allocate 4 * N for Segment Tree array
int[] tree = new int[4 * n];</pre>
                        </div>
                    </div>
                </div>
            </div>"""
}

base_dir = "F:/dsa/bookfinal"
count = 0

for filename, snippet in utils_html_snippets.items():
    filepath = os.path.join(base_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already injected
        if "REUSABLE" in content and "UTILITIES" in content:
            print(f"Already has utilities: {filename}")
            continue
            
        # Inject right after Page 1 header-top or goal-badge / first section-box
        if '<div class="page" id="page1">' in content:
            pos = content.find('<div class="page" id="page1">')
            # Find the end of header-top
            end_header = content.find('</div>', pos)
            if end_header != -1:
                # Find end of goal badge if present
                if 'goal-badge' in content[pos:pos+1500]:
                    gb_end = content.find('</div>', content.find('goal-badge', pos))
                    if gb_end != -1:
                        target_pos = gb_end + 6
                    else:
                        target_pos = end_header + 6
                else:
                    target_pos = end_header + 6
                
                new_content = content[:target_pos] + "\n" + snippet + content[target_pos:]
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += 1
                print(f"Injected utilities into {filename}")

print(f"\nDone! Injected utilities into {count} files.")

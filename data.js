const dsaData = [

  // ─── 0. INTRO ─────────────────────────────────────────────────────────────
  {
    title: "👋 Start Here: Pattern Decision Tree",
    color: "#333333",
    patterns: [
      {
        name: "How to Pick a Pattern in Interviews",
        recognition: "Read the problem → spot keywords → pick pattern → state complexity → code.",
        mentalModel: "Input sorted? → Two Pointers/BS. Grid/tree? → BFS/DFS. All combos? → Backtracking. Min/Max/Count? → DP. Greedy local=global? → Greedy.",
        pitfalls: "Never jump to code. State brute force O(N²) first, explain why it's slow, then optimize.",
        problems: [
          { num: "1", name: "Two Sum", url: "https://leetcode.com/problems/two-sum/" },
          { num: "200", name: "Number of Islands", url: "https://leetcode.com/problems/number-of-islands/" }
        ],
        code: {
          "Java": `// 🧭 PATTERN DECISION TREE
// Array sorted?            → Two Pointers, Binary Search
// Subarray / Substring?    → Sliding Window
// Frequency / Lookup?      → HashMap / HashSet
// Find ALL combos?         → Backtracking
// Shortest path?           → BFS (unweighted), Dijkstra (weighted)
// All paths / structure?   → DFS
// Min/Max optimization?    → DP (overlapping subproblems)
// Greedy local = global?   → Greedy
// Intervals overlap?       → Sort + Sweep / Heap
// Prefix match?            → Trie
// Connected components?    → Union Find / BFS / DFS
// Dependencies/ordering?   → Topological Sort
// Top K elements?          → Heap / QuickSelect
// Range query fast?        → Segment Tree / Fenwick Tree
// ─────────────────────────────────────────────
// ALWAYS: brute force → optimize → complexity`,
          "Kotlin": `// 🧭 COMPLEXITY CHEATSHEET
// O(1)       → Math, HashMap, Array access
// O(log N)   → Binary Search, Balanced BST
// O(N)       → Linear scan, Sliding Window, BFS, DFS
// O(N log N) → Sorting, Heap insertions
// O(N²)      → Nested loops, 2D DP
// O(2^N)     → Subsets, Backtracking
// O(N!)      → Permutations
//
// JAVA COLLECTIONS CHEATSHEET:
// List   → ArrayList   → O(1) get/add
// Set    → HashSet     → O(1) add/contains
// Map    → HashMap     → O(1) put/get
// Queue  → LinkedList  → O(1) offer/poll
// Stack  → ArrayDeque  → O(1) push/pop
// Heap   → PriorityQueue → O(logN) offer/poll
// Deque  → ArrayDeque  → O(1) both ends`,
          "Python": `# 🧭 INTERVIEW CHECKLIST
# 1. CLARIFY: negatives? duplicates? empty? sorted? bounds?
# 2. BRUTE FORCE: state O(N²) approach first
# 3. OPTIMIZE: explain insight → better solution
# 4. COMPLEXITY: say time + space before coding
# 5. CODE: clean, readable, handle edge cases
# 6. DRY RUN: trace small example after writing
# 7. EDGE CASES: empty, single, all same, negatives
#
# PYTHON COLLECTIONS:
# list  → append/pop O(1)
# set   → add/in O(1)
# dict  → get/set O(1)
# deque → appendleft/popleft O(1)
# heapq → heappush/heappop O(logN)
# Counter(arr) → freq map in one line
# sorted(arr, key=lambda x: x[0]) → sort by field`
        }
      }
    ]
  },

  // ─── 1. ARRAYS & STRINGS ─────────────────────────────────────────────────
  {
    title: "Arrays & Strings",
    color: "#b5563c",
    patterns: [
      {
        name: "Traversal & Basic Operations",
        recognition: "Process every element. Find max/min. Rotate array.",
        mentalModel: "Simple loop 0 to N-1. Track index carefully. Use modulo for rotation.",
        pitfalls: "Off-by-one. Modifying array while iterating.",
        problems: [
          { num: "189", name: "Rotate Array", url: "https://leetcode.com/problems/rotate-array/" },
          { num: "238", name: "Product of Array Except Self", url: "https://leetcode.com/problems/product-of-array-except-self/" }
        ],
        code: {
          "Java": `// Rotate array right by k steps
int n = arr.length; k %= n;
reverse(arr, 0, n-1);
reverse(arr, 0, k-1);
reverse(arr, k, n-1);

// Product except self (prefix * suffix)
int[] res = new int[n];
int prefix = 1;
for (int i = 0; i < n; i++) { res[i] = prefix; prefix *= nums[i]; }
int suffix = 1;
for (int i = n-1; i >= 0; i--) { res[i] *= suffix; suffix *= nums[i]; }`,
          "Kotlin": `// Rotate
val n = arr.size; val k = k % n
arr.reverse(); arr.reverse(0, k); arr.reverse(k, n)`,
          "Python": `# Rotate array right by k
arr[:] = arr[-k:] + arr[:-k]
# Product except self
prefix = [1] * n
for i in range(1, n): prefix[i] = prefix[i-1] * nums[i-1]
suffix = 1
for i in range(n-1, -1, -1):
    prefix[i] *= suffix; suffix *= nums[i]`
        }
      },
      {
        name: "Frequency Count (HashMap)",
        recognition: "Count occurrences. Anagram check. Most frequent. Group by frequency.",
        mentalModel: "Map element → count. Query the map. Use bucket sort for O(N) top-K.",
        pitfalls: "getOrDefault() not get(). Null pointer on .get(). Use Counter in Python.",
        problems: [
          { num: "242", name: "Valid Anagram", url: "https://leetcode.com/problems/valid-anagram/" },
          { num: "347", name: "Top K Frequent Elements", url: "https://leetcode.com/problems/top-k-frequent-elements/" }
        ],
        code: {
          "Java": `Map<Integer, Integer> freq = new HashMap<>();
for (int x : arr)
    freq.put(x, freq.getOrDefault(x, 0) + 1);
// Top K via bucket sort O(N)
List<Integer>[] bucket = new List[n + 1];
for (int k : freq.keySet()) {
    int f = freq.get(k);
    if (bucket[f] == null) bucket[f] = new ArrayList<>();
    bucket[f].add(k);
}`,
          "Kotlin": `val freq = mutableMapOf<Int, Int>()
for (x in arr) freq[x] = (freq[x] ?: 0) + 1`,
          "Python": `from collections import Counter
freq = Counter(arr)
# Top K
top_k = freq.most_common(k)
# Bucket sort O(N)
bucket = [[] for _ in range(len(arr) + 1)]
for num, cnt in freq.items(): bucket[cnt].append(num)`
        }
      },
      {
        name: "Prefix Sum",
        recognition: "Range sum queries. Subarray sum = K. Count subarrays.",
        mentalModel: "pre[i+1] = pre[i] + arr[i]. Range[L,R] = pre[R+1] - pre[L]. For subarray sum K: use HashMap {prefix: count}.",
        pitfalls: "Initialize map with {0:1}. 1-based prefix confusion.",
        problems: [
          { num: "303", name: "Range Sum Query", url: "https://leetcode.com/problems/range-sum-query-immutable/" },
          { num: "560", name: "Subarray Sum Equals K", url: "https://leetcode.com/problems/subarray-sum-equals-k/" }
        ],
        code: {
          "Java": `// Build prefix sum
int[] pre = new int[n + 1];
for (int i = 0; i < n; i++) pre[i+1] = pre[i] + arr[i];
int rangeSum = pre[R+1] - pre[L]; // sum from L to R

// Subarray sum = K → O(N)
Map<Integer,Integer> map = new HashMap<>();
map.put(0, 1); int sum = 0, res = 0;
for (int x : arr) {
    sum += x;
    res += map.getOrDefault(sum - k, 0);
    map.put(sum, map.getOrDefault(sum, 0) + 1);
}`,
          "Kotlin": `val pre = IntArray(n + 1)
for (i in 0 until n) pre[i+1] = pre[i] + arr[i]
val rangeSum = pre[R+1] - pre[L]`,
          "Python": `pre = [0] * (n + 1)
for i in range(n): pre[i+1] = pre[i] + arr[i]
range_sum = pre[R+1] - pre[L]
# Subarray sum = K
from collections import defaultdict
count = defaultdict(int); count[0] = 1
res = s = 0
for x in arr:
    s += x; res += count[s - k]; count[s] += 1`
        }
      },
      {
        name: "Difference Array",
        recognition: "Multiple range update queries then read final values.",
        mentalModel: "diff[L] += val, diff[R+1] -= val. Sweep prefix sum to get result.",
        pitfalls: "Don't forget the final sweep step.",
        problems: [
          { num: "1109", name: "Corporate Flight Bookings", url: "https://leetcode.com/problems/corporate-flight-bookings/" },
          { num: "1094", name: "Car Pooling", url: "https://leetcode.com/problems/car-pooling/" }
        ],
        code: {
          "Java": `int[] diff = new int[n + 1];
diff[L] += val; diff[R + 1] -= val;
// Sweep
int[] res = new int[n]; res[0] = diff[0];
for (int i = 1; i < n; i++) res[i] = res[i-1] + diff[i];`,
          "Kotlin": `val diff = IntArray(n + 1)
diff[L] += `val`; diff[R + 1] -= `val`
val res = IntArray(n).also { it[0] = diff[0] }
for (i in 1 until n) res[i] = res[i-1] + diff[i]`,
          "Python": `diff = [0] * (n + 1)
diff[L] += val; diff[R + 1] -= val
res = [0] * n; res[0] = diff[0]
for i in range(1, n): res[i] = res[i-1] + diff[i]`
        }
      },
      {
        name: "Kadane's Algorithm",
        recognition: "Maximum subarray sum. Continuous segment. Circular subarray.",
        mentalModel: "maxEnd = max(x, maxEnd + x). Reset when going negative. All-negative: return max element.",
        pitfalls: "All-negative array: return max element not 0. Circular: totalSum - minSubarray.",
        problems: [
          { num: "53", name: "Maximum Subarray", url: "https://leetcode.com/problems/maximum-subarray/" },
          { num: "918", name: "Max Sum Circular Subarray", url: "https://leetcode.com/problems/maximum-sum-circular-subarray/" }
        ],
        code: {
          "Java": `int maxEnd = arr[0], best = arr[0];
for (int i = 1; i < arr.length; i++) {
    maxEnd = Math.max(arr[i], maxEnd + arr[i]);
    best = Math.max(best, maxEnd);
}
return best;`,
          "Kotlin": `var maxEnd = arr[0]; var best = arr[0]
for (i in 1 until arr.size) {
    maxEnd = maxOf(arr[i], maxEnd + arr[i])
    best = maxOf(best, maxEnd)
}`,
          "Python": `max_end = best = arr[0]
for x in arr[1:]:
    max_end = max(x, max_end + x)
    best = max(best, max_end)`
        }
      },
      {
        name: "Matrix Traversal",
        recognition: "2D grid, spiral order, rotate 90°, 4-directional BFS/DFS.",
        mentalModel: "4 directions: dx=[0,0,1,-1], dy=[1,-1,0,0]. Boundary check before accessing.",
        pitfalls: "Out of bounds. Double-visiting (use visited array). Row vs column confusion.",
        problems: [
          { num: "54", name: "Spiral Matrix", url: "https://leetcode.com/problems/spiral-matrix/" },
          { num: "48", name: "Rotate Image", url: "https://leetcode.com/problems/rotate-image/" }
        ],
        code: {
          "Java": `int[] dx = {0,0,1,-1}, dy = {1,-1,0,0};
for (int d = 0; d < 4; d++) {
    int nr = r + dx[d], nc = c + dy[d];
    if (nr >= 0 && nr < R && nc >= 0 && nc < C)
        // process (nr, nc)
}
// Rotate 90° clockwise: transpose then reverse each row
for (int i=0;i<n;i++) for (int j=i+1;j<n;j++) swap(mat,i,j,j,i);
for (int[] row : mat) reverse(row);`,
          "Kotlin": `val dx = intArrayOf(0,0,1,-1); val dy = intArrayOf(1,-1,0,0)
for (d in 0..3) {
    val nr = r + dx[d]; val nc = c + dy[d]
    if (nr in 0 until R && nc in 0 until C) { /* process */ }
}`,
          "Python": `dx, dy = [0,0,1,-1], [1,-1,0,0]
for d in range(4):
    nr, nc = r+dx[d], c+dy[d]
    if 0 <= nr < R and 0 <= nc < C:
        pass  # process
# Rotate 90° clockwise
matrix[:] = [list(row) for row in zip(*matrix[::-1])]`
        }
      }
    ]
  },

  // ─── 2. TWO POINTERS ─────────────────────────────────────────────────────
  {
    title: "Two Pointers",
    color: "#1f3a5f",
    patterns: [
      {
        name: "Opposite Direction",
        recognition: "Sorted array, pair sum, 3Sum, palindrome, container.",
        mentalModel: "Left at start, right at end. Move inward based on comparison.",
        pitfalls: "l < r not <=. Must sort first for most problems. Deduplicate with while loop.",
        problems: [
          { num: "167", name: "Two Sum II", url: "https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/" },
          { num: "15", name: "3Sum", url: "https://leetcode.com/problems/3sum/" },
          { num: "11", name: "Container With Most Water", url: "https://leetcode.com/problems/container-with-most-water/" }
        ],
        code: {
          "Java": `int l = 0, r = arr.length - 1;
while (l < r) {
    int sum = arr[l] + arr[r];
    if (sum == target) return new int[]{l, r};
    if (sum < target) l++; else r--;
}
// 3Sum: fix one, two-pointer rest
Arrays.sort(nums);
for (int i = 0; i < n-2; i++) {
    if (i > 0 && nums[i] == nums[i-1]) continue; // skip dups
    int l = i+1, r = n-1;
    while (l < r) { /* two pointer logic */ }
}`,
          "Kotlin": `var l = 0; var r = arr.size - 1
while (l < r) {
    val sum = arr[l] + arr[r]
    when { sum == target -> return intArrayOf(l,r)
           sum < target -> l++; else -> r-- }
}`,
          "Python": `l, r = 0, len(arr) - 1
while l < r:
    s = arr[l] + arr[r]
    if s == target: return [l, r]
    elif s < target: l += 1
    else: r -= 1`
        }
      },
      {
        name: "Same Direction (Slow & Fast)",
        recognition: "In-place remove, deduplicate, partition array.",
        mentalModel: "slow = write pointer. fast = read pointer. Copy fast→slow when condition met.",
        pitfalls: "Overwriting before reading. Return slow as new length.",
        problems: [
          { num: "26", name: "Remove Duplicates", url: "https://leetcode.com/problems/remove-duplicates-from-sorted-array/" },
          { num: "283", name: "Move Zeroes", url: "https://leetcode.com/problems/move-zeroes/" },
          { num: "75", name: "Sort Colors", url: "https://leetcode.com/problems/sort-colors/" }
        ],
        code: {
          "Java": `int slow = 0;
for (int fast = 0; fast < n; fast++) {
    if (isValid(arr[fast])) // condition varies
        arr[slow++] = arr[fast];
}
// Dutch flag (3-way partition)
int lo=0, mid=0, hi=n-1;
while (mid <= hi) {
    if (nums[mid]==0) swap(lo++,mid++);
    else if (nums[mid]==2) swap(mid,hi--);
    else mid++;
}`,
          "Kotlin": `var slow = 0
for (fast in 0 until n)
    if (isValid(arr[fast])) arr[slow++] = arr[fast]`,
          "Python": `slow = 0
for fast in range(len(arr)):
    if is_valid(arr[fast]):
        arr[slow] = arr[fast]; slow += 1`
        }
      },
      {
        name: "Fast & Slow Pointer",
        recognition: "Cycle detection, find middle, happy number.",
        mentalModel: "Fast moves 2x. They meet if cycle. When fast=null, slow=middle.",
        pitfalls: "Check fast!=null AND fast.next!=null. Start both at head.",
        problems: [
          { num: "141", name: "Linked List Cycle", url: "https://leetcode.com/problems/linked-list-cycle/" },
          { num: "876", name: "Middle of Linked List", url: "https://leetcode.com/problems/middle-of-the-linked-list/" },
          { num: "202", name: "Happy Number", url: "https://leetcode.com/problems/happy-number/" }
        ],
        code: {
          "Java": `ListNode slow = head, fast = head;
while (fast != null && fast.next != null) {
    slow = slow.next;
    fast = fast.next.next;
    if (slow == fast) return true; // cycle!
}
// slow = middle when fast = null`,
          "Kotlin": `var slow = head; var fast = head
while (fast?.next != null) {
    slow = slow?.next; fast = fast.next?.next
    if (slow === fast) return true
}`,
          "Python": `slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast: return True`
        }
      }
    ]
  },

  // ─── 3. SLIDING WINDOW ───────────────────────────────────────────────────
  {
    title: "Sliding Window",
    color: "#9c7a2e",
    patterns: [
      {
        name: "Fixed Window",
        recognition: "Max/min/average over all subarrays of size K exactly.",
        mentalModel: "Initialize first K. Then slide: add right, remove left element.",
        pitfalls: "Build initial window before loop. Result after window reaches K.",
        problems: [
          { num: "643", name: "Max Avg Subarray I", url: "https://leetcode.com/problems/maximum-average-subarray-i/" }
        ],
        code: {
          "Java": `int sum = 0;
for (int i = 0; i < k; i++) sum += arr[i];
int best = sum;
for (int i = k; i < n; i++) {
    sum += arr[i] - arr[i-k];
    best = Math.max(best, sum);
}`,
          "Kotlin": `var sum = arr.take(k).sum(); var best = sum
for (i in k until arr.size) { sum += arr[i] - arr[i-k]; best = maxOf(best, sum) }`,
          "Python": `window = sum(arr[:k]); best = window
for i in range(k, len(arr)):
    window += arr[i] - arr[i-k]; best = max(best, window)`
        }
      },
      {
        name: "Variable Window",
        recognition: "Longest/shortest subarray satisfying condition. No fixed K.",
        mentalModel: "Expand right always. Shrink left WHILE invalid. Update result after shrink.",
        pitfalls: "Update result OUTSIDE while loop. Shrink until VALID.",
        problems: [
          { num: "3", name: "Longest Substring No Repeat", url: "https://leetcode.com/problems/longest-substring-without-repeating-characters/" },
          { num: "209", name: "Min Size Subarray Sum", url: "https://leetcode.com/problems/minimum-size-subarray-sum/" },
          { num: "424", name: "Longest Repeating Char Replace", url: "https://leetcode.com/problems/longest-repeating-character-replacement/" }
        ],
        code: {
          "Java": `int l = 0, res = 0;
Map<Character, Integer> win = new HashMap<>();
for (int r = 0; r < s.length(); r++) {
    win.merge(s.charAt(r), 1, Integer::sum);
    while (/* invalid */) {
        win.merge(s.charAt(l), -1, Integer::sum);
        if (win.get(s.charAt(l)) == 0) win.remove(s.charAt(l));
        l++;
    }
    res = Math.max(res, r - l + 1);
}`,
          "Kotlin": `var l = 0; var res = 0
val win = mutableMapOf<Char, Int>()
for (r in s.indices) {
    win[s[r]] = (win[s[r]] ?: 0) + 1
    while (/* invalid */) { win[s[l]] = win[s[l]]!! - 1; if (win[s[l]] == 0) win.remove(s[l]); l++ }
    res = maxOf(res, r - l + 1)
}`,
          "Python": `l = res = 0; win = {}
for r, c in enumerate(s):
    win[c] = win.get(c, 0) + 1
    while False:  # invalid condition
        win[s[l]] -= 1
        if win[s[l]] == 0: del win[s[l]]
        l += 1
    res = max(res, r - l + 1)`
        }
      },
      {
        name: "Frequency Map Window (Exactly K)",
        recognition: "Window with at most/exactly K distinct elements.",
        mentalModel: "Exactly K = atMost(K) - atMost(K-1). Shrink when map.size() > K.",
        pitfalls: "Remove key from map when count hits 0. Exactly K trick is key.",
        problems: [
          { num: "76", name: "Min Window Substring", url: "https://leetcode.com/problems/minimum-window-substring/" },
          { num: "992", name: "Subarrays with K Different", url: "https://leetcode.com/problems/subarrays-with-k-different-integers/" }
        ],
        code: {
          "Java": `// Min Window Substring
Map<Character,Integer> need = new HashMap<>(), win = new HashMap<>();
for (char c : t.toCharArray()) need.merge(c, 1, Integer::sum);
int formed=0, l=0, minLen=Integer.MAX_VALUE; String res="";
for (int r=0; r < s.length(); r++) {
    char c = s.charAt(r);
    win.merge(c, 1, Integer::sum);
    if (need.containsKey(c) && win.get(c).equals(need.get(c))) formed++;
    while (formed == need.size()) {
        if (r-l+1 < minLen) { minLen=r-l+1; res=s.substring(l,r+1); }
        char lc = s.charAt(l++);
        win.merge(lc,-1,Integer::sum);
        if (need.containsKey(lc) && win.get(lc) < need.get(lc)) formed--;
    }
}`,
          "Kotlin": `fun atMost(arr: IntArray, k: Int): Int {
    val freq = mutableMapOf<Int,Int>(); var l=0; var res=0
    for (r in arr.indices) {
        freq[arr[r]] = (freq[arr[r]] ?: 0) + 1
        while (freq.size > k) { freq[arr[l]] = freq[arr[l]]!!-1; if(freq[arr[l]]==0) freq.remove(arr[l]); l++ }
        res += r - l + 1
    }; return res
}`,
          "Python": `def at_most(arr, k):
    freq = {}; l = res = 0
    for r, x in enumerate(arr):
        freq[x] = freq.get(x, 0) + 1
        while len(freq) > k:
            freq[arr[l]] -= 1
            if freq[arr[l]] == 0: del freq[arr[l]]
            l += 1
        res += r - l + 1
    return res
# Exactly K = at_most(K) - at_most(K-1)`
        }
      }
    ]
  },

  // ─── 4. HASHMAP & HASHSET ─────────────────────────────────────────────────
  {
    title: "HashMap & HashSet",
    color: "#c47a2e",
    patterns: [
      {
        name: "Counting & Grouping",
        recognition: "Group anagrams. Top K frequent. Count occurrences by key.",
        mentalModel: "Map signature → group. Map element → count. Build then query.",
        pitfalls: "Arrays.sort() for anagram key. Always getOrDefault().",
        problems: [
          { num: "49", name: "Group Anagrams", url: "https://leetcode.com/problems/group-anagrams/" },
          { num: "347", name: "Top K Frequent", url: "https://leetcode.com/problems/top-k-frequent-elements/" }
        ],
        code: {
          "Java": `Map<String, List<String>> map = new HashMap<>();
for (String w : words) {
    char[] c = w.toCharArray(); Arrays.sort(c);
    map.computeIfAbsent(new String(c), k -> new ArrayList<>()).add(w);
}`,
          "Kotlin": `val map = mutableMapOf<String, MutableList<String>>()
for (w in words) {
    val key = w.toCharArray().sorted().joinToString("")
    map.getOrPut(key) { mutableListOf() }.add(w)
}`,
          "Python": `from collections import defaultdict
map = defaultdict(list)
for w in words: map[tuple(sorted(w))].append(w)`
        }
      },
      {
        name: "Lookup & Deduplication",
        recognition: "Check existence O(1). Longest consecutive. Contains duplicate.",
        mentalModel: "HashSet = O(1) contains. Only start sequence from element with no left neighbor.",
        pitfalls: "equals()/hashCode() for custom objects. Only start from sequence beginning.",
        problems: [
          { num: "128", name: "Longest Consecutive", url: "https://leetcode.com/problems/longest-consecutive-sequence/" },
          { num: "217", name: "Contains Duplicate", url: "https://leetcode.com/problems/contains-duplicate/" },
          { num: "1", name: "Two Sum", url: "https://leetcode.com/problems/two-sum/" }
        ],
        code: {
          "Java": `// Longest Consecutive O(N)
Set<Integer> set = new HashSet<>();
for (int n : nums) set.add(n);
int best = 0;
for (int n : set) {
    if (!set.contains(n-1)) { // start of sequence only!
        int len = 1;
        while (set.contains(n + len)) len++;
        best = Math.max(best, len);
    }
}`,
          "Kotlin": `val set = nums.toHashSet()
val best = set.filter { it-1 !in set }.maxOfOrNull { n ->
    var len=1; while(n+len in set) len++; len
} ?: 0`,
          "Python": `s = set(nums); best = 0
for n in s:
    if n - 1 not in s:
        length = 1
        while n + length in s: length += 1
        best = max(best, length)`
        }
      }
    ]
  },

  // ─── 5. STACK ────────────────────────────────────────────────────────────
  {
    title: "Stack",
    color: "#4f7a4a",
    patterns: [
      {
        name: "Basic Stack (Parentheses Matching)",
        recognition: "Matching pairs, undo operations, balanced brackets.",
        mentalModel: "Push opening brackets. On closing, pop and check match. Empty at end = valid.",
        pitfalls: "Pop on empty stack (check first!). Stack must be empty at end.",
        problems: [
          { num: "20", name: "Valid Parentheses", url: "https://leetcode.com/problems/valid-parentheses/" },
          { num: "155", name: "Min Stack", url: "https://leetcode.com/problems/min-stack/" }
        ],
        code: {
          "Java": `Map<Character,Character> map = Map.of(')','(', ']','[', '}','{');
Deque<Character> st = new ArrayDeque<>();
for (char c : s.toCharArray()) {
    if ("([{".indexOf(c) >= 0) st.push(c);
    else if (st.isEmpty() || st.pop() != map.get(c)) return false;
}
return st.isEmpty();`,
          "Kotlin": `val pair = mapOf(')' to '(', ']' to '[', '}' to '{')
val st = ArrayDeque<Char>()
for (c in s) {
    if (c in "([{") st.addLast(c)
    else if (st.isEmpty() || st.removeLast() != pair[c]) return false
}
return st.isEmpty()`,
          "Python": `pair = {')':'(', ']':'[', '}':'{'}
st = []
for c in s:
    if c in "([{": st.append(c)
    elif not st or st.pop() != pair[c]: return False
return len(st) == 0`
        }
      },
      {
        name: "Monotonic Decreasing Stack (Next Greater)",
        recognition: "Next greater element. Daily temperatures. Stock span.",
        mentalModel: "Pop elements SMALLER than current → they found their next greater. Stack stays decreasing.",
        pitfalls: "Store indices not values for distance. Pop when arr[stack.top] < arr[i].",
        problems: [
          { num: "739", name: "Daily Temperatures", url: "https://leetcode.com/problems/daily-temperatures/" },
          { num: "496", name: "Next Greater Element I", url: "https://leetcode.com/problems/next-greater-element-i/" }
        ],
        code: {
          "Java": `int[] res = new int[n];
Deque<Integer> st = new ArrayDeque<>(); // indices
for (int i = 0; i < n; i++) {
    while (!st.isEmpty() && arr[st.peek()] < arr[i]) {
        int idx = st.pop();
        res[idx] = i - idx; // days until warmer
    }
    st.push(i);
}`,
          "Kotlin": `val res = IntArray(n); val st = ArrayDeque<Int>()
for (i in 0 until n) {
    while (st.isNotEmpty() && arr[st.last()] < arr[i])
        res[st.removeLast()] = i - st.lastOrNull()!! // fix as needed
    st.addLast(i)
}`,
          "Python": `res = [0] * n; st = []
for i, x in enumerate(arr):
    while st and arr[st[-1]] < x:
        idx = st.pop()
        res[idx] = i - idx
    st.append(i)`
        }
      },
      {
        name: "Monotonic Increasing Stack (Next Smaller)",
        recognition: "Largest rectangle in histogram. Trapping rain water.",
        mentalModel: "Pop elements LARGER than current. Stack stays increasing.",
        pitfalls: "Add sentinel 0 at end for histogram. Width calculation using stack top.",
        problems: [
          { num: "84", name: "Largest Rectangle in Histogram", url: "https://leetcode.com/problems/largest-rectangle-in-histogram/" },
          { num: "42", name: "Trapping Rain Water", url: "https://leetcode.com/problems/trapping-rain-water/" }
        ],
        code: {
          "Java": `int res = 0;
Deque<Integer> st = new ArrayDeque<>();
for (int i = 0; i <= n; i++) {
    int h = (i == n) ? 0 : heights[i];
    while (!st.isEmpty() && heights[st.peek()] > h) {
        int height = heights[st.pop()];
        int width = st.isEmpty() ? i : i - st.peek() - 1;
        res = Math.max(res, height * width);
    }
    st.push(i);
}`,
          "Kotlin": `val st = ArrayDeque<Int>(); var res = 0
for (i in 0..n) {
    val h = if (i == n) 0 else heights[i]
    while (st.isNotEmpty() && heights[st.last()] > h) {
        val height = heights[st.removeLast()]
        val width = if (st.isEmpty()) i else i - st.last() - 1
        res = maxOf(res, height * width)
    }
    st.addLast(i)
}`,
          "Python": `st = []; res = 0
for i in range(len(heights) + 1):
    h = 0 if i == len(heights) else heights[i]
    while st and heights[st[-1]] > h:
        height = heights[st.pop()]
        width = i if not st else i - st[-1] - 1
        res = max(res, height * width)
    st.append(i)`
        }
      },
      {
        name: "Expression Evaluation",
        recognition: "Calculate string expression with +,-,*,/. Operators with precedence.",
        mentalModel: "Scan left-right. On + or -: push. On * or /: pop and compute. Sum stack at end.",
        pitfalls: "Handle negative numbers. Integer division truncates toward zero in Java.",
        problems: [
          { num: "224", name: "Basic Calculator", url: "https://leetcode.com/problems/basic-calculator/" },
          { num: "227", name: "Basic Calculator II", url: "https://leetcode.com/problems/basic-calculator-ii/" }
        ],
        code: {
          "Java": `// Basic Calculator II (+,-,*,/)
Deque<Integer> st = new ArrayDeque<>();
int num = 0; char op = '+';
for (int i = 0; i < s.length(); i++) {
    char c = s.charAt(i);
    if (Character.isDigit(c)) num = num * 10 + (c - '0');
    if (!Character.isDigit(c) && c != ' ' || i == s.length()-1) {
        if (op=='+') st.push(num);
        else if (op=='-') st.push(-num);
        else if (op=='*') st.push(st.pop() * num);
        else st.push(st.pop() / num);
        op = c; num = 0;
    }
}
int res = 0; while (!st.isEmpty()) res += st.pop();
return res;`,
          "Kotlin": `val st = ArrayDeque<Int>(); var num = 0; var op = '+'
for (i in s.indices) {
    val c = s[i]
    if (c.isDigit()) num = num * 10 + (c - '0')
    if (!c.isDigit() && c != ' ' || i == s.length-1) {
        when (op) { '+' -> st.addLast(num); '-' -> st.addLast(-num)
                    '*' -> st.addLast(st.removeLast() * num)
                    '/' -> st.addLast(st.removeLast() / num) }
        op = c; num = 0
    }
}`,
          "Python": `st = []; num = 0; op = '+'
s = s + '+'  # sentinel
for c in s:
    if c.isdigit(): num = num * 10 + int(c)
    elif c != ' ':
        if op == '+': st.append(num)
        elif op == '-': st.append(-num)
        elif op == '*': st.append(st.pop() * num)
        elif op == '/': st.append(int(st.pop() / num))
        op = c; num = 0
return sum(st)`
        }
      }
    ]
  },

  // ─── 6. QUEUE & DEQUE ────────────────────────────────────────────────────
  {
    title: "Queue & Deque",
    color: "#2e7a9c",
    patterns: [
      {
        name: "Basic Queue (FIFO)",
        recognition: "Process in order received. Level-by-level. First in first out.",
        mentalModel: "offer() adds to back. poll() removes from front. Use LinkedList or ArrayDeque.",
        pitfalls: "LinkedList is slower than ArrayDeque. Use peek() to check front without removing.",
        problems: [
          { num: "933", name: "Number of Recent Calls", url: "https://leetcode.com/problems/number-of-recent-calls/" },
          { num: "346", name: "Moving Average From Data Stream", url: "https://leetcode.com/problems/moving-average-from-data-stream/" }
        ],
        code: {
          "Java": `// Queue operations
Queue<Integer> q = new LinkedList<>(); // or ArrayDeque
q.offer(val);         // add to back
int front = q.poll(); // remove from front
int peek = q.peek();  // view front, don't remove
int size = q.size();  // number of elements
boolean empty = q.isEmpty();

// Moving average with queue
Deque<Integer> window = new ArrayDeque<>();
double sum = 0;
void add(int val) {
    window.offer(val); sum += val;
    if (window.size() > k) sum -= window.poll();
}`,
          "Kotlin": `val q = ArrayDeque<Int>()
q.addLast(val)         // offer
val front = q.removeFirst() // poll
val peek = q.first()   // peek`,
          "Python": `from collections import deque
q = deque()
q.append(val)       # add to back (offer)
front = q.popleft() # remove from front (poll)
peek = q[0]         # view front
# Moving average
window = deque(); total = 0
def add(val):
    window.append(val); total += val
    if len(window) > k: total -= window.popleft()`
        }
      },
      {
        name: "BFS Queue (Shortest Path)",
        recognition: "Shortest path unweighted. Minimum steps. Level-order traversal.",
        mentalModel: "Queue + visited set. Mark visited WHEN adding to queue. Process level by level with size snapshot.",
        pitfalls: "Mark visited BEFORE adding to queue, not after polling. Otherwise duplicates enter queue.",
        problems: [
          { num: "102", name: "Level Order Traversal", url: "https://leetcode.com/problems/binary-tree-level-order-traversal/" },
          { num: "127", name: "Word Ladder", url: "https://leetcode.com/problems/word-ladder/" },
          { num: "994", name: "Rotting Oranges", url: "https://leetcode.com/problems/rotting-oranges/" }
        ],
        code: {
          "Java": `Queue<Integer> q = new LinkedList<>();
boolean[] visited = new boolean[n];
q.offer(start); visited[start] = true; // ← mark when adding!
int steps = 0;
while (!q.isEmpty()) {
    int size = q.size(); // ← snapshot for level
    for (int i = 0; i < size; i++) {
        int node = q.poll();
        if (node == target) return steps;
        for (int nb : adj.get(node))
            if (!visited[nb]) { visited[nb]=true; q.offer(nb); }
    }
    steps++;
}`,
          "Kotlin": `val q = ArrayDeque<Int>(); val vis = BooleanArray(n)
q.addLast(start); vis[start] = true; var steps = 0
while (q.isNotEmpty()) {
    repeat(q.size) {
        val node = q.removeFirst()
        for (nb in adj[node]) if (!vis[nb]) { vis[nb]=true; q.addLast(nb) }
    }; steps++
}`,
          "Python": `from collections import deque
q = deque([start]); visited = {start}; steps = 0
while q:
    for _ in range(len(q)):
        node = q.popleft()
        if node == target: return steps
        for nb in adj[node]:
            if nb not in visited:
                visited.add(nb); q.append(nb)
    steps += 1`
        }
      },
      {
        name: "Monotonic Deque (Sliding Window Max)",
        recognition: "Sliding window maximum/minimum. O(N) instead of O(NK).",
        mentalModel: "Deque stores INDICES. Pop front if out of window. Pop back while smaller than current. Front = current max.",
        pitfalls: "Store indices not values. Deque front always = max of current window.",
        problems: [
          { num: "239", name: "Sliding Window Maximum", url: "https://leetcode.com/problems/sliding-window-maximum/" }
        ],
        code: {
          "Java": `Deque<Integer> dq = new ArrayDeque<>();
int[] res = new int[n - k + 1];
for (int i = 0; i < n; i++) {
    if (!dq.isEmpty() && dq.peekFirst() == i-k) dq.pollFirst(); // out of window
    while (!dq.isEmpty() && arr[dq.peekLast()] < arr[i]) dq.pollLast(); // remove smaller
    dq.offerLast(i);
    if (i >= k-1) res[i-k+1] = arr[dq.peekFirst()]; // front = max
}`,
          "Kotlin": `val dq = ArrayDeque<Int>(); val res = IntArray(n-k+1)
for (i in 0 until n) {
    if (dq.isNotEmpty() && dq.first() == i-k) dq.removeFirst()
    while (dq.isNotEmpty() && arr[dq.last()] < arr[i]) dq.removeLast()
    dq.addLast(i)
    if (i >= k-1) res[i-k+1] = arr[dq.first()]
}`,
          "Python": `from collections import deque
dq = deque(); res = []
for i, x in enumerate(arr):
    if dq and dq[0] == i-k: dq.popleft()
    while dq and arr[dq[-1]] < x: dq.pop()
    dq.append(i)
    if i >= k-1: res.append(arr[dq[0]])`
        }
      }
    ]
  },

  // ─── 7. BINARY SEARCH ────────────────────────────────────────────────────
  {
    title: "Binary Search",
    color: "#6b4f8a",
    patterns: [
      {
        name: "Classic Binary Search",
        recognition: "Find exact value in sorted array. O(log N).",
        mentalModel: "Halve search space each iteration. Mid = l + (r-l)/2.",
        pitfalls: "l+(r-l)/2 to avoid overflow. l<=r for exact match. l<r for boundary search.",
        problems: [
          { num: "704", name: "Binary Search", url: "https://leetcode.com/problems/binary-search/" }
        ],
        code: {
          "Java": `int l = 0, r = n - 1;
while (l <= r) {
    int mid = l + (r - l) / 2;
    if (arr[mid] == target) return mid;
    if (arr[mid] < target) l = mid + 1;
    else r = mid - 1;
}
return -1;`,
          "Kotlin": `var l = 0; var r = arr.size - 1
while (l <= r) {
    val mid = l + (r-l)/2
    when { arr[mid]==target -> return mid
           arr[mid]<target -> l=mid+1; else -> r=mid-1 }
}`,
          "Python": `l, r = 0, len(arr)-1
while l <= r:
    mid = l + (r-l)//2
    if arr[mid] == target: return mid
    if arr[mid] < target: l = mid + 1
    else: r = mid - 1`
        }
      },
      {
        name: "Lower Bound / Upper Bound",
        recognition: "First/last occurrence. First element >= target. Insert position.",
        mentalModel: "Lower: if arr[mid]>=target → r=mid. Upper: if arr[mid]>target → r=mid. Return l.",
        pitfalls: "r = n (not n-1). Return l not mid. l<r loop.",
        problems: [
          { num: "34", name: "First and Last Position", url: "https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/" },
          { num: "35", name: "Search Insert Position", url: "https://leetcode.com/problems/search-insert-position/" }
        ],
        code: {
          "Java": `// Lower bound: first index where arr[i] >= target
int l=0, r=n; // r=n not n-1!
while (l < r) {
    int m = l + (r-l)/2;
    if (arr[m] >= target) r = m;
    else l = m + 1;
}
return l; // l==r, first position >= target`,
          "Kotlin": `var l=0; var r=arr.size // r=n!
while (l < r) { val m=l+(r-l)/2; if(arr[m]>=target) r=m else l=m+1 }
return l`,
          "Python": `import bisect
# Lower bound (first >= target)
bisect.bisect_left(arr, target)
# Upper bound (first > target)
bisect.bisect_right(arr, target)
# Manual:
l, r = 0, len(arr)
while l < r:
    m = (l+r)//2
    if arr[m] >= target: r = m
    else: l = m + 1`
        }
      },
      {
        name: "Rotated Array Search",
        recognition: "Sorted but rotated at unknown pivot.",
        mentalModel: "One half is ALWAYS sorted. Check which half, then check if target is in it.",
        pitfalls: "Check arr[l]<=arr[mid] for left sorted (not <). Handle duplicates separately.",
        problems: [
          { num: "33", name: "Search in Rotated Array", url: "https://leetcode.com/problems/search-in-rotated-sorted-array/" },
          { num: "153", name: "Find Minimum in Rotated", url: "https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/" }
        ],
        code: {
          "Java": `int l=0, r=arr.length-1;
while (l <= r) {
    int m = l+(r-l)/2;
    if (arr[m]==target) return m;
    if (arr[l] <= arr[m]) { // left sorted
        if (target>=arr[l] && target<arr[m]) r=m-1;
        else l=m+1;
    } else { // right sorted
        if (target>arr[m] && target<=arr[r]) l=m+1;
        else r=m-1;
    }
}`,
          "Kotlin": `var l=0; var r=arr.size-1
while (l<=r) {
    val m=l+(r-l)/2
    if(arr[m]==target) return m
    if(arr[l]<=arr[m]) { if(target in arr[l] until arr[m]) r=m-1 else l=m+1 }
    else { if(target in (arr[m]+1)..arr[r]) l=m+1 else r=m-1 }
}`,
          "Python": `l, r = 0, len(arr)-1
while l <= r:
    m = (l+r)//2
    if arr[m]==target: return m
    if arr[l]<=arr[m]: # left sorted
        if arr[l]<=target<arr[m]: r=m-1
        else: l=m+1
    else: # right sorted
        if arr[m]<target<=arr[r]: l=m+1
        else: r=m-1`
        }
      },
      {
        name: "Binary Search on Answer",
        recognition: "Minimize max / Maximize min. 'Can we do X with Y speed?'",
        mentalModel: "Search the answer space. Write isValid(mid) function. If valid→try smaller, else→try larger.",
        pitfalls: "isValid logic is the hard part. Boundary values must cover all possible answers.",
        problems: [
          { num: "875", name: "Koko Eating Bananas", url: "https://leetcode.com/problems/koko-eating-bananas/" },
          { num: "410", name: "Split Array Largest Sum", url: "https://leetcode.com/problems/split-array-largest-sum/" },
          { num: "1011", name: "Capacity to Ship Packages", url: "https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/" }
        ],
        code: {
          "Java": `int l = minPossible, r = maxPossible;
while (l < r) {
    int mid = l + (r-l)/2;
    if (isValid(mid)) r = mid; // try smaller
    else l = mid + 1;
}
return l;
// isValid: can we achieve goal with parameter=mid?`,
          "Kotlin": `var l=minPossible; var r=maxPossible
while (l < r) { val mid=l+(r-l)/2; if(isValid(mid)) r=mid else l=mid+1 }
return l`,
          "Python": `l, r = min_possible, max_possible
while l < r:
    mid = (l+r)//2
    if is_valid(mid): r = mid  # try smaller
    else: l = mid + 1
return l`
        }
      }
    ]
  },

  // ─── 8. LINKED LIST ──────────────────────────────────────────────────────
  {
    title: "Linked List",
    color: "#7a2e5c",
    patterns: [
      {
        name: "Reverse Linked List",
        recognition: "Reverse entire or k-group or between positions.",
        mentalModel: "Three pointers: prev=null, curr=head, next. Flip curr.next=prev. Advance all.",
        pitfalls: "Save next BEFORE overwriting curr.next. Dummy node for edge cases.",
        problems: [
          { num: "206", name: "Reverse Linked List", url: "https://leetcode.com/problems/reverse-linked-list/" },
          { num: "92", name: "Reverse Linked List II", url: "https://leetcode.com/problems/reverse-linked-list-ii/" },
          { num: "25", name: "Reverse Nodes in K-Group", url: "https://leetcode.com/problems/reverse-nodes-in-k-group/" }
        ],
        code: {
          "Java": `ListNode prev = null, curr = head;
while (curr != null) {
    ListNode next = curr.next; // save next
    curr.next = prev;          // flip
    prev = curr; curr = next;  // advance
}
return prev; // new head`,
          "Kotlin": `var prev: ListNode? = null; var curr: ListNode? = head
while (curr != null) {
    val next = curr.next; curr.next = prev; prev = curr; curr = next
}
return prev`,
          "Python": `prev, curr = None, head
while curr:
    nxt = curr.next
    curr.next = prev
    prev, curr = curr, nxt
return prev`
        }
      },
      {
        name: "Find Middle & Remove Nth",
        recognition: "Find middle node. Remove nth from end. One-pass solutions.",
        mentalModel: "Fast pointer N steps ahead of slow. When fast hits end, slow is at target.",
        pitfalls: "Dummy node prevents edge case of removing head. Fast advances N+1 times for Nth.",
        problems: [
          { num: "876", name: "Middle of Linked List", url: "https://leetcode.com/problems/middle-of-the-linked-list/" },
          { num: "19", name: "Remove Nth From End", url: "https://leetcode.com/problems/remove-nth-node-from-end-of-list/" }
        ],
        code: {
          "Java": `// Middle: when fast reaches end, slow = middle
ListNode slow=head, fast=head;
while (fast!=null && fast.next!=null) { slow=slow.next; fast=fast.next.next; }
// slow = middle

// Remove Nth from end
ListNode dummy=new ListNode(0,head), fast=dummy, slow=dummy;
for (int i=0; i<=n; i++) fast=fast.next;
while (fast!=null) { slow=slow.next; fast=fast.next; }
slow.next = slow.next.next;
return dummy.next;`,
          "Kotlin": `// Middle
var slow=head; var fast=head
while(fast?.next!=null){slow=slow?.next;fast=fast.next?.next}`,
          "Python": `slow = fast = head
while fast and fast.next:
    slow = slow.next; fast = fast.next.next
# slow = middle`
        }
      },
      {
        name: "Cycle Detection & Entry Point",
        recognition: "Detect cycle. Find where cycle starts. Floyd's algorithm.",
        mentalModel: "Phase 1: fast+slow meet in cycle. Phase 2: move one pointer to head, advance both by 1 until they meet = entry.",
        pitfalls: "Phase 2 starts with slow=head, fast=meeting point (not head).",
        problems: [
          { num: "141", name: "Linked List Cycle", url: "https://leetcode.com/problems/linked-list-cycle/" },
          { num: "142", name: "Linked List Cycle II", url: "https://leetcode.com/problems/linked-list-cycle-ii/" }
        ],
        code: {
          "Java": `// Detect cycle
ListNode slow=head, fast=head;
while (fast!=null && fast.next!=null) {
    slow=slow.next; fast=fast.next.next;
    if (slow==fast) break; // cycle found!
}
if (fast==null||fast.next==null) return null; // no cycle
// Find entry point
slow = head;
while (slow != fast) { slow=slow.next; fast=fast.next; }
return slow; // entry node`,
          "Kotlin": `var slow=head; var fast=head; var hasCycle=false
while(fast?.next!=null){slow=slow?.next;fast=fast.next?.next;if(slow===fast){hasCycle=true;break}}
if(!hasCycle) return null
slow=head
while(slow!==fast){slow=slow?.next;fast=fast?.next}
return slow`,
          "Python": `slow = fast = head
while fast and fast.next:
    slow = slow.next; fast = fast.next.next
    if slow == fast: break
else: return None  # no cycle
slow = head
while slow != fast:
    slow = slow.next; fast = fast.next
return slow  # entry point`
        }
      },
      {
        name: "Merge Lists & Reorder",
        recognition: "Merge K sorted lists. Reorder L0→Ln→L1→Ln-1.",
        mentalModel: "Merge two: compare heads. Reorder: find mid + reverse second half + interleave.",
        pitfalls: "Merge K: use min-heap. Reorder: break second half connection after reversing.",
        problems: [
          { num: "21", name: "Merge Two Sorted Lists", url: "https://leetcode.com/problems/merge-two-sorted-lists/" },
          { num: "23", name: "Merge K Sorted Lists", url: "https://leetcode.com/problems/merge-k-sorted-lists/" },
          { num: "143", name: "Reorder List", url: "https://leetcode.com/problems/reorder-list/" }
        ],
        code: {
          "Java": `// Merge Two
ListNode dummy=new ListNode(0), cur=dummy;
while(l1!=null&&l2!=null) {
    if(l1.val<l2.val){cur.next=l1;l1=l1.next;}
    else{cur.next=l2;l2=l2.next;}
    cur=cur.next;
}
cur.next=(l1!=null)?l1:l2;
// Merge K: min-heap O(N logK)
PriorityQueue<ListNode> pq=new PriorityQueue<>((a,b)->a.val-b.val);
for(ListNode n:lists) if(n!=null) pq.offer(n);
while(!pq.isEmpty()){ListNode n=pq.poll();cur.next=n;cur=cur.next;if(n.next!=null)pq.offer(n.next);}`,
          "Kotlin": `val dummy=ListNode(0); var cur:ListNode?=dummy
while(l1!=null&&l2!=null){if(l1.`val`<l2.`val`){cur?.next=l1;l1=l1.next}else{cur?.next=l2;l2=l2.next};cur=cur?.next}
cur?.next=l1?:l2`,
          "Python": `dummy = cur = ListNode(0)
while l1 and l2:
    if l1.val < l2.val: cur.next, l1 = l1, l1.next
    else: cur.next, l2 = l2, l2.next
    cur = cur.next
cur.next = l1 or l2`
        }
      },
      {
        name: "Rotate List & Random Pointer",
        recognition: "Rotate by K. Copy list with random pointers.",
        mentalModel: "Rotate: find tail, make circular, break at (n-k)th node. Random: use HashMap old→new.",
        pitfalls: "Rotate: k = k%n to handle k>=n. Random: two-pass: create all nodes, then assign nexts and randoms.",
        problems: [
          { num: "61", name: "Rotate List", url: "https://leetcode.com/problems/rotate-list/" },
          { num: "138", name: "Copy List with Random Pointer", url: "https://leetcode.com/problems/copy-list-with-random-pointer/" }
        ],
        code: {
          "Java": `// Rotate List
int len=1; ListNode tail=head;
while(tail.next!=null){tail=tail.next;len++;}
k=k%len; if(k==0) return head;
tail.next=head; // make circular
int steps=len-k; ListNode newTail=head;
for(int i=0;i<steps-1;i++) newTail=newTail.next;
ListNode newHead=newTail.next; newTail.next=null;
return newHead;
// Random Pointer
Map<Node,Node> map=new HashMap<>();
Node cur=head;
while(cur!=null){map.put(cur,new Node(cur.val));cur=cur.next;}
cur=head;
while(cur!=null){map.get(cur).next=map.get(cur.next);map.get(cur).random=map.get(cur.random);cur=cur.next;}`,
          "Kotlin": `// Rotate: find len, k%=len, make circular, break at len-k`,
          "Python": `# Random Pointer
map = {}
cur = head
while cur: map[cur] = Node(cur.val); cur = cur.next
cur = head
while cur:
    if cur.next: map[cur].next = map[cur.next]
    if cur.random: map[cur].random = map[cur.random]
    cur = cur.next
return map[head]`
        }
      }
    ]
  },

  // ─── 9. TREES ────────────────────────────────────────────────────────────
  {
    title: "Trees (DFS & BFS)",
    color: "#5a3a8a",
    patterns: [
      {
        name: "🌿 Preorder DFS (Root → Left → Right)",
        recognition: "Serialize tree. Copy structure. Print top-down.",
        mentalModel: "Visit root FIRST, then go left, then right. Use stack for iterative.",
        pitfalls: "Always check null FIRST. Iterative: push right before left (stack is LIFO).",
        problems: [
          { num: "144", name: "Binary Tree Preorder", url: "https://leetcode.com/problems/binary-tree-preorder-traversal/" },
          { num: "105", name: "Construct from Preorder+Inorder", url: "https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/" }
        ],
        code: {
          "Java": `void preorder(TreeNode root, List<Integer> res) {
    if (root == null) return;    // ← null check first!
    res.add(root.val);           // 1. ROOT
    preorder(root.left, res);    // 2. Left
    preorder(root.right, res);   // 3. Right
}
// Iterative
Deque<TreeNode> st = new ArrayDeque<>();
st.push(root);
while (!st.isEmpty()) {
    TreeNode n = st.pop();
    res.add(n.val);
    if (n.right != null) st.push(n.right); // right FIRST (LIFO)
    if (n.left  != null) st.push(n.left);
}`,
          "Kotlin": `fun preorder(root: TreeNode?, res: MutableList<Int>) {
    if (root == null) return
    res.add(root.\`val\`)        // root
    preorder(root.left, res)   // left
    preorder(root.right, res)  // right
}`,
          "Python": `def preorder(root, res=[]):
    if not root: return
    res.append(root.val)        # root
    preorder(root.left, res)    # left
    preorder(root.right, res)   # right`
        }
      },
      {
        name: "🌿 Inorder DFS (Left → Root → Right)",
        recognition: "BST sorted order. Kth smallest. Validate BST. Morris traversal.",
        mentalModel: "Go ALL the way left, then visit root, then right. BST Inorder = sorted array!",
        pitfalls: "BST validate: pass (min,max) bounds, not just previous node.",
        problems: [
          { num: "94", name: "Binary Tree Inorder", url: "https://leetcode.com/problems/binary-tree-inorder-traversal/" },
          { num: "230", name: "Kth Smallest in BST", url: "https://leetcode.com/problems/kth-smallest-element-in-a-bst/" },
          { num: "98", name: "Validate BST", url: "https://leetcode.com/problems/validate-binary-search-tree/" }
        ],
        code: {
          "Java": `void inorder(TreeNode root, List<Integer> res) {
    if (root == null) return;
    inorder(root.left, res);     // 1. Left
    res.add(root.val);           // 2. ROOT ← middle!
    inorder(root.right, res);    // 3. Right
}
// BST Inorder = SORTED array
// Iterative Inorder
Deque<TreeNode> st = new ArrayDeque<>();
TreeNode curr = root;
while (curr != null || !st.isEmpty()) {
    while (curr != null) { st.push(curr); curr = curr.left; }
    curr = st.pop(); res.add(curr.val); curr = curr.right;
}`,
          "Kotlin": `fun inorder(root: TreeNode?, res: MutableList<Int>) {
    if (root == null) return
    inorder(root.left, res)
    res.add(root.\`val\`)         // ROOT in middle
    inorder(root.right, res)
}`,
          "Python": `def inorder(root, res=[]):
    if not root: return
    inorder(root.left, res)
    res.append(root.val)        # ROOT in middle
    inorder(root.right, res)
# BST inorder → sorted!`
        }
      },
      {
        name: "🌿 Postorder DFS (Left → Right → Root)",
        recognition: "Height, diameter, delete tree, evaluate tree, Tree DP.",
        mentalModel: "Calculate children first, THEN process root. Information flows up from leaves.",
        pitfalls: "Diameter: global variable for answer, return height. Don't confuse return value with answer.",
        problems: [
          { num: "145", name: "Binary Tree Postorder", url: "https://leetcode.com/problems/binary-tree-postorder-traversal/" },
          { num: "104", name: "Max Depth", url: "https://leetcode.com/problems/maximum-depth-of-binary-tree/" },
          { num: "543", name: "Diameter of Binary Tree", url: "https://leetcode.com/problems/diameter-of-binary-tree/" }
        ],
        code: {
          "Java": `void postorder(TreeNode root, List<Integer> res) {
    if (root == null) return;
    postorder(root.left, res);   // 1. Left
    postorder(root.right, res);  // 2. Right
    res.add(root.val);           // 3. ROOT ← last!
}
// Max Depth (postorder)
int maxDepth(TreeNode root) {
    if (root == null) return 0;
    return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
}
// Diameter: global max, return height
int ans = 0;
int dfs(TreeNode root) {
    if (root == null) return 0;
    int l = dfs(root.left), r = dfs(root.right);
    ans = Math.max(ans, l + r); // update GLOBAL
    return 1 + Math.max(l, r);  // return HEIGHT
}`,
          "Kotlin": `fun maxDepth(root: TreeNode?): Int {
    if (root == null) return 0
    return 1 + maxOf(maxDepth(root.left), maxDepth(root.right))
}`,
          "Python": `def max_depth(root):
    if not root: return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

ans = [0]
def dfs(root):
    if not root: return 0
    l, r = dfs(root.left), dfs(root.right)
    ans[0] = max(ans[0], l + r)  # global max
    return 1 + max(l, r)          # return height`
        }
      },
      {
        name: "🌊 BFS Level Order (List<List<Integer>>)",
        recognition: "Level-by-level. Right/Left side view. Zigzag. Min depth.",
        mentalModel: "Queue + SNAPSHOT size at start of level loop. Inner for processes ONE level.",
        pitfalls: "Snapshot q.size() BEFORE inner loop — don't call it inside!",
        problems: [
          { num: "102", name: "Level Order Traversal", url: "https://leetcode.com/problems/binary-tree-level-order-traversal/" },
          { num: "199", name: "Right Side View", url: "https://leetcode.com/problems/binary-tree-right-side-view/" },
          { num: "103", name: "Zigzag Level Order", url: "https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/" },
          { num: "111", name: "Minimum Depth", url: "https://leetcode.com/problems/minimum-depth-of-binary-tree/" }
        ],
        code: {
          "Java": `List<List<Integer>> res = new ArrayList<>();
if (root == null) return res;
Queue<TreeNode> q = new LinkedList<>();
q.offer(root);
boolean leftToRight = true;
while (!q.isEmpty()) {
    int size = q.size(); // ← SNAPSHOT HERE!
    LinkedList<Integer> level = new LinkedList<>();
    for (int i = 0; i < size; i++) { // ← process one level
        TreeNode n = q.poll();
        if (leftToRight) level.addLast(n.val);
        else level.addFirst(n.val); // zigzag
        if (n.left  != null) q.offer(n.left);
        if (n.right != null) q.offer(n.right);
    }
    res.add(level);
    leftToRight = !leftToRight; // flip for zigzag
}
// Right Side View: res.add(level.getLast())
// Left Side View:  res.add(level.getFirst())`,
          "Kotlin": `val q = ArrayDeque<TreeNode>(); q.addLast(root)
while (q.isNotEmpty()) {
    val size = q.size    // snapshot!
    val level = mutableListOf<Int>()
    repeat(size) {
        val n = q.removeFirst()
        level.add(n.\`val\`)
        n.left?.let { q.addLast(it) }
        n.right?.let { q.addLast(it) }
    }
    res.add(level)
}`,
          "Python": `from collections import deque
res = []; q = deque([root]) if root else deque()
left_to_right = True
while q:
    level = []
    for _ in range(len(q)):    # snapshot len(q)!
        n = q.popleft()
        level.append(n.val)
        if n.left:  q.append(n.left)
        if n.right: q.append(n.right)
    if not left_to_right: level.reverse()  # zigzag
    res.append(level)
    left_to_right = not left_to_right`
        }
      },
      {
        name: "🔑 Balanced, Max Path Sum, LCA",
        recognition: "Check height balance. Max path through any node. Find LCA.",
        mentalModel: "Balanced: postorder return height or -1 if unbalanced. MaxPath: track global via left+root+right.",
        pitfalls: "Max Path Sum: include root.val in answer but can only extend one direction upward.",
        problems: [
          { num: "110", name: "Balanced Binary Tree", url: "https://leetcode.com/problems/balanced-binary-tree/" },
          { num: "124", name: "Binary Tree Max Path Sum", url: "https://leetcode.com/problems/binary-tree-maximum-path-sum/" },
          { num: "236", name: "LCA of Binary Tree", url: "https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/" }
        ],
        code: {
          "Java": `// Balanced: return -1 if unbalanced
int check(TreeNode root) {
    if (root == null) return 0;
    int l = check(root.left), r = check(root.right);
    if (l==-1 || r==-1 || Math.abs(l-r)>1) return -1;
    return 1 + Math.max(l, r);
}
// Max Path Sum
int maxSum = Integer.MIN_VALUE;
int dfs(TreeNode root) {
    if (root == null) return 0;
    int l = Math.max(0, dfs(root.left));  // ignore negative
    int r = Math.max(0, dfs(root.right)); // ignore negative
    maxSum = Math.max(maxSum, l + root.val + r);
    return root.val + Math.max(l, r); // extend ONE side up
}
// LCA
TreeNode lca(TreeNode root, TreeNode p, TreeNode q) {
    if (root==null||root==p||root==q) return root;
    TreeNode l=lca(root.left,p,q), r=lca(root.right,p,q);
    return (l!=null&&r!=null)?root:(l!=null?l:r);
}`,
          "Kotlin": `fun check(root: TreeNode?): Int {
    if (root == null) return 0
    val l=check(root.left); val r=check(root.right)
    if (l==-1||r==-1||Math.abs(l-r)>1) return -1
    return 1+maxOf(l,r)
}`,
          "Python": `# Max Path Sum
max_sum = [float('-inf')]
def dfs(root):
    if not root: return 0
    l = max(0, dfs(root.left))   # ignore negative
    r = max(0, dfs(root.right))  # ignore negative
    max_sum[0] = max(max_sum[0], l + root.val + r)
    return root.val + max(l, r)  # extend ONE side`
        }
      },
      {
        name: "🌳 Validate BST & BST Operations",
        recognition: "BST property: all left < root < all right (not just parent).",
        mentalModel: "Pass (min, max) bounds at each node. Left narrows max, right narrows min.",
        pitfalls: "Integer overflow with INT_MIN/MAX → use Long. BST insert/delete are recursive.",
        problems: [
          { num: "98", name: "Validate BST", url: "https://leetcode.com/problems/validate-binary-search-tree/" },
          { num: "701", name: "Insert into a BST", url: "https://leetcode.com/problems/insert-into-a-binary-search-tree/" },
          { num: "450", name: "Delete Node in BST", url: "https://leetcode.com/problems/delete-node-in-a-bst/" }
        ],
        code: {
          "Java": `// Validate BST with bounds
boolean isValid(TreeNode root, long min, long max) {
    if (root == null) return true;
    if (root.val <= min || root.val >= max) return false;
    return isValid(root.left, min, root.val) &&
           isValid(root.right, root.val, max);
}
// Call: isValid(root, Long.MIN_VALUE, Long.MAX_VALUE)

// Insert into BST
TreeNode insert(TreeNode root, int val) {
    if (root == null) return new TreeNode(val);
    if (val < root.val) root.left = insert(root.left, val);
    else root.right = insert(root.right, val);
    return root;
}`,
          "Kotlin": `fun isValid(root: TreeNode?, min: Long, max: Long): Boolean {
    if (root == null) return true
    if (root.\`val\`.toLong() <= min || root.\`val\`.toLong() >= max) return false
    return isValid(root.left, min, root.\`val\`.toLong()) &&
           isValid(root.right, root.\`val\`.toLong(), max)
}`,
          "Python": `def is_valid(root, min_val=float('-inf'), max_val=float('inf')):
    if not root: return True
    if not (min_val < root.val < max_val): return False
    return (is_valid(root.left, min_val, root.val) and
            is_valid(root.right, root.val, max_val))`
        }
      }
    ]
  },

  // ─── 10. HEAP / PRIORITY QUEUE ───────────────────────────────────────────
  {
    title: "Heap / Priority Queue",
    color: "#2e6b7a",
    patterns: [
      {
        name: "Min Heap & Max Heap Basics",
        recognition: "Always get smallest (min-heap) or largest (max-heap) in O(log N).",
        mentalModel: "Min-heap: smallest on top. Max-heap: negate values in Python. Java: reverseOrder().",
        pitfalls: "Python heapq is min-heap only. Negate for max-heap. Java comparator (a,b)->b-a for max.",
        problems: [
          { num: "703", name: "Kth Largest in Stream", url: "https://leetcode.com/problems/kth-largest-element-in-a-stream/" }
        ],
        code: {
          "Java": `// Min-Heap (default)
PriorityQueue<Integer> minH = new PriorityQueue<>();
minH.offer(5); minH.offer(1); minH.offer(3);
int min = minH.peek(); // 1, O(1)
int removed = minH.poll(); // 1, O(logN)

// Max-Heap
PriorityQueue<Integer> maxH = new PriorityQueue<>(Collections.reverseOrder());
// or: new PriorityQueue<>((a,b) -> b-a)

// Custom comparator (by index 0)
PriorityQueue<int[]> pq = new PriorityQueue<>((a,b) -> a[0]-b[0]);`,
          "Kotlin": `val minH = PriorityQueue<Int>()     // min-heap
val maxH = PriorityQueue<Int>(compareByDescending{it}) // max-heap
minH.offer(5); val top = minH.poll()`,
          "Python": `import heapq
# Min-heap
h = []; heapq.heappush(h, 5)
top = heapq.heappop(h)  # smallest

# Max-heap (negate values!)
maxH = []
heapq.heappush(maxH, -5)   # push negated
top = -heapq.heappop(maxH) # negate back

# Heapify in-place O(N)
arr = [3,1,4,1,5]; heapq.heapify(arr)`
        }
      },
      {
        name: "Top K Problems",
        recognition: "K largest, K smallest, K most frequent, K closest.",
        mentalModel: "Top K Largest → min-heap of size K. Top K Smallest → max-heap of size K. Pop when size > K.",
        pitfalls: "Min-heap for LARGEST (counterintuitive). Size limit K is key.",
        problems: [
          { num: "215", name: "Kth Largest Element", url: "https://leetcode.com/problems/kth-largest-element-in-an-array/" },
          { num: "347", name: "Top K Frequent Elements", url: "https://leetcode.com/problems/top-k-frequent-elements/" },
          { num: "973", name: "K Closest Points to Origin", url: "https://leetcode.com/problems/k-closest-points-to-origin/" }
        ],
        code: {
          "Java": `// Top K Largest → min-heap size K
PriorityQueue<Integer> pq = new PriorityQueue<>();
for (int x : arr) {
    pq.offer(x);
    if (pq.size() > k) pq.poll(); // pop smallest
}
return pq.peek(); // kth largest

// K Closest Points (by distance)
PriorityQueue<int[]> pq = new PriorityQueue<>(
    (a,b) -> (b[0]*b[0]+b[1]*b[1]) - (a[0]*a[0]+a[1]*a[1])); // max-heap by dist
for (int[] p : points) {
    pq.offer(p);
    if (pq.size() > k) pq.poll();
}`,
          "Kotlin": `val pq = PriorityQueue<Int>()
for (x in arr) { pq.offer(x); if(pq.size>k) pq.poll() }
return pq.peek()`,
          "Python": `import heapq
# Top K Largest
heap = []
for x in arr:
    heapq.heappush(heap, x)
    if len(heap) > k: heapq.heappop(heap)
return heap[0]

# Pythonic: nlargest
heapq.nlargest(k, arr)  # O(N logK)`
        }
      },
      {
        name: "Merge K Sorted Lists & K-way Merge",
        recognition: "Merge multiple sorted lists/arrays into one sorted stream.",
        mentalModel: "Min-heap stores (value, listIndex, elementIndex). Always pop smallest, push next from same list.",
        pitfalls: "Push next element from same list after popping. Handle empty lists.",
        problems: [
          { num: "23", name: "Merge K Sorted Lists", url: "https://leetcode.com/problems/merge-k-sorted-lists/" },
          { num: "295", name: "Find Median from Data Stream", url: "https://leetcode.com/problems/find-median-from-data-stream/" }
        ],
        code: {
          "Java": `// Merge K Lists
PriorityQueue<ListNode> pq = new PriorityQueue<>((a,b)->a.val-b.val);
for (ListNode n : lists) if (n!=null) pq.offer(n);
ListNode dummy=new ListNode(0), cur=dummy;
while (!pq.isEmpty()) {
    ListNode n=pq.poll(); cur.next=n; cur=cur.next;
    if (n.next!=null) pq.offer(n.next);
}
// Median from Stream: two heaps
PriorityQueue<Integer> lo=new PriorityQueue<>(reverseOrder()); // max
PriorityQueue<Integer> hi=new PriorityQueue<>(); // min
void add(int n){lo.offer(n);hi.offer(lo.poll());if(lo.size()<hi.size())lo.offer(hi.poll());}
double median(){return lo.size()>hi.size()?lo.peek():(lo.peek()+hi.peek())/2.0;}`,
          "Kotlin": `val pq=PriorityQueue<ListNode>(compareBy{it.\`val\`})
for(n in lists) if(n!=null) pq.offer(n)`,
          "Python": `import heapq
# K-way merge
heap = [(lists[i].val, i, lists[i]) for i in range(len(lists)) if lists[i]]
heapq.heapify(heap)
dummy = cur = ListNode(0)
while heap:
    val, i, node = heapq.heappop(heap)
    cur.next = node; cur = cur.next
    if node.next: heapq.heappush(heap, (node.next.val, i, node.next))`
        }
      }
    ]
  },

  // ─── 11. BACKTRACKING ────────────────────────────────────────────────────
  {
    title: "Backtracking",
    color: "#8a3a4f",
    patterns: [
      {
        name: "Subsets & Combinations",
        recognition: "All subsets. Combinations of size K. Power set.",
        mentalModel: "At each index: include → recurse → exclude (backtrack). Start index prevents duplicates.",
        pitfalls: "Add COPY of path (new ArrayList<>(path)). Use start index for combinations.",
        problems: [
          { num: "78", name: "Subsets", url: "https://leetcode.com/problems/subsets/" },
          { num: "90", name: "Subsets II (Duplicates)", url: "https://leetcode.com/problems/subsets-ii/" },
          { num: "77", name: "Combinations", url: "https://leetcode.com/problems/combinations/" }
        ],
        code: {
          "Java": `void backtrack(int start, List<Integer> path) {
    res.add(new ArrayList<>(path)); // ← add COPY
    for (int i = start; i < nums.length; i++) {
        if (i > start && nums[i] == nums[i-1]) continue; // skip dups
        path.add(nums[i]);
        backtrack(i + 1, path);  // i+1 for no-reuse, i for reuse
        path.remove(path.size()-1); // ← backtrack
    }
}
// Call: Arrays.sort(nums); backtrack(0, new ArrayList<>());`,
          "Kotlin": `fun backtrack(start: Int, path: MutableList<Int>) {
    res.add(path.toList()) // copy
    for (i in start until nums.size) {
        if (i > start && nums[i] == nums[i-1]) continue
        path.add(nums[i]); backtrack(i+1, path); path.removeLast()
    }
}`,
          "Python": `def backtrack(start, path):
    res.append(list(path))  # copy!
    for i in range(start, len(nums)):
        if i > start and nums[i] == nums[i-1]: continue  # skip dups
        path.append(nums[i])
        backtrack(i + 1, path)
        path.pop()`
        }
      },
      {
        name: "Combination Sum",
        recognition: "Find all combinations that sum to target. Elements can repeat.",
        mentalModel: "Same as subsets but check target. Pass i (not i+1) to allow reuse.",
        pitfalls: "Sort nums first. Prune with if nums[i] > target: break.",
        problems: [
          { num: "39", name: "Combination Sum", url: "https://leetcode.com/problems/combination-sum/" },
          { num: "40", name: "Combination Sum II", url: "https://leetcode.com/problems/combination-sum-ii/" }
        ],
        code: {
          "Java": `void backtrack(int start, int target, List<Integer> path) {
    if (target == 0) { res.add(new ArrayList<>(path)); return; }
    for (int i = start; i < nums.length; i++) {
        if (nums[i] > target) break; // pruning!
        path.add(nums[i]);
        backtrack(i, target-nums[i], path); // i = allow reuse
        path.remove(path.size()-1);
    }
}`,
          "Kotlin": `fun backtrack(start: Int, target: Int, path: MutableList<Int>) {
    if (target == 0) { res.add(path.toList()); return }
    for (i in start until nums.size) {
        if (nums[i] > target) break
        path.add(nums[i]); backtrack(i, target-nums[i], path); path.removeLast()
    }
}`,
          "Python": `def backtrack(start, target, path):
    if target == 0: res.append(list(path)); return
    for i in range(start, len(nums)):
        if nums[i] > target: break  # pruning
        path.append(nums[i])
        backtrack(i, target - nums[i], path)  # i = allow reuse
        path.pop()`
        }
      },
      {
        name: "Permutations",
        recognition: "All orderings. Each element used exactly once.",
        mentalModel: "Track used[]. Loop all elements each time. Mark/unmark as you go.",
        pitfalls: "Start loop from 0 (not i) every call. used[] array must be reset.",
        problems: [
          { num: "46", name: "Permutations", url: "https://leetcode.com/problems/permutations/" },
          { num: "47", name: "Permutations II (Duplicates)", url: "https://leetcode.com/problems/permutations-ii/" }
        ],
        code: {
          "Java": `void backtrack(List<Integer> path, boolean[] used) {
    if (path.size() == nums.length) { res.add(new ArrayList<>(path)); return; }
    for (int i = 0; i < nums.length; i++) {
        if (used[i]) continue;
        if (i>0 && nums[i]==nums[i-1] && !used[i-1]) continue; // skip dups
        used[i] = true; path.add(nums[i]);
        backtrack(path, used);
        used[i] = false; path.remove(path.size()-1);
    }
}`,
          "Kotlin": `fun backtrack(path: MutableList<Int>, used: BooleanArray) {
    if (path.size == nums.size) { res.add(path.toList()); return }
    for (i in nums.indices) {
        if (used[i] || i>0 && nums[i]==nums[i-1] && !used[i-1]) continue
        used[i]=true; path.add(nums[i]); backtrack(path,used)
        used[i]=false; path.removeLast()
    }
}`,
          "Python": `def backtrack(path, used):
    if len(path) == len(nums): res.append(list(path)); return
    for i in range(len(nums)):
        if used[i]: continue
        if i > 0 and nums[i] == nums[i-1] and not used[i-1]: continue
        used[i] = True; path.append(nums[i])
        backtrack(path, used)
        used[i] = False; path.pop()`
        }
      },
      {
        name: "N-Queens & Word Search",
        recognition: "Constraint satisfaction on grid. Place N queens. Find word in grid.",
        mentalModel: "Try each position. Check validity. Recurse. Undo if invalid.",
        pitfalls: "Track cols + diagonals (row-col) + anti-diagonals (row+col) for N-Queens.",
        problems: [
          { num: "51", name: "N-Queens", url: "https://leetcode.com/problems/n-queens/" },
          { num: "79", name: "Word Search", url: "https://leetcode.com/problems/word-search/" }
        ],
        code: {
          "Java": `// N-Queens
Set<Integer> cols=new HashSet<>(), d1=new HashSet<>(), d2=new HashSet<>();
void solve(int row) {
    if (row == n) { res.add(build()); return; }
    for (int col = 0; col < n; col++) {
        if (cols.contains(col)||d1.contains(row-col)||d2.contains(row+col)) continue;
        cols.add(col); d1.add(row-col); d2.add(row+col); queens[row]=col;
        solve(row+1);
        cols.remove(col); d1.remove(row-col); d2.remove(row+col);
    }
}
// Word Search
boolean dfs(int r, int c, int i) {
    if (i==word.length()) return true;
    if (r<0||c<0||r>=R||c>=C||board[r][c]!=word.charAt(i)) return false;
    char tmp=board[r][c]; board[r][c]='#'; // mark visited
    boolean found=dfs(r+1,c,i+1)||dfs(r-1,c,i+1)||dfs(r,c+1,i+1)||dfs(r,c-1,i+1);
    board[r][c]=tmp; // restore
    return found;
}`,
          "Kotlin": `// Word Search
fun dfs(r:Int,c:Int,i:Int):Boolean {
    if(i==word.length) return true
    if(r!in 0 until R||c!in 0 until C||board[r][c]!=word[i]) return false
    val tmp=board[r][c]; board[r][c]='#'
    val found=dfs(r+1,c,i+1)||dfs(r-1,c,i+1)||dfs(r,c+1,i+1)||dfs(r,c-1,i+1)
    board[r][c]=tmp; return found
}`,
          "Python": `def dfs(r, c, i):
    if i == len(word): return True
    if r<0 or r>=R or c<0 or c>=C or board[r][c]!=word[i]: return False
    tmp=board[r][c]; board[r][c]='#'  # mark
    res=(dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or
         dfs(r,c+1,i+1) or dfs(r,c-1,i+1))
    board[r][c]=tmp  # restore
    return res`
        }
      }
    ]
  },

  // ─── 12. GRAPHS ──────────────────────────────────────────────────────────
  {
    title: "Graphs",
    color: "#3a5a8a",
    patterns: [
      {
        name: "Graph Representation",
        recognition: "Build graph from edge list. Adjacency list vs matrix.",
        mentalModel: "Adjacency list: Map<Integer, List<Integer>>. Better for sparse graphs. Matrix: O(V²) space.",
        pitfalls: "Undirected: add both directions. Directed: one direction only.",
        problems: [
          { num: "207", name: "Course Schedule", url: "https://leetcode.com/problems/course-schedule/" }
        ],
        code: {
          "Java": `// Adjacency List (most common)
List<List<Integer>> adj = new ArrayList<>();
for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
for (int[] e : edges) {
    adj.get(e[0]).add(e[1]); // directed
    adj.get(e[1]).add(e[0]); // undirected: also add reverse
}
// Weighted: List<int[]> where int[] = {neighbor, weight}`,
          "Kotlin": `val adj = List(n) { mutableListOf<Int>() }
for ((u, v) in edges) { adj[u].add(v); adj[v].add(u) }`,
          "Python": `from collections import defaultdict
adj = defaultdict(list)
for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)  # undirected`
        }
      },
      {
        name: "Graph DFS",
        recognition: "Connected components. All paths. Cycle detection. Flood fill. Islands.",
        mentalModel: "Recursion + visited. Mark BEFORE recursing. Explores deepest path first.",
        pitfalls: "Mark visited BEFORE recursing (not after). Grid DFS: mark cell in-place.",
        problems: [
          { num: "200", name: "Number of Islands", url: "https://leetcode.com/problems/number-of-islands/" },
          { num: "695", name: "Max Area of Island", url: "https://leetcode.com/problems/max-area-of-island/" },
          { num: "133", name: "Clone Graph", url: "https://leetcode.com/problems/clone-graph/" }
        ],
        code: {
          "Java": `// General DFS
void dfs(int node, boolean[] vis) {
    vis[node] = true; // ← BEFORE recursing
    for (int nb : adj.get(node))
        if (!vis[nb]) dfs(nb, vis);
}
// Count components
int count = 0;
for (int i=0;i<n;i++) if(!vis[i]){dfs(i,vis);count++;}

// Grid DFS (Islands)
void dfs(char[][] g, int r, int c) {
    if (r<0||r>=g.length||c<0||c>=g[0].length||g[r][c]=='0') return;
    g[r][c]='0'; // mark visited
    dfs(g,r+1,c);dfs(g,r-1,c);dfs(g,r,c+1);dfs(g,r,c-1);
}`,
          "Kotlin": `fun dfs(node: Int, vis: BooleanArray) {
    vis[node] = true
    for (nb in adj[node]) if (!vis[nb]) dfs(nb, vis)
}`,
          "Python": `# DFS with visited set
def dfs(node, visited, adj):
    visited.add(node)  # mark FIRST
    for nb in adj[node]:
        if nb not in visited: dfs(nb, visited, adj)

# Grid DFS
def dfs(r, c):
    if r<0 or r>=R or c<0 or c>=C or grid[r][c]=='0': return
    grid[r][c]='0'  # mark visited in-place
    for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]: dfs(r+dr, c+dc)`
        }
      },
      {
        name: "Graph BFS",
        recognition: "Shortest path (unweighted). Min steps. Level distance.",
        mentalModel: "Queue + visited. Mark visited WHEN adding (not polling). Process level by level.",
        pitfalls: "Mark visited when ADDING to queue. Not when polling. Otherwise O(V²) revisits.",
        problems: [
          { num: "127", name: "Word Ladder", url: "https://leetcode.com/problems/word-ladder/" },
          { num: "994", name: "Rotting Oranges", url: "https://leetcode.com/problems/rotting-oranges/" },
          { num: "542", name: "01 Matrix", url: "https://leetcode.com/problems/01-matrix/" }
        ],
        code: {
          "Java": `Queue<Integer> q = new LinkedList<>();
boolean[] vis = new boolean[n];
q.offer(start); vis[start]=true; // ← mark when adding!
int steps=0;
while (!q.isEmpty()) {
    int size=q.size(); // level snapshot
    for (int i=0;i<size;i++) {
        int node=q.poll();
        if (node==target) return steps;
        for (int nb:adj.get(node))
            if(!vis[nb]){vis[nb]=true;q.offer(nb);}
    }
    steps++;
}`,
          "Kotlin": `val q=ArrayDeque<Int>(); val vis=BooleanArray(n)
q.addLast(start); vis[start]=true; var steps=0
while(q.isNotEmpty()){
    repeat(q.size){val node=q.removeFirst()
        for(nb in adj[node]) if(!vis[nb]){vis[nb]=true;q.addLast(nb)}}
    steps++}`,
          "Python": `from collections import deque
q=deque([start]); vis={start}; steps=0
while q:
    for _ in range(len(q)):
        node=q.popleft()
        if node==target: return steps
        for nb in adj[node]:
            if nb not in vis: vis.add(nb); q.append(nb)
    steps+=1`
        }
      },
      {
        name: "Cycle Detection & Bipartite",
        recognition: "Has cycle? Can 2-color graph? Course is completable?",
        mentalModel: "Directed cycle: state 0=unvis,1=in-stack,2=done. Bipartite: color 0/1, check neighbors.",
        pitfalls: "Directed graph: in-stack state (1) ≠ visited state (2). Undirected: skip parent.",
        problems: [
          { num: "207", name: "Course Schedule", url: "https://leetcode.com/problems/course-schedule/" },
          { num: "785", name: "Is Graph Bipartite?", url: "https://leetcode.com/problems/is-graph-bipartite/" }
        ],
        code: {
          "Java": `// Directed cycle detection
int[] state = new int[n]; // 0=unvis,1=in-stack,2=done
boolean hasCycle(int u) {
    state[u]=1;
    for (int v:adj.get(u)) {
        if (state[v]==1) return true; // back edge!
        if (state[v]==0 && hasCycle(v)) return true;
    }
    state[u]=2; return false;
}
// Bipartite
int[] color = new int[n]; Arrays.fill(color,-1);
// BFS: color[start]=0, color[nb]=1-color[cur]`,
          "Kotlin": `val state=IntArray(n)
fun hasCycle(u:Int):Boolean{
    state[u]=1
    for(v in adj[u]){if(state[v]==1) return true;if(state[v]==0&&hasCycle(v)) return true}
    state[u]=2; return false
}`,
          "Python": `state = [0] * n  # 0=unvis,1=in-stack,2=done
def has_cycle(u):
    state[u] = 1
    for v in adj[u]:
        if state[v] == 1: return True  # back edge
        if state[v] == 0 and has_cycle(v): return True
    state[u] = 2; return False`
        }
      }
    ]
  },

  // ─── 13. TOPOLOGICAL SORT ────────────────────────────────────────────────
  {
    title: "Topological Sort",
    color: "#5a8a3a",
    patterns: [
      {
        name: "Kahn's Algorithm (BFS In-Degree)",
        recognition: "Linear ordering of DAG. Course schedule. Build order. Prerequisites.",
        mentalModel: "In-degree array. Queue all nodes with in-degree=0. Pop, add to order, decrement neighbors.",
        pitfalls: "If result.size() ≠ n → cycle exists. Build adj AND in-degree simultaneously.",
        problems: [
          { num: "207", name: "Course Schedule", url: "https://leetcode.com/problems/course-schedule/" },
          { num: "210", name: "Course Schedule II", url: "https://leetcode.com/problems/course-schedule-ii/" }
        ],
        code: {
          "Java": `int[] indeg=new int[n];
List<List<Integer>> adj=new ArrayList<>();
for(int i=0;i<n;i++) adj.add(new ArrayList<>());
for(int[] e:edges){adj.get(e[1]).add(e[0]);indeg[e[0]]++;}
Queue<Integer> q=new LinkedList<>();
for(int i=0;i<n;i++) if(indeg[i]==0) q.offer(i);
List<Integer> order=new ArrayList<>();
while(!q.isEmpty()){
    int u=q.poll(); order.add(u);
    for(int v:adj.get(u)) if(--indeg[v]==0) q.offer(v);
}
return order.size()==n; // false = cycle`,
          "Kotlin": `val indeg=IntArray(n)
for((u,v) in edges){adj[v].add(u);indeg[u]++}
val q=ArrayDeque<Int>()
for(i in 0 until n) if(indeg[i]==0) q.addLast(i)
val order=mutableListOf<Int>()
while(q.isNotEmpty()){val u=q.removeFirst();order.add(u);for(v in adj[u]) if(--indeg[v]==0) q.addLast(v)}
return order.size==n`,
          "Python": `from collections import deque
indeg=[0]*n
for u,v in edges: adj[v].append(u); indeg[u]+=1
q=deque(i for i in range(n) if indeg[i]==0)
order=[]
while q:
    u=q.popleft(); order.append(u)
    for v in adj[u]:
        indeg[v]-=1
        if indeg[v]==0: q.append(v)
return len(order)==n  # False=cycle`
        }
      },
      {
        name: "Alien Dictionary (Advanced Topo Sort)",
        recognition: "Derive character ordering from sorted word list.",
        mentalModel: "Compare adjacent words → find first different char → edge: word1[i] → word2[i]. Then topo sort.",
        pitfalls: "If word1 is prefix of word2 and word1 comes after → invalid. Empty result = cycle.",
        problems: [
          { num: "269", name: "Alien Dictionary", url: "https://leetcode.com/problems/alien-dictionary/" }
        ],
        code: {
          "Java": `// Build graph from adjacent word pairs
Map<Character,List<Character>> adj=new HashMap<>();
Map<Character,Integer> indeg=new HashMap<>();
for (char c : allChars) { adj.put(c,new ArrayList<>()); indeg.put(c,0); }
for (int i=0;i<words.length-1;i++) {
    String w1=words[i], w2=words[i+1];
    int len=Math.min(w1.length(),w2.length());
    for (int j=0;j<len;j++) {
        if (w1.charAt(j)!=w2.charAt(j)) {
            adj.get(w1.charAt(j)).add(w2.charAt(j));
            indeg.merge(w2.charAt(j),1,Integer::sum);
            break;
        }
    }
}
// Then run Kahn's on the character graph`,
          "Kotlin": `// Same logic but with Char keys`,
          "Python": `adj = {c: [] for w in words for c in w}
indeg = {c: 0 for c in adj}
for i in range(len(words)-1):
    w1, w2 = words[i], words[i+1]
    for c1, c2 in zip(w1, w2):
        if c1 != c2:
            adj[c1].append(c2); indeg[c2]+=1; break
# Run Kahn's on adj/indeg`
        }
      }
    ]
  },

  // ─── 14. UNION FIND ──────────────────────────────────────────────────────
  {
    title: "Union Find (DSU)",
    color: "#2e8a5a",
    patterns: [
      {
        name: "Path Compression + Union by Rank",
        recognition: "Connected components. Cycle detection in undirected graph. Kruskal MST.",
        mentalModel: "find() with path compression flattens tree. Union by rank keeps balanced. O(α(N)) ≈ O(1).",
        pitfalls: "Initialize parent[i]=i. find() must be recursive for path compression. Return false if already connected.",
        problems: [
          { num: "684", name: "Redundant Connection", url: "https://leetcode.com/problems/redundant-connection/" },
          { num: "323", name: "Number of Connected Components", url: "https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/" },
          { num: "547", name: "Number of Provinces", url: "https://leetcode.com/problems/number-of-provinces/" }
        ],
        code: {
          "Java": `int[] parent=new int[n], rank=new int[n];
for(int i=0;i<n;i++) parent[i]=i;

int find(int x) {
    if(parent[x]!=x) parent[x]=find(parent[x]); // path compression
    return parent[x];
}
boolean union(int a, int b) {
    int ra=find(a), rb=find(b);
    if(ra==rb) return false; // already connected = cycle!
    if(rank[ra]<rank[rb]) parent[ra]=rb;
    else if(rank[ra]>rank[rb]) parent[rb]=ra;
    else { parent[rb]=ra; rank[ra]++; }
    return true;
}`,
          "Kotlin": `val parent=IntArray(n){it}; val rank=IntArray(n)
fun find(x:Int):Int{ if(parent[x]!=x) parent[x]=find(parent[x]); return parent[x] }
fun union(a:Int,b:Int):Boolean{
    val ra=find(a);val rb=find(b); if(ra==rb) return false
    if(rank[ra]<rank[rb]) parent[ra]=rb
    else if(rank[ra]>rank[rb]) parent[rb]=ra
    else{parent[rb]=ra;rank[ra]++}; return true
}`,
          "Python": `parent=list(range(n)); rank=[0]*n
def find(x):
    if parent[x]!=x: parent[x]=find(parent[x])  # path compression
    return parent[x]
def union(a,b):
    ra,rb=find(a),find(b)
    if ra==rb: return False  # already connected = cycle!
    if rank[ra]<rank[rb]: parent[ra]=rb
    elif rank[ra]>rank[rb]: parent[rb]=ra
    else: parent[rb]=ra; rank[ra]+=1
    return True`
        }
      }
    ]
  },

  // ─── 15. TRIE ────────────────────────────────────────────────────────────
  {
    title: "Trie",
    color: "#8a2e5a",
    patterns: [
      {
        name: "Insert, Search, StartsWith",
        recognition: "Prefix matching. Autocomplete. Word dictionary. Longest common prefix.",
        mentalModel: "Each node has children[] array (or HashMap) + isWord flag. Walk one char at a time.",
        pitfalls: "search() checks isWord. startsWith() doesn't. Don't confuse them.",
        problems: [
          { num: "208", name: "Implement Trie", url: "https://leetcode.com/problems/implement-trie-prefix-tree/" }
        ],
        code: {
          "Java": `class TrieNode {
    TrieNode[] children = new TrieNode[26];
    boolean isWord;
}
void insert(String w) {
    TrieNode cur=root;
    for (char c:w.toCharArray()) {
        int i=c-'a';
        if(cur.children[i]==null) cur.children[i]=new TrieNode();
        cur=cur.children[i];
    }
    cur.isWord=true;
}
boolean search(String w) {
    TrieNode cur=root;
    for (char c:w.toCharArray()) {
        int i=c-'a';
        if(cur.children[i]==null) return false;
        cur=cur.children[i];
    }
    return cur.isWord; // ← isWord check!
}
boolean startsWith(String pre) {
    // same but return true (no isWord check)
}`,
          "Kotlin": `class TrieNode { val children=arrayOfNulls<TrieNode>(26); var isWord=false }
fun insert(w:String){ var cur=root; for(c in w){val i=c-'a'; if(cur.children[i]==null) cur.children[i]=TrieNode(); cur=cur.children[i]!!}; cur.isWord=true }
fun search(w:String):Boolean{ var cur=root; for(c in w){val i=c-'a'; if(cur.children[i]==null) return false; cur=cur.children[i]!!}; return cur.isWord }`,
          "Python": `class TrieNode:
    def __init__(self): self.children={}; self.is_word=False

class Trie:
    def __init__(self): self.root=TrieNode()
    def insert(self, w):
        cur=self.root
        for c in w:
            if c not in cur.children: cur.children[c]=TrieNode()
            cur=cur.children[c]
        cur.is_word=True
    def search(self, w):
        cur=self.root
        for c in w:
            if c not in cur.children: return False
            cur=cur.children[c]
        return cur.is_word  # ← check is_word!`
        }
      },
      {
        name: "Word Dictionary (Wildcard) & Word Search II",
        recognition: "Search with '.' wildcard. Find all words from list in a grid.",
        mentalModel: "Wildcard: DFS all 26 children when '.' encountered. Word Search II: Build trie from words, DFS grid.",
        pitfalls: "Word Search II: remove word from trie after finding (avoid duplicates). Prune early.",
        problems: [
          { num: "211", name: "Design Add and Search Words", url: "https://leetcode.com/problems/design-add-and-search-words-data-structure/" },
          { num: "212", name: "Word Search II", url: "https://leetcode.com/problems/word-search-ii/" }
        ],
        code: {
          "Java": `// Search with wildcard '.'
boolean search(String w, int i, TrieNode node) {
    if(i==w.length()) return node.isWord;
    char c=w.charAt(i);
    if(c=='.') {
        for(TrieNode child:node.children)
            if(child!=null && search(w,i+1,child)) return true;
        return false;
    }
    TrieNode next=node.children[c-'a'];
    return next!=null && search(w,i+1,next);
}
// Word Search II: build trie, DFS grid
void dfs(char[][] board, int r, int c, TrieNode node, String path) {
    if(node.isWord){res.add(path);node.isWord=false;} // mark found
    if(r<0||r>=R||c<0||c>=C||board[r][c]=='#') return;
    char ch=board[r][c];
    TrieNode next=node.children[ch-'a'];
    if(next==null) return;
    board[r][c]='#';
    dfs(board,r+1,c,next,path+ch);dfs(board,r-1,c,next,path+ch);
    dfs(board,r,c+1,next,path+ch);dfs(board,r,c-1,next,path+ch);
    board[r][c]=ch;
}`,
          "Kotlin": `fun search(w: String, i: Int, node: TrieNode): Boolean {
    if(i==w.length) return node.isWord
    val c=w[i]
    if(c=='.') return node.children.any{it!=null&&search(w,i+1,it)}
    return node.children[c-'a']?.let{search(w,i+1,it)}?:false
}`,
          "Python": `def search(w, i, node):
    if i == len(w): return node.is_word
    c = w[i]
    if c == '.':
        return any(search(w, i+1, child) for child in node.children.values())
    if c not in node.children: return False
    return search(w, i+1, node.children[c])`
        }
      }
    ]
  },

  // ─── 16. DYNAMIC PROGRAMMING ─────────────────────────────────────────────
  {
    title: "Dynamic Programming",
    color: "#1f7a72",
    patterns: [
      {
        name: "DP Fundamentals (Memo vs Tabulation)",
        recognition: "Overlapping subproblems + optimal substructure = DP.",
        mentalModel: "Memoization = top-down recursion + cache. Tabulation = bottom-up iterative. Same complexity.",
        pitfalls: "DP can only optimize if subproblems OVERLAP. Identify STATE variables first.",
        problems: [
          { num: "509", name: "Fibonacci Number", url: "https://leetcode.com/problems/fibonacci-number/" }
        ],
        code: {
          "Java": `// STEP 1: Define state: dp[i] = answer for input i
// STEP 2: Write recurrence: dp[i] = f(dp[i-1], dp[i-2])
// STEP 3: Base cases: dp[0], dp[1]
// STEP 4: Order (bottom-up) or memoize (top-down)

// Memoization (top-down)
Map<Integer,Integer> memo=new HashMap<>();
int fib(int n){
    if(n<=1) return n;
    if(memo.containsKey(n)) return memo.get(n);
    int res=fib(n-1)+fib(n-2);
    memo.put(n,res); return res;
}
// Tabulation (bottom-up)
int[] dp=new int[n+1]; dp[0]=0; dp[1]=1;
for(int i=2;i<=n;i++) dp[i]=dp[i-1]+dp[i-2];`,
          "Kotlin": `// Memoization
val memo=mutableMapOf<Int,Int>()
fun fib(n:Int):Int{
    if(n<=1) return n
    return memo.getOrPut(n){fib(n-1)+fib(n-2)}
}`,
          "Python": `# Memoization (top-down)
from functools import lru_cache
@lru_cache(None)
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)

# Tabulation (bottom-up)
dp = [0] * (n+1); dp[1] = 1
for i in range(2, n+1): dp[i] = dp[i-1] + dp[i-2]`
        }
      },
      {
        name: "1D DP (Climbing Stairs, House Robber)",
        recognition: "State depends on 1 or 2 previous states. Space optimize to O(1).",
        mentalModel: "dp[i] = dp[i-1] + dp[i-2]. Space optimize with 2 variables a, b.",
        pitfalls: "Base cases. House Robber: can't take adjacent. dp[i] = max(dp[i-1], dp[i-2]+val).",
        problems: [
          { num: "70", name: "Climbing Stairs", url: "https://leetcode.com/problems/climbing-stairs/" },
          { num: "198", name: "House Robber", url: "https://leetcode.com/problems/house-robber/" },
          { num: "213", name: "House Robber II", url: "https://leetcode.com/problems/house-robber-ii/" },
          { num: "322", name: "Coin Change", url: "https://leetcode.com/problems/coin-change/" }
        ],
        code: {
          "Java": `// Climbing Stairs O(1) space
int a=1,b=1;
for(int i=2;i<=n;i++){int c=a+b;a=b;b=c;}
return b;
// House Robber
int inc=0,exc=0;
for(int x:nums){int tmp=inc;inc=exc+x;exc=Math.max(tmp,exc);}
return Math.max(inc,exc);
// House Robber II: run twice (exclude first or last)
// Coin Change (unbounded knapsack)
int[] dp=new int[sum+1]; Arrays.fill(dp,Integer.MAX_VALUE); dp[0]=0;
for(int c:coins) for(int i=c;i<=sum;i++)
    if(dp[i-c]!=Integer.MAX_VALUE) dp[i]=Math.min(dp[i],1+dp[i-c]);`,
          "Kotlin": `var a=1;var b=1
for(i in 2..n){val c=a+b;a=b;b=c}
return b`,
          "Python": `# Climbing Stairs
a = b = 1
for _ in range(2, n+1): a, b = b, a + b
return b
# House Robber
inc = exc = 0
for x in nums: inc, exc = exc+x, max(inc, exc)
return max(inc, exc)
# Coin Change
dp = [float('inf')]*(sum+1); dp[0]=0
for c in coins:
    for i in range(c, sum+1):
        dp[i]=min(dp[i], 1+dp[i-c])`
        }
      },
      {
        name: "2D DP (Grid Paths, Unique Paths)",
        recognition: "Grid traversal. Count paths. Min cost path. Obstacles.",
        mentalModel: "dp[i][j] = dp[i-1][j] + dp[i][j-1]. Initialize first row/col to 1.",
        pitfalls: "Obstacle: set dp to 0. Watch boundary initialization.",
        problems: [
          { num: "62", name: "Unique Paths", url: "https://leetcode.com/problems/unique-paths/" },
          { num: "64", name: "Minimum Path Sum", url: "https://leetcode.com/problems/minimum-path-sum/" },
          { num: "63", name: "Unique Paths II", url: "https://leetcode.com/problems/unique-paths-ii/" }
        ],
        code: {
          "Java": `int[][] dp=new int[m][n];
for(int i=0;i<m;i++) dp[i][0]=1;
for(int j=0;j<n;j++) dp[0][j]=1;
for(int i=1;i<m;i++) for(int j=1;j<n;j++)
    dp[i][j]=dp[i-1][j]+dp[i][j-1];
return dp[m-1][n-1];`,
          "Kotlin": `val dp=Array(m){IntArray(n){1}}
for(i in 1 until m) for(j in 1 until n) dp[i][j]=dp[i-1][j]+dp[i][j-1]
return dp[m-1][n-1]`,
          "Python": `dp=[[1]*n for _ in range(m)]
for i in range(1,m):
    for j in range(1,n): dp[i][j]=dp[i-1][j]+dp[i][j-1]
return dp[m-1][n-1]`
        }
      },
      {
        name: "Knapsack (0/1 and Unbounded)",
        recognition: "Select items with weight/value constraints. Partition problem.",
        mentalModel: "0/1: loop weights BACKWARDS. Unbounded: loop forwards. dp[0]=true/0.",
        pitfalls: "0/1 must iterate reverse to avoid using item twice. Init correctly.",
        problems: [
          { num: "416", name: "Partition Equal Subset Sum", url: "https://leetcode.com/problems/partition-equal-subset-sum/" },
          { num: "494", name: "Target Sum", url: "https://leetcode.com/problems/target-sum/" },
          { num: "322", name: "Coin Change (Unbounded)", url: "https://leetcode.com/problems/coin-change/" }
        ],
        code: {
          "Java": `// 0/1 Knapsack (boolean subset sum)
boolean[] dp=new boolean[sum+1]; dp[0]=true;
for(int x:nums)
    for(int j=sum;j>=x;j--) // ← REVERSE!
        dp[j]|=dp[j-x];

// Unbounded Knapsack (coin change)
int[] dp=new int[sum+1]; Arrays.fill(dp,MAX); dp[0]=0;
for(int c:coins)
    for(int i=c;i<=sum;i++) // ← FORWARD
        if(dp[i-c]!=MAX) dp[i]=Math.min(dp[i],1+dp[i-c]);`,
          "Kotlin": `val dp=BooleanArray(sum+1).also{it[0]=true}
for(x in nums) for(j in sum downTo x) dp[j]=dp[j]||dp[j-x]`,
          "Python": `# 0/1 Knapsack (REVERSE!)
dp=[False]*(sum+1); dp[0]=True
for x in nums:
    for j in range(sum, x-1, -1):  # REVERSE!
        dp[j]|=dp[j-x]
# Unbounded (FORWARD)
dp=[float('inf')]*(sum+1); dp[0]=0
for c in coins:
    for i in range(c, sum+1):  # FORWARD
        dp[i]=min(dp[i], 1+dp[i-c])`
        }
      },
      {
        name: "LCS, LIS, Edit Distance",
        recognition: "String matching. Subsequences. Edit operations. Palindromes.",
        mentalModel: "LCS: match→diagonal+1, else→max(up,left). LIS O(NlogN): binary search on tails array.",
        pitfalls: "LCS 1-indexed → dp[0][*]=0, dp[*][0]=0. Edit distance: 3 operations.",
        problems: [
          { num: "1143", name: "LCS", url: "https://leetcode.com/problems/longest-common-subsequence/" },
          { num: "300", name: "LIS", url: "https://leetcode.com/problems/longest-increasing-subsequence/" },
          { num: "72", name: "Edit Distance", url: "https://leetcode.com/problems/edit-distance/" },
          { num: "5", name: "Longest Palindromic Substring", url: "https://leetcode.com/problems/longest-palindromic-substring/" }
        ],
        code: {
          "Java": `// LCS
int[][] dp=new int[m+1][n+1];
for(int i=1;i<=m;i++) for(int j=1;j<=n;j++)
    dp[i][j]=(s1.charAt(i-1)==s2.charAt(j-1))?dp[i-1][j-1]+1:Math.max(dp[i-1][j],dp[i][j-1]);
// LIS O(NlogN): binary search on tails
List<Integer> tails=new ArrayList<>();
for(int x:nums){
    int pos=Collections.binarySearch(tails,x);
    if(pos<0) pos=-(pos+1);
    if(pos==tails.size()) tails.add(x); else tails.set(pos,x);
}
return tails.size();
// Edit Distance
dp[i][j]=(s1[i-1]==s2[j-1])?dp[i-1][j-1]:1+Math.min(dp[i-1][j-1],Math.min(dp[i-1][j],dp[i][j-1]));`,
          "Kotlin": `val dp=Array(m+1){IntArray(n+1)}
for(i in 1..m) for(j in 1..n)
    dp[i][j]=if(s1[i-1]==s2[j-1]) dp[i-1][j-1]+1 else maxOf(dp[i-1][j],dp[i][j-1])`,
          "Python": `# LCS
dp=[[0]*(n+1) for _ in range(m+1)]
for i in range(1,m+1):
    for j in range(1,n+1):
        if s1[i-1]==s2[j-1]: dp[i][j]=dp[i-1][j-1]+1
        else: dp[i][j]=max(dp[i-1][j],dp[i][j-1])
# LIS O(NlogN)
import bisect
tails=[]
for x in nums:
    pos=bisect.bisect_left(tails,x)
    if pos==len(tails): tails.append(x)
    else: tails[pos]=x`
        }
      },
      {
        name: "Palindrome DP & Partition DP",
        recognition: "Longest palindromic subsequence/substring. Min cuts for palindrome partition.",
        mentalModel: "Palindrome DP: expand from center (odd/even). Or DP[i][j]=is s[i..j] palindrome.",
        pitfalls: "Substring vs subsequence. Expand center for O(N²) vs DP table.",
        problems: [
          { num: "5", name: "Longest Palindromic Substring", url: "https://leetcode.com/problems/longest-palindromic-substring/" },
          { num: "516", name: "Longest Palindromic Subsequence", url: "https://leetcode.com/problems/longest-palindromic-subsequence/" },
          { num: "132", name: "Palindrome Partitioning II", url: "https://leetcode.com/problems/palindrome-partitioning-ii/" }
        ],
        code: {
          "Java": `// Longest Palindromic Substring: expand from center
String best="";
for(int i=0;i<n;i++){
    String odd=expand(s,i,i);   // odd length
    String even=expand(s,i,i+1); // even length
    if(odd.length()>best.length()) best=odd;
    if(even.length()>best.length()) best=even;
}
String expand(String s,int l,int r){
    while(l>=0&&r<s.length()&&s.charAt(l)==s.charAt(r)){l--;r++;}
    return s.substring(l+1,r);
}
// Longest Palindromic Subsequence
// LPS(s) = LCS(s, reverse(s))`,
          "Kotlin": `fun expand(s:String,l:Int,r:Int):Int{
    var lo=l;var hi=r
    while(lo>=0&&hi<s.length&&s[lo]==s[hi]){lo--;hi++}
    return hi-lo-1
}`,
          "Python": `# Expand from center
def expand(l, r):
    while l >= 0 and r < n and s[l] == s[r]:
        l -= 1; r += 1
    return s[l+1:r]
best = ''
for i in range(n):
    for p in [expand(i,i), expand(i,i+1)]:
        if len(p) > len(best): best = p
# Palindrome Subsequence = LCS(s, s[::-1])`
        }
      }
    ]
  },

  // ─── 17. INTERVALS & GREEDY ──────────────────────────────────────────────
  {
    title: "Intervals & Greedy",
    color: "#7a5a2e",
    patterns: [
      {
        name: "Merge & Insert Intervals",
        recognition: "Overlapping ranges. Merge. Insert new interval. Meeting rooms.",
        mentalModel: "Sort by start. Merge if next.start <= last.end. Update end = max(both).",
        pitfalls: "Sort first. Insert: 3 zones (before, overlap, after). Meeting Rooms II: min-heap of end times.",
        problems: [
          { num: "56", name: "Merge Intervals", url: "https://leetcode.com/problems/merge-intervals/" },
          { num: "57", name: "Insert Interval", url: "https://leetcode.com/problems/insert-interval/" },
          { num: "253", name: "Meeting Rooms II", url: "https://leetcode.com/problems/meeting-rooms-ii/" }
        ],
        code: {
          "Java": `// Merge Intervals
Arrays.sort(intervals,(a,b)->a[0]-b[0]);
List<int[]> res=new ArrayList<>();
for(int[] i:intervals){
    if(res.isEmpty()||res.get(res.size()-1)[1]<i[0]) res.add(i);
    else res.get(res.size()-1)[1]=Math.max(res.get(res.size()-1)[1],i[1]);
}
// Meeting Rooms II: min-heap of end times
Arrays.sort(intervals,(a,b)->a[0]-b[0]);
PriorityQueue<Integer> pq=new PriorityQueue<>();
for(int[] i:intervals){
    if(!pq.isEmpty()&&pq.peek()<=i[0]) pq.poll(); // free room
    pq.offer(i[1]);
}
return pq.size(); // rooms needed`,
          "Kotlin": `intervals.sortBy{it[0]}
val res=mutableListOf<IntArray>()
for(i in intervals)
    if(res.isEmpty()||res.last()[1]<i[0]) res.add(i)
    else res.last()[1]=maxOf(res.last()[1],i[1])`,
          "Python": `intervals.sort(key=lambda x: x[0])
res=[]
for i in intervals:
    if not res or res[-1][1]<i[0]: res.append(i)
    else: res[-1][1]=max(res[-1][1],i[1])
# Meeting Rooms II
import heapq
heapq.heapify(heap:=[])
for start,end in sorted(intervals):
    if heap and heap[0]<=start: heapq.heappop(heap)
    heapq.heappush(heap,end)`
        }
      },
      {
        name: "Jump Game & Gas Station",
        recognition: "Can we reach end? Min jumps? Circular gas station.",
        mentalModel: "Jump Game: track maxReach. If i>maxReach: stuck. Gas Station: if totalGas>=0, answer exists.",
        pitfalls: "Jump Game II: update nextReach greedily. Gas Station: total >= 0 guarantees solution.",
        problems: [
          { num: "55", name: "Jump Game", url: "https://leetcode.com/problems/jump-game/" },
          { num: "45", name: "Jump Game II", url: "https://leetcode.com/problems/jump-game-ii/" },
          { num: "134", name: "Gas Station", url: "https://leetcode.com/problems/gas-station/" }
        ],
        code: {
          "Java": `// Jump Game
int reach=0;
for(int i=0;i<n&&i<=reach;i++) reach=Math.max(reach,i+nums[i]);
return reach>=n-1;
// Jump Game II (min jumps)
int jumps=0,curEnd=0,farthest=0;
for(int i=0;i<n-1;i++){
    farthest=Math.max(farthest,i+nums[i]);
    if(i==curEnd){jumps++;curEnd=farthest;}
}
// Gas Station
int total=0,cur=0,start=0;
for(int i=0;i<n;i++){
    total+=gas[i]-cost[i]; cur+=gas[i]-cost[i];
    if(cur<0){start=i+1;cur=0;}
}
return total>=0?start:-1;`,
          "Kotlin": `var reach=0
for(i in 0 until n){ if(i>reach) break; reach=maxOf(reach,i+nums[i]) }
return reach>=n-1`,
          "Python": `# Jump Game
reach = 0
for i in range(n):
    if i > reach: return False
    reach = max(reach, i + nums[i])
return True
# Gas Station
total=cur=start=0
for i in range(n):
    total+=gas[i]-cost[i]; cur+=gas[i]-cost[i]
    if cur<0: start=i+1; cur=0
return start if total>=0 else -1`
        }
      },
      {
        name: "Task Scheduler & Scheduling",
        recognition: "CPU scheduling with cooldown. Minimum time to finish tasks.",
        mentalModel: "Max frequency task determines idle slots. slots = (maxFreq-1)*n + count(tasks with maxFreq).",
        pitfalls: "Result = max(len(tasks), calculated_slots). Never less than total tasks.",
        problems: [
          { num: "621", name: "Task Scheduler", url: "https://leetcode.com/problems/task-scheduler/" },
          { num: "435", name: "Non-overlapping Intervals", url: "https://leetcode.com/problems/non-overlapping-intervals/" }
        ],
        code: {
          "Java": `// Task Scheduler
int[] freq=new int[26];
for(char c:tasks) freq[c-'A']++;
int maxFreq=0;
for(int f:freq) maxFreq=Math.max(maxFreq,f);
int maxCount=0;
for(int f:freq) if(f==maxFreq) maxCount++;
int slots=(maxFreq-1)*(n+1)+maxCount;
return Math.max(slots,tasks.length);
// Non-overlapping: remove min intervals to make non-overlapping
// Sort by end time. Count non-overlapping. Remove = total - count.
Arrays.sort(intervals,(a,b)->a[1]-b[1]);
int count=0,end=Integer.MIN_VALUE;
for(int[] i:intervals) if(i[0]>=end){count++;end=i[1];}
return intervals.length-count;`,
          "Kotlin": `val freq=IntArray(26); for(c in tasks) freq[c-'A']++
val maxFreq=freq.max()!!
val maxCount=freq.count{it==maxFreq}
val slots=(maxFreq-1)*(n+1)+maxCount
return maxOf(slots,tasks.size)`,
          "Python": `from collections import Counter
freq=Counter(tasks)
max_freq=max(freq.values())
max_count=sum(1 for f in freq.values() if f==max_freq)
slots=(max_freq-1)*(n+1)+max_count
return max(slots, len(tasks))`
        }
      }
    ]
  },

  // ─── 18. BIT MANIPULATION ─────────────────────────────────────────────────
  {
    title: "Bit Manipulation",
    color: "#3a7a6a",
    patterns: [
      {
        name: "XOR Tricks (Single Number, Missing)",
        recognition: "Find unique element. Missing number. XOR properties.",
        mentalModel: "x^x=0, x^0=x. XOR all: pairs cancel. Missing: XOR 1..n with array.",
        pitfalls: "Integer overflow with sum approach. XOR is better.",
        problems: [
          { num: "136", name: "Single Number", url: "https://leetcode.com/problems/single-number/" },
          { num: "268", name: "Missing Number", url: "https://leetcode.com/problems/missing-number/" },
          { num: "137", name: "Single Number II", url: "https://leetcode.com/problems/single-number-ii/" }
        ],
        code: {
          "Java": `// Single Number: x^x=0
int res=0; for(int x:arr) res^=x; return res;
// Missing Number
int res=n; for(int i=0;i<n;i++) res^=i^nums[i]; return res;
// Single Number II (appears 3x, find 1x)
int ones=0,twos=0;
for(int x:arr){ones=(ones^x)&~twos;twos=(twos^x)&~ones;}
return ones;`,
          "Kotlin": `val res=arr.fold(0){acc,x->acc xor x}`,
          "Python": `# Single Number
from functools import reduce
import operator
res = reduce(operator.xor, arr)
# Missing Number
return n*(n+1)//2 - sum(nums)`
        }
      },
      {
        name: "Bit Masks (Set/Clear/Toggle/Count)",
        recognition: "State compression. Subset enumeration. Power of two check.",
        mentalModel: "1<<i sets bit i. n&(n-1) removes lowest bit. n&(-n) isolates lowest bit.",
        pitfalls: "Operator precedence: (a&b)==0 not a&b==0. Use parentheses!",
        problems: [
          { num: "338", name: "Counting Bits", url: "https://leetcode.com/problems/counting-bits/" },
          { num: "191", name: "Number of 1 Bits", url: "https://leetcode.com/problems/number-of-1-bits/" },
          { num: "78", name: "Subsets via Bitmask", url: "https://leetcode.com/problems/subsets/" }
        ],
        code: {
          "Java": `// Bit trick cheatsheet
num | (1<<i)      // set bit i
num & ~(1<<i)     // clear bit i
num ^ (1<<i)      // toggle bit i
(num>>i)&1        // check bit i (1 or 0)
num & (num-1)     // remove lowest set bit
num & (-num)      // isolate lowest set bit
n>0 && (n&(n-1))==0 // power of 2?
Integer.bitCount(n)  // popcount

// Counting bits DP
int[] dp=new int[n+1];
for(int i=1;i<=n;i++) dp[i]=dp[i>>1]+(i&1);

// Enumerate all subsets
for(int mask=0;mask<(1<<n);mask++)
    for(int i=0;i<n;i++)
        if((mask&(1<<i))!=0) // bit i is set`,
          "Kotlin": `// Kotlin uses 'shr', 'shl', 'and', 'or', 'xor', 'inv'
val setBit = num or (1 shl i)
val checkBit = (num shr i) and 1
val isPow2 = num>0 && (num and (num-1))==0`,
          "Python": `# Bit tricks
n | (1<<i)      # set bit i
n & ~(1<<i)     # clear bit i
n ^ (1<<i)      # toggle bit i
(n >> i) & 1    # check bit i
n & (n-1)       # remove lowest set bit
n & (-n)        # isolate lowest set bit
bin(n).count('1')  # popcount
n>0 and (n&(n-1))==0  # power of 2?
# Counting bits
dp=[0]*(n+1)
for i in range(1,n+1): dp[i]=dp[i>>1]+(i&1)`
        }
      }
    ]
  },

  // ─── 19. ADVANCED (Google/Meta L5+) ─────────────────────────────────────
  {
    title: "Advanced: Shortest Paths",
    color: "#6a1f5a",
    patterns: [
      {
        name: "Dijkstra's Algorithm",
        recognition: "Shortest path in weighted graph (non-negative weights). Network delay.",
        mentalModel: "Min-heap (dist, node). Relax edges. Skip stale entries (if d > dist[u]: continue).",
        pitfalls: "Doesn't work with negative weights (use Bellman-Ford). Skip stale heap entries.",
        problems: [
          { num: "743", name: "Network Delay Time", url: "https://leetcode.com/problems/network-delay-time/" },
          { num: "1514", name: "Path with Maximum Probability", url: "https://leetcode.com/problems/path-with-maximum-probability/" }
        ],
        code: {
          "Java": `int[] dist=new int[n]; Arrays.fill(dist,Integer.MAX_VALUE); dist[src]=0;
PriorityQueue<int[]> pq=new PriorityQueue<>((a,b)->a[0]-b[0]); // (dist, node)
pq.offer(new int[]{0,src});
while(!pq.isEmpty()){
    int[] cur=pq.poll(); int d=cur[0],u=cur[1];
    if(d>dist[u]) continue; // stale entry!
    for(int[] e:adj.get(u)){
        int v=e[0],w=e[1];
        if(dist[u]+w<dist[v]){dist[v]=dist[u]+w;pq.offer(new int[]{dist[v],v});}
    }
}`,
          "Kotlin": `val dist=IntArray(n){Int.MAX_VALUE}.also{it[src]=0}
val pq=PriorityQueue<IntArray>(compareBy{it[0]})
pq.offer(intArrayOf(0,src))
while(pq.isNotEmpty()){
    val(d,u)=pq.poll()
    if(d>dist[u]) continue
    for((v,w) in adj[u]) if(dist[u]+w<dist[v]){dist[v]=dist[u]+w;pq.offer(intArrayOf(dist[v],v))}
}`,
          "Python": `import heapq
dist=[float('inf')]*n; dist[src]=0
pq=[(0,src)]
while pq:
    d,u=heapq.heappop(pq)
    if d>dist[u]: continue  # stale!
    for v,w in adj[u]:
        if dist[u]+w<dist[v]:
            dist[v]=dist[u]+w; heapq.heappush(pq,(dist[v],v))`
        }
      },
      {
        name: "Bellman-Ford & Floyd-Warshall",
        recognition: "Negative weights (Bellman-Ford). All-pairs shortest path (Floyd-Warshall).",
        mentalModel: "Bellman-Ford: relax all edges N-1 times. Floyd: for each k, try routing through k.",
        pitfalls: "Bellman-Ford: Nth relaxation finds negative cycle. Floyd: O(V³) space and time.",
        problems: [
          { num: "787", name: "Cheapest Flights Within K Stops", url: "https://leetcode.com/problems/cheapest-flights-within-k-stops/" }
        ],
        code: {
          "Java": `// Bellman-Ford: O(VE)
int[] dist=new int[n]; Arrays.fill(dist,INF); dist[src]=0;
for(int i=0;i<n-1;i++) // relax n-1 times
    for(int[] e:edges)
        if(dist[e[0]]!=INF && dist[e[0]]+e[2]<dist[e[1]])
            dist[e[1]]=dist[e[0]]+e[2];
// Check negative cycle: do one more relaxation
for(int[] e:edges) if(dist[e[0]]+e[2]<dist[e[1]]) /* negative cycle! */;

// Floyd-Warshall: O(V³) all-pairs
int[][] dist=new int[n][n]; // init with edge weights
for(int k=0;k<n;k++)
    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
            dist[i][j]=Math.min(dist[i][j],dist[i][k]+dist[k][j]);`,
          "Kotlin": `// Bellman-Ford
val dist=IntArray(n){INT_MAX}.also{it[src]=0}
repeat(n-1){for((u,v,w) in edges) if(dist[u]!=INT_MAX&&dist[u]+w<dist[v]) dist[v]=dist[u]+w}`,
          "Python": `# Bellman-Ford
dist=[float('inf')]*n; dist[src]=0
for _ in range(n-1):
    for u,v,w in edges:
        if dist[u]+w<dist[v]: dist[v]=dist[u]+w
# Floyd-Warshall
for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])`
        }
      },
      {
        name: "Minimum Spanning Tree (Kruskal & Prim)",
        recognition: "Connect all nodes with minimum total edge weight.",
        mentalModel: "Kruskal: sort edges by weight, add if no cycle (Union Find). Prim: greedy grow from any node.",
        pitfalls: "Kruskal: sort ascending. Prim: mark visited. Both produce same MST weight.",
        problems: [
          { num: "1584", name: "Min Cost to Connect All Points", url: "https://leetcode.com/problems/min-cost-to-connect-all-points/" }
        ],
        code: {
          "Java": `// Kruskal: O(E logE)
Arrays.sort(edges,(a,b)->a[2]-b[2]); // sort by weight
int cost=0,count=0;
for(int[] e:edges){
    if(union(e[0],e[1])){ // add if no cycle
        cost+=e[2]; if(++count==n-1) break;
    }
}
// Prim: O(E logV)
PriorityQueue<int[]> pq=new PriorityQueue<>((a,b)->a[0]-b[0]);
boolean[] vis=new boolean[n]; pq.offer(new int[]{0,0});
int cost=0;
while(!pq.isEmpty()){
    int[] cur=pq.poll(); if(vis[cur[1]]) continue;
    vis[cur[1]]=true; cost+=cur[0];
    for(int[] nb:adj.get(cur[1])) if(!vis[nb[0]]) pq.offer(new int[]{nb[1],nb[0]});
}`,
          "Kotlin": `// Kruskal with Union-Find
edges.sortBy{it[2]}
var cost=0; var count=0
for((u,v,w) in edges) if(union(u,v)){cost+=w; if(++count==n-1) break}`,
          "Python": `# Kruskal
edges.sort(key=lambda x: x[2])
cost=count=0
for u,v,w in edges:
    if union(u,v): cost+=w; count+=1
    if count==n-1: break
# Prim
import heapq
vis=[False]*n; pq=[(0,0)]; cost=0
while pq:
    w,u=heapq.heappop(pq)
    if vis[u]: continue
    vis[u]=True; cost+=w
    for v,wt in adj[u]:
        if not vis[v]: heapq.heappush(pq,(wt,v))`
        }
      }
    ]
  },

  // ─── 20. ADVANCED: STRING ALGORITHMS ─────────────────────────────────────
  {
    title: "Advanced: String Algorithms",
    color: "#4a2e7a",
    patterns: [
      {
        name: "KMP Pattern Matching",
        recognition: "Find pattern in text O(N+M). Multiple occurrences.",
        mentalModel: "Build LPS (Longest Proper Prefix=Suffix) array. On mismatch, jump to lps[j-1].",
        pitfalls: "LPS is 0-indexed. j resets to lps[j-1] not 0 on mismatch.",
        problems: [
          { num: "28", name: "Find Index of First Occurrence", url: "https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/" },
          { num: "459", name: "Repeated Substring Pattern", url: "https://leetcode.com/problems/repeated-substring-pattern/" }
        ],
        code: {
          "Java": `// Build LPS array
int[] lps=new int[m]; int j=0;
for(int i=1;i<m;){
    if(pat[i]==pat[j]) lps[i++]=++j;
    else if(j>0) j=lps[j-1];
    else lps[i++]=0;
}
// Search
for(int i=0,k=0;i<n;){
    if(text[i]==pat[k]){i++;k++;}
    if(k==m){occurrences.add(i-m);k=lps[k-1];}
    else if(i<n&&text[i]!=pat[k]){
        if(k>0) k=lps[k-1]; else i++;
    }
}`,
          "Kotlin": `fun buildLPS(pat:String):IntArray{
    val lps=IntArray(pat.length); var j=0; var i=1
    while(i<pat.length){
        if(pat[i]==pat[j]) lps[i++]=++j
        else if(j>0) j=lps[j-1] else i++
    }; return lps
}`,
          "Python": `def build_lps(pat):
    lps=[0]*len(pat); j=0; i=1
    while i<len(pat):
        if pat[i]==pat[j]: lps[i]=j+1; i+=1; j+=1
        elif j>0: j=lps[j-1]
        else: i+=1
    return lps`
        }
      },
      {
        name: "Rabin-Karp Rolling Hash",
        recognition: "Pattern matching with rolling hash. Find substring. Multiple pattern search.",
        mentalModel: "Hash pattern. Slide hash window: remove left char, add right char in O(1).",
        pitfalls: "Hash collision: verify match with string comparison. Use large prime modulus.",
        problems: [
          { num: "187", name: "Repeated DNA Sequences", url: "https://leetcode.com/problems/repeated-dna-sequences/" }
        ],
        code: {
          "Java": `// Rolling hash
long BASE=31,MOD=(long)1e9+7;
long hash=0,power=1;
// Initial window
for(int i=0;i<m;i++){hash=(hash*BASE+pat.charAt(i))%MOD;if(i>0)power=power*BASE%MOD;}
// Slide
for(int i=m;i<n;i++){
    hash=(hash*BASE+text.charAt(i))%MOD;
    hash=(hash-text.charAt(i-m)*power%MOD+MOD)%MOD;
    if(hash==patHash) // verify with .equals()!
}`,
          "Kotlin": `val BASE=31L; val MOD=1_000_000_007L`,
          "Python": `BASE, MOD = 31, 10**9+7
def rolling_hash(s, m):
    h = 0; power = pow(BASE, m-1, MOD)
    for c in s[:m]: h = (h*BASE + ord(c)) % MOD
    yield h
    for i in range(m, len(s)):
        h = (h*BASE + ord(s[i]) - ord(s[i-m])*power) % MOD
        yield h`
        }
      },
      {
        name: "Segment Tree",
        recognition: "Range queries (sum/min/max) + point/range updates. O(log N) each.",
        mentalModel: "Build tree bottom-up. Each node stores aggregate for range. Update propagates up.",
        pitfalls: "1-indexed tree: root=1, left=2i, right=2i+1. Tree size = 4*n.",
        problems: [
          { num: "307", name: "Range Sum Query Mutable", url: "https://leetcode.com/problems/range-sum-query-mutable/" }
        ],
        code: {
          "Java": `int[] tree=new int[4*n];
void build(int[] arr,int node,int start,int end){
    if(start==end){tree[node]=arr[start];return;}
    int mid=(start+end)/2;
    build(arr,2*node,start,mid);
    build(arr,2*node+1,mid+1,end);
    tree[node]=tree[2*node]+tree[2*node+1]; // merge
}
int query(int node,int start,int end,int l,int r){
    if(r<start||end<l) return 0; // out of range
    if(l<=start&&end<=r) return tree[node]; // full overlap
    int mid=(start+end)/2;
    return query(2*node,start,mid,l,r)+query(2*node+1,mid+1,end,l,r);
}
void update(int node,int start,int end,int idx,int val){
    if(start==end){tree[node]=val;return;}
    int mid=(start+end)/2;
    if(idx<=mid) update(2*node,start,mid,idx,val);
    else update(2*node+1,mid+1,end,idx,val);
    tree[node]=tree[2*node]+tree[2*node+1];
}`,
          "Kotlin": `val tree=IntArray(4*n)
fun build(arr:IntArray,node:Int,start:Int,end:Int){
    if(start==end){tree[node]=arr[start];return}
    val mid=(start+end)/2
    build(arr,2*node,start,mid); build(arr,2*node+1,mid+1,end)
    tree[node]=tree[2*node]+tree[2*node+1]
}`,
          "Python": `tree=[0]*(4*n)
def build(arr,node,start,end):
    if start==end: tree[node]=arr[start]; return
    mid=(start+end)//2
    build(arr,2*node,start,mid); build(arr,2*node+1,mid+1,end)
    tree[node]=tree[2*node]+tree[2*node+1]
def query(node,start,end,l,r):
    if r<start or end<l: return 0
    if l<=start and end<=r: return tree[node]
    mid=(start+end)//2
    return query(2*node,start,mid,l,r)+query(2*node+1,mid+1,end,l,r)`
        }
      },
      {
        name: "Fenwick Tree (Binary Indexed Tree)",
        recognition: "Prefix sum with point updates. Simpler than Segment Tree. O(log N).",
        mentalModel: "BIT[i] stores sum for a range determined by lowest set bit. Update propagates using i += i&(-i).",
        pitfalls: "1-indexed. Update AND query both use i += i&(-i) or i -= i&(-i).",
        problems: [
          { num: "307", name: "Range Sum Query Mutable", url: "https://leetcode.com/problems/range-sum-query-mutable/" },
          { num: "315", name: "Count of Smaller Numbers After Self", url: "https://leetcode.com/problems/count-of-smaller-numbers-after-self/" }
        ],
        code: {
          "Java": `int[] bit=new int[n+1]; // 1-indexed
void update(int i,int val){
    for(;i<=n;i+=i&(-i)) bit[i]+=val; // add lowest bit
}
int query(int i){ // prefix sum [1..i]
    int sum=0;
    for(;i>0;i-=i&(-i)) sum+=bit[i]; // remove lowest bit
    return sum;
}
int rangeQuery(int l,int r){return query(r)-query(l-1);}`,
          "Kotlin": `val bit=IntArray(n+1)
fun update(i:Int,v:Int){var x=i; while(x<=n){bit[x]+=v;x+=x and(-x)}}
fun query(i:Int):Int{var x=i;var s=0; while(x>0){s+=bit[x];x-=x and(-x)};return s}`,
          "Python": `bit=[0]*(n+1)  # 1-indexed
def update(i, val):
    while i <= n: bit[i]+=val; i+=i&(-i)
def query(i):
    s=0
    while i>0: s+=bit[i]; i-=i&(-i)
    return s`
        }
      },
      {
        name: "Tarjan's SCC & Bridges",
        recognition: "Strongly connected components. Find bridges/articulation points.",
        mentalModel: "DFS with disc (discovery time) and low (lowest disc reachable). SCC: use stack.",
        pitfalls: "Track disc and low separately. Node on stack = still in DFS path.",
        problems: [
          { num: "1192", name: "Critical Connections in Network", url: "https://leetcode.com/problems/critical-connections-in-a-network/" }
        ],
        code: {
          "Java": `// Find Bridges (Critical Connections)
int[] disc=new int[n],low=new int[n]; boolean[] vis=new boolean[n];
int[] timer={0};
void dfs(int u,int parent){
    disc[u]=low[u]=timer[0]++;vis[u]=true;
    for(int v:adj.get(u)){
        if(!vis[v]){
            dfs(v,u);
            low[u]=Math.min(low[u],low[v]);
            if(low[v]>disc[u]) bridges.add(List.of(u,v)); // bridge!
        } else if(v!=parent) low[u]=Math.min(low[u],disc[v]);
    }
}`,
          "Kotlin": `val disc=IntArray(n); val low=IntArray(n); val vis=BooleanArray(n)
var time=0
fun dfs(u:Int,parent:Int){
    disc[u]=time; low[u]=time++; vis[u]=true
    for(v in adj[u]){
        if(!vis[v]){dfs(v,u);low[u]=minOf(low[u],low[v]);if(low[v]>disc[u]) bridges.add(listOf(u,v))}
        else if(v!=parent) low[u]=minOf(low[u],disc[v])
    }
}`,
          "Python": `disc=[0]*n; low=[0]*n; vis=[False]*n; timer=[0]
def dfs(u, parent):
    disc[u]=low[u]=timer[0]; timer[0]+=1; vis[u]=True
    for v in adj[u]:
        if not vis[v]:
            dfs(v,u); low[u]=min(low[u],low[v])
            if low[v]>disc[u]: bridges.append([u,v])  # bridge!
        elif v!=parent: low[u]=min(low[u],disc[v])`
        }
      }
    ]
  }

];

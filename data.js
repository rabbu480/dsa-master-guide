const dsaData = [

  // ─── 1. ARRAYS & STRINGS ─────────────────────────────────────────────────
  {
    title: "Arrays & Strings",
    color: "#b5563c",
    patterns: [
      {
        name: "Traversal",
        recognition: "Process every element once. Linear scan.",
        mentalModel: "Simple loop 0 to N. Track indices carefully.",
        pitfalls: "Off-by-one. Modifying array while iterating.",
        problems: [
          { num: "1", name: "Two Sum", url: "https://leetcode.com/problems/two-sum/" },
          { num: "27", name: "Remove Element", url: "https://leetcode.com/problems/remove-element/" }
        ],
        code: {
          "Java": `for (int i = 0; i < arr.length; i++) {\n    // process arr[i]\n}\n// or for-each\nfor (int x : arr) {\n    // process x\n}`,
          "Kotlin": `for (i in arr.indices) {\n    // process arr[i]\n}\n// or for-each\nfor (x in arr) {\n    // process x\n}`,
          "Python": `for i in range(len(arr)):\n    # process arr[i]\n\n# or enumerate\nfor i, x in enumerate(arr):\n    # process x`
        }
      },
      {
        name: "Frequency Count (HashMap)",
        recognition: "Count occurrences. Find most frequent. Anagram check.",
        mentalModel: "Map element → count. Then query the map.",
        pitfalls: "Forgetting getOrDefault(). Null pointer on .get().",
        problems: [
          { num: "242", name: "Valid Anagram", url: "https://leetcode.com/problems/valid-anagram/" },
          { num: "347", name: "Top K Frequent Elements", url: "https://leetcode.com/problems/top-k-frequent-elements/" }
        ],
        code: {
          "Java": `Map<Integer, Integer> freq = new HashMap<>();\nfor (int x : arr) {\n    freq.put(x, freq.getOrDefault(x, 0) + 1);\n}\n// query\nint count = freq.getOrDefault(target, 0);`,
          "Kotlin": `val freq = mutableMapOf<Int, Int>()\nfor (x in arr) {\n    freq[x] = (freq[x] ?: 0) + 1\n}\nval count = freq.getOrDefault(target, 0)`,
          "Python": `from collections import Counter\nfreq = Counter(arr)\n# or manually:\nfreq = {}\nfor x in arr:\n    freq[x] = freq.get(x, 0) + 1`
        }
      },
      {
        name: "Prefix Sum",
        recognition: "Range sum queries. Subarray sum equals K.",
        mentalModel: "pre[i+1] = pre[i] + arr[i]. Range [L,R] = pre[R+1] - pre[L].",
        pitfalls: "1-based prefix array confusion. Initialize map with {0:1} for subarray problems.",
        problems: [
          { num: "303", name: "Range Sum Query", url: "https://leetcode.com/problems/range-sum-query-immutable/" },
          { num: "560", name: "Subarray Sum Equals K", url: "https://leetcode.com/problems/subarray-sum-equals-k/" }
        ],
        code: {
          "Java": `int[] pre = new int[n + 1];\nfor (int i = 0; i < n; i++) pre[i+1] = pre[i] + arr[i];\n// range sum L to R:\nint rangeSum = pre[R+1] - pre[L];\n\n// Subarray sum = K\nMap<Integer,Integer> map = new HashMap<>();\nmap.put(0, 1); int sum = 0, res = 0;\nfor (int x : arr) {\n    sum += x;\n    res += map.getOrDefault(sum - k, 0);\n    map.put(sum, map.getOrDefault(sum, 0) + 1);\n}`,
          "Kotlin": `val pre = IntArray(n + 1)\nfor (i in 0 until n) pre[i+1] = pre[i] + arr[i]\nval rangeSum = pre[R+1] - pre[L]`,
          "Python": `pre = [0] * (n + 1)\nfor i in range(n):\n    pre[i+1] = pre[i] + arr[i]\nrange_sum = pre[R+1] - pre[L]\n\n# Subarray sum = K\nfrom collections import defaultdict\ncount = defaultdict(int)\ncount[0] = 1\nres = s = 0\nfor x in arr:\n    s += x\n    res += count[s - k]\n    count[s] += 1`
        }
      },
      {
        name: "Difference Array",
        recognition: "Multiple range update queries, then final array.",
        mentalModel: "diff[L] += val, diff[R+1] -= val. Then prefix sum to get result.",
        pitfalls: "Forgetting the sweep step after all updates.",
        problems: [
          { num: "1109", name: "Corporate Flight Bookings", url: "https://leetcode.com/problems/corporate-flight-bookings/" },
          { num: "1094", name: "Car Pooling", url: "https://leetcode.com/problems/car-pooling/" }
        ],
        code: {
          "Java": `int[] diff = new int[n + 1];\n// range update [L, R] with val\ndiff[L] += val;\ndiff[R + 1] -= val;\n// rebuild final array\nint[] result = new int[n];\nresult[0] = diff[0];\nfor (int i = 1; i < n; i++) {\n    result[i] = result[i-1] + diff[i];\n}`,
          "Kotlin": `val diff = IntArray(n + 1)\ndiff[L] += `val`\ndiff[R + 1] -= `val`\nval result = IntArray(n)\nresult[0] = diff[0]\nfor (i in 1 until n) result[i] = result[i-1] + diff[i]`,
          "Python": `diff = [0] * (n + 1)\ndiff[L] += val\ndiff[R + 1] -= val\nresult = [0] * n\nresult[0] = diff[0]\nfor i in range(1, n):\n    result[i] = result[i-1] + diff[i]`
        }
      },
      {
        name: "Kadane's Algorithm",
        recognition: "Maximum subarray sum. Continuous segment.",
        mentalModel: "maxEnd = max(x, maxEnd + x). Reset when negative.",
        pitfalls: "All-negative array: return max element, not 0.",
        problems: [
          { num: "53", name: "Maximum Subarray", url: "https://leetcode.com/problems/maximum-subarray/" },
          { num: "918", name: "Max Sum Circular Subarray", url: "https://leetcode.com/problems/maximum-sum-circular-subarray/" }
        ],
        code: {
          "Java": `int maxEnd = arr[0], maxSoFar = arr[0];\nfor (int i = 1; i < arr.length; i++) {\n    maxEnd = Math.max(arr[i], maxEnd + arr[i]);\n    maxSoFar = Math.max(maxSoFar, maxEnd);\n}\nreturn maxSoFar;`,
          "Kotlin": `var maxEnd = arr[0]\nvar maxSoFar = arr[0]\nfor (i in 1 until arr.size) {\n    maxEnd = maxOf(arr[i], maxEnd + arr[i])\n    maxSoFar = maxOf(maxSoFar, maxEnd)\n}\nreturn maxSoFar`,
          "Python": `max_end = max_so_far = arr[0]\nfor x in arr[1:]:\n    max_end = max(x, max_end + x)\n    max_so_far = max(max_so_far, max_end)\nreturn max_so_far`
        }
      },
      {
        name: "Matrix Traversal",
        recognition: "2D grid, spiral, diagonal, rotate 90°.",
        mentalModel: "Use 4 direction arrays dx=[0,0,1,-1], dy=[1,-1,0,0]. Boundary checks.",
        pitfalls: "Out of bounds. Visiting same cell twice (use visited set).",
        problems: [
          { num: "54", name: "Spiral Matrix", url: "https://leetcode.com/problems/spiral-matrix/" },
          { num: "48", name: "Rotate Image", url: "https://leetcode.com/problems/rotate-image/" }
        ],
        code: {
          "Java": `int[] dx = {0, 0, 1, -1};\nint[] dy = {1, -1, 0, 0};\n// BFS from (r, c)\nboolean[][] vis = new boolean[R][C];\nQueue<int[]> q = new LinkedList<>();\nq.offer(new int[]{r, c});\nvis[r][c] = true;\nwhile (!q.isEmpty()) {\n    int[] cur = q.poll();\n    for (int d = 0; d < 4; d++) {\n        int nr = cur[0] + dx[d];\n        int nc = cur[1] + dy[d];\n        if (nr>=0 && nr<R && nc>=0 && nc<C && !vis[nr][nc]) {\n            vis[nr][nc] = true;\n            q.offer(new int[]{nr, nc});\n        }\n    }\n}`,
          "Kotlin": `val dx = intArrayOf(0, 0, 1, -1)\nval dy = intArrayOf(1, -1, 0, 0)\nfor (d in 0..3) {\n    val nr = r + dx[d]\n    val nc = c + dy[d]\n    if (nr in 0 until R && nc in 0 until C) {\n        // process\n    }\n}`,
          "Python": `dx = [0, 0, 1, -1]\ndy = [1, -1, 0, 0]\nfor d in range(4):\n    nr, nc = r + dx[d], c + dy[d]\n    if 0 <= nr < R and 0 <= nc < C:\n        pass  # process`
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
        recognition: "Sorted array, pair sum, palindrome, reverse.",
        mentalModel: "Left at 0, right at end. Move based on comparison.",
        pitfalls: "l < r not l <= r. Must be sorted first.",
        problems: [
          { num: "167", name: "Two Sum II", url: "https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/" },
          { num: "11", name: "Container With Most Water", url: "https://leetcode.com/problems/container-with-most-water/" },
          { num: "125", name: "Valid Palindrome", url: "https://leetcode.com/problems/valid-palindrome/" }
        ],
        code: {
          "Java": `int l = 0, r = arr.length - 1;\nwhile (l < r) {\n    int sum = arr[l] + arr[r];\n    if (sum == target) return new int[]{l, r};\n    else if (sum < target) l++;\n    else r--;\n}`,
          "Kotlin": `var l = 0; var r = arr.size - 1\nwhile (l < r) {\n    val sum = arr[l] + arr[r]\n    when {\n        sum == target -> return intArrayOf(l, r)\n        sum < target -> l++\n        else -> r--\n    }\n}`,
          "Python": `l, r = 0, len(arr) - 1\nwhile l < r:\n    s = arr[l] + arr[r]\n    if s == target: return [l, r]\n    elif s < target: l += 1\n    else: r -= 1`
        }
      },
      {
        name: "Same Direction",
        recognition: "In-place modification, remove duplicates, partition.",
        mentalModel: "Slow tracks valid zone, fast explores. Copy fast to slow when valid.",
        pitfalls: "Overwriting data before reading it.",
        problems: [
          { num: "26", name: "Remove Duplicates", url: "https://leetcode.com/problems/remove-duplicates-from-sorted-array/" },
          { num: "283", name: "Move Zeroes", url: "https://leetcode.com/problems/move-zeroes/" }
        ],
        code: {
          "Java": `int slow = 0;\nfor (int fast = 0; fast < n; fast++) {\n    if (isValid(arr[fast])) {\n        arr[slow++] = arr[fast];\n    }\n}\n// slow = new length`,
          "Kotlin": `var slow = 0\nfor (fast in 0 until n) {\n    if (isValid(arr[fast])) {\n        arr[slow++] = arr[fast]\n    }\n}`,
          "Python": `slow = 0\nfor fast in range(len(arr)):\n    if is_valid(arr[fast]):\n        arr[slow] = arr[fast]\n        slow += 1`
        }
      },
      {
        name: "Fast & Slow Pointer",
        recognition: "Cycle detection, middle of linked list.",
        mentalModel: "Fast moves 2x. They meet inside cycle or fast reaches null.",
        pitfalls: "Null check: fast != null AND fast.next != null.",
        problems: [
          { num: "141", name: "Linked List Cycle", url: "https://leetcode.com/problems/linked-list-cycle/" },
          { num: "876", name: "Middle of Linked List", url: "https://leetcode.com/problems/middle-of-the-linked-list/" }
        ],
        code: {
          "Java": `ListNode slow = head, fast = head;\nwhile (fast != null && fast.next != null) {\n    slow = slow.next;\n    fast = fast.next.next;\n    if (slow == fast) return true; // cycle\n}\n// slow = middle`,
          "Kotlin": `var slow = head; var fast = head\nwhile (fast?.next != null) {\n    slow = slow?.next\n    fast = fast.next?.next\n    if (slow === fast) return true\n}`,
          "Python": `slow = fast = head\nwhile fast and fast.next:\n    slow = slow.next\n    fast = fast.next.next\n    if slow == fast:\n        return True  # cycle`
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
        recognition: "Subarray of exact size K. Max/min/avg over all windows.",
        mentalModel: "Slide a window of size K. Add right element, remove left element.",
        pitfalls: "Update result AFTER window reaches size K.",
        problems: [
          { num: "643", name: "Max Avg Subarray I", url: "https://leetcode.com/problems/maximum-average-subarray-i/" }
        ],
        code: {
          "Java": `int sum = 0;\nfor (int i = 0; i < k; i++) sum += arr[i];\nint best = sum;\nfor (int i = k; i < n; i++) {\n    sum += arr[i] - arr[i - k];\n    best = Math.max(best, sum);\n}\nreturn best;`,
          "Kotlin": `var sum = arr.take(k).sum()\nvar best = sum\nfor (i in k until arr.size) {\n    sum += arr[i] - arr[i - k]\n    best = maxOf(best, sum)\n}\nreturn best`,
          "Python": `window = sum(arr[:k])\nbest = window\nfor i in range(k, len(arr)):\n    window += arr[i] - arr[i - k]\n    best = max(best, window)\nreturn best`
        }
      },
      {
        name: "Variable Window",
        recognition: "Longest/shortest window satisfying a condition.",
        mentalModel: "Expand right always. Shrink left while condition breaks.",
        pitfalls: "Update result OUTSIDE the while loop (after shrinking).",
        problems: [
          { num: "3", name: "Longest Substring No Repeat", url: "https://leetcode.com/problems/longest-substring-without-repeating-characters/" },
          { num: "209", name: "Min Size Subarray Sum", url: "https://leetcode.com/problems/minimum-size-subarray-sum/" }
        ],
        code: {
          "Java": `int l = 0, res = 0;\nfor (int r = 0; r < n; r++) {\n    // add arr[r] to window state\n    while (/* window invalid */) {\n        // remove arr[l] from state\n        l++;\n    }\n    res = Math.max(res, r - l + 1);\n}`,
          "Kotlin": `var l = 0; var res = 0\nfor (r in 0 until n) {\n    // add arr[r] to state\n    while (/* invalid */) {\n        // remove arr[l]\n        l++\n    }\n    res = maxOf(res, r - l + 1)\n}`,
          "Python": `l = res = 0\nfor r in range(len(arr)):\n    # add arr[r] to state\n    while False:  # invalid condition\n        # remove arr[l]\n        l += 1\n    res = max(res, r - l + 1)`
        }
      },
      {
        name: "Frequency Map Window",
        recognition: "Window with at most/exactly K distinct characters/elements.",
        mentalModel: "HashMap tracks freq. Shrink when map.size() > K. Exactly K = AtMost(K) - AtMost(K-1).",
        pitfalls: "Remove key from map when count reaches 0. Exactly K trick.",
        problems: [
          { num: "76", name: "Minimum Window Substring", url: "https://leetcode.com/problems/minimum-window-substring/" },
          { num: "992", name: "Subarrays with K Different", url: "https://leetcode.com/problems/subarrays-with-k-different-integers/" }
        ],
        code: {
          "Java": `// Exactly K = AtMost(K) - AtMost(K-1)\nprivate int atMost(int[] arr, int k) {\n    Map<Integer,Integer> freq = new HashMap<>();\n    int l = 0, res = 0;\n    for (int r = 0; r < arr.length; r++) {\n        freq.merge(arr[r], 1, Integer::sum);\n        while (freq.size() > k) {\n            freq.merge(arr[l], -1, Integer::sum);\n            if (freq.get(arr[l]) == 0) freq.remove(arr[l]);\n            l++;\n        }\n        res += r - l + 1;\n    }\n    return res;\n}`,
          "Kotlin": `fun atMost(arr: IntArray, k: Int): Int {\n    val freq = mutableMapOf<Int, Int>()\n    var l = 0; var res = 0\n    for (r in arr.indices) {\n        freq[arr[r]] = (freq[arr[r]] ?: 0) + 1\n        while (freq.size > k) {\n            freq[arr[l]] = freq[arr[l]]!! - 1\n            if (freq[arr[l]] == 0) freq.remove(arr[l])\n            l++\n        }\n        res += r - l + 1\n    }\n    return res\n}`,
          "Python": `def at_most(arr, k):\n    freq = {}\n    l = res = 0\n    for r, x in enumerate(arr):\n        freq[x] = freq.get(x, 0) + 1\n        while len(freq) > k:\n            freq[arr[l]] -= 1\n            if freq[arr[l]] == 0: del freq[arr[l]]\n            l += 1\n        res += r - l + 1\n    return res`
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
        recognition: "Group anagrams. Frequency analysis. Top K frequent.",
        mentalModel: "Map each element or signature to a group/count.",
        pitfalls: "Arrays.sort() for anagram key. getOrDefault() always.",
        problems: [
          { num: "49", name: "Group Anagrams", url: "https://leetcode.com/problems/group-anagrams/" },
          { num: "347", name: "Top K Frequent", url: "https://leetcode.com/problems/top-k-frequent-elements/" }
        ],
        code: {
          "Java": `Map<String, List<String>> map = new HashMap<>();\nfor (String w : words) {\n    char[] c = w.toCharArray(); Arrays.sort(c);\n    String key = new String(c);\n    map.computeIfAbsent(key, k -> new ArrayList<>()).add(w);\n}`,
          "Kotlin": `val map = mutableMapOf<String, MutableList<String>>()\nfor (w in words) {\n    val key = w.toCharArray().sorted().joinToString(\"\")\n    map.getOrPut(key) { mutableListOf() }.add(w)\n}`,
          "Python": `from collections import defaultdict\nmap = defaultdict(list)\nfor w in words:\n    key = ''.join(sorted(w))\n    map[key].append(w)`
        }
      },
      {
        name: "Lookup & Deduplication",
        recognition: "Check if element exists. Remove duplicates. Longest consecutive.",
        mentalModel: "HashSet = O(1) existence check. No ordering needed.",
        pitfalls: "Set vs Map. equals()/hashCode() for custom objects.",
        problems: [
          { num: "128", name: "Longest Consecutive", url: "https://leetcode.com/problems/longest-consecutive-sequence/" },
          { num: "217", name: "Contains Duplicate", url: "https://leetcode.com/problems/contains-duplicate/" }
        ],
        code: {
          "Java": `Set<Integer> set = new HashSet<>();\nfor (int n : nums) set.add(n);\nint best = 0;\nfor (int n : set) {\n    if (!set.contains(n - 1)) { // start of sequence\n        int len = 1;\n        while (set.contains(n + len)) len++;\n        best = Math.max(best, len);\n    }\n}`,
          "Kotlin": `val set = nums.toHashSet()\nvar best = 0\nfor (n in set) {\n    if (n - 1 !in set) {\n        var len = 1\n        while (n + len in set) len++\n        best = maxOf(best, len)\n    }\n}`,
          "Python": `s = set(nums)\nbest = 0\nfor n in s:\n    if n - 1 not in s:\n        length = 1\n        while n + length in s:\n            length += 1\n        best = max(best, length)`
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
        name: "Basic Stack (Parentheses)",
        recognition: "Matching pairs, undo operations, reverse order.",
        mentalModel: "Push opening. On closing, pop and check match.",
        pitfalls: "Pop on empty stack. Check stack is empty at end.",
        problems: [
          { num: "20", name: "Valid Parentheses", url: "https://leetcode.com/problems/valid-parentheses/" },
          { num: "150", name: "Evaluate RPN", url: "https://leetcode.com/problems/evaluate-reverse-polish-notation/" }
        ],
        code: {
          "Java": `Deque<Character> st = new ArrayDeque<>();\nfor (char c : s.toCharArray()) {\n    if (c == '(') st.push(c);\n    else if (c == ')') {\n        if (st.isEmpty()) return false;\n        st.pop();\n    }\n}\nreturn st.isEmpty();`,
          "Kotlin": `val st = ArrayDeque<Char>()\nfor (c in s) {\n    if (c == '(') st.addLast(c)\n    else if (c == ')') {\n        if (st.isEmpty()) return false\n        st.removeLast()\n    }\n}\nreturn st.isEmpty()`,
          "Python": `st = []\nfor c in s:\n    if c == '(': st.append(c)\n    elif c == ')':\n        if not st: return False\n        st.pop()\nreturn len(st) == 0`
        }
      },
      {
        name: "Monotonic Increasing Stack",
        recognition: "Next Smaller Element. Previous Smaller Element.",
        mentalModel: "Pop elements GREATER than current. Stack stays increasing.",
        pitfalls: "Store indices not values for distance calculations.",
        problems: [
          { num: "84", name: "Largest Rectangle", url: "https://leetcode.com/problems/largest-rectangle-in-histogram/" }
        ],
        code: {
          "Java": `Deque<Integer> st = new ArrayDeque<>(); // stores indices\nfor (int i = 0; i <= n; i++) {\n    int h = (i == n) ? 0 : heights[i];\n    while (!st.isEmpty() && heights[st.peek()] > h) {\n        int height = heights[st.pop()];\n        int width = st.isEmpty() ? i : i - st.peek() - 1;\n        res = Math.max(res, height * width);\n    }\n    st.push(i);\n}`,
          "Kotlin": `val st = ArrayDeque<Int>()\nfor (i in 0..n) {\n    val h = if (i == n) 0 else heights[i]\n    while (st.isNotEmpty() && heights[st.last()] > h) {\n        val height = heights[st.removeLast()]\n        val width = if (st.isEmpty()) i else i - st.last() - 1\n        res = maxOf(res, height * width)\n    }\n    st.addLast(i)\n}`,
          "Python": `st = []  # indices\nfor i in range(len(heights) + 1):\n    h = 0 if i == len(heights) else heights[i]\n    while st and heights[st[-1]] > h:\n        height = heights[st.pop()]\n        width = i if not st else i - st[-1] - 1\n        res = max(res, height * width)\n    st.append(i)`
        }
      },
      {
        name: "Monotonic Decreasing Stack",
        recognition: "Next Greater Element. Temperatures. Span.",
        mentalModel: "Pop elements SMALLER than current. Stack stays decreasing.",
        pitfalls: "Indices vs values. Answer array initialization.",
        problems: [
          { num: "739", name: "Daily Temperatures", url: "https://leetcode.com/problems/daily-temperatures/" },
          { num: "496", name: "Next Greater Element I", url: "https://leetcode.com/problems/next-greater-element-i/" }
        ],
        code: {
          "Java": `int[] res = new int[n];\nDeque<Integer> st = new ArrayDeque<>();\nfor (int i = 0; i < n; i++) {\n    while (!st.isEmpty() && arr[st.peek()] < arr[i]) {\n        res[st.pop()] = i - st.peek(); // days until warmer\n    }\n    st.push(i);\n}`,
          "Kotlin": `val res = IntArray(n)\nval st = ArrayDeque<Int>()\nfor (i in 0 until n) {\n    while (st.isNotEmpty() && arr[st.last()] < arr[i]) {\n        res[st.removeLast()] = arr[i] // next greater value\n    }\n    st.addLast(i)\n}`,
          "Python": `res = [0] * n\nst = []\nfor i, x in enumerate(arr):\n    while st and arr[st[-1]] < x:\n        res[st.pop()] = x\n    st.append(i)`
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
        name: "BFS Queue",
        recognition: "Shortest path in unweighted graph. Level-by-level.",
        mentalModel: "Queue + visited set. Process level using size snapshot.",
        pitfalls: "Mark visited WHEN enqueuing, not when dequeuing.",
        problems: [
          { num: "102", name: "Level Order Traversal", url: "https://leetcode.com/problems/binary-tree-level-order-traversal/" },
          { num: "127", name: "Word Ladder", url: "https://leetcode.com/problems/word-ladder/" }
        ],
        code: {
          "Java": `Queue<Node> q = new LinkedList<>();\nSet<Node> vis = new HashSet<>();\nq.offer(start); vis.add(start);\nwhile (!q.isEmpty()) {\n    int size = q.size();\n    for (int i = 0; i < size; i++) {\n        Node cur = q.poll();\n        for (Node nb : neighbors(cur)) {\n            if (!vis.contains(nb)) {\n                vis.add(nb); q.offer(nb);\n            }\n        }\n    }\n}`,
          "Kotlin": `val q = ArrayDeque<Node>()\nval vis = mutableSetOf<Node>()\nq.addLast(start); vis.add(start)\nwhile (q.isNotEmpty()) {\n    repeat(q.size) {\n        val cur = q.removeFirst()\n        for (nb in neighbors(cur)) {\n            if (nb !in vis) { vis.add(nb); q.addLast(nb) }\n        }\n    }\n}`,
          "Python": `from collections import deque\nq = deque([start])\nvis = {start}\nwhile q:\n    for _ in range(len(q)):\n        cur = q.popleft()\n        for nb in neighbors(cur):\n            if nb not in vis:\n                vis.add(nb)\n                q.append(nb)`
        }
      },
      {
        name: "Monotonic Deque",
        recognition: "Sliding window maximum or minimum.",
        mentalModel: "Deque stores indices. Pop front if out-of-window. Pop back if smaller than new element.",
        pitfalls: "Store indices not values. Deque front = current max.",
        problems: [
          { num: "239", name: "Sliding Window Maximum", url: "https://leetcode.com/problems/sliding-window-maximum/" }
        ],
        code: {
          "Java": `Deque<Integer> dq = new ArrayDeque<>();\nint[] res = new int[n - k + 1];\nfor (int i = 0; i < n; i++) {\n    // Remove out-of-window\n    if (!dq.isEmpty() && dq.peekFirst() == i - k) dq.pollFirst();\n    // Remove smaller from back\n    while (!dq.isEmpty() && arr[dq.peekLast()] < arr[i]) dq.pollLast();\n    dq.offerLast(i);\n    if (i >= k - 1) res[i - k + 1] = arr[dq.peekFirst()];\n}`,
          "Kotlin": `val dq = ArrayDeque<Int>()\nval res = IntArray(n - k + 1)\nfor (i in 0 until n) {\n    if (dq.isNotEmpty() && dq.first() == i - k) dq.removeFirst()\n    while (dq.isNotEmpty() && arr[dq.last()] < arr[i]) dq.removeLast()\n    dq.addLast(i)\n    if (i >= k - 1) res[i - k + 1] = arr[dq.first()]\n}`,
          "Python": `from collections import deque\ndq = deque()\nres = []\nfor i, x in enumerate(arr):\n    if dq and dq[0] == i - k: dq.popleft()\n    while dq and arr[dq[-1]] < x: dq.pop()\n    dq.append(i)\n    if i >= k - 1: res.append(arr[dq[0]])`
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
        recognition: "Find exact target in sorted array. O(log N).",
        mentalModel: "Halve search space based on mid comparison.",
        pitfalls: "mid = l + (r-l)/2 to avoid overflow. l<=r for classic.",
        problems: [
          { num: "704", name: "Binary Search", url: "https://leetcode.com/problems/binary-search/" }
        ],
        code: {
          "Java": `int l = 0, r = n - 1;\nwhile (l <= r) {\n    int mid = l + (r - l) / 2;\n    if (arr[mid] == target) return mid;\n    if (arr[mid] < target) l = mid + 1;\n    else r = mid - 1;\n}\nreturn -1;`,
          "Kotlin": `var l = 0; var r = arr.size - 1\nwhile (l <= r) {\n    val mid = l + (r - l) / 2\n    when {\n        arr[mid] == target -> return mid\n        arr[mid] < target -> l = mid + 1\n        else -> r = mid - 1\n    }\n}`,
          "Python": `l, r = 0, len(arr) - 1\nwhile l <= r:\n    mid = l + (r - l) // 2\n    if arr[mid] == target: return mid\n    if arr[mid] < target: l = mid + 1\n    else: r = mid - 1\nreturn -1`
        }
      },
      {
        name: "Lower / Upper Bound",
        recognition: "First or last occurrence of target. First element >= target.",
        mentalModel: "If match: keep searching left (lower) or right (upper). l < r variant.",
        pitfalls: "l < r for boundaries. Return l not mid.",
        problems: [
          { num: "34", name: "First and Last Position", url: "https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/" },
          { num: "35", name: "Search Insert Position", url: "https://leetcode.com/problems/search-insert-position/" }
        ],
        code: {
          "Java": `// Lower bound (first >= target)\nint l = 0, r = n;\nwhile (l < r) {\n    int m = l + (r - l) / 2;\n    if (arr[m] >= target) r = m;\n    else l = m + 1;\n}\nreturn l;\n\n// Upper bound (first > target)\n// Replace >= with >`,
          "Kotlin": `// Lower bound\nvar l = 0; var r = arr.size\nwhile (l < r) {\n    val m = l + (r - l) / 2\n    if (arr[m] >= target) r = m\n    else l = m + 1\n}\nreturn l`,
          "Python": `import bisect\n# lower bound (first >= target)\nbisect.bisect_left(arr, target)\n# upper bound (first > target)\nbisect.bisect_right(arr, target)\n\n# Manual lower bound:\nl, r = 0, len(arr)\nwhile l < r:\n    m = (l + r) // 2\n    if arr[m] >= target: r = m\n    else: l = m + 1`
        }
      },
      {
        name: "Rotated Array Search",
        recognition: "Array rotated at unknown pivot. No duplicates.",
        mentalModel: "One half is always sorted. Check which half and whether target is in it.",
        pitfalls: "Duplicates require special handling. Check sorted half first.",
        problems: [
          { num: "33", name: "Search in Rotated Array", url: "https://leetcode.com/problems/search-in-rotated-sorted-array/" },
          { num: "153", name: "Find Min in Rotated", url: "https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/" }
        ],
        code: {
          "Java": `int l = 0, r = arr.length - 1;\nwhile (l <= r) {\n    int m = l + (r - l) / 2;\n    if (arr[m] == target) return m;\n    if (arr[l] <= arr[m]) { // left half sorted\n        if (target >= arr[l] && target < arr[m]) r = m - 1;\n        else l = m + 1;\n    } else { // right half sorted\n        if (target > arr[m] && target <= arr[r]) l = m + 1;\n        else r = m - 1;\n    }\n}`,
          "Kotlin": `var l = 0; var r = arr.size - 1\nwhile (l <= r) {\n    val m = l + (r - l) / 2\n    if (arr[m] == target) return m\n    if (arr[l] <= arr[m]) {\n        if (target in arr[l] until arr[m]) r = m - 1 else l = m + 1\n    } else {\n        if (target in (arr[m]+1)..arr[r]) l = m + 1 else r = m - 1\n    }\n}`,
          "Python": `l, r = 0, len(arr) - 1\nwhile l <= r:\n    m = (l + r) // 2\n    if arr[m] == target: return m\n    if arr[l] <= arr[m]:  # left sorted\n        if arr[l] <= target < arr[m]: r = m - 1\n        else: l = m + 1\n    else:  # right sorted\n        if arr[m] < target <= arr[r]: l = m + 1\n        else: r = m - 1`
        }
      },
      {
        name: "Binary Search on Answer",
        recognition: "Minimize max / Maximize min. 'Smallest X such that...'",
        mentalModel: "Search the ANSWER space (not array). Check if answer is feasible.",
        pitfalls: "isValid function logic is often the hard part. Boundary hi/lo values.",
        problems: [
          { num: "875", name: "Koko Eating Bananas", url: "https://leetcode.com/problems/koko-eating-bananas/" },
          { num: "410", name: "Split Array Largest Sum", url: "https://leetcode.com/problems/split-array-largest-sum/" }
        ],
        code: {
          "Java": `int l = minPossible, r = maxPossible;\nwhile (l < r) {\n    int mid = l + (r - l) / 2;\n    if (isValid(mid)) r = mid; // try smaller\n    else l = mid + 1;\n}\nreturn l; // minimum valid answer`,
          "Kotlin": `var l = minPossible; var r = maxPossible\nwhile (l < r) {\n    val mid = l + (r - l) / 2\n    if (isValid(mid)) r = mid\n    else l = mid + 1\n}\nreturn l`,
          "Python": `l, r = min_possible, max_possible\nwhile l < r:\n    mid = (l + r) // 2\n    if is_valid(mid):\n        r = mid  # try smaller\n    else:\n        l = mid + 1\nreturn l`
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
        name: "Reverse List",
        recognition: "Reverse entire or partial linked list.",
        mentalModel: "Three pointers: prev, curr, next. Save next before overwriting.",
        pitfalls: "Losing next pointer. Always use dummy node.",
        problems: [
          { num: "206", name: "Reverse Linked List", url: "https://leetcode.com/problems/reverse-linked-list/" },
          { num: "92", name: "Reverse Between", url: "https://leetcode.com/problems/reverse-linked-list-ii/" }
        ],
        code: {
          "Java": `ListNode prev = null, curr = head;\nwhile (curr != null) {\n    ListNode next = curr.next;\n    curr.next = prev;\n    prev = curr;\n    curr = next;\n}\nreturn prev; // new head`,
          "Kotlin": `var prev: ListNode? = null\nvar curr: ListNode? = head\nwhile (curr != null) {\n    val next = curr.next\n    curr.next = prev\n    prev = curr\n    curr = next\n}\nreturn prev`,
          "Python": `prev, curr = None, head\nwhile curr:\n    nxt = curr.next\n    curr.next = prev\n    prev = curr\n    curr = nxt\nreturn prev`
        }
      },
      {
        name: "Remove Nth & Middle Node",
        recognition: "Remove Nth from end. Find middle. Two-pass or one-pass.",
        mentalModel: "Fast pointer N steps ahead. Both move together until fast hits end.",
        pitfalls: "Dummy node prevents edge case of removing head.",
        problems: [
          { num: "19", name: "Remove Nth From End", url: "https://leetcode.com/problems/remove-nth-node-from-end-of-list/" },
          { num: "876", name: "Middle of Linked List", url: "https://leetcode.com/problems/middle-of-the-linked-list/" }
        ],
        code: {
          "Java": `ListNode dummy = new ListNode(0, head);\nListNode fast = dummy, slow = dummy;\nfor (int i = 0; i <= n; i++) fast = fast.next;\nwhile (fast != null) { slow = slow.next; fast = fast.next; }\nslow.next = slow.next.next;\nreturn dummy.next;`,
          "Kotlin": `val dummy = ListNode(0).apply { next = head }\nvar fast: ListNode? = dummy; var slow: ListNode? = dummy\nfor (i in 0..n) fast = fast?.next\nwhile (fast != null) { slow = slow?.next; fast = fast?.next }\nslow?.next = slow?.next?.next\nreturn dummy.next`,
          "Python": `dummy = ListNode(0, head)\nfast = slow = dummy\nfor _ in range(n + 1):\n    fast = fast.next\nwhile fast:\n    slow = slow.next\n    fast = fast.next\nslow.next = slow.next.next\nreturn dummy.next`
        }
      },
      {
        name: "Merge & Reorder Lists",
        recognition: "Merge K sorted lists. Reorder L0→Ln→L1→Ln-1.",
        mentalModel: "Merge two: compare heads. Reorder: find mid + reverse second half + interleave.",
        pitfalls: "Breaking links when splitting. Min-heap for merge K lists.",
        problems: [
          { num: "21", name: "Merge Two Sorted Lists", url: "https://leetcode.com/problems/merge-two-sorted-lists/" },
          { num: "143", name: "Reorder List", url: "https://leetcode.com/problems/reorder-list/" },
          { num: "23", name: "Merge K Sorted Lists", url: "https://leetcode.com/problems/merge-k-sorted-lists/" }
        ],
        code: {
          "Java": `// Merge Two\nListNode dummy = new ListNode(0), cur = dummy;\nwhile (l1 != null && l2 != null) {\n    if (l1.val < l2.val) { cur.next = l1; l1 = l1.next; }\n    else { cur.next = l2; l2 = l2.next; }\n    cur = cur.next;\n}\ncur.next = (l1 != null) ? l1 : l2;`,
          "Kotlin": `val dummy = ListNode(0); var cur: ListNode? = dummy\nwhile (l1 != null && l2 != null) {\n    if (l1.`val` < l2.`val`) { cur?.next = l1; l1 = l1.next }\n    else { cur?.next = l2; l2 = l2.next }\n    cur = cur?.next\n}\ncur?.next = l1 ?: l2`,
          "Python": `dummy = ListNode(0)\ncur = dummy\nwhile l1 and l2:\n    if l1.val < l2.val:\n        cur.next, l1 = l1, l1.next\n    else:\n        cur.next, l2 = l2, l2.next\n    cur = cur.next\ncur.next = l1 or l2`
        }
      }
    ]
  },

  // ─── 9. TREES ────────────────────────────────────────────────────────────
  {
    title: "Trees: DFS Traversals",
    color: "#5a3a8a",
    patterns: [
      {
        name: "Preorder / Inorder / Postorder DFS",
        recognition: "Tree exploration. BST sorted order (inorder). Height calculation (postorder).",
        mentalModel: "Pre = Root first. In = Left-Root-Right (BST sorted). Post = Root last (calculate up from leaves).",
        pitfalls: "Always handle null base case first.",
        problems: [
          { num: "144", name: "Preorder Traversal", url: "https://leetcode.com/problems/binary-tree-preorder-traversal/" },
          { num: "230", name: "Kth Smallest in BST", url: "https://leetcode.com/problems/kth-smallest-element-in-a-bst/" },
          { num: "104", name: "Max Depth", url: "https://leetcode.com/problems/maximum-depth-of-binary-tree/" }
        ],
        code: {
          "Java": `void preorder(Node r) { if(r==null) return; visit(r); preorder(r.left); preorder(r.right); }\nvoid inorder(Node r)  { if(r==null) return; inorder(r.left); visit(r); inorder(r.right); }\nvoid postorder(Node r){ if(r==null) return; postorder(r.left); postorder(r.right); visit(r); }\n\n// Height (postorder)\nint height(Node r) {\n    if (r == null) return 0;\n    return 1 + Math.max(height(r.left), height(r.right));\n}`,
          "Kotlin": `fun preorder(r: Node?) { if(r==null) return; visit(r); preorder(r.left); preorder(r.right) }\nfun inorder(r: Node?)  { if(r==null) return; inorder(r.left); visit(r); inorder(r.right) }\nfun postorder(r: Node?){ if(r==null) return; postorder(r.left); postorder(r.right); visit(r) }\n\nfun height(r: Node?): Int {\n    if (r == null) return 0\n    return 1 + maxOf(height(r.left), height(r.right))\n}`,
          "Python": `def preorder(r):\n    if not r: return\n    visit(r); preorder(r.left); preorder(r.right)\n\ndef inorder(r):\n    if not r: return\n    inorder(r.left); visit(r); inorder(r.right)\n\ndef postorder(r):\n    if not r: return\n    postorder(r.left); postorder(r.right); visit(r)\n\ndef height(r):\n    if not r: return 0\n    return 1 + max(height(r.left), height(r.right))`
        }
      },
      {
        name: "Recursive Patterns (Diameter, LCA, Path Sum)",
        recognition: "Properties computed from subtree info. Pass up result.",
        mentalModel: "Postorder: compute left and right subtree values, combine for root.",
        pitfalls: "Diameter: update global max inside helper but return height. LCA: return non-null child.",
        problems: [
          { num: "543", name: "Diameter of Binary Tree", url: "https://leetcode.com/problems/diameter-of-binary-tree/" },
          { num: "236", name: "Lowest Common Ancestor", url: "https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/" },
          { num: "112", name: "Path Sum", url: "https://leetcode.com/problems/path-sum/" }
        ],
        code: {
          "Java": `// Diameter\nint res = 0;\nint dfs(Node r) {\n    if (r == null) return 0;\n    int l = dfs(r.left), ri = dfs(r.right);\n    res = Math.max(res, l + ri);\n    return 1 + Math.max(l, ri);\n}\n\n// LCA\nNode lca(Node r, Node p, Node q) {\n    if (r==null||r==p||r==q) return r;\n    Node l = lca(r.left,p,q), ri = lca(r.right,p,q);\n    return (l!=null&&ri!=null) ? r : (l!=null?l:ri);\n}`,
          "Kotlin": `// Diameter\nvar res = 0\nfun dfs(r: Node?): Int {\n    if (r == null) return 0\n    val l = dfs(r.left); val ri = dfs(r.right)\n    res = maxOf(res, l + ri)\n    return 1 + maxOf(l, ri)\n}`,
          "Python": `# Diameter\nres = [0]\ndef dfs(r):\n    if not r: return 0\n    l, ri = dfs(r.left), dfs(r.right)\n    res[0] = max(res[0], l + ri)\n    return 1 + max(l, ri)\n\n# LCA\ndef lca(r, p, q):\n    if not r or r == p or r == q: return r\n    l = lca(r.left, p, q)\n    ri = lca(r.right, p, q)\n    return r if l and ri else (l or ri)`
        }
      },
      {
        name: "BFS: Level Order, Zigzag, Right/Left View",
        recognition: "Level-by-level properties. Min depth. Right side visible nodes.",
        mentalModel: "Queue + size snapshot per level. Alternate direction for zigzag.",
        pitfalls: "Cache q.size() at start of level loop—not inside.",
        problems: [
          { num: "102", name: "Level Order", url: "https://leetcode.com/problems/binary-tree-level-order-traversal/" },
          { num: "103", name: "Zigzag Level Order", url: "https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/" },
          { num: "199", name: "Right Side View", url: "https://leetcode.com/problems/binary-tree-right-side-view/" }
        ],
        code: {
          "Java": `Queue<Node> q = new LinkedList<>();\nq.offer(root);\nboolean leftToRight = true;\nwhile (!q.isEmpty()) {\n    int size = q.size();\n    LinkedList<Integer> level = new LinkedList<>();\n    for (int i = 0; i < size; i++) {\n        Node n = q.poll();\n        if (leftToRight) level.addLast(n.val);\n        else level.addFirst(n.val); // zigzag\n        if (n.left != null) q.offer(n.left);\n        if (n.right != null) q.offer(n.right);\n    }\n    leftToRight = !leftToRight;\n}`,
          "Kotlin": `val q = ArrayDeque<Node>()\nq.addLast(root)\nvar leftToRight = true\nwhile (q.isNotEmpty()) {\n    val level = ArrayDeque<Int>()\n    repeat(q.size) {\n        val n = q.removeFirst()\n        if (leftToRight) level.addLast(n.`val`) else level.addFirst(n.`val`)\n        n.left?.let { q.addLast(it) }\n        n.right?.let { q.addLast(it) }\n    }\n    leftToRight = !leftToRight\n}`,
          "Python": `from collections import deque\nq = deque([root])\nleft_to_right = True\nwhile q:\n    level = []\n    for _ in range(len(q)):\n        n = q.popleft()\n        level.append(n.val)\n        if n.left: q.append(n.left)\n        if n.right: q.append(n.right)\n    if not left_to_right: level.reverse()\n    left_to_right = not left_to_right`
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
        name: "Top K & K-way Merge",
        recognition: "K largest, K smallest, K most frequent, Merge K sorted.",
        mentalModel: "Min-Heap size K for top K largest. Max-Heap size K for top K smallest.",
        pitfalls: "Comparator direction. Size check before peek.",
        problems: [
          { num: "215", name: "Kth Largest", url: "https://leetcode.com/problems/kth-largest-element-in-an-array/" },
          { num: "23", name: "Merge K Sorted Lists", url: "https://leetcode.com/problems/merge-k-sorted-lists/" },
          { num: "973", name: "K Closest Points", url: "https://leetcode.com/problems/k-closest-points-to-origin/" }
        ],
        code: {
          "Java": `// Top K Largest (min-heap of size K)\nPriorityQueue<Integer> pq = new PriorityQueue<>();\nfor (int x : arr) {\n    pq.offer(x);\n    if (pq.size() > k) pq.poll();\n}\nreturn pq.peek();\n\n// Merge K Lists\nPriorityQueue<ListNode> pq = new PriorityQueue<>((a,b)->a.val-b.val);\nfor (ListNode node : lists) if (node != null) pq.offer(node);\nListNode dummy = new ListNode(0), cur = dummy;\nwhile (!pq.isEmpty()) {\n    ListNode n = pq.poll(); cur.next = n; cur = cur.next;\n    if (n.next != null) pq.offer(n.next);\n}`,
          "Kotlin": `val pq = PriorityQueue<Int>()\nfor (x in arr) {\n    pq.offer(x)\n    if (pq.size > k) pq.poll()\n}\nreturn pq.peek()`,
          "Python": `import heapq\n# Top K Largest\nheap = []\nfor x in arr:\n    heapq.heappush(heap, x)\n    if len(heap) > k: heapq.heappop(heap)\nreturn heap[0]\n\n# Top K Smallest (use max-heap with negation)\nheap = []\nfor x in arr:\n    heapq.heappush(heap, -x)\n    if len(heap) > k: heapq.heappop(heap)\nreturn -heap[0]`
        }
      },
      {
        name: "Median from Data Stream",
        recognition: "Find median dynamically as numbers are added.",
        mentalModel: "Two heaps: Max-Heap for lower half, Min-Heap for upper half. Balance after each insert.",
        pitfalls: "Rebalance after every insertion. Max-Heap uses negation in Python.",
        problems: [
          { num: "295", name: "Find Median From Data Stream", url: "https://leetcode.com/problems/find-median-from-data-stream/" }
        ],
        code: {
          "Java": `PriorityQueue<Integer> lo = new PriorityQueue<>(Collections.reverseOrder()); // max-heap\nPriorityQueue<Integer> hi = new PriorityQueue<>(); // min-heap\nvoid addNum(int n) {\n    lo.offer(n);\n    hi.offer(lo.poll());\n    if (lo.size() < hi.size()) lo.offer(hi.poll());\n}\ndouble findMedian() {\n    return lo.size() > hi.size() ? lo.peek() : (lo.peek() + hi.peek()) / 2.0;\n}`,
          "Kotlin": `val lo = PriorityQueue<Int>(compareByDescending { it }) // max-heap\nval hi = PriorityQueue<Int>() // min-heap\nfun addNum(n: Int) {\n    lo.offer(n); hi.offer(lo.poll())\n    if (lo.size < hi.size) lo.offer(hi.poll())\n}\nfun findMedian() = if (lo.size > hi.size) lo.peek().toDouble() else (lo.peek() + hi.peek()) / 2.0`,
          "Python": `import heapq\nlo = []  # max-heap (negated)\nhi = []  # min-heap\n\ndef add_num(n):\n    heapq.heappush(lo, -n)\n    heapq.heappush(hi, -heapq.heappop(lo))\n    if len(lo) < len(hi):\n        heapq.heappush(lo, -heapq.heappop(hi))\n\ndef find_median():\n    if len(lo) > len(hi): return -lo[0]\n    return (-lo[0] + hi[0]) / 2`
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
        recognition: "Generate all subsets/combinations of size K or with target sum.",
        mentalModel: "At each index: include element and recurse, OR skip it.",
        pitfalls: "Add a COPY of path, not reference. Use start index to avoid duplicates.",
        problems: [
          { num: "78", name: "Subsets", url: "https://leetcode.com/problems/subsets/" },
          { num: "39", name: "Combination Sum", url: "https://leetcode.com/problems/combination-sum/" },
          { num: "77", name: "Combinations", url: "https://leetcode.com/problems/combinations/" }
        ],
        code: {
          "Java": `void backtrack(int start, List<Integer> path) {\n    res.add(new ArrayList<>(path)); // add copy\n    for (int i = start; i < nums.length; i++) {\n        path.add(nums[i]);          // choose\n        backtrack(i + 1, path);    // explore (use i to allow reuse)\n        path.remove(path.size()-1); // unchoose\n    }\n}`,
          "Kotlin": `fun backtrack(start: Int, path: MutableList<Int>) {\n    res.add(path.toList())\n    for (i in start until nums.size) {\n        path.add(nums[i])\n        backtrack(i + 1, path)\n        path.removeLast()\n    }\n}`,
          "Python": `def backtrack(start, path):\n    res.append(list(path))  # copy!\n    for i in range(start, len(nums)):\n        path.append(nums[i])\n        backtrack(i + 1, path)\n        path.pop()`
        }
      },
      {
        name: "Permutations",
        recognition: "All orderings of elements. Each element used exactly once.",
        mentalModel: "Loop all elements. Skip if used. Mark/unmark visited.",
        pitfalls: "visited[] array. Start from 0 (not i) every time.",
        problems: [
          { num: "46", name: "Permutations", url: "https://leetcode.com/problems/permutations/" },
          { num: "47", name: "Permutations II", url: "https://leetcode.com/problems/permutations-ii/" }
        ],
        code: {
          "Java": `void backtrack(List<Integer> path, boolean[] used) {\n    if (path.size() == nums.length) { res.add(new ArrayList<>(path)); return; }\n    for (int i = 0; i < nums.length; i++) {\n        if (used[i]) continue;\n        used[i] = true; path.add(nums[i]);\n        backtrack(path, used);\n        used[i] = false; path.remove(path.size()-1);\n    }\n}`,
          "Kotlin": `fun backtrack(path: MutableList<Int>, used: BooleanArray) {\n    if (path.size == nums.size) { res.add(path.toList()); return }\n    for (i in nums.indices) {\n        if (used[i]) continue\n        used[i] = true; path.add(nums[i])\n        backtrack(path, used)\n        used[i] = false; path.removeLast()\n    }\n}`,
          "Python": `def backtrack(path, used):\n    if len(path) == len(nums):\n        res.append(list(path)); return\n    for i in range(len(nums)):\n        if used[i]: continue\n        used[i] = True; path.append(nums[i])\n        backtrack(path, used)\n        used[i] = False; path.pop()`
        }
      },
      {
        name: "N-Queens & Word Search",
        recognition: "Constraint satisfaction. Valid placement. Grid path.",
        mentalModel: "Try placing at each position. Backtrack if invalid.",
        pitfalls: "Mark visited before recursing, unmark after. Track cols+diagonals.",
        problems: [
          { num: "51", name: "N-Queens", url: "https://leetcode.com/problems/n-queens/" },
          { num: "79", name: "Word Search", url: "https://leetcode.com/problems/word-search/" }
        ],
        code: {
          "Java": `// N-Queens\nvoid solve(int row, Set<Integer> cols, Set<Integer> d1, Set<Integer> d2) {\n    if (row == n) { res.add(buildBoard()); return; }\n    for (int col = 0; col < n; col++) {\n        if (cols.contains(col)||d1.contains(row-col)||d2.contains(row+col)) continue;\n        cols.add(col); d1.add(row-col); d2.add(row+col); queens[row]=col;\n        solve(row+1, cols, d1, d2);\n        cols.remove(col); d1.remove(row-col); d2.remove(row+col);\n    }\n}`,
          "Kotlin": `fun search(r: Int, c: Int, i: Int): Boolean {\n    if (i == word.length) return true\n    if (r !in 0 until R || c !in 0 until C || board[r][c] != word[i]) return false\n    val tmp = board[r][c]; board[r][c] = '#'\n    val found = search(r+1,c,i+1)||search(r-1,c,i+1)||search(r,c+1,i+1)||search(r,c-1,i+1)\n    board[r][c] = tmp; return found\n}`,
          "Python": `def dfs(r, c, i):\n    if i == len(word): return True\n    if r < 0 or r >= R or c < 0 or c >= C or board[r][c] != word[i]: return False\n    tmp = board[r][c]; board[r][c] = '#'\n    res = dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1)\n    board[r][c] = tmp\n    return res`
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
        name: "DFS, BFS, Islands & Clone",
        recognition: "Connected components, flood fill, number of islands.",
        mentalModel: "DFS: recursion + visited. BFS: queue + visited. Mark visited when adding to queue.",
        pitfalls: "Mark as visited BEFORE enqueuing. Adjacency list vs matrix.",
        problems: [
          { num: "200", name: "Number of Islands", url: "https://leetcode.com/problems/number-of-islands/" },
          { num: "133", name: "Clone Graph", url: "https://leetcode.com/problems/clone-graph/" },
          { num: "695", name: "Max Area of Island", url: "https://leetcode.com/problems/max-area-of-island/" }
        ],
        code: {
          "Java": `// Number of Islands\nvoid dfs(char[][] g, int r, int c) {\n    if (r<0||c<0||r>=g.length||c>=g[0].length||g[r][c]=='0') return;\n    g[r][c] = '0'; // mark visited\n    dfs(g,r+1,c); dfs(g,r-1,c); dfs(g,r,c+1); dfs(g,r,c-1);\n}\nint numIslands(char[][] g) {\n    int count = 0;\n    for (int r=0;r<g.length;r++) for(int c=0;c<g[0].length;c++)\n        if (g[r][c]=='1') { dfs(g,r,c); count++; }\n    return count;\n}`,
          "Kotlin": `fun dfs(g: Array<CharArray>, r: Int, c: Int) {\n    if (r !in g.indices || c !in g[0].indices || g[r][c] == '0') return\n    g[r][c] = '0'\n    dfs(g,r+1,c); dfs(g,r-1,c); dfs(g,r,c+1); dfs(g,r,c-1)\n}`,
          "Python": `def dfs(r, c):\n    if r < 0 or r >= R or c < 0 or c >= C or grid[r][c] == '0': return\n    grid[r][c] = '0'\n    dfs(r+1,c); dfs(r-1,c); dfs(r,c+1); dfs(r,c-1)\n\ncount = 0\nfor r in range(R):\n    for c in range(C):\n        if grid[r][c] == '1': dfs(r,c); count += 1`
        }
      },
      {
        name: "Cycle Detection & Bipartite",
        recognition: "Is graph a DAG? Can we color with 2 colors? Course prerequisites.",
        mentalModel: "DFS: track recursion stack for directed. Track colors for bipartite.",
        pitfalls: "State: 0=unvisited, 1=in-stack, 2=done. Undirected: skip parent.",
        problems: [
          { num: "207", name: "Course Schedule", url: "https://leetcode.com/problems/course-schedule/" },
          { num: "785", name: "Is Graph Bipartite", url: "https://leetcode.com/problems/is-graph-bipartite/" }
        ],
        code: {
          "Java": `// Cycle detection (directed)\nint[] state = new int[n]; // 0,1,2\nboolean hasCycle(int node) {\n    if (state[node] == 1) return true;\n    if (state[node] == 2) return false;\n    state[node] = 1;\n    for (int nb : adj[node]) if (hasCycle(nb)) return true;\n    state[node] = 2;\n    return false;\n}`,
          "Kotlin": `val color = IntArray(n) { -1 }\nfun bfs(src: Int): Boolean {\n    val q = ArrayDeque<Int>()\n    q.addLast(src); color[src] = 0\n    while (q.isNotEmpty()) {\n        val u = q.removeFirst()\n        for (v in adj[u]) {\n            if (color[v] == -1) { color[v] = 1 - color[u]; q.addLast(v) }\n            else if (color[v] == color[u]) return false\n        }\n    }\n    return true\n}`,
          "Python": `state = [0] * n  # 0=unvis,1=in-stack,2=done\ndef has_cycle(node):\n    if state[node] == 1: return True\n    if state[node] == 2: return False\n    state[node] = 1\n    for nb in adj[node]:\n        if has_cycle(nb): return True\n    state[node] = 2\n    return False`
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
        name: "Kahn's Algorithm (BFS)",
        recognition: "Dependency ordering. Course schedule. Build order.",
        mentalModel: "In-degree array. Queue nodes with 0 in-degree. Process and reduce neighbors.",
        pitfalls: "If result length != n, there is a cycle.",
        problems: [
          { num: "207", name: "Course Schedule", url: "https://leetcode.com/problems/course-schedule/" },
          { num: "210", name: "Course Schedule II", url: "https://leetcode.com/problems/course-schedule-ii/" }
        ],
        code: {
          "Java": `int[] indeg = new int[n];\nfor (int[] e : edges) indeg[e[1]]++;\nQueue<Integer> q = new LinkedList<>();\nfor (int i = 0; i < n; i++) if (indeg[i] == 0) q.offer(i);\nList<Integer> order = new ArrayList<>();\nwhile (!q.isEmpty()) {\n    int u = q.poll(); order.add(u);\n    for (int v : adj[u]) if (--indeg[v] == 0) q.offer(v);\n}\nreturn order.size() == n; // false = cycle`,
          "Kotlin": `val indeg = IntArray(n)\nfor ((u,v) in edges) indeg[v]++\nval q = ArrayDeque<Int>()\nfor (i in 0 until n) if (indeg[i] == 0) q.addLast(i)\nval order = mutableListOf<Int>()\nwhile (q.isNotEmpty()) {\n    val u = q.removeFirst(); order.add(u)\n    for (v in adj[u]) if (--indeg[v] == 0) q.addLast(v)\n}\nreturn order.size == n`,
          "Python": `from collections import deque\nindeg = [0] * n\nfor u, v in edges: indeg[v] += 1\nq = deque(i for i in range(n) if indeg[i] == 0)\norder = []\nwhile q:\n    u = q.popleft(); order.append(u)\n    for v in adj[u]:\n        indeg[v] -= 1\n        if indeg[v] == 0: q.append(v)\nreturn len(order) == n  # False = cycle`
        }
      },
      {
        name: "DFS Topological Sort",
        recognition: "Same as Kahn's but recursive DFS based.",
        mentalModel: "Post-order DFS: after visiting all descendants, push node to stack. Reverse stack = topo order.",
        pitfalls: "Works only on DAG. Reverse final list.",
        problems: [
          { num: "210", name: "Course Schedule II", url: "https://leetcode.com/problems/course-schedule-ii/" }
        ],
        code: {
          "Java": `boolean[] vis = new boolean[n];\nDeque<Integer> stack = new ArrayDeque<>();\nvoid dfs(int u) {\n    vis[u] = true;\n    for (int v : adj[u]) if (!vis[v]) dfs(v);\n    stack.push(u);\n}`,
          "Kotlin": `val vis = BooleanArray(n)\nval stack = ArrayDeque<Int>()\nfun dfs(u: Int) {\n    vis[u] = true\n    for (v in adj[u]) if (!vis[v]) dfs(v)\n    stack.addFirst(u)\n}`,
          "Python": `vis = [False] * n\nstack = []\ndef dfs(u):\n    vis[u] = True\n    for v in adj[u]:\n        if not vis[v]: dfs(v)\n    stack.append(u)\nfor i in range(n):\n    if not vis[i]: dfs(i)\nreturn stack[::-1]  # reverse`
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
        name: "Path Compression & Union by Rank",
        recognition: "Connected components. Cycle in undirected graph. Kruskal MST.",
        mentalModel: "find() with path compression flattens tree. Union by rank keeps tree balanced.",
        pitfalls: "Initialize parent[i] = i. find() must be recursive for path compression.",
        problems: [
          { num: "684", name: "Redundant Connection", url: "https://leetcode.com/problems/redundant-connection/" },
          { num: "323", name: "Number of Connected Components", url: "https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/" }
        ],
        code: {
          "Java": `int[] parent = new int[n], rank = new int[n];\nfor (int i = 0; i < n; i++) parent[i] = i;\n\nint find(int x) {\n    if (parent[x] != x) parent[x] = find(parent[x]); // path compression\n    return parent[x];\n}\n\nboolean union(int a, int b) {\n    int ra = find(a), rb = find(b);\n    if (ra == rb) return false; // cycle!\n    if (rank[ra] < rank[rb]) parent[ra] = rb;\n    else if (rank[ra] > rank[rb]) parent[rb] = ra;\n    else { parent[rb] = ra; rank[ra]++; }\n    return true;\n}`,
          "Kotlin": `val parent = IntArray(n) { it }\nval rank = IntArray(n)\n\nfun find(x: Int): Int {\n    if (parent[x] != x) parent[x] = find(parent[x])\n    return parent[x]\n}\n\nfun union(a: Int, b: Int): Boolean {\n    val ra = find(a); val rb = find(b)\n    if (ra == rb) return false\n    if (rank[ra] < rank[rb]) parent[ra] = rb\n    else if (rank[ra] > rank[rb]) parent[rb] = ra\n    else { parent[rb] = ra; rank[ra]++ }\n    return true\n}`,
          "Python": `parent = list(range(n))\nrank = [0] * n\n\ndef find(x):\n    if parent[x] != x:\n        parent[x] = find(parent[x])  # path compression\n    return parent[x]\n\ndef union(a, b):\n    ra, rb = find(a), find(b)\n    if ra == rb: return False  # cycle!\n    if rank[ra] < rank[rb]: parent[ra] = rb\n    elif rank[ra] > rank[rb]: parent[rb] = ra\n    else: parent[rb] = ra; rank[ra] += 1\n    return True`
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
        recognition: "Prefix matching, word dictionary, autocomplete.",
        mentalModel: "Each node has 26 children + isWord flag. Walk per character.",
        pitfalls: "Don't return true on startsWith if isWord not checked for search.",
        problems: [
          { num: "208", name: "Implement Trie", url: "https://leetcode.com/problems/implement-trie-prefix-tree/" },
          { num: "211", name: "Design Add & Search Words", url: "https://leetcode.com/problems/design-add-and-search-words-data-structure/" }
        ],
        code: {
          "Java": `class TrieNode {\n    TrieNode[] children = new TrieNode[26];\n    boolean isWord;\n}\nvoid insert(String w) {\n    TrieNode cur = root;\n    for (char c : w.toCharArray()) {\n        int i = c - 'a';\n        if (cur.children[i] == null) cur.children[i] = new TrieNode();\n        cur = cur.children[i];\n    }\n    cur.isWord = true;\n}\nboolean search(String w) {\n    TrieNode cur = root;\n    for (char c : w.toCharArray()) {\n        int i = c - 'a';\n        if (cur.children[i] == null) return false;\n        cur = cur.children[i];\n    }\n    return cur.isWord; // startsWith: return true\n}`,
          "Kotlin": `class TrieNode { val children = arrayOfNulls<TrieNode>(26); var isWord = false }\nfun insert(w: String) {\n    var cur = root\n    for (c in w) {\n        val i = c - 'a'\n        if (cur.children[i] == null) cur.children[i] = TrieNode()\n        cur = cur.children[i]!!\n    }\n    cur.isWord = true\n}`,
          "Python": `class TrieNode:\n    def __init__(self):\n        self.children = {}\n        self.is_word = False\n\ndef insert(word):\n    cur = root\n    for c in word:\n        if c not in cur.children:\n            cur.children[c] = TrieNode()\n        cur = cur.children[c]\n    cur.is_word = True\n\ndef search(word):\n    cur = root\n    for c in word:\n        if c not in cur.children: return False\n        cur = cur.children[c]\n    return cur.is_word`
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
        name: "1D DP (Fibonacci, Stairs, House Robber)",
        recognition: "Count ways, optimize next state from previous states.",
        mentalModel: "dp[i] depends on dp[i-1] or dp[i-2]. Space optimize to 2 vars.",
        pitfalls: "Base cases. House Robber: start from 3rd element.",
        problems: [
          { num: "70", name: "Climbing Stairs", url: "https://leetcode.com/problems/climbing-stairs/" },
          { num: "198", name: "House Robber", url: "https://leetcode.com/problems/house-robber/" },
          { num: "213", name: "House Robber II", url: "https://leetcode.com/problems/house-robber-ii/" }
        ],
        code: {
          "Java": `// Climbing Stairs\nint a = 1, b = 1;\nfor (int i = 2; i <= n; i++) { int c = a + b; a = b; b = c; }\nreturn b;\n\n// House Robber\nint inc = 0, exc = 0;\nfor (int x : nums) {\n    int tmp = inc;\n    inc = exc + x;\n    exc = Math.max(tmp, exc);\n}\nreturn Math.max(inc, exc);`,
          "Kotlin": `// Climbing Stairs\nvar a = 1; var b = 1\nfor (i in 2..n) { val c = a + b; a = b; b = c }\nreturn b\n\n// House Robber\nvar inc = 0; var exc = 0\nfor (x in nums) {\n    val tmp = inc; inc = exc + x; exc = maxOf(tmp, exc)\n}\nreturn maxOf(inc, exc)`,
          "Python": `# Climbing Stairs\na = b = 1\nfor _ in range(2, n + 1):\n    a, b = b, a + b\nreturn b\n\n# House Robber\ninc = exc = 0\nfor x in nums:\n    inc, exc = exc + x, max(inc, exc)\nreturn max(inc, exc)`
        }
      },
      {
        name: "2D DP (Grid Paths, Unique Paths)",
        recognition: "Grid traversal counting paths. Min cost path.",
        mentalModel: "dp[i][j] = dp[i-1][j] + dp[i][j-1]. Initialize edges to 1.",
        pitfalls: "Initialize first row and column. Obstacles set dp to 0.",
        problems: [
          { num: "62", name: "Unique Paths", url: "https://leetcode.com/problems/unique-paths/" },
          { num: "64", name: "Minimum Path Sum", url: "https://leetcode.com/problems/minimum-path-sum/" }
        ],
        code: {
          "Java": `int[][] dp = new int[m][n];\nfor (int i = 0; i < m; i++) dp[i][0] = 1;\nfor (int j = 0; j < n; j++) dp[0][j] = 1;\nfor (int i = 1; i < m; i++)\n    for (int j = 1; j < n; j++)\n        dp[i][j] = dp[i-1][j] + dp[i][j-1];\nreturn dp[m-1][n-1];`,
          "Kotlin": `val dp = Array(m) { IntArray(n) { 1 } }\nfor (i in 1 until m)\n    for (j in 1 until n)\n        dp[i][j] = dp[i-1][j] + dp[i][j-1]\nreturn dp[m-1][n-1]`,
          "Python": `dp = [[1]*n for _ in range(m)]\nfor i in range(1, m):\n    for j in range(1, n):\n        dp[i][j] = dp[i-1][j] + dp[i][j-1]\nreturn dp[m-1][n-1]`
        }
      },
      {
        name: "Knapsack & Coin Change",
        recognition: "Select items with constraints (weight/value). Count/min ways to make sum.",
        mentalModel: "0/1 Knapsack: iterate j backwards. Unbounded: forwards.",
        pitfalls: "Iterate weights in reverse for 0/1. Initialize dp[0]=0, rest=INF.",
        problems: [
          { num: "322", name: "Coin Change", url: "https://leetcode.com/problems/coin-change/" },
          { num: "416", name: "Partition Equal Subset", url: "https://leetcode.com/problems/partition-equal-subset-sum/" }
        ],
        code: {
          "Java": `// Coin Change (unbounded)\nint[] dp = new int[sum + 1];\nArrays.fill(dp, Integer.MAX_VALUE); dp[0] = 0;\nfor (int c : coins)\n    for (int i = c; i <= sum; i++)\n        if (dp[i-c] != Integer.MAX_VALUE)\n            dp[i] = Math.min(dp[i], 1 + dp[i-c]);\n\n// 0/1 Knapsack\nboolean[] dp = new boolean[sum + 1]; dp[0] = true;\nfor (int x : nums)\n    for (int j = sum; j >= x; j--) // REVERSE!\n        dp[j] |= dp[j - x];`,
          "Kotlin": `val dp = IntArray(sum + 1) { Int.MAX_VALUE }.also { it[0] = 0 }\nfor (c in coins)\n    for (i in c..sum)\n        if (dp[i-c] != Int.MAX_VALUE)\n            dp[i] = minOf(dp[i], 1 + dp[i-c])`,
          "Python": `# Coin Change\ndp = [float('inf')] * (sum + 1)\ndp[0] = 0\nfor c in coins:\n    for i in range(c, sum + 1):\n        dp[i] = min(dp[i], 1 + dp[i - c])\n\n# 0/1 Knapsack\ndp = [False] * (sum + 1); dp[0] = True\nfor x in nums:\n    for j in range(sum, x-1, -1):  # REVERSE!\n        dp[j] |= dp[j - x]`
        }
      },
      {
        name: "LCS, LIS, Edit Distance",
        recognition: "String comparison, subsequence, edit operations, palindrome.",
        mentalModel: "LCS: match = 1+diagonal, else max(up,left). LIS: O(N logN) with BS.",
        pitfalls: "LCS: 1-indexed dp means dp[0][*] = dp[*][0] = 0 as base.",
        problems: [
          { num: "1143", name: "Longest Common Subsequence", url: "https://leetcode.com/problems/longest-common-subsequence/" },
          { num: "300", name: "Longest Increasing Subsequence", url: "https://leetcode.com/problems/longest-increasing-subsequence/" },
          { num: "72", name: "Edit Distance", url: "https://leetcode.com/problems/edit-distance/" }
        ],
        code: {
          "Java": `// LCS\nint[][] dp = new int[m+1][n+1];\nfor (int i=1;i<=m;i++) for (int j=1;j<=n;j++)\n    dp[i][j] = (s1.charAt(i-1)==s2.charAt(j-1)) ? dp[i-1][j-1]+1 : Math.max(dp[i-1][j],dp[i][j-1]);\n\n// LIS O(N log N)\nList<Integer> tails = new ArrayList<>();\nfor (int x : nums) {\n    int pos = Collections.binarySearch(tails, x);\n    if (pos < 0) pos = -(pos + 1);\n    if (pos == tails.size()) tails.add(x); else tails.set(pos, x);\n}`,
          "Kotlin": `// LCS\nval dp = Array(m+1) { IntArray(n+1) }\nfor (i in 1..m) for (j in 1..n)\n    dp[i][j] = if (s1[i-1]==s2[j-1]) dp[i-1][j-1]+1 else maxOf(dp[i-1][j],dp[i][j-1])`,
          "Python": `# LCS\ndp = [[0]*(n+1) for _ in range(m+1)]\nfor i in range(1,m+1):\n    for j in range(1,n+1):\n        if s1[i-1]==s2[j-1]: dp[i][j]=dp[i-1][j-1]+1\n        else: dp[i][j]=max(dp[i-1][j],dp[i][j-1])\n\n# LIS O(N log N)\nimport bisect\ntails = []\nfor x in nums:\n    pos = bisect.bisect_left(tails, x)\n    if pos == len(tails): tails.append(x)\n    else: tails[pos] = x`
        }
      }
    ]
  },

  // ─── 17. INTERVALS ────────────────────────────────────────────────────────
  {
    title: "Intervals & Greedy",
    color: "#7a5a2e",
    patterns: [
      {
        name: "Merge & Insert Intervals",
        recognition: "Overlapping ranges, merge, insert, schedule.",
        mentalModel: "Sort by start. Merge if next.start <= last.end. Update end = max(both).",
        pitfalls: "Sort first. New interval insertion: handle 3 zones (before, overlap, after).",
        problems: [
          { num: "56", name: "Merge Intervals", url: "https://leetcode.com/problems/merge-intervals/" },
          { num: "57", name: "Insert Interval", url: "https://leetcode.com/problems/insert-interval/" },
          { num: "253", name: "Meeting Rooms II", url: "https://leetcode.com/problems/meeting-rooms-ii/" }
        ],
        code: {
          "Java": `Arrays.sort(intervals, (a, b) -> a[0] - b[0]);\nList<int[]> res = new ArrayList<>();\nfor (int[] i : intervals) {\n    if (res.isEmpty() || res.get(res.size()-1)[1] < i[0])\n        res.add(i);\n    else\n        res.get(res.size()-1)[1] = Math.max(res.get(res.size()-1)[1], i[1]);\n}\n// Meeting rooms: min-heap of end times\nPriorityQueue<Integer> pq = new PriorityQueue<>();\nfor (int[] i : sorted) {\n    if (!pq.isEmpty() && pq.peek() <= i[0]) pq.poll();\n    pq.offer(i[1]);\n}`,
          "Kotlin": `intervals.sortBy { it[0] }\nval res = mutableListOf<IntArray>()\nfor (i in intervals) {\n    if (res.isEmpty() || res.last()[1] < i[0]) res.add(i)\n    else res.last()[1] = maxOf(res.last()[1], i[1])\n}`,
          "Python": `intervals.sort(key=lambda x: x[0])\nres = []\nfor i in intervals:\n    if not res or res[-1][1] < i[0]: res.append(i)\n    else: res[-1][1] = max(res[-1][1], i[1])`
        }
      },
      {
        name: "Greedy (Jump Game, Gas Station)",
        recognition: "Local optimal leads to global optimal. Sorting by end time.",
        mentalModel: "Jump Game: track max reach. Gas Station: total >= 0 means solution exists.",
        pitfalls: "Jump Game II: update next_reach greedily. Gas: find start where local sum >= 0.",
        problems: [
          { num: "55", name: "Jump Game", url: "https://leetcode.com/problems/jump-game/" },
          { num: "45", name: "Jump Game II", url: "https://leetcode.com/problems/jump-game-ii/" },
          { num: "134", name: "Gas Station", url: "https://leetcode.com/problems/gas-station/" }
        ],
        code: {
          "Java": `// Jump Game\nint reach = 0;\nfor (int i = 0; i <= reach && i < n; i++)\n    reach = Math.max(reach, i + nums[i]);\nreturn reach >= n - 1;\n\n// Gas Station\nint total = 0, cur = 0, start = 0;\nfor (int i = 0; i < n; i++) {\n    total += gas[i] - cost[i];\n    cur += gas[i] - cost[i];\n    if (cur < 0) { start = i + 1; cur = 0; }\n}\nreturn total >= 0 ? start : -1;`,
          "Kotlin": `var reach = 0\nfor (i in 0..minOf(reach, n-1))\n    reach = maxOf(reach, i + nums[i])\nreturn reach >= n - 1`,
          "Python": `# Jump Game\nreach = 0\nfor i in range(n):\n    if i > reach: break\n    reach = max(reach, i + nums[i])\nreturn reach >= n - 1\n\n# Gas Station\ntotal = cur = start = 0\nfor i in range(n):\n    total += gas[i] - cost[i]\n    cur += gas[i] - cost[i]\n    if cur < 0: start = i + 1; cur = 0\nreturn start if total >= 0 else -1`
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
        name: "XOR, Missing Number, Single Number",
        recognition: "Find unique element, missing number, pairs.",
        mentalModel: "x ^ x = 0, x ^ 0 = x. XOR all elements: pairs cancel out.",
        pitfalls: "XOR is commutative and associative. Integer overflow on sum trick.",
        problems: [
          { num: "136", name: "Single Number", url: "https://leetcode.com/problems/single-number/" },
          { num: "268", name: "Missing Number", url: "https://leetcode.com/problems/missing-number/" }
        ],
        code: {
          "Java": `// Single Number\nint res = 0;\nfor (int x : arr) res ^= x;\nreturn res;\n\n// Missing Number\nint res = nums.length;\nfor (int i = 0; i < nums.length; i++) res ^= i ^ nums[i];\nreturn res;`,
          "Kotlin": `val res = arr.fold(0) { acc, x -> acc xor x }`,
          "Python": `# Single Number\nfrom functools import reduce\nimport operator\nreturn reduce(operator.xor, arr)\n\n# Missing Number\nreturn (n*(n+1)//2) - sum(nums)`
        }
      },
      {
        name: "Bitmask, Set/Toggle/Count Bits",
        recognition: "State compression, subsets, power of two.",
        mentalModel: "1 << i sets bit i. n & (n-1) removes lowest bit. n & (-n) isolates lowest bit.",
        pitfalls: "Operator precedence: (a & b) == 0 not a & b == 0.",
        problems: [
          { num: "338", name: "Counting Bits", url: "https://leetcode.com/problems/counting-bits/" },
          { num: "191", name: "Number of 1 Bits", url: "https://leetcode.com/problems/number-of-1-bits/" },
          { num: "78", name: "Subsets via Bitmask", url: "https://leetcode.com/problems/subsets/" }
        ],
        code: {
          "Java": `// Bit tricks cheatsheet\nint setBit   = n | (1 << i);   // set bit i\nint clearBit = n & ~(1 << i);  // clear bit i\nint toggleBit= n ^ (1 << i);   // toggle bit i\nboolean isSet = (n & (1 << i)) != 0;\nboolean isPow2 = n > 0 && (n & (n-1)) == 0;\nint lowest = n & (-n);          // isolate lowest set bit\nint count = Integer.bitCount(n);\n\n// Subsets via bitmask\nfor (int mask = 0; mask < (1 << n); mask++) {\n    List<Integer> sub = new ArrayList<>();\n    for (int i = 0; i < n; i++)\n        if ((mask & (1 << i)) != 0) sub.add(nums[i]);\n}`,
          "Kotlin": `// Counting bits dp\nval dp = IntArray(n+1)\nfor (i in 1..n) dp[i] = dp[i shr 1] + (i and 1)`,
          "Python": `# Bit tricks\nn | (1 << i)     # set bit i\nn & ~(1 << i)    # clear bit i\nn ^ (1 << i)     # toggle bit i\n(n >> i) & 1     # check bit i\nn & (n - 1)      # remove lowest set bit\nn & (-n)         # isolate lowest set bit\nbin(n).count('1')  # popcount\n\n# Subsets\nfor mask in range(1 << n):\n    sub = [nums[i] for i in range(n) if mask & (1 << i)]`
        }
      }
    ]
  },

  // ─── 19. ADVANCED (Google/Meta L5+) ─────────────────────────────────────
  {
    title: "Advanced (L5+ / Staff)",
    color: "#6a1f5a",
    patterns: [
      {
        name: "Dijkstra's Algorithm",
        recognition: "Shortest path in weighted graph (non-negative weights).",
        mentalModel: "Min-heap (dist, node). Relax edges of popped node. Skip if already better dist found.",
        pitfalls: "Does NOT work with negative weights. Stale entries in heap.",
        problems: [
          { num: "743", name: "Network Delay Time", url: "https://leetcode.com/problems/network-delay-time/" },
          { num: "787", name: "Cheapest Flights Within K Stops", url: "https://leetcode.com/problems/cheapest-flights-within-k-stops/" }
        ],
        code: {
          "Java": `int[] dist = new int[n]; Arrays.fill(dist, Integer.MAX_VALUE); dist[src] = 0;\nPriorityQueue<int[]> pq = new PriorityQueue<>((a,b)->a[0]-b[0]);\npq.offer(new int[]{0, src});\nwhile (!pq.isEmpty()) {\n    int[] cur = pq.poll(); int d = cur[0], u = cur[1];\n    if (d > dist[u]) continue; // stale\n    for (int[] e : adj[u]) {\n        int v = e[0], w = e[1];\n        if (dist[u] + w < dist[v]) {\n            dist[v] = dist[u] + w;\n            pq.offer(new int[]{dist[v], v});\n        }\n    }\n}`,
          "Kotlin": `val dist = IntArray(n) { Int.MAX_VALUE }.also { it[src] = 0 }\nval pq = PriorityQueue<IntArray>(compareBy { it[0] })\npq.offer(intArrayOf(0, src))\nwhile (pq.isNotEmpty()) {\n    val (d, u) = pq.poll()\n    if (d > dist[u]) continue\n    for ((v, w) in adj[u])\n        if (dist[u] + w < dist[v]) {\n            dist[v] = dist[u] + w\n            pq.offer(intArrayOf(dist[v], v))\n        }\n}`,
          "Python": `import heapq\ndist = [float('inf')] * n; dist[src] = 0\npq = [(0, src)]\nwhile pq:\n    d, u = heapq.heappop(pq)\n    if d > dist[u]: continue\n    for v, w in adj[u]:\n        if dist[u] + w < dist[v]:\n            dist[v] = dist[u] + w\n            heapq.heappush(pq, (dist[v], v))`
        }
      },
      {
        name: "KMP Pattern Matching",
        recognition: "Find pattern in text. Multiple occurrences. O(N+M).",
        mentalModel: "Build failure function (LPS array). On mismatch, jump using LPS.",
        pitfalls: "LPS array is off by one. j resets to lps[j-1] not 0.",
        problems: [
          { num: "28", name: "Find Index of First Occurrence", url: "https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/" }
        ],
        code: {
          "Java": `int[] lps = new int[pat.length];\nfor (int i=1, j=0; i<pat.length;) {\n    if (pat[i]==pat[j]) { lps[i++]=++j; }\n    else if (j>0) j=lps[j-1];\n    else lps[i++]=0;\n}\n// Search\nfor (int i=0,j=0; i<text.length;) {\n    if (text[i]==pat[j]) { i++; j++; }\n    if (j==pat.length) { /* found at i-j */ j=lps[j-1]; }\n    else if (i<text.length && text[i]!=pat[j]) {\n        if (j>0) j=lps[j-1]; else i++;\n    }\n}`,
          "Kotlin": `fun buildLPS(pat: String): IntArray {\n    val lps = IntArray(pat.length)\n    var j = 0; var i = 1\n    while (i < pat.length) {\n        if (pat[i] == pat[j]) { lps[i++] = ++j }\n        else if (j > 0) j = lps[j-1] else lps[i++] = 0\n    }\n    return lps\n}`,
          "Python": `def build_lps(pat):\n    lps = [0] * len(pat)\n    j = 0; i = 1\n    while i < len(pat):\n        if pat[i] == pat[j]: lps[i] = j + 1; i += 1; j += 1\n        elif j > 0: j = lps[j-1]\n        else: i += 1\n    return lps`
        }
      }
    ]
  }

];

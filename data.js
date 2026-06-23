const dsaData = [
  {
    title: "Arrays & Strings",
    color: "#b5563c",
    patterns: [
      {
        name: "Prefix Sum & Difference Array",
        recognition: "Range sum queries, contiguous subarrays, range updates.",
        mentalModel: "Precompute cumulative sum array to query O(1). Or add val at start and subtract at end+1 for range updates.",
        pitfalls: "Off-by-one errors with 1-based indexing.",
        problems: [
          { num: "303", name: "Range Sum Query", url: "https://leetcode.com/problems/range-sum-query-immutable/" },
          { num: "560", name: "Subarray Sum Equals K", url: "https://leetcode.com/problems/subarray-sum-equals-k/" }
        ],
        code: {
          "Java": `int[] pre = new int[n + 1];\nfor(int i = 0; i < n; i++) {\n    pre[i + 1] = pre[i] + arr[i];\n}\n\n// Difference Array (update L to R with X)\ndiff[L] += X;\ndiff[R + 1] -= X;`,
          "Kotlin": `val pre = IntArray(n + 1)\nfor (i in 0 until n) {\n    pre[i + 1] = pre[i] + arr[i]\n}`,
          "Python": `pre = [0] * (n + 1)\nfor i in range(n):\n    pre[i + 1] = pre[i] + arr[i]`
        }
      },
      {
        name: "Kadane's Algorithm",
        recognition: "Maximum subarray sum.",
        mentalModel: "Local max is either current element or current + prev max.",
        problems: [
          { num: "53", name: "Maximum Subarray", url: "https://leetcode.com/problems/maximum-subarray/" }
        ],
        code: {
          "Java": `int maxEnd = arr[0], maxSoFar = arr[0];\nfor(int i = 1; i < n; i++) {\n    maxEnd = Math.max(arr[i], maxEnd + arr[i]);\n    maxSoFar = Math.max(maxSoFar, maxEnd);\n}`,
          "Kotlin": `var maxEnd = arr[0]\nvar maxSoFar = arr[0]\nfor (i in 1 until n) {\n    maxEnd = maxOf(arr[i], maxEnd + arr[i])\n    maxSoFar = maxOf(maxSoFar, maxEnd)\n}`,
          "Python": `max_end = max_so_far = arr[0]\nfor x in arr[1:]:\n    max_end = max(x, max_end + x)\n    max_so_far = max(max_so_far, max_end)`
        }
      },
      {
        name: "Intervals & Sorting",
        recognition: "Overlapping intervals, scheduling, merge ranges.",
        mentalModel: "Sort by start time, merge if next start <= current end.",
        problems: [
          { num: "56", name: "Merge Intervals", url: "https://leetcode.com/problems/merge-intervals/" },
          { num: "57", name: "Insert Interval", url: "https://leetcode.com/problems/insert-interval/" }
        ],
        code: {
          "Java": `Arrays.sort(intervals, (a, b) -> a[0] - b[0]);\nList<int[]> res = new ArrayList<>();\nfor(int[] i : intervals) {\n    if(res.isEmpty() || res.get(res.size()-1)[1] < i[0]) res.add(i);\n    else res.get(res.size()-1)[1] = Math.max(res.get(res.size()-1)[1], i[1]);\n}`,
          "Kotlin": `intervals.sortBy { it[0] }\nval res = mutableListOf<IntArray>()\nfor (i in intervals) {\n    if (res.isEmpty() || res.last()[1] < i[0]) res.add(i)\n    else res.last()[1] = maxOf(res.last()[1], i[1])\n}`,
          "Python": `intervals.sort(key=lambda x: x[0])\nres = []\nfor i in intervals:\n    if not res or res[-1][1] < i[0]: res.append(i)\n    else: res[-1][1] = max(res[-1][1], i[1])`
        }
      }
    ]
  },
  {
    title: "Pointers & Windows",
    color: "#1f3a5f",
    patterns: [
      {
        name: "Two Pointers (Opposite)",
        recognition: "Sorted array, finding pairs, checking palindromes.",
        mentalModel: "One pointer at start, one at end. Move based on conditions.",
        problems: [
          { num: "167", name: "Two Sum II", url: "https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/" },
          { num: "11", name: "Container With Most Water", url: "https://leetcode.com/problems/container-with-most-water/" }
        ],
        code: {
          "Java": `int l = 0, r = n - 1;\nwhile(l < r) {\n    int sum = arr[l] + arr[r];\n    if(sum == target) return new int[]{l, r};\n    if(sum < target) l++;\n    else r--;\n}`,
          "Kotlin": `var l = 0\nvar r = arr.size - 1\nwhile (l < r) {\n    val sum = arr[l] + arr[r]\n    if (sum == target) return intArrayOf(l, r)\n    if (sum < target) l++ else r--\n}`,
          "Python": `l, r = 0, len(arr) - 1\nwhile l < r:\n    curr = arr[l] + arr[r]\n    if curr == target: return [l, r]\n    if curr < target: l += 1\n    else: r -= 1`
        }
      },
      {
        name: "Variable Sliding Window",
        recognition: "Longest/Shortest subarray satisfying a condition.",
        mentalModel: "Expand right until invalid, shrink left until valid.",
        problems: [
          { num: "3", name: "Longest Substring Without Repeats", url: "https://leetcode.com/problems/longest-substring-without-repeating-characters/" },
          { num: "76", name: "Minimum Window Substring", url: "https://leetcode.com/problems/minimum-window-substring/" }
        ],
        code: {
          "Java": `int l = 0, maxLen = 0;\nfor(int r = 0; r < n; r++) {\n    // Add arr[r] state\n    while(!isValid()) {\n        // Remove arr[l] state\n        l++;\n    }\n    maxLen = Math.max(maxLen, r - l + 1);\n}`,
          "Kotlin": `var l = 0\nvar maxLen = 0\nfor (r in 0 until n) {\n    // Add arr[r] state\n    while (!isValid()) {\n        // Remove arr[l] state\n        l++\n    }\n    maxLen = maxOf(maxLen, r - l + 1)\n}`,
          "Python": `l = max_len = 0\nfor r in range(len(arr)):\n    # add arr[r] to state\n    while not is_valid():\n        # remove arr[l] from state\n        l += 1\n    max_len = max(max_len, r - l + 1)`
        }
      }
    ]
  },
  {
    title: "Stacks, Queues & Sets",
    color: "#4f7a4a",
    patterns: [
      {
        name: "Monotonic Stack",
        recognition: "Find next greater or next smaller element.",
        mentalModel: "Keep elements in stack strictly increasing/decreasing. Pop smaller elements out.",
        problems: [
          { num: "739", name: "Daily Temperatures", url: "https://leetcode.com/problems/daily-temperatures/" },
          { num: "84", name: "Largest Rectangle in Histogram", url: "https://leetcode.com/problems/largest-rectangle-in-histogram/" }
        ],
        code: {
          "Java": `Stack<Integer> st = new Stack<>();\nfor(int i=0; i<n; i++) {\n    while(!st.isEmpty() && arr[st.peek()] < arr[i]) {\n        res[st.pop()] = arr[i];\n    }\n    st.push(i);\n}`,
          "Kotlin": `val st = ArrayDeque<Int>()\nfor(i in 0 until n) {\n    while(st.isNotEmpty() && arr[st.last()] < arr[i]) {\n        res[st.removeLast()] = arr[i]\n    }\n    st.addLast(i)\n}`,
          "Python": `st = []\nfor i in range(len(arr)):\n    while st and arr[st[-1]] < arr[i]:\n        res[st.pop()] = arr[i]\n    st.append(i)`
        }
      },
      {
        name: "Queue & Monotonic Deque",
        recognition: "Sliding window maximum, processing in order (FIFO).",
        mentalModel: "Deque stores indices. Pop out-of-window front, pop smaller from back.",
        problems: [
          { num: "239", name: "Sliding Window Maximum", url: "https://leetcode.com/problems/sliding-window-maximum/" }
        ],
        code: {
          "Java": `Deque<Integer> dq = new ArrayDeque<>();\nfor(int i=0; i<n; i++) {\n    if(!dq.isEmpty() && dq.peekFirst() == i-k) dq.pollFirst();\n    while(!dq.isEmpty() && arr[dq.peekLast()] < arr[i]) dq.pollLast();\n    dq.offerLast(i);\n    if(i >= k-1) res.add(arr[dq.peekFirst()]);\n}`,
          "Kotlin": `val dq = ArrayDeque<Int>()\nfor(i in 0 until n) {\n    if(dq.isNotEmpty() && dq.first() == i-k) dq.removeFirst()\n    while(dq.isNotEmpty() && arr[dq.last()] < arr[i]) dq.removeLast()\n    dq.addLast(i)\n    if(i >= k-1) res.add(arr[dq.first()])\n}`,
          "Python": `dq = deque()\nfor i in range(len(arr)):\n    if dq and dq[0] == i - k: dq.popleft()\n    while dq and arr[dq[-1]] < arr[i]: dq.pop()\n    dq.append(i)\n    if i >= k - 1: res.append(arr[dq[0]])`
        }
      }
    ]
  },
  {
    title: "Trees & Traversals",
    color: "#6b4f8a",
    patterns: [
      {
        name: "DFS Traversals (Pre/In/Post)",
        recognition: "Exploring all paths, checking tree structure, BST sorting.",
        mentalModel: "Pre = Root-L-R, In = L-Root-R, Post = L-R-Root.",
        problems: [
          { num: "230", name: "Kth Smallest Element in BST", url: "https://leetcode.com/problems/kth-smallest-element-in-a-bst/" },
          { num: "236", name: "Lowest Common Ancestor", url: "https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/" }
        ],
        code: {
          "Java": `void dfs(Node root) {\n    if(root == null) return;\n    // pre-order\n    dfs(root.left);\n    // in-order\n    dfs(root.right);\n    // post-order\n}`,
          "Kotlin": `fun dfs(root: Node?) {\n    if (root == null) return\n    // pre-order\n    dfs(root.left)\n    // in-order\n    dfs(root.right)\n    // post-order\n}`,
          "Python": `def dfs(root):\n    if not root: return\n    # pre-order\n    dfs(root.left)\n    # in-order\n    dfs(root.right)\n    # post-order`
        }
      },
      {
        name: "BFS (Level Order)",
        recognition: "Shortest path in unweighted graphs or level-order tree traversal.",
        mentalModel: "Use a Queue. Process level by level using size loop.",
        problems: [
          { num: "102", name: "Level Order Traversal", url: "https://leetcode.com/problems/binary-tree-level-order-traversal/" }
        ],
        code: {
          "Java": `Queue<Node> q = new LinkedList<>();\nq.offer(root);\nwhile(!q.isEmpty()) {\n    int size = q.size();\n    for(int i=0; i<size; i++) {\n        Node curr = q.poll();\n        if(curr.left != null) q.offer(curr.left);\n        if(curr.right != null) q.offer(curr.right);\n    }\n}`,
          "Kotlin": `val q = ArrayDeque<Node>()\nq.addLast(root)\nwhile(q.isNotEmpty()) {\n    val size = q.size\n    for(i in 0 until size) {\n        val curr = q.removeFirst()\n        curr.left?.let { q.addLast(it) }\n        curr.right?.let { q.addLast(it) }\n    }\n}`,
          "Python": `q = deque([root])\nwhile q:\n    for _ in range(len(q)):\n        curr = q.popleft()\n        if curr.left: q.append(curr.left)\n        if curr.right: q.append(curr.right)`
        }
      }
    ]
  },
  {
    title: "Advanced DSA (Heaps, Graphs, DP)",
    color: "#1f7a72",
    patterns: [
      {
        name: "Top K Pattern (Heap)",
        recognition: "Find K largest/smallest elements, K closest points.",
        mentalModel: "Use Min-Heap of size K for Largest. Max-Heap for Smallest.",
        problems: [
          { num: "215", name: "Kth Largest Element", url: "https://leetcode.com/problems/kth-largest-element-in-an-array/" },
          { num: "973", name: "K Closest Points", url: "https://leetcode.com/problems/k-closest-points-to-origin/" }
        ],
        code: {
          "Java": `PriorityQueue<Integer> pq = new PriorityQueue<>();\nfor(int x : arr) {\n    pq.offer(x);\n    if(pq.size() > k) pq.poll();\n}\nreturn pq.peek();`,
          "Kotlin": `val pq = PriorityQueue<Int>()\nfor(x in arr) {\n    pq.offer(x)\n    if(pq.size > k) pq.poll()\n}\nreturn pq.peek()`,
          "Python": `import heapq\npq = []\nfor x in arr:\n    heapq.heappush(pq, x)\n    if len(pq) > k: heapq.heappop(pq)\nreturn pq[0]`
        }
      },
      {
        name: "Graphs (Islands & Union Find)",
        recognition: "Grid connected components, cycle detection in undirected graphs.",
        mentalModel: "DFS 4-directions and mark water. Or use Disjoint Set with path compression.",
        problems: [
          { num: "200", name: "Number of Islands", url: "https://leetcode.com/problems/number-of-islands/" },
          { num: "684", name: "Redundant Connection", url: "https://leetcode.com/problems/redundant-connection/" }
        ],
        code: {
          "Java": `int find(int i) {\n    if(p[i] == i) return i;\n    return p[i] = find(p[i]);\n}\nvoid union(int i, int j) {\n    p[find(i)] = find(j);\n}`,
          "Kotlin": `fun find(i: Int): Int {\n    if (p[i] == i) return i\n    p[i] = find(p[i])\n    return p[i]\n}\nfun union(i: Int, j: Int) {\n    p[find(i)] = find(j)\n}`,
          "Python": `def find(i):\n    if p[i] == i: return i\n    p[i] = find(p[i])\n    return p[i]\n\ndef union(i, j):\n    p[find(i)] = find(j)`
        }
      },
      {
        name: "Dynamic Programming (Knapsack & 1D)",
        recognition: "Min/Max optimization, combinations, overlapping subproblems.",
        mentalModel: "Break into smaller states. 1D array or 2D matrix. dp[i] = dp[i-1] + ...",
        problems: [
          { num: "322", name: "Coin Change", url: "https://leetcode.com/problems/coin-change/" },
          { num: "1143", name: "Longest Common Subsequence", url: "https://leetcode.com/problems/longest-common-subsequence/" }
        ],
        code: {
          "Java": `// Coin Change 1D\nArrays.fill(dp, MAX);\ndp[0] = 0;\nfor(int c : coins) {\n    for(int i = c; i <= sum; i++) {\n        dp[i] = Math.min(dp[i], 1 + dp[i - c]);\n    }\n}`,
          "Kotlin": `val dp = IntArray(sum + 1) { MAX }\ndp[0] = 0\nfor (c in coins) {\n    for (i in c..sum) {\n        dp[i] = minOf(dp[i], 1 + dp[i - c])\n    }\n}`,
          "Python": `dp = [float('inf')] * (sum + 1)\ndp[0] = 0\nfor c in coins:\n    for i in range(c, sum + 1):\n        dp[i] = min(dp[i], 1 + dp[i - c])`
        }
      }
    ]
  }
];

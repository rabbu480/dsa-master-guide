const dsaData = [
  {
    title: "Arrays",
    color: "#b5563c",
    patterns: [
      {
        name: "Prefix Sum",
        recognition: "Range sum queries, contiguous subarrays.",
        mentalModel: "Precompute cumulative sum array to query O(1).",
        problems: [
          { name: "Range Sum Query", url: "https://leetcode.com/problems/range-sum-query-immutable/" }
        ],
        code: {
          "Java": `int[] pre = new int[n + 1];\nfor(int i = 0; i < n; i++) {\n    pre[i + 1] = pre[i] + arr[i];\n}`,
          "Kotlin": `val pre = IntArray(n + 1)\nfor (i in 0 until n) {\n    pre[i + 1] = pre[i] + arr[i]\n}`,
          "Python": `pre = [0] * (n + 1)\nfor i in range(n):\n    pre[i + 1] = pre[i] + arr[i]`
        }
      },
      {
        name: "Kadane's Algorithm",
        recognition: "Maximum subarray sum.",
        mentalModel: "Local max is either current element or current + prev max.",
        problems: [
          { name: "Maximum Subarray", url: "https://leetcode.com/problems/maximum-subarray/" }
        ],
        code: {
          "Java": `int maxEnd = arr[0], maxSoFar = arr[0];\nfor(int i = 1; i < n; i++) {\n    maxEnd = Math.max(arr[i], maxEnd + arr[i]);\n    maxSoFar = Math.max(maxSoFar, maxEnd);\n}`,
          "Kotlin": `var maxEnd = arr[0]\nvar maxSoFar = arr[0]\nfor (i in 1 until n) {\n    maxEnd = maxOf(arr[i], maxEnd + arr[i])\n    maxSoFar = maxOf(maxSoFar, maxEnd)\n}`,
          "Python": `max_end = max_so_far = arr[0]\nfor x in arr[1:]:\n    max_end = max(x, max_end + x)\n    max_so_far = max(max_so_far, max_end)`
        }
      }
    ]
  },
  {
    title: "Two Pointers",
    color: "#1f3a5f",
    patterns: [
      {
        name: "Opposite Direction",
        recognition: "Sorted array, finding pairs, checking palindromes.",
        mentalModel: "One pointer at start, one at end. Move based on conditions.",
        problems: [
          { name: "Two Sum II", url: "https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/" },
          { name: "Valid Palindrome", url: "https://leetcode.com/problems/valid-palindrome/" }
        ],
        code: {
          "Java": `int l = 0, r = n - 1;\nwhile(l < r) {\n    int sum = arr[l] + arr[r];\n    if(sum == target) return new int[]{l, r};\n    if(sum < target) l++;\n    else r--;\n}`,
          "Kotlin": `var l = 0\nvar r = arr.size - 1\nwhile (l < r) {\n    val sum = arr[l] + arr[r]\n    if (sum == target) return intArrayOf(l, r)\n    if (sum < target) l++ else r--\n}`,
          "Python": `l, r = 0, len(arr) - 1\nwhile l < r:\n    curr = arr[l] + arr[r]\n    if curr == target: return [l, r]\n    if curr < target: l += 1\n    else: r -= 1\nreturn []`
        }
      },
      {
        name: "Fast & Slow Pointer",
        recognition: "Linked list cycles, finding middle element.",
        mentalModel: "Fast pointer moves 2x speed, slow moves 1x.",
        problems: [
          { name: "Linked List Cycle", url: "https://leetcode.com/problems/linked-list-cycle/" }
        ],
        code: {
          "Java": `ListNode slow = head, fast = head;\nwhile(fast != null && fast.next != null) {\n    slow = slow.next;\n    fast = fast.next.next;\n    if(slow == fast) return true;\n}\nreturn false;`,
          "Kotlin": `var slow = head\nvar fast = head\nwhile (fast?.next != null) {\n    slow = slow?.next\n    fast = fast.next?.next\n    if (slow === fast) return true\n}\nreturn false`,
          "Python": `slow = fast = head\nwhile fast and fast.next:\n    slow = slow.next\n    fast = fast.next.next\n    if slow == fast:\n        return True\nreturn False`
        }
      }
    ]
  },
  {
    title: "Sliding Window",
    color: "#9c7a2e",
    patterns: [
      {
        name: "Variable Window",
        recognition: "Longest/Shortest subarray satisfying a condition.",
        mentalModel: "Expand right until invalid, shrink left until valid.",
        problems: [
          { name: "Longest Substring", url: "https://leetcode.com/problems/longest-substring-without-repeating-characters/" }
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
    title: "Stack & Queues",
    color: "#4f7a4a",
    patterns: [
      {
        name: "Monotonic Stack",
        recognition: "Find next greater or next smaller element.",
        mentalModel: "Keep elements in stack strictly increasing/decreasing.",
        problems: [
          { name: "Daily Temperatures", url: "https://leetcode.com/problems/daily-temperatures/" }
        ],
        code: {
          "Java": `Stack<Integer> st = new Stack<>();\nfor(int i=0; i<n; i++) {\n    while(!st.isEmpty() && arr[st.peek()] < arr[i]) {\n        res[st.pop()] = arr[i];\n    }\n    st.push(i);\n}`,
          "Kotlin": `val st = ArrayDeque<Int>()\nfor(i in 0 until n) {\n    while(st.isNotEmpty() && arr[st.last()] < arr[i]) {\n        res[st.removeLast()] = arr[i]\n    }\n    st.addLast(i)\n}`,
          "Python": `st = []\nfor i in range(len(arr)):\n    while st and arr[st[-1]] < arr[i]:\n        res[st.pop()] = arr[i]\n    st.append(i)`
        }
      }
    ]
  },
  {
    title: "Trees & Graphs",
    color: "#6b4f8a",
    patterns: [
      {
        name: "Breadth-First Search (BFS)",
        recognition: "Shortest path in unweighted graphs or level-order tree traversal.",
        mentalModel: "Use a Queue. Process level by level using size loop.",
        problems: [
          { name: "Level Order Traversal", url: "https://leetcode.com/problems/binary-tree-level-order-traversal/" }
        ],
        code: {
          "Java": `Queue<Node> q = new LinkedList<>();\nq.offer(root);\nwhile(!q.isEmpty()) {\n    int size = q.size();\n    for(int i=0; i<size; i++) {\n        Node curr = q.poll();\n        if(curr.left != null) q.offer(curr.left);\n        if(curr.right != null) q.offer(curr.right);\n    }\n}`,
          "Kotlin": `val q = ArrayDeque<Node>()\nq.addLast(root)\nwhile(q.isNotEmpty()) {\n    val size = q.size\n    for(i in 0 until size) {\n        val curr = q.removeFirst()\n        curr.left?.let { q.addLast(it) }\n        curr.right?.let { q.addLast(it) }\n    }\n}`,
          "Python": `q = deque([root])\nwhile q:\n    for _ in range(len(q)):\n        curr = q.popleft()\n        if curr.left: q.append(curr.left)\n        if curr.right: q.append(curr.right)`
        }
      }
    ]
  }
];

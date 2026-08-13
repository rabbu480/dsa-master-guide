# BOOK 1 — MASTER BLUEPRINT
## Java FAANG / Senior SWE DSA Handbook
### Source of Truth for All HTML Chapter Generation
### Version: 1.0 | Total Pages: 200 | Status: LOCKED

---

> **READ THIS FIRST**
> This is NOT the handbook.
> This is NOT HTML. This is NOT code.
> This is the architectural blueprint that governs every chapter, every page, every subtopic.
> No HTML generator may deviate from this document without updating it first.

---

# SECTION 1: COMPLETE HIERARCHICAL BLUEPRINT

```
Book 1 — Java DSA Handbook (200 pages)
│
├── Part 0: Orientation (3 pages)
│   ├── 0.1 How to Use This Book (1 page)
│   ├── 0.2 Teaching Philosophy + Frequency Legend (0.5 page)
│   ├── 0.3 Dependency Roadmap — Visual Tree (1 page)
│   └── 0.4 Fast-Track Revision Schedule (0.5 page)
│
├── Part 1: Foundations (10 pages)
│   ├── 1.1 Big-O Analysis (2 pages)
│   │   ├── Teaching Block: Recognition → Rules → Common Classes
│   │   ├── ASCII: Complexity growth curve
│   │   ├── Dry Run: Nested loop analysis
│   │   ├── Complexity Table: O(1) → O(n!) ranked
│   │   └── Revision Box
│   │
│   ├── 1.2 Time vs Space Tradeoffs (1 page)
│   │   ├── Teaching Block: When to trade space for time
│   │   ├── Pattern Comparison: Memoization vs Recomputation
│   │   └── Revision Box
│   │
│   ├── 1.3 Mathematics for DSA (3 pages)
│   │   ├── 1.3A GCD / LCM (0.75 page)
│   │   │   ├── Mental Model + ASCII trace
│   │   │   └── Interview Tip: When modular arithmetic + GCD together
│   │   ├── 1.3B Prime Numbers / Sieve of Eratosthenes (0.75 page)
│   │   │   ├── ASCII: Sieve grid visualization
│   │   │   └── AHA: Why Sieve is O(n log log n)
│   │   ├── 1.3C Modular Arithmetic (0.75 page)
│   │   │   ├── Rules: add/mul/pow under mod
│   │   │   └── Interview Tip: Large number problems always mod 10^9+7
│   │   └── 1.3D Combinatorics Basics (0.75 page)
│   │       ├── nCr, nPr, Pigeonhole
│   │       └── When interviewers expect it
│   │
│   ├── 1.4 Bit Manipulation (3 pages)
│   │   ├── 1.4A AND / OR / XOR / NOT / Shifts (1.5 pages)
│   │   │   ├── ASCII: Bit-level truth table
│   │   │   ├── Dry Run: XOR swap, single number isolation
│   │   │   └── Revision Box
│   │   └── 1.4B Bit Masking + Interview Tricks (1.5 pages)
│   │       ├── Trick Table: set/clear/flip/check a bit
│   │       ├── Patterns: Power of 2, Count set bits, Missing number
│   │       ├── Interview Tips: When to reach for XOR immediately
│   │       └── Revision Box
│   │
│   └── 1.5 Complexity Cheat Sheet (1 page)
│       └── Full Table: Data Structure × Operation × Time × Space
│
├── Part 2: Arrays, Strings & Searching (30 pages)
│   │
│   ├── 2.1 Arrays (5 pages)
│   │   ├── 2.1A Traversal Patterns (0.5 page)
│   │   │   └── Single-pass, two-pass, diagonal, spiral
│   │   ├── 2.1B Prefix Sum (1.25 pages)
│   │   │   ├── Mental Model: Running total snapshot
│   │   │   ├── ASCII: prefix[i] = prefix[i-1] + arr[i] diagram
│   │   │   ├── Dry Run: Range sum query trace
│   │   │   ├── Problems: Range Sum Query (Easy) → Subarray Sum = K (Medium) → Max Sum Subarray / Kadane's (Medium)
│   │   │   └── Pattern Evolution: Prefix Sum → Prefix Sum + HashMap → 2D Prefix Sum
│   │   ├── 2.1C Difference Array (0.75 page)
│   │   │   ├── Mental Model: Defer range updates
│   │   │   ├── ASCII: Range increment visualization
│   │   │   └── Problems: Car Pooling (Medium)
│   │   ├── 2.1D Sorting + Comparators (0.75 page)
│   │   │   ├── Arrays.sort() + Comparator lambda patterns
│   │   │   ├── Interview Tip: Custom sort as interview trick
│   │   │   └── Problems: Sort Colors (Medium), Meeting Rooms (Medium)
│   │   └── 2.1E Hashing for Arrays (0.75 page)
│   │       ├── freq[], int[26], HashMap encoding
│   │       └── Problems: Contains Duplicate (Easy) → Two Sum (Easy) → Group Anagrams (Medium)
│   │
│   ├── 2.2 Strings (7 pages)
│   │   ├── 2.2A Character Arrays + Frequency Counting (0.75 page)
│   │   │   ├── freq[c-'a']++ pattern
│   │   │   └── Problems: Valid Anagram (Easy)
│   │   ├── 2.2B StringBuilder + Palindrome Checks (1.0 page)
│   │   │   ├── ASCII: two-pointer palindrome trace
│   │   │   └── Problems: Valid Palindrome (Easy) → Longest Palindromic Substring (Medium)
│   │   ├── 2.2C KMP Pattern Matching (2.0 pages)
│   │   │   ├── Mental Model: Never re-examine matched characters
│   │   │   ├── ASCII: Failure function construction trace
│   │   │   ├── Dry Run: Full KMP search trace step-by-step
│   │   │   ├── AHA: Prefix = Suffix insight
│   │   │   ├── Problems: Find Index of First Occurrence (Easy/Medium)
│   │   │   └── Pattern Evolution: KMP → Z-Algorithm → Rabin-Karp
│   │   ├── 2.2D Z-Algorithm (1.0 page)
│   │   │   ├── ASCII: Z-array construction diagram
│   │   │   ├── Dry Run: Z-array values for sample string
│   │   │   └── Pattern Comparison: KMP vs Z-Algorithm (when to use which)
│   │   └── 2.2E Rabin-Karp / Rolling Hash (1.25 pages)
│   │       ├── Mental Model: Hash window, slide and subtract
│   │       ├── ASCII: Rolling hash window shift
│   │       ├── Dry Run: Hash recomputation trace
│   │       └── Problems: Repeated DNA Sequences (Medium)
│   │       └── Pattern Evolution: Rolling Hash → Polynomial Hash → Multi-hash (anti-collision)
│   │
│   ├── 2.3 Hashing Deep Dive (2 pages)
│   │   ├── 2.3A HashMap Internals (0.5 page)
│   │   │   └── Interview Tip: Load factor, collision, O(1) amortized
│   │   ├── 2.3B HashMap API Patterns (0.75 page)
│   │   │   ├── getOrDefault, computeIfAbsent, merge
│   │   │   └── freq-map template
│   │   └── 2.3C HashSet Patterns (0.75 page)
│   │       └── Problems: Longest Consecutive Sequence (Medium)
│   │
│   ├── 2.4 Two Pointers (4 pages)
│   │   ├── Mental Model: Shrink search space from both ends
│   │   ├── ASCII: Two-pointer converging diagram
│   │   ├── Template Block: Sorted array two-pointer skeleton
│   │   ├── Dry Runs (3): Two Sum II, 3Sum, Container With Most Water
│   │   ├── Problems:
│   │   │   ├── Easy: Valid Palindrome
│   │   │   ├── Medium: 3Sum, Container With Most Water, Trapping Rain Water
│   │   │   └── Hard: 4Sum
│   │   ├── Pattern Evolution: Two Pointers → Sliding Window → Dutch National Flag
│   │   ├── Common Mistakes: Forgetting sorted order requirement, pointer collision
│   │   └── Revision Box
│   │
│   ├── 2.5 Sliding Window (4 pages)
│   │   ├── 2.5A Fixed-Size Window (1.5 pages)
│   │   │   ├── Mental Model: Move the frame, drop leftmost, add rightmost
│   │   │   ├── ASCII: Window-slide animation
│   │   │   ├── Dry Run: Max sum subarray of size k
│   │   │   └── Problems: Maximum Average Subarray I (Easy) → Permutation in String (Medium)
│   │   └── 2.5B Variable-Size Window (2.5 pages)
│   │       ├── Mental Model: Expand until invalid, shrink until valid
│   │       ├── ASCII: Expand/shrink pointer trace
│   │       ├── Template Block: shrink condition skeleton
│   │       ├── Dry Runs (2): Longest Substring Without Repeating, Minimum Window Substring
│   │       ├── Problems:
│   │       │   ├── Easy: Longest Substring Without Repeating Characters
│   │       │   ├── Medium: Longest Repeating Character Replacement, Fruits Into Baskets
│   │       │   └── Hard: Minimum Window Substring, Sliding Window Maximum
│   │       ├── Pattern Evolution: Fixed Window → Variable → Variable + Freq Map → Monotonic Queue Window
│   │       ├── Common Mistakes: Wrong shrink condition, updating answer too early/late
│   │       └── Revision Box
│   │
│   ├── 2.6 Binary Search (5 pages)
│   │   ├── 2.6A Exact Match Template (1.0 page)
│   │   │   ├── Mental Model: Eliminate impossible halves
│   │   │   ├── ASCII: lo/hi/mid pointer collapse
│   │   │   ├── Dry Run: Search in sorted array
│   │   │   └── Common Mistakes: Off-by-one in while condition, mid overflow
│   │   ├── 2.6B Lower Bound + Upper Bound Templates (1.0 page)
│   │   │   ├── ASCII: First/Last position diagrams side-by-side
│   │   │   ├── Dry Run: Both bounds on same array
│   │   │   └── AHA: The direction of bias determines which bound
│   │   ├── 2.6C Rotated Array + Matrix Binary Search (1.25 pages)
│   │   │   ├── ASCII: Rotation point visualization
│   │   │   ├── Dry Run: Rotated sorted array search
│   │   │   └── Problems: Search in Rotated Sorted Array (Medium) → Find Min in Rotated (Medium)
│   │   └── 2.6D Binary Search on Answer (1.75 pages)
│   │       ├── Mental Model: Search space = valid answers, not array indices
│   │       ├── ASCII: Answer-space diagram (monotone predicate)
│   │       ├── Dry Runs (2): Koko Eating Bananas, Ship Within D Days
│   │       ├── Problems:
│   │       │   ├── Medium: Koko Eating Bananas, Capacity to Ship Packages
│   │       │   └── Hard: Split Array Largest Sum, Find Kth Smallest in Matrix
│   │       ├── Pattern Evolution: BS Exact → BS on Answer → Binary Search + Greedy
│   │       └── Revision Box
│   │
│   └── 2.7 Synthesis + Revision (3 pages)
│       ├── 2.7A Pattern Comparison Table (1.5 pages)
│       │   └── Two Pointers vs Sliding Window vs Binary Search: Signal → Use Case → Template → O
│       ├── 2.7B Part 2 AHA Moments + Common Mistakes (0.5 page)
│       └── 2.7C Part 2 One-Page Revision Sheet (1.0 page)
│
├── Part 3: Linked Lists (8 pages)
│   ├── 3.1 LL Fundamentals (2 pages)
│   │   ├── 3.1A Singly LL: Node structure, traversal template (0.75 page)
│   │   │   └── ASCII: Singly LL node chain diagram
│   │   ├── 3.1B Doubly LL + Circular LL (0.75 page)
│   │   │   └── ASCII: prev/next pointer diagram
│   │   └── 3.1C Dummy Node Technique (0.5 page)
│   │       └── AHA: Dummy node eliminates null head edge case
│   │
│   ├── 3.2 Fast / Slow Pointer (2 pages)
│   │   ├── Mental Model: Tortoise and hare — distance gap = k
│   │   ├── ASCII Diagrams (3): Midpoint, Kth from end, Cycle entry
│   │   ├── Dry Runs (2): Find middle, Detect cycle
│   │   ├── Problems:
│   │   │   ├── Easy: Middle of Linked List
│   │   │   ├── Medium: Linked List Cycle II, Happy Number
│   │   │   └── Hard: Find Duplicate Number
│   │   ├── Pattern Evolution: Fast/Slow → Cycle Entry → Floyd's Extension
│   │   └── Revision Box
│   │
│   ├── 3.3 Reverse + Merge (2 pages)
│   │   ├── 3.3A Reverse (iterative + recursive) (1.25 pages)
│   │   │   ├── ASCII: prev/curr/next pointer swap sequence
│   │   │   ├── Dry Run: 5-node reversal trace
│   │   │   └── Problems: Reverse LL (Easy) → Reverse in K-Group (Hard)
│   │   └── 3.3B Merge Two Sorted Lists (0.75 page)
│   │       ├── ASCII: Merge pointer alternation
│   │       └── Problems: Merge Two Sorted Lists (Easy) → Merge K Sorted Lists (Hard)
│   │
│   ├── 3.4 Cycle Detection + LRU Foundation (1 page)
│   │   ├── Floyd's Cycle Detection: Phase 1 + Phase 2 explanation
│   │   ├── ASCII: Cycle entry math diagram
│   │   ├── LRU Cache Foundation: Why LL + HashMap
│   │   └── Pattern Evolution: Cycle Detection → LRU Cache → LFU Cache
│   │
│   └── 3.5 Part 3 Revision Sheet (1 page)
│
├── Part 4: Stack, Queue, Deque, Monotonic (12 pages)
│   ├── 4.1 Stack (1.5 pages)
│   │   ├── Mental Model: LIFO — last in, last out
│   │   ├── ASCII: push/pop diagram
│   │   ├── Template Block: Java Deque as stack
│   │   ├── Problems: Valid Parentheses (Easy) → Min Stack (Medium)
│   │   └── Pattern Evolution: Stack → Recursive call simulation → DFS iterative
│   │
│   ├── 4.2 Queue + Deque (1.5 pages)
│   │   ├── Mental Model: FIFO — first in, first out
│   │   ├── ASCII: enqueue/dequeue diagram
│   │   ├── Template Block: Java ArrayDeque
│   │   ├── Problems: Implement Queue using Stacks (Easy) → Sliding Window Maximum (Hard)
│   │   └── Pattern Evolution: Queue → BFS → Monotonic Queue
│   │
│   ├── 4.3 Monotonic Stack (3 pages)
│   │   ├── Mental Model: Maintain strictly increasing (or decreasing) order in stack
│   │   ├── ASCII (2): Increasing stack trace + Decreasing stack trace
│   │   ├── Dry Runs (2): Next Greater Element trace, Stock Span trace
│   │   ├── Template Block: mono-stack skeleton (increasing + decreasing)
│   │   ├── Problems:
│   │   │   ├── Easy: Next Greater Element I
│   │   │   ├── Medium: Daily Temperatures, Stock Span, Car Fleet
│   │   │   └── Hard: Largest Rectangle in Histogram, Trapping Rain Water (stack version)
│   │   ├── Pattern Evolution: NGE → Histogram → Sum of Subarray Minimums → Online Stock Span
│   │   ├── Common Mistakes: Wrong pop condition, forgetting to drain stack at end
│   │   └── Revision Box
│   │
│   ├── 4.4 Monotonic Queue (2 pages)
│   │   ├── Mental Model: Window max/min in O(1) amortized — deque as sorted buffer
│   │   ├── ASCII: Deque state per window step
│   │   ├── Dry Run: Sliding Window Maximum trace (window of 3)
│   │   ├── Template Block: mono-deque skeleton for variable window
│   │   ├── Problems:
│   │   │   ├── Medium: Sliding Window Maximum
│   │   │   └── Hard: Shortest Subarray with Sum at Least K
│   │   ├── Pattern Evolution: Fixed Window Max → Variable Window → Monotonic Queue + DP
│   │   └── Revision Box
│   │
│   ├── 4.5 Classic Applications (3 pages)
│   │   ├── 4.5A Next Greater / Smaller Element (0.75 page)
│   │   ├── 4.5B Largest Rectangle in Histogram (1.25 pages)
│   │   │   ├── ASCII: Bar heights + left/right boundary diagram
│   │   │   └── Dry Run: Full index trace
│   │   └── 4.5C Comparison Table (1.0 page)
│   │       └── Stack vs Queue vs Deque vs MonoStack vs MonoQueue: signal → use
│   │
│   └── 4.6 Part 4 Revision Sheet (1 page)
│
├── Part 5: Recursion & Backtracking (13 pages)
│   ├── 5.1 Recursion Fundamentals (2 pages)
│   │   ├── Mental Model: Trust the function, define base + recursive case
│   │   ├── ASCII: Call stack frame diagram for factorial(4)
│   │   ├── Recursion Tree: Fibonacci tree with overlapping subproblems highlighted
│   │   ├── Dry Run: Fibonacci call trace showing duplicate work
│   │   ├── AHA: Overlapping subproblems → memoize → DP
│   │   └── Revision Box
│   │
│   ├── 5.2 Decision Tree Mental Model (1 page)
│   │   ├── ASCII: Decision tree for [1,2,3] subsets
│   │   └── Insight: Every backtracking problem is a path through this tree
│   │
│   ├── 5.3 Backtracking Master Template (2 pages)
│   │   ├── Mental Model: Choose → Explore → Unchoose
│   │   ├── ASCII: Three-phase recursion diagram
│   │   ├── Template Block: Universal backtracking skeleton
│   │   ├── Pattern Comparison: DFS vs Backtracking (what is undone vs not)
│   │   └── Revision Box
│   │
│   ├── 5.4 Subsets (2 pages)
│   │   ├── ASCII: Subset decision tree for [1,2,3]
│   │   ├── Dry Run: Include/exclude trace
│   │   ├── Problems:
│   │   │   ├── Medium: Subsets, Subsets II (with duplicates)
│   │   │   └── Medium: Letter Case Permutation
│   │   └── Pattern Evolution: Subsets → Power Set → Bitmask enumeration
│   │
│   ├── 5.5 Permutations (1.5 pages)
│   │   ├── ASCII: Permutation swap tree for [1,2,3]
│   │   ├── Dry Run: visited[] array trace
│   │   ├── Problems:
│   │   │   ├── Medium: Permutations, Permutations II (duplicates)
│   │   │   └── Hard: Next Permutation
│   │   └── Pattern Evolution: Permutations → Permutations with Constraints → TSP bitmask
│   │
│   ├── 5.6 Combination Sum (1.5 pages)
│   │   ├── ASCII: Combination tree with reuse vs no-reuse branches
│   │   ├── Dry Run: Candidates=[2,3,6], target=7 trace
│   │   ├── Problems:
│   │   │   ├── Medium: Combination Sum, Combination Sum II
│   │   │   └── Medium: Combination Sum III
│   │   └── Pattern Evolution: CombSum → Knapsack DP
│   │
│   ├── 5.7 N-Queens (1.5 pages)
│   │   ├── ASCII: 4x4 board state at each recursion step
│   │   ├── Dry Run: Column + diagonal constraint check
│   │   ├── Problems:
│   │   │   └── Hard: N-Queens, N-Queens II
│   │   └── AHA: columnSet + diagSet + antiDiagSet trick
│   │
│   ├── 5.8 Sudoku Solver (1 page)
│   │   ├── ASCII: 3x3 box index formula diagram
│   │   └── Problems: Hard: Sudoku Solver
│   │
│   └── 5.9 Part 5 Revision Sheet (0.5 page)
│
├── Part 6: Trees (20 pages)
│   ├── 6.1 Binary Tree Fundamentals (2 pages)
│   │   ├── ASCII: Node structure, full vs complete vs perfect tree
│   │   ├── Template Block: TreeNode class
│   │   ├── Insight: Every tree problem = variant of DFS or BFS
│   │   └── Revision Box
│   │
│   ├── 6.2 DFS: Pre / In / Post Order (3 pages)
│   │   ├── Mental Model: Visit order determines Pre vs In vs Post
│   │   ├── ASCII (3): Three traversal order diagrams side-by-side
│   │   ├── Template Blocks (3): Recursive templates for each order
│   │   ├── Template Blocks (3): Iterative templates (Stack-based)
│   │   ├── Dry Runs (2): Inorder trace, Postorder height computation
│   │   ├── Problems:
│   │   │   ├── Easy: Binary Tree Inorder Traversal
│   │   │   ├── Medium: Binary Tree Zigzag, Path Sum II
│   │   │   └── Hard: Binary Tree Maximum Path Sum
│   │   ├── Pattern Evolution: DFS → Return-value DFS → Global-variable DFS → Tree DP
│   │   └── Revision Box
│   │
│   ├── 6.3 BFS: Level Order (2 pages)
│   │   ├── Mental Model: Queue = frontier, process level by level
│   │   ├── ASCII: Level-by-level queue drain diagram
│   │   ├── Template Block: BFS with level size trick
│   │   ├── Dry Run: 3-level tree BFS trace
│   │   ├── Problems:
│   │   │   ├── Easy: Binary Tree Level Order Traversal
│   │   │   ├── Medium: Zigzag Level Order, Right Side View, Average of Levels
│   │   │   └── Medium: Minimum Depth
│   │   ├── Pattern Evolution: Level-Order → Right Side View → Vertical Order → Connect Next Pointers
│   │   └── Revision Box
│   │
│   ├── 6.4 Binary Tree Problems — Classic Set (3 pages)
│   │   ├── 6.4A Diameter of Binary Tree (0.75 page)
│   │   │   ├── ASCII: Diameter path through root diagram
│   │   │   └── AHA: diameter != always through root; postorder trick
│   │   ├── 6.4B Balanced Binary Tree (0.5 page)
│   │   ├── 6.4C Invert Binary Tree (0.5 page)
│   │   ├── 6.4D Max Depth + Min Depth (0.5 page)
│   │   └── 6.4E Same Tree + Subtree of Another Tree (0.75 page)
│   │       └── Pattern Evolution: Same Tree → Subtree → Symmetric → Mirror
│   │
│   ├── 6.5 Binary Search Tree (4 pages)
│   │   ├── 6.5A BST Property + Search + Insert (1.0 page)
│   │   │   ├── ASCII: BST property invariant diagram
│   │   │   └── AHA: Inorder of BST = sorted array
│   │   ├── 6.5B BST Delete (3 cases) (1.0 page)
│   │   │   ├── ASCII: 3-case deletion diagram
│   │   │   └── Common Mistake: Missing successor/predecessor logic
│   │   ├── 6.5C Validate BST + Kth Smallest (0.75 page)
│   │   │   └── Problems: Validate BST (Medium), Kth Smallest in BST (Medium)
│   │   └── 6.5D LCA in BST + Binary Tree (1.25 pages)
│   │       ├── ASCII: LCA ancestor path diagram (BST vs Binary Tree)
│   │       ├── Dry Run: Both LCA variants traced
│   │       ├── Problems: LCA of BST (Medium) → LCA of Binary Tree (Medium) → LCA III (Hard)
│   │       └── Pattern Evolution: LCA → LCA with Parent Pointer → Binary Lifting (Staff)
│   │
│   ├── 6.6 Tree Construction + Serialization (2 pages)
│   │   ├── 6.6A Construct from Preorder + Inorder (1.0 page)
│   │   │   ├── ASCII: Index mapping + recursive split visualization
│   │   │   ├── Dry Run: 5-node construction trace
│   │   │   └── Problems: Construct Binary Tree from Pre+In (Medium)
│   │   └── 6.6B Serialization + Deserialization (1.0 page)
│   │       ├── ASCII: Encoded string format diagram
│   │       └── Problems: Serialize and Deserialize Binary Tree (Hard)
│   │
│   ├── 6.7 Segment Tree + Fenwick Tree (2 pages)
│   │   ├── 6.7A Segment Tree (1.25 pages)
│   │   │   ├── Mental Model: Binary tree over array ranges
│   │   │   ├── ASCII: Segment tree node → range mapping diagram
│   │   │   ├── Operations: build O(n), query O(log n), update O(log n)
│   │   │   └── Problems: Range Sum Query — Mutable (Medium)
│   │   └── 6.7B Fenwick Tree / BIT (0.75 page)
│   │       ├── ASCII: i & (-i) trick index diagram
│   │       └── AHA: Simpler than Segment Tree for prefix sums
│   │
│   └── 6.8 Part 6 Synthesis + Revision (2 pages)
│       ├── Tree Decision Table: BFS vs DFS vs BST vs Segment — when each is needed
│       ├── AHA Moments + Common Mistakes (0.5 page)
│       └── Part 6 One-Page Revision Sheet (1.0 page)
│
├── Part 7: Heap / Priority Queue (8 pages)
│   ├── 7.1 PriorityQueue Fundamentals (1.5 pages)
│   │   ├── Mental Model: Always gives you the most important element
│   │   ├── ASCII: Min-heap tree + backing array mapping
│   │   ├── Java API Block: PriorityQueue constructors + common operations
│   │   ├── AHA: Default Java PriorityQueue is MIN heap; negate for MAX
│   │   └── Revision Box
│   │
│   ├── 7.2 Heapify — Build from Array O(n) (0.5 page)
│   │   └── AHA: Why O(n) and not O(n log n)
│   │
│   ├── 7.3 Top K Pattern (2 pages)
│   │   ├── Mental Model: Min-heap of size k — pop when size exceeds k
│   │   ├── ASCII: Running top-k heap state trace
│   │   ├── Dry Run: Top K Frequent Elements trace
│   │   ├── Problems:
│   │   │   ├── Easy: Kth Largest Element in Stream
│   │   │   ├── Medium: Top K Frequent Elements, K Closest Points to Origin
│   │   │   └── Hard: Find Median from Data Stream (partial)
│   │   ├── Pattern Evolution: Top-K → K Closest → Kth Smallest → Stream median
│   │   └── Revision Box
│   │
│   ├── 7.4 K-Way Merge (1.5 pages)
│   │   ├── Mental Model: Always pick the globally smallest from K fronts
│   │   ├── ASCII: K sorted lists + heap pointer diagram
│   │   ├── Dry Run: 3-list merge trace
│   │   ├── Problems:
│   │   │   ├── Hard: Merge K Sorted Lists
│   │   │   └── Medium: Kth Smallest Element in Sorted Matrix
│   │   └── Pattern Evolution: Merge 2 → Merge K → External Sort
│   │
│   ├── 7.5 Two Heaps — Median from Data Stream (1.5 pages)
│   │   ├── Mental Model: Lower half in Max-Heap, Upper half in Min-Heap
│   │   ├── ASCII: Two-heap balance diagram
│   │   ├── Dry Run: Insert sequence + rebalance trace
│   │   ├── Problems:
│   │   │   └── Hard: Find Median from Data Stream
│   │   └── Pattern Evolution: Two Heaps → Sliding Window Median
│   │
│   └── 7.6 Part 7 Revision Sheet (1 page)
│
├── Part 8: Trie (9 pages)
│   ├── 8.1 Trie Fundamentals (1.5 pages)
│   │   ├── Mental Model: Tree where each edge = one character
│   │   ├── ASCII: Trie for "cat", "cap", "car", "cart"
│   │   ├── Template Block: TrieNode class (children[26] + isEnd)
│   │   ├── AHA: Why Trie beats HashMap for prefix queries
│   │   └── Revision Box
│   │
│   ├── 8.2 Core Operations (1.5 pages)
│   │   ├── Template Blocks (3): insert, search, startsWith
│   │   ├── Dry Run: All 3 operations traced on "cat/cap/car"
│   │   ├── Problems:
│   │   │   └── Medium: Implement Trie (LeetCode 208)
│   │   └── Common Mistakes: Not marking isEnd; returning node vs boolean
│   │
│   ├── 8.3 Delete Operation (0.75 page)
│   │   └── ASCII: Node pruning diagram (when to delete parent)
│   │
│   ├── 8.4 Wildcard Search (1.0 page)
│   │   ├── ASCII: '.' wildcard branching diagram
│   │   ├── Dry Run: search("c.t") matching trace
│   │   └── Problems: Medium: Design Add and Search Words (LeetCode 211)
│   │
│   ├── 8.5 Word Search II — Trie + Grid DFS (2.0 pages)
│   │   ├── Mental Model: Build Trie from dictionary; DFS grid and check Trie
│   │   ├── ASCII: Grid + Trie pointer combined diagram
│   │   ├── Dry Run: Grid traversal + Trie path trace
│   │   ├── Problems: Hard: Word Search II (LeetCode 212)
│   │   ├── Pattern Evolution: Word Search I (DFS) → Word Search II (Trie+DFS) → Boggle
│   │   └── Revision Box
│   │
│   ├── 8.6 Autocomplete System (0.75 page)
│   │   ├── Design: Trie node augmented with frequency counter
│   │   └── Problems: Hard: Design Search Autocomplete System (LeetCode 642)
│   │
│   ├── 8.7 Bit Trie + Maximum XOR (1.5 pages)
│   │   ├── Mental Model: Trie of 32-bit integers (MSB → LSB)
│   │   ├── ASCII: Bit-level branching diagram
│   │   ├── Dry Run: Max XOR search trace
│   │   └── Problems: Medium: Maximum XOR of Two Numbers (LeetCode 421)
│   │
│   └── 8.8 Part 8 Revision Sheet (1.0 page)
│
├── Part 9: Graphs (25 pages)
│   │
│   ├── 9A. Graph Foundations (3 pages)
│   │   ├── 9A.1 Graph Representations (1.25 pages)
│   │   │   ├── ASCII (3): Edge List / Adjacency List / Adjacency Matrix side-by-side
│   │   │   ├── Template Blocks (2): Adj List builder (directed + undirected)
│   │   │   └── Comparison Table: Repr × Space × Edge query × Neighbor query
│   │   ├── 9A.2 Grid Graph + Tree→Graph (0.75 page)
│   │   │   ├── ASCII: Grid cell → 4-direction neighbor formula
│   │   │   └── Template Block: 4-direction iteration snippet
│   │   └── 9A.3 Graph Types Taxonomy (1.0 page)
│   │       ├── Directed / Undirected / Weighted / DAG / Bipartite
│   │       └── Comparison Table: type → algorithms applicable
│   │
│   ├── 9B. Helper Arrays (1 page)
│   │   ├── Table: visited[] / parent[] / distance[] / cost[] / indegree[]
│   │   │        outdegree[] / direction[] / color[]
│   │   └── When-to-initialize guide
│   │
│   ├── 9C. Traversal (4 pages)
│   │   ├── 9C.1 DFS — Recursive Template (1.0 page)
│   │   │   ├── ASCII: DFS traversal order on sample graph
│   │   │   ├── Dry Run: visited[] state per step
│   │   │   └── Problems: Easy: Number of Islands, Connected Components
│   │   ├── 9C.2 DFS — Iterative Template (0.75 page)
│   │   │   ├── Template Block: Stack-based DFS
│   │   │   └── AHA: Stack push order must mirror recursive call order
│   │   ├── 9C.3 BFS Template (1.25 pages)
│   │   │   ├── ASCII: BFS level expansion diagram
│   │   │   ├── Dry Run: Queue drain trace with distance[]
│   │   │   └── Problems: Medium: Shortest Path in Binary Matrix, Rotting Oranges
│   │   └── 9C.4 Multi-Source BFS (1.0 page)
│   │       ├── ASCII: Multiple start nodes expanding simultaneously
│   │       ├── AHA: Add ALL sources to queue before starting
│   │       ├── Problems: Medium: 01 Matrix, Pacific Atlantic Water Flow
│   │       └── Pattern Evolution: Single BFS → Multi-Source BFS → BFS + Topological Sort
│   │
│   ├── 9D. Structural Algorithms (5 pages)
│   │   ├── 9D.1 Cycle Detection — Directed Graph (1.25 pages)
│   │   │   ├── ASCII: DFS color states (WHITE/GRAY/BLACK)
│   │   │   ├── Dry Run: Cycle vs non-cycle graph trace
│   │   │   └── Problems: Medium: Course Schedule I
│   │   ├── 9D.2 Cycle Detection — Undirected Graph (0.75 page)
│   │   │   ├── Template: parent[] check during DFS
│   │   │   └── AHA: Union-Find detects undirected cycles more cleanly
│   │   ├── 9D.3 Topological Sort — Kahn's (BFS) (1.25 pages)
│   │   │   ├── Mental Model: Process zero-indegree nodes first
│   │   │   ├── ASCII: Indegree countdown per step
│   │   │   ├── Dry Run: Course Schedule II trace
│   │   │   └── Problems: Medium: Course Schedule II, Alien Dictionary
│   │   ├── 9D.4 Topological Sort — DFS-based (0.75 page)
│   │   │   └── Pattern Comparison: Kahn's vs DFS-Topo: same result, different access pattern
│   │   └── 9D.5 Union-Find (2.0 pages)
│   │       ├── Mental Model: Group elements into sets; merge groups
│   │       ├── ASCII: Union operations + path compression diagram
│   │       ├── Dry Run: Union + Find with rank + compression trace
│   │       ├── Template Block: Full UF implementation
│   │       ├── Problems:
│   │       │   ├── Medium: Number of Connected Components, Redundant Connection
│   │       │   └── Hard: Accounts Merge, Number of Islands II
│   │       └── Pattern Evolution: Basic UF → Weighted UF → DSU on Tree
│   │
│   ├── 9E. Shortest Path Algorithms (4 pages)
│   │   ├── 9E.1 Dijkstra (2.0 pages)
│   │   │   ├── Mental Model: Always relax the globally cheapest unvisited node
│   │   │   ├── ASCII: Priority queue processing order diagram
│   │   │   ├── Dry Run: 5-node weighted graph — full dist[] trace
│   │   │   ├── Template Block: PriorityQueue + adj list Dijkstra
│   │   │   ├── Problems: Medium: Network Delay Time, Path With Min Effort
│   │   │   ├── AHA: Dijkstra fails with negative edges → use Bellman-Ford
│   │   │   └── Pattern Evolution: Dijkstra → Bidirectional Dijkstra → A*
│   │   ├── 9E.2 Bellman-Ford (1.25 pages)
│   │   │   ├── Mental Model: Relax ALL edges N-1 times
│   │   │   ├── Dry Run: Edge relaxation trace per iteration
│   │   │   ├── AHA: Nth relaxation finds negative cycle
│   │   │   └── Problems: Medium: Cheapest Flights Within K Stops
│   │   └── 9E.3 Floyd-Warshall (0.75 page)
│   │       ├── Mental Model: dp[i][j] = min through any intermediate k
│   │       ├── Complexity: O(V³) — use only on small V (<= 400)
│   │       └── Problems: Medium: Find the City With the Smallest Number of Neighbors
│   │
│   ├── 9F. MST Algorithms (2 pages)
│   │   ├── 9F.1 Prim's Algorithm (1.0 page)
│   │   │   ├── ASCII: MST edge selection diagram
│   │   │   └── Problems: Medium: Min Cost to Connect All Points
│   │   └── 9F.2 Kruskal's Algorithm (1.0 page)
│   │       ├── Mental Model: Sort edges by weight, add if no cycle (Union-Find)
│   │       └── Pattern Comparison: Prim (dense) vs Kruskal (sparse) — when to choose
│   │
│   └── 9G. Synthesis (6 pages)
│       ├── 9G.1 Graph Decision Flowchart (1.0 page) — full-page diagram
│       ├── 9G.2 Algorithm Comparison Table (1.0 page)
│       │   └── DFS/BFS/Dijkstra/Bellman/Floyd/Topo/UF × Use Case × Complexity
│       ├── 9G.3 AHA Moments + Common Mistakes (0.75 page)
│       ├── 9G.4 Hard Problems Synthesis (2.25 pages)
│       │   ├── Word Ladder (Hard) — BFS + graph construction
│       │   ├── Critical Connections (Hard) — Tarjan bridges
│       │   └── Parallel Courses III (Hard) — Topo + DP on DAG
│       └── 9G.5 Part 9 Revision Sheet (1.0 page)
│
├── Part 10: Dynamic Programming (22 pages)
│   ├── 10.1 SC→RBR→MTS Framework (2 pages)
│   │   ├── Step 1 — Subproblem Choice: What decision is made at each step?
│   │   ├── Step 2 — Recurrence: How is subproblem result used?
│   │   ├── Step 3 — Memoization → Tabulation → Space Optimization
│   │   ├── ASCII: Framework flowchart
│   │   └── AHA: You don't invent DP. You discover the recurrence.
│   │
│   ├── 10.2 Memoization vs Tabulation (1 page)
│   │   ├── Side-by-side pseudocode comparison (same problem, both approaches)
│   │   └── Comparison Table: Top-down vs Bottom-up × Cache × Stack Risk × Space
│   │
│   ├── 10.3 1D DP (3 pages)
│   │   ├── 10.3A Climbing Stairs / Fibonacci (0.75 page)
│   │   │   ├── ASCII: dp[i] depends on dp[i-1], dp[i-2]
│   │   │   └── Pattern Evolution: Fibonacci → Climbing Stairs → Min Cost Climbing → Decode Ways
│   │   ├── 10.3B House Robber I + II (1.25 pages)
│   │   │   ├── Dry Run: dp[] array state trace
│   │   │   └── AHA: Circular constraint → solve twice (exclude first, exclude last)
│   │   └── 10.3C Decode Ways (1.0 page)
│   │       ├── ASCII: Decision tree with valid/invalid decodings
│   │       └── Problems: Medium: Decode Ways, Decode Ways II
│   │
│   ├── 10.4 2D DP (2.5 pages)
│   │   ├── 10.4A Unique Paths + Min Path Sum (1.0 page)
│   │   │   └── ASCII: Grid fill visualization with dp[i][j] arrows
│   │   └── 10.4B Edit Distance (1.5 pages)
│   │       ├── ASCII: DP table fill with operation labeling
│   │       └── Problems: Medium: Edit Distance, Minimum ASCII Delete Sum
│   │
│   ├── 10.5 0/1 Knapsack (2.5 pages)
│   │   ├── Mental Model: Include or exclude each item exactly once
│   │   ├── ASCII: 2D DP table (items × capacity) with fill arrows
│   │   ├── Dry Run: Full 4-item knapsack table trace
│   │   ├── Space Optimization: 1D rolling array
│   │   ├── Problems:
│   │   │   ├── Medium: Partition Equal Subset Sum, Target Sum
│   │   │   └── Hard: Last Stone Weight II
│   │   └── Pattern Evolution: 0/1 Knapsack → Subset Sum → Partition → Count Paths
│   │
│   ├── 10.6 Unbounded Knapsack (1 page)
│   │   ├── AHA: Items can be reused → only iterate forwards
│   │   └── Problems: Medium: Coin Change, Coin Change II
│   │
│   ├── 10.7 LCS — Longest Common Subsequence (2 pages)
│   │   ├── ASCII: DP table with diagonal/left/up fill logic
│   │   ├── Dry Run: "ABCDE" vs "ACE" table trace
│   │   ├── Problems:
│   │   │   ├── Medium: LCS, Longest Common Substring
│   │   │   └── Medium: Uncrossed Lines, Delete Operation for Two Strings
│   │   └── Pattern Evolution: LCS → LCS + Reconstruction → LCS variants (palindrome, distinct)
│   │
│   ├── 10.8 LIS — Longest Increasing Subsequence (2 pages)
│   │   ├── ASCII: O(n²) vs O(n log n) patience sort diagram
│   │   ├── Dry Run: Both approaches on same input
│   │   ├── Problems:
│   │   │   ├── Medium: LIS
│   │   │   └── Hard: Russian Doll Envelopes
│   │   └── Pattern Evolution: LIS → 2D LIS (Envelopes) → LIS on DP DAG
│   │
│   ├── 10.9 Interval DP (1.5 pages)
│   │   ├── Mental Model: dp[i][j] = best answer for range [i..j]
│   │   ├── ASCII: Range [i,j] fill order diagram
│   │   └── Problems: Hard: Burst Balloons, Strange Printer
│   │
│   ├── 10.10 Bitmask DP (1.5 pages)
│   │   ├── Mental Model: State = bitmask of visited nodes
│   │   ├── ASCII: Bitmask state transition diagram
│   │   └── Problems: Hard: Shortest Path Visiting All Nodes
│   │
│   ├── 10.11 State Machine DP (1 page)
│   │   ├── ASCII: State diagram for Buy/Sell/Hold/Cooldown/Fee
│   │   └── Problems: Medium: Best Time to Buy/Sell Stock with Cooldown + Fee
│   │
│   ├── 10.12 Tree DP + Graph DP on DAG (1 page)
│   │   └── Problems: Medium: House Robber III (Tree DP)
│   │
│   └── 10.13 Part 10 Synthesis + Revision (2 pages)
│       ├── DP Decision Table: 1D/2D/Knapsack/LCS/LIS/Interval/Bitmask/StateMachine — signals
│       ├── AHA Moments + Top 5 Mistakes
│       └── Part 10 One-Page Revision Sheet
│
├── Part 11: Greedy (8 pages)
│   ├── 11.1 Greedy Foundations (1 page)
│   │   ├── Mental Model: Make locally optimal choice; prove it extends globally
│   │   ├── Exchange Argument proof sketch
│   │   ├── AHA: Greedy = DP where each state has exactly one optimal choice
│   │   └── Revision Box
│   │
│   ├── 11.2 Interval Problems (2 pages)
│   │   ├── 11.2A Merge Intervals (0.75 page)
│   │   │   ├── ASCII: Sort then sweep diagram
│   │   │   └── Problems: Medium: Merge Intervals, Insert Interval
│   │   ├── 11.2B Non-Overlapping / Meeting Rooms (0.75 page)
│   │   │   └── Problems: Medium: Non-Overlapping Intervals, Meeting Rooms II
│   │   └── 11.2C Pattern Evolution (0.5 page)
│   │       └── Intervals → Sweep Line → Skyline Problem
│   │
│   ├── 11.3 Jump Game (1.5 pages)
│   │   ├── Mental Model: Greedily extend max reach
│   │   ├── Dry Run: Jump Game I + II reach-extension trace
│   │   └── Problems: Medium: Jump Game I + II
│   │
│   ├── 11.4 Gas Station (1 page)
│   │   ├── ASCII: Net gain circular trace
│   │   └── Problems: Medium: Gas Station
│   │
│   ├── 11.5 Greedy vs DP Decision Table (1 page)
│   │   └── Side-by-side: When greedy is provably optimal vs when DP is needed
│   │
│   └── 11.6 Part 11 Revision Sheet (1.5 pages)
│       ├── AHA Moments + Common Mistakes
│       └── One-page revision
│
├── Part 12: Staff-Level Data Structures (8 pages)
│   ├── 12.1 LRU Cache (2 pages)
│   │   ├── Design: HashMap + Doubly Linked List
│   │   ├── ASCII: Internal structure diagram
│   │   ├── Dry Run: put/get/evict sequence trace
│   │   └── Problems: Medium: LRU Cache (LeetCode 146)
│   │
│   ├── 12.2 LFU Cache (1.5 pages)
│   │   ├── Design: Two HashMaps + Doubly LL per frequency
│   │   ├── ASCII: Frequency bucket diagram
│   │   └── Problems: Hard: LFU Cache (LeetCode 460)
│   │
│   ├── 12.3 Rate Limiter Patterns (1 page)
│   │   ├── Token Bucket + Sliding Window Log + Fixed Window Counter
│   │   └── Trade-off table: memory vs accuracy vs burstiness
│   │
│   ├── 12.4 Autocomplete System (1.5 pages)
│   │   ├── Design: Trie + frequency augmented node + MinHeap for top-3
│   │   ├── ASCII: Architecture diagram
│   │   └── Problems: Hard: Design Search Autocomplete System (LeetCode 642)
│   │
│   ├── 12.5 Sparse Table — RMQ in O(1) (1 page)
│   │   ├── Mental Model: Precompute power-of-2 windows
│   │   └── AHA: Overlapping ranges are OK for min/max (idempotent)
│   │
│   └── 12.6 Consistent Hashing + Design Patterns in Algorithms (1 page)
│       └── Why interviewers ask this at Staff-level; high-level mental model
│
├── Part 13: Interview Meta Layer (8 pages)
│   ├── 13.1 Pattern Recognition Master Guide (2 pages)
│   │   ├── Full Signal → Pattern → Template → Complexity mapping table
│   │   └── "If you see X → Think Y" condensed decision tree
│   │
│   ├── 13.2 Interview Communication Script (1 page)
│   │   └── Verbatim 7-step script: Clarify → Example → Brute → Optimize → Code → Test → Complexity
│   │
│   ├── 13.3 Debugging Checklist (0.5 page)
│   │   └── Off-by-one, null, empty, overflow, visited[], base case, return type
│   │
│   ├── 13.4 Mock Interview Rubric (0.5 page)
│   │   └── Scoring table: Pattern Recognition / Communication / Code / Complexity / Optimization
│   │
│   ├── 13.5 Master Cheat Sheet — All Patterns (2 pages)
│   │   └── Dense table: Pattern × Signal × Template × Time × Space × Gotcha
│   │
│   ├── 13.6 3-Hour Pre-Interview Cram Sequence (1 page)
│   │   └── Hour-by-hour: which revision sheets to read + which templates to mentally trace
│   │
│   └── 13.7 Company-Specific Pattern Variations (1 page)
│       └── Google / Meta / Amazon / Uber / Airbnb / Coupang: top-3 patterns per company
│
└── Appendix A: Master Java Template Library (16 pages)
    ├── A.1  DFS — Recursive (1 page)
    ├── A.2  DFS — Iterative (1 page)
    ├── A.3  Tree DFS: Pre/In/Post (1 page)
    ├── A.4  Grid DFS (1 page)
    ├── A.5  BFS — Standard (1 page)
    ├── A.6  Multi-Source BFS (1 page)
    ├── A.7  Topological Sort — Kahn's (1 page)
    ├── A.8  Topological Sort — DFS (0.5 page)
    ├── A.9  Binary Search — Exact / Lower / Upper (1 page)
    ├── A.10 Binary Search on Answer (0.5 page)
    ├── A.11 Two Pointers (0.5 page)
    ├── A.12 Sliding Window — Fixed + Variable (1 page)
    ├── A.13 Prefix Sum + Difference Array (0.5 page)
    ├── A.14 Monotonic Stack + Queue (1 page)
    ├── A.15 Heap / Top-K + K-Way Merge (1 page)
    ├── A.16 Union-Find (1 page)
    ├── A.17 Dijkstra (1 page)
    ├── A.18 Bellman-Ford (0.5 page)
    ├── A.19 Prim + Kruskal (0.5 page)
    ├── A.20 Segment Tree + Fenwick Tree (1 page)
    ├── A.21 Trie — TrieNode + 3 ops (1 page)
    ├── A.22 Backtracking Skeleton (0.5 page)
    └── A.23 DP — Memo + Tabulation Skeletons (0.5 page)
```

---

# SECTION 2: PAGE ALLOCATION TABLE

| Part | Pages | Subtopics | Problems | Revision Pages |
|---|---|---|---|---|
| Part 0: Orientation | 3 | 4 | 0 | 0.5 |
| Part 1: Foundations | 10 | 9 | 0 | 1.0 |
| Part 2: Arrays/Strings/Searching | 30 | 19 | 35 | 3.0 |
| Part 3: Linked Lists | 8 | 8 | 10 | 1.0 |
| Part 4: Stack/Queue/Monotonic | 12 | 9 | 12 | 1.0 |
| Part 5: Recursion/Backtracking | 13 | 9 | 14 | 0.5 |
| Part 6: Trees | 20 | 15 | 20 | 2.0 |
| Part 7: Heap | 8 | 6 | 8 | 1.0 |
| Part 8: Trie | 9 | 8 | 7 | 1.0 |
| Part 9: Graphs | 25 | 20 | 18 | 2.0 |
| Part 10: DP | 22 | 13 | 22 | 2.0 |
| Part 11: Greedy | 8 | 6 | 8 | 1.5 |
| Part 12: Staff-Level Structures | 8 | 6 | 5 | 0 |
| Part 13: Interview Meta | 8 | 7 | 0 | 0 |
| Appendix A: Templates | 16 | 23 | 0 | 0 |
| **TOTAL** | **200** | **162** | **159** | **16.5** |

---

# SECTION 3: TOPIC DEPENDENCY TREE

```
Part 0 (Orientation)
 └── Part 1 (Foundations: Big-O, Math, Bits)
      └── Part 2 (Arrays, Strings, Two Pointers, Sliding Window, Binary Search)
           ├── Part 3 (Linked Lists)
           │    └── Part 4 (Stack, Queue, Mono)
           │         └── Part 5 (Recursion, Backtracking)
           │              └── Part 6 (Trees)
           │                   ├── Part 7 (Heap)
           │                   │    └── Part 12 (Staff: LRU, LFU, Autocomplete)
           │                   ├── Part 8 (Trie)
           │                   │    └── Part 12 (Autocomplete)
           │                   └── Part 9 (Graphs)
           │                        ├── Part 10 (DP)
           │                        │    └── Part 11 (Greedy)
           │                        │         └── Part 13 (Interview Meta)
           │                        └── Appendix A (Templates)
           └── Appendix A (Templates — Binary Search, Two Pointers, Prefix Sum)
```

**Strict Dependency Rules:**
- A topic is never introduced before its prerequisites.
- Recursion (Part 5) must precede Trees, Graphs, and Backtracking.
- Union-Find is taught inside Graphs (Part 9), NOT as a standalone structure.
- Segment Tree and Fenwick Tree are taught inside Trees (Part 6) because they are tree-backed.
- DP (Part 10) requires Recursion (Part 5) and Graphs (Part 9) for DAG-based DP.

---

# SECTION 4: TEACHING BLOCKS FOR EVERY SUBTOPIC

## Universal Teaching Block Order (for all major subtopics)

```
Block 1:  Concept Statement      — One sentence. What does this do?
Block 2:  Recognition Trigger    — What problem keywords trigger this?
Block 3:  When to Use            — Positive conditions
Block 4:  When NOT to Use        — Negative conditions + alternative
Block 5:  Mental Model           — Intuitive description (no jargon)
Block 6:  Visualization          — ASCII diagram or box diagram
Block 7:  Core Concept           — Precise explanation of the mechanism
Block 8:  Java Template          — Minimal commented Java code
Block 9:  Template Walkthrough   — Line-by-line explanation of template
Block 10: Complexity Analysis    — Time + Space table
Block 11: Dry Run                — Step-by-step state trace
Block 12: Common Mistakes        — Top 3 interview failure points
Block 13: AHA Moment             — The insight that makes it click
Block 14: Pattern Comparison     — vs nearest alternative (table format)
Block 15: NeetCode Mapping       — NeetCode 150 problems in this pattern
Block 16: Easy Problem           — Representative easy problem + approach
Block 17: Medium Problem         — Representative medium + approach
Block 18: Hard Problem           — Representative hard (where applicable)
Block 19: Interview Follow-Up    — 3 follow-up questions interviewers ask
Block 20: Revision Box           — Half-page condensed cheat card
```

### Block assignment per subtopic category:

| Subtopic Category | Blocks Applied | Approx Pages |
|---|---|---|
| Foundation (Big-O, Math, Bits) | 1,3,5,6,7,10,12,13,20 | 0.75–1.0 |
| Core Pattern (Two Ptr, Sliding, BS) | All 20 blocks | 3.5–5.0 |
| Data Structure (Stack, Queue, Heap, Trie) | 1–15, 16–18, 20 | 2.0–3.0 |
| Algorithm (Dijkstra, DP variants) | All 20 blocks | 2.0–2.5 |
| Advanced (Segment Tree, LRU, Autocomplete) | 1,5,6,7,8,10,11,13,17,18 | 1.0–2.0 |

---

# SECTION 5: REPRESENTATIVE LEETCODE PROBLEM PROGRESSIONS

## 2.4 Two Pointers
| # | Problem | Level | Pattern Insight |
|---|---|---|---|
| 125 | Valid Palindrome | Easy | Two pointers converging |
| 167 | Two Sum II | Easy | Sorted array shrink |
| 15 | 3Sum | Medium | Fix one, two-pointer the rest |
| 11 | Container With Most Water | Medium | Maximize by moving shorter side |
| 42 | Trapping Rain Water | Hard | Left-max + right-max arrays |
| 18 | 4Sum | Hard | Extend 3Sum with another loop |
→ Evolution: 2-pointer sorted → 3Sum → 4Sum → k-Sum (Generalized)

## 2.5 Sliding Window
| # | Problem | Level | Pattern Insight |
|---|---|---|---|
| 643 | Max Average Subarray I | Easy | Fixed window |
| 3 | Longest Substring Without Repeating | Medium | Variable window + HashSet |
| 567 | Permutation in String | Medium | Fixed window + freq map |
| 424 | Longest Repeating Character Replacement | Medium | Window + max count trick |
| 239 | Sliding Window Maximum | Hard | Monotonic deque |
| 76 | Minimum Window Substring | Hard | Variable + two freq maps |
→ Evolution: Fixed → Variable → Variable+FreqMap → MonoDeque Window

## 2.6 Binary Search
| # | Problem | Level | Pattern Insight |
|---|---|---|---|
| 704 | Binary Search | Easy | Exact match |
| 34 | First and Last Position | Medium | Lower + Upper bound |
| 33 | Search in Rotated Sorted Array | Medium | Identify sorted half |
| 74 | Search 2D Matrix | Medium | Flatten matrix to 1D |
| 875 | Koko Eating Bananas | Medium | BS on answer |
| 410 | Split Array Largest Sum | Hard | BS on answer + greedy check |
→ Evolution: Exact → Bounds → Rotated → Matrix → Answer Space → Answer+Greedy

## 6.2 Tree DFS
| # | Problem | Level | Pattern Insight |
|---|---|---|---|
| 144 | Binary Tree Preorder | Easy | Root→Left→Right |
| 104 | Max Depth | Easy | Postorder height |
| 543 | Diameter | Medium | Postorder + global var |
| 112 | Path Sum II | Medium | DFS + path tracking |
| 297 | Serialize/Deserialize | Hard | Preorder + null markers |
| 124 | Binary Tree Max Path Sum | Hard | Postorder + global sum |
→ Evolution: Traversal → Height → Diameter → Path Sum → Serialize → Max Path

## 9C BFS + Multi-Source BFS
| # | Problem | Level | Pattern Insight |
|---|---|---|---|
| 111 | Min Depth | Easy | BFS level count |
| 994 | Rotting Oranges | Medium | Multi-source BFS |
| 127 | Word Ladder | Hard | BFS on implicit graph |
| 126 | Word Ladder II | Hard | BFS + backtrack paths |
→ Evolution: Single-source BFS → Multi-Source BFS → BFS on implicit graph

## 9D.5 Union-Find
| # | Problem | Level | Pattern Insight |
|---|---|---|---|
| 547 | Number of Provinces | Medium | Basic union-find |
| 684 | Redundant Connection | Medium | Cycle detection via UF |
| 200 | Number of Islands | Medium | UF or DFS |
| 721 | Accounts Merge | Hard | UF on emails |
| 305 | Number of Islands II | Hard | Dynamic UF |
→ Evolution: Basic UF → Cycle Detection → Dynamic UF → Weighted UF

## 10.5 0/1 Knapsack
| # | Problem | Level | Pattern Insight |
|---|---|---|---|
| 416 | Partition Equal Subset Sum | Medium | Knapsack as subset-sum |
| 494 | Target Sum | Medium | +/- assignment = knapsack |
| 1049 | Last Stone Weight II | Hard | Minimize difference = knapsack |
→ Evolution: 0/1 Knapsack → Subset Sum → Count ways → Minimize difference

## 10.7 LCS
| # | Problem | Level | Pattern Insight |
|---|---|---|---|
| 1143 | LCS | Medium | Classic 2D DP |
| 583 | Delete Operation for Two Strings | Medium | LCS variant |
| 712 | Min ASCII Delete Sum | Medium | LCS with costs |
| 72 | Edit Distance | Hard | LCS generalized |
→ Evolution: LCS → LCS with constraints → Edit Distance → Distinct Subsequences

---

# SECTION 6: REVISION STRATEGY

## Per-Chapter Revision (after each part)
1. Read only the **Revision Box** at end of each subtopic.
2. Cover the template and write it from memory.
3. Trace one dry run from memory.

## Weekly Revision Cycle
| Day | Focus |
|---|---|
| Day 1 | Parts 1–4 Revision Sheets |
| Day 2 | Parts 5–7 Revision Sheets |
| Day 3 | Parts 8–9 Revision Sheets |
| Day 4 | Parts 10–11 Revision Sheets |
| Day 5 | Appendix A — Write templates from memory |
| Day 6 | Solve 3 unseen medium problems |
| Day 7 | Full Pattern Comparison Table + Master Cheat Sheet |

## 3-Hour Pre-Interview Cram (Part 13.6 expansion)
| Time | Action |
|---|---|
| 0:00–0:30 | Read Part 13.5 Master Cheat Sheet (Pattern × Signal × Complexity) |
| 0:30–1:00 | Mentally trace: DFS, BFS, Dijkstra, Mono-Stack, Two Pointers templates |
| 1:00–1:30 | Read Parts 2+4 Revision Sheets (Arrays, Strings, Stack) |
| 1:30–2:00 | Read Parts 6+9 Revision Sheets (Trees, Graphs) |
| 2:00–2:30 | Read Part 10 Revision Sheet (DP patterns) |
| 2:30–3:00 | Read Part 13.7 Company-Specific Patterns for your target company |

---

# SECTION 7: VALIDATION TABLE — EXACTLY 200 PAGES

| # | Part | Subtopics | Problems | Revision | Diagrams/Dry-Runs | Total |
|---|---|---|---|---|---|---|
| 0 | Orientation | 1.5 | 0 | 0.5 | 1.0 | **3.0** |
| 1 | Foundations | 6.0 | 0 | 1.0 | 3.0 | **10.0** |
| 2 | Arrays/Strings/Search | 16.5 | 5.5 | 3.0 | 5.0 | **30.0** |
| 3 | Linked Lists | 4.5 | 1.5 | 1.0 | 1.0 | **8.0** |
| 4 | Stack/Queue/Mono | 6.5 | 2.5 | 1.0 | 2.0 | **12.0** |
| 5 | Recursion/Backtracking | 7.0 | 2.5 | 0.5 | 3.0 | **13.0** |
| 6 | Trees | 11.0 | 3.0 | 2.0 | 4.0 | **20.0** |
| 7 | Heap | 4.5 | 1.5 | 1.0 | 1.0 | **8.0** |
| 8 | Trie | 5.5 | 1.5 | 1.0 | 1.0 | **9.0** |
| 9 | Graphs | 13.5 | 3.5 | 2.0 | 6.0 | **25.0** |
| 10 | DP | 13.0 | 4.0 | 2.0 | 3.0 | **22.0** |
| 11 | Greedy | 4.5 | 1.5 | 1.5 | 0.5 | **8.0** |
| 12 | Staff Structures | 6.0 | 1.0 | 0 | 1.0 | **8.0** |
| 13 | Interview Meta | 7.0 | 0 | 0 | 1.0 | **8.0** |
| A | Appendix A Templates | 13.0 | 0 | 0 | 3.0 | **16.0** |
| | **TOTAL** | **120.0** | **28.0** | **16.5** | **35.5** | **200.0** ✓ |

> **Validation:** 120.0 + 28.0 + 16.5 + 35.5 = **200.0** ✓
> Every page has exactly one owner. No page is unaccounted for.

---

# GENERATION ORDER FOR HTML CHAPTERS

When generating HTML from this blueprint, follow this strict order:

```
Step 1:  Appendix A (freeze template numbering first — all cross-refs depend on it)
Step 2:  Part 0 (Orientation — sets up all references used in other parts)
Step 3:  Part 1 (Foundations — prerequisite for all)
Step 4:  Part 2 (Arrays/Strings/Search)
Step 5:  Part 3 (Linked Lists)
Step 6:  Part 4 (Stack/Queue/Mono)
Step 7:  Part 5 (Recursion/Backtracking)
Step 8:  Part 6 (Trees)
Step 9:  Part 7 (Heap)
Step 10: Part 8 (Trie)
Step 11: Part 9 (Graphs)
Step 12: Part 10 (DP)
Step 13: Part 11 (Greedy)
Step 14: Part 12 (Staff Structures)
Step 15: Part 13 (Interview Meta — last, references all prior parts)
```

Each HTML chapter must:
- Reference the exact Appendix A template numbers
- Link back to prerequisite parts
- Follow the 20-block teaching flow defined in Section 4
- Use the problem progressions defined in Section 5
- End with a Revision Box matching the strategy in Section 6

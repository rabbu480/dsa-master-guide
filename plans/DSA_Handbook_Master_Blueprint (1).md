# MASTER BLUEPRINT
## The Complete FAANG/Staff-Level Java DSA Engineering Handbook
### Target: ~200 A4 pages · Java only · Zero → Staff Engineer

---

## 0. DESIGN PHILOSOPHY (applies to every module below)

- **Dependency-ordered**: nothing is used before it is taught.
- **Every module follows the same 26-node tree** (shown once here, applied to every topic):

```
Topic
├── Why                         (motivation, real-world/interview relevance)
├── Learning Objective          (what you must be able to DO after this page)
├── Prerequisites               (exact prior topics required)
├── Mental Model                (one clean metaphor/picture)
├── Core Concepts                (the 3–6 ideas that define the topic)
├── Internal Working            (what happens under the hood, step by step)
├── Memory Layout                (how it sits in memory / object graph)
├── Construction                  (how it's built from raw input)
├── Input Formats                 (how FAANG problems typically hand you the data)
├── Output Formats                 (what you're expected to return)
├── Conversions                     (X → Y representations, e.g. tree→array, matrix→graph)
├── Helper Data Structures            (stack, queue, heap, map, etc. it leans on)
├── Helper Arrays                      (visited[], dist[], parent[], indeg[], dp[], etc.)
├── Helper Templates                    (reusable skeleton before language-specific code)
├── Java Templates                       (copy-paste-safe canonical Java code)
├── Complexity                            (time/space, best/avg/worst, per operation)
├── Pattern Recognition                    (keyword → technique mapping)
├── Decision Tree                           (interviewer says X → do Y)
├── Debugging                                (how this breaks, how to trace it)
├── Common Mistakes                           (ranked by frequency in real interviews)
├── Interview Questions                        (canonical + follow-up variants)
├── Follow Ups                                  (what a Staff-level interviewer asks next)
├── AHA Moments                                  (deep insights that unlock understanding)
├── Problem Roadmap: Easy / Medium / Hard          (ordered practice ladder)
├── Revision                                        (condensed re-read, 60 seconds)
└── Cheat Sheet                                      (one glance, exam-day reference)
```

- **Page budgets below are per-topic**, sized to fit this 26-node tree at handbook density (dense cards/tables/diagrams, not prose).
- Topics marked **[CORE]** are load-bearing — every later part depends on them.
- Topics marked **[STAFF]** are added specifically for Staff-level depth (system-adjacent DSA, advanced data structures).

---

## PART-LEVEL PAGE BUDGET (Total ≈ 200 pages)

| Part | Title | Pages | Cumulative |
|---|---|---|---|
| 0 | Orientation & How to Use This Book | 4 | 4 |
| 1 | Complexity, Math & Bit Foundations | 10 | 14 |
| 2 | Arrays, Strings & Searching | 30 | 44 |
| 3 | Linked Lists | 10 | 54 |
| 4 | Stacks, Queues & Monotonic Structures | 10 | 64 |
| 5 | Recursion & Backtracking | 12 | 76 |
| 6 | Trees (incl. Segment Tree / BIT) | 24 | 100 |
| 7 | Heaps & Priority Queues | 8 | 108 |
| 8 | Trie | 12 | 120 |
| 9 | Graphs | 30 | 150 |
| 10 | Dynamic Programming | 26 | 176 |
| 11 | Greedy Algorithms | 8 | 184 |
| 12 | Staff-Level Advanced Structures & Design-Adjacent DSA | 10 | 194 |
| 13 | Interview Meta-Layer & Master Revision | 6 | 200 |

---

## PART 0 — ORIENTATION (4 pages) [CORE]

**Prerequisites:** none — this is page zero.

```
0.1  How This Book Works             (1 pg)  — the 26-node tree, box color system, how to re-read in 60s
0.2  Java Environment & Idioms       (1 pg)  — collections cheat sheet, autoboxing traps, comparator syntax
0.3  Complexity Notation Primer      (1 pg)  — Big-O/Θ/Ω, amortized cost, why interviewers ask "worst case"
0.4  How To Practice With This Book  (1 pg)  — spaced repetition plan, roadmap-following order, mock-interview loop
```
**AHA seed:** "Every data structure in this book is just an array or a pointer graph wearing a costume." Everything downstream reduces to these two primitives — this is the thesis of the whole handbook.

---

## PART 1 — COMPLEXITY, MATH & BIT FOUNDATIONS (10 pages) [CORE]

**Prerequisites:** Part 0.
**Why this comes first:** every later structure's complexity proof and every bit-trick (Trie's Bit-Trie, DP's bitmask, Graph's XOR shortest path) depends on this.

```
1.1  Big-O / Big-Θ / Big-Ω formally           (1 pg)
1.2  Recurrences & the Master Theorem (intuition, not proof)  (1 pg)
1.3  Amortized Analysis (dynamic array doubling, union-find)   (1 pg)
1.4  Number Theory Basics: GCD/LCM, primes, sieve, modular arithmetic  (2 pg)
1.5  Combinatorics for interviews: nCr, factorial tricks, Pascal's triangle  (1 pg)
1.6  Bit Manipulation Core: AND/OR/XOR/NOT/shifts, masks, popcount  (2 pg)
1.7  Bit Manipulation Patterns: subsets via bitmask, Kernighan's bit trick, XOR-swap, single-number family  (2 pg)
```
Each of the 7 sub-topics gets the FULL 26-node tree at reduced page-fraction (dense single-page cards). Bit manipulation (1.6–1.7) is flagged **[CORE]** — it is a hard prerequisite for: Trie §8 (Bit Trie, Maximum XOR), DP §10 (bitmask DP), Graph §9 (XOR shortest path variants).

**Problem Roadmap (Part 1):**
- Easy: Number of 1 Bits, Counting Bits, Power of Two
- Medium: Single Number II/III, Subsets via bitmask, GCD of Strings
- Hard: Maximum XOR of two numbers (bridges into Part 8 Bit Trie)

---

## PART 2 — ARRAYS, STRINGS & SEARCHING (30 pages) [CORE]

**Prerequisites:** Part 1 (complexity, bit basics for coordinate compression / difference arrays).

### 2A. Arrays Core (12 pages)
Full 26-node tree applied to each, at sub-page density:
```
2A.1  Traversal & Invariants                (1 pg)
2A.2  Insertion / Deletion (in-place shifting cost)  (1 pg)
2A.3  Reverse (in-place, recursive, two-pointer)     (1 pg)
2A.4  Rotation (reversal algorithm, cyclic replacement) (1 pg)
2A.5  Prefix Sum                              (1 pg)
2A.6  Suffix Sum                              (1 pg)
2A.7  Difference Array (range update in O(1))   (1 pg)
2A.8  Coordinate Compression                     (1 pg)
2A.9  Matrix Traversal Patterns (spiral, diagonal, transpose, rotate 90°) (2 pg)
2A.10 Simulation Problems (game of life, snake, etc.) (1 pg)
2A.11 Arrays → Pattern Roadmap (map every array trick to a keyword) (1 pg)
```

### 2B. Two Pointers & Sliding Window (6 pages) [CORE]
**Prerequisites:** 2A.1–2A.3.
```
2B.1  Two Pointers — Opposite Direction (pair sum, container with most water) (2 pg)
2B.2  Two Pointers — Same Direction / Fast-Slow on arrays (remove duplicates) (1 pg)
2B.3  Sliding Window — Fixed Size                (1 pg)
2B.4  Sliding Window — Variable Size (expand/shrink invariant) (2 pg)
```
**Decision Tree seed:** "contiguous subarray/substring + condition on sum/count/distinct" → sliding window; "sorted array + pair/triplet target" → two pointers.

### 2C. Binary Search (5 pages) [CORE]
**Prerequisites:** 2A.1.
```
2C.1  Binary Search on Sorted Array (exact, lower/upper bound)  (1 pg)
2C.2  Binary Search on Answer (monotonic predicate)             (2 pg)
2C.3  Binary Search on Rotated / Nearly-Sorted Arrays            (1 pg)
2C.4  2D Binary Search (matrix search)                            (1 pg)
```
**AHA:** "Binary search isn't about sorted data — it's about a monotonic true/false predicate over a search space." This reframing unlocks 2C.2, later reused in Part 10 (DP on answer) and Part 9 (Dijkstra-with-binary-search hybrids).

### 2D. Sorting — Relation to Arrays (3 pages)
**Prerequisites:** 2A, recursion (forward reference — flag to revisit after Part 5).
```
2D.1  Comparison Sorts Overview (merge/quick/heap) + when interviewers expect which  (1 pg)
2D.2  Non-Comparison Sorts (counting, radix, bucket) + O(n) conditions               (1 pg)
2D.3  Custom Comparators in Java + stability                                         (1 pg)
```

### 2E. Strings & Pattern Matching (4 pages)
**Prerequisites:** 2A, 2B (sliding window is reused heavily here).
```
2E.1  String Basics (immutability cost, StringBuilder, char[] tricks) (1 pg)
2E.2  Pattern Matching: naive, Rabin-Karp (rolling hash)              (1 pg)
2E.3  KMP (failure function) & Z-Algorithm (conceptual, when to reach for it) (1 pg)
2E.4  Palindromes & Anagrams (expand-around-center, frequency maps)   (1 pg)
```

**Part 2 Problem Roadmap:**
- Easy: Two Sum, Reverse String, Best Time to Buy/Sell Stock, Valid Anagram
- Medium: Product of Array Except Self, 3Sum, Longest Substring Without Repeat, Rotate Image, Search in Rotated Sorted Array
- Hard: Trapping Rain Water, Minimum Window Substring, Median of Two Sorted Arrays

---

## PART 3 — LINKED LISTS (10 pages) [CORE]

**Prerequisites:** Part 2 (pointer/index intuition transfers directly).

```
3.1  Node Design & Memory Model (singly, doubly, circular)       (1 pg)
3.2  Traversal & Dummy Head Pattern                              (1 pg)
3.3  Insertion / Deletion (all positions)                        (1 pg)
3.4  Reversal (iterative, recursive, in groups of k)              (2 pg)
3.5  Fast & Slow Pointers (cycle detection, middle node, Floyd's) (2 pg)
3.6  Merge Patterns (merge two sorted, merge k sorted → bridges to Part 7 Heaps) (2 pg)
3.7  Linked List ↔ Array Conversions & when each representation wins (1 pg)
```
Full 26-node tree per sub-topic. **AHA seed:** "A linked list is a Trie with exactly one child per node." (This foreshadows Part 8.)

**Problem Roadmap:**
- Easy: Reverse Linked List, Merge Two Sorted Lists, Linked List Cycle
- Medium: Add Two Numbers, Remove Nth From End, Reorder List, Copy List with Random Pointer
- Hard: Merge k Sorted Lists, Reverse Nodes in k-Group

---

## PART 4 — STACKS, QUEUES & MONOTONIC STRUCTURES (10 pages) [CORE]

**Prerequisites:** Part 2 (arrays as backing store), Part 3 (linked-list-backed implementations).

```
4.1  Stack: Array vs Linked-List backed, LIFO memory model    (1 pg)
4.2  Queue & Deque: circular buffer memory model               (1 pg)
4.3  Stack Applications: valid parentheses, expression eval, calculator  (2 pg)
4.4  Monotonic Stack (next greater/smaller element family)      (2 pg)
4.5  Monotonic Queue (sliding window maximum)                    (1 pg)
4.6  Design Patterns: Min Stack, Max Stack, Queue-via-two-Stacks (2 pg)
4.7  Stack ↔ Recursion Duality (forward reference to Part 5)     (1 pg)
```
**Decision Tree seed:** "next greater/smaller / span / histogram area" → monotonic stack; "sliding window max/min" → monotonic deque.

**Problem Roadmap:**
- Easy: Valid Parentheses, Implement Queue using Stacks, Baseball Game
- Medium: Daily Temperatures, Next Greater Element II, Min Stack, Evaluate RPN
- Hard: Largest Rectangle in Histogram, Trapping Rain Water (stack variant), Sliding Window Maximum

---

## PART 5 — RECURSION & BACKTRACKING (12 pages) [CORE]

**Prerequisites:** Part 4.7 (stack/recursion duality), Part 2A (arrays as state).
**Why here:** Trees, Tries, DFS-on-graphs, and DP all require fluent recursion before they can be taught — this must land before Part 6.

```
5.1  Recursion Fundamentals: call stack, base case, stack frame ownership of locals (2 pg)
5.2  Recursion Tree Visualization & Manual Tracing                              (1 pg)
5.3  Tail Recursion vs Head Recursion & Java's lack of TCO                       (1 pg)
5.4  Backtracking Framework: choose → explore → un-choose                        (2 pg)
5.5  Permutations & Combinations (with/without duplicates)                        (2 pg)
5.6  Subsets (bitmask vs recursive, ties back to Part 1.7)                        (1 pg)
5.7  Constraint Satisfaction: N-Queens, Sudoku Solver                              (2 pg)
5.8  Pruning Strategies (early termination, memo-assisted backtracking → forward ref to Part 10) (1 pg)
```
**AHA:** "Backtracking = DFS + undo. The 'undo' step must fire on unwind, never before recursing deeper." (This exact insight is reused verbatim in Part 8's Trie+Backtracking and Part 9's Graph DFS.)

**Problem Roadmap:**
- Easy: Fibonacci (recursive), Power of Two (recursive)
- Medium: Permutations, Subsets, Combination Sum, Generate Parentheses
- Hard: N-Queens, Sudoku Solver, Word Search (forward ref, revisited fully in Part 8)

---

## PART 6 — TREES (24 pages) [CORE]

**Prerequisites:** Part 5 (recursion/backtracking), Part 4 (stack for iterative traversal), Part 7 forward-linked for heap-as-tree.

### 6A. Binary Trees Foundations (8 pages)
```
6A.1  Node Design & Memory Layout (pointer graph, not array — contrast with 6D) (1 pg)
6A.2  Traversals: preorder/inorder/postorder — recursive AND iterative (stack-based) (2 pg)
6A.3  Level-Order Traversal (BFS on trees, queue-based)                            (1 pg)
6A.4  Tree Construction (from traversals, from arrays, from strings)              (2 pg)
6A.5  Views: left/right/top/bottom view, boundary traversal                        (2 pg)
```

### 6B. Binary Search Trees (4 pages)
```
6B.1  BST Property & Internal Working (insert/search/delete)  (2 pg)
6B.2  BST Validation & In-order Monotonicity                    (1 pg)
6B.3  BST → Sorted Array Conversions (both directions)          (1 pg)
```

### 6C. Balanced Trees Overview (3 pages)
```
6C.1  Why Balance Matters (worst-case degrade to linked list)  (1 pg)
6C.2  AVL Trees — rotations conceptual overview (not full impl) (1 pg)
6C.3  Red-Black Trees — how Java's TreeMap uses them (conceptual) (1 pg)
```

### 6D. Tree Metrics & Patterns (4 pages) [CORE]
```
6D.1  Height & Diameter (post-order aggregation pattern)   (1 pg)
6D.2  Path Sum Family (root-to-leaf, any-path, max path sum)  (1 pg)
6D.3  Lowest Common Ancestor (recursive, binary lifting preview → forward ref Part 9) (1 pg)
6D.4  Tree DP (house robber III style — forward ref to Part 10)  (1 pg)
```

### 6E. Serialization & Advanced Structures (5 pages) [STAFF]
```
6E.1  Serialization / Deserialization (preorder + null markers)  (1 pg)
6E.2  Segment Tree (construction, range query, point update)      (2 pg)
6E.3  Binary Indexed Tree / Fenwick Tree (prefix-sum in O(log n))  (2 pg)
```
**AHA:** "A segment tree is a binary tree wearing an array's clothing — every node's index math (2i, 2i+1) replaces pointers." Directly reuses Part 1's bit intuition and Part 2A's array intuition.

**Problem Roadmap (Part 6):**
- Easy: Max Depth, Invert Binary Tree, Same Tree
- Medium: Validate BST, Kth Smallest in BST, Diameter, Construct from Preorder/Inorder, LCA of BST
- Hard: Serialize/Deserialize, Binary Tree Max Path Sum, Range Sum Query (Segment Tree/BIT)

---

## PART 7 — HEAPS & PRIORITY QUEUES (8 pages) [CORE]

**Prerequisites:** Part 6A (tree shape), Part 2A (array-backed structure — heap is stored as an array).

```
7.1  Heap Property & Array-Based Memory Layout (2i+1, 2i+2 indexing)  (1 pg)
7.2  Heapify (build-heap in O(n)) & Sift-Up / Sift-Down               (1 pg)
7.3  Java PriorityQueue: comparator gotchas, min-heap vs max-heap idiom (1 pg)
7.4  Top-K Pattern (heap of size k)                                     (1 pg)
7.5  Two-Heap Pattern (running median)                                   (1 pg)
7.6  K-Way Merge Pattern (merge k sorted lists/arrays — reuses Part 3.6)  (1 pg)
7.7  Heap vs BST vs Sorted Array — when each wins                         (1 pg)
7.8  Problem Roadmap page                                                  (1 pg)
```
**AHA:** "A heap is the array from Part 2 pretending to be the tree from Part 6 — no pointers, just index arithmetic." This is the same insight pattern as Segment Trees (6E.2), stated for reinforcement.

**Problem Roadmap:**
- Easy: Kth Largest Element in a Stream, Last Stone Weight
- Medium: Top K Frequent Elements, K Closest Points to Origin, Task Scheduler
- Hard: Find Median from Data Stream, Merge k Sorted Lists, Smallest Range Covering K Lists

---

## PART 8 — TRIE (12 pages) [CORE]

**Prerequisites:** Part 5 (recursion/backtracking — required for wildcard DFS and grid+Trie), Part 3 (linked-node mental model), Part 1.6–1.7 (bit tricks — required for Bit Trie).

```
8.1  Node Design (children array vs HashMap, isWord flag, memory layout)  (1 pg)
8.2  Insert / Search / StartsWith (canonical templates, iterative)         (1 pg)
8.3  Delete (concept): recursive prune-on-unwind                            (1 pg)
8.4  Wildcard Search ('.' matching via DFS, recursion tree)                  (2 pg)
8.5  Trie + Backtracking (Word Search II: grid DFS, node.word=null dedup)     (2 pg)
8.6  Autocomplete / Search Suggestions (prefix walk + sorted DFS collect)      (1 pg)
8.7  Bit Trie (binary representation as trie edges, 0/1 children)              (2 pg)
8.8  Maximum XOR of Two Numbers (Bit Trie applied — greedy bit-by-bit)          (1 pg)
8.9  Problem Roadmap + Cheat Sheet                                               (1 pg)
```
Each sub-topic still carries the full 26-node tree (this handbook's earlier 8-page "Trie standalone" edition maps 1:1 onto 8.1–8.6 above; 8.7–8.8 are the **[STAFF]** extension unique to this master edition).

**Decision Tree seed:** "dictionary/prefix" → 8.2 · "wildcard/unknown char" → 8.4 · "grid + word list" → 8.5 · "autocomplete/top-k suggestions" → 8.6 · "maximum XOR / bitwise prefix" → 8.7–8.8.

**Problem Roadmap:**
- Easy: Implement Trie (208), Longest Common Prefix
- Medium: Replace Words (648), Design Add and Search Words (211), Search Suggestions System (1268), Map Sum Pairs
- Hard: Word Search II (212), Maximum XOR of Two Numbers in an Array, Palindrome Pairs

---

## PART 9 — GRAPHS (30 pages) [CORE]

**Prerequisites:** Part 5 (recursion/DFS), Part 4 (queue for BFS), Part 7 (heap for Dijkstra/Prim), Part 6D.3 (LCA groundwork for advanced graph-tree hybrids).
**Why largest module:** graphs generalize trees, linked lists, and grids — nearly every prior structure is a special case of a graph, so this module intentionally revisits and unifies them.

### 9A. Representation Layer (6 pages)
```
9A.1  Edge List                       (1 pg)
9A.2  Adjacency Matrix                (1 pg)
9A.3  Adjacency List                  (1 pg)
9A.4  Grid Graph (2D grid as implicit graph)  (1 pg)
9A.5  Tree → Graph, Node Graph (LeetCode-style Node class)  (1 pg)
9A.6  Reverse Graph & Directed vs Undirected, Weighted vs Unweighted, Sparse vs Dense (1 pg)
```
**Conversion table required here:** Edge List ↔ Adjacency Matrix ↔ Adjacency List, with time/space tradeoffs per representation and "when interviewer's input format dictates which to build."

### 9B. Helper Arrays (3 pages) [CORE — referenced by every algorithm below]
```
9B.1  Visited Array, Parent Array (path reconstruction)       (1 pg)
9B.2  Distance Array, Cost Array                                (1 pg)
9B.3  Direction Array (grid dx/dy), Indegree / Outdegree Arrays   (1 pg)
```

### 9C. Traversal (5 pages)
```
9C.1  DFS (recursive + iterative w/ explicit stack)     (2 pg)
9C.2  BFS (queue-based, level tracking)                  (1 pg)
9C.3  Multi-Source BFS (rotting oranges pattern)          (1 pg)
9C.4  DFS vs BFS Decision Matrix                            (1 pg)
```

### 9D. Structural Algorithms (6 pages)
```
9D.1  Cycle Detection — Directed (colors/recursion stack) & Undirected (parent tracking)  (2 pg)
9D.2  Topological Sort (Kahn's BFS + DFS-based)                                            (2 pg)
9D.3  Union-Find / Disjoint Set (path compression + union by rank, with cycle detection)   (2 pg)
```

### 9E. Shortest Path Family (6 pages)
```
9E.1  Dijkstra (heap-based, from Part 7)         (2 pg)
9E.2  Bellman-Ford (negative edges, relaxation)   (2 pg)
9E.3  Floyd-Warshall (all-pairs, DP-on-graph — forward ref Part 10) (2 pg)
```

### 9F. Minimum Spanning Tree (2 pages)
```
9F.1  Prim's Algorithm (heap-based, grows from a node)    (1 pg)
9F.2  Kruskal's Algorithm (sorted edges + Union-Find)      (1 pg)
```

### 9G. Graph Problem Roadmap & Pattern Recognition (2 pages)
```
9G.1  Master Decision Tree: keyword → representation → algorithm  (1 pg)
9G.2  Full Problem Roadmap: Easy/Medium/Hard                        (1 pg)
```

**AHA (Part 9 capstone):** "DFS-with-backtracking (Part 5), Trie traversal (Part 8), and Graph DFS (9C.1) are the SAME four-line skeleton: check base/visited → mark → recurse on neighbors/children → (optionally) unmark. Once you see this, every tree/trie/graph DFS problem becomes a fill-in-the-blank."

**Problem Roadmap:**
- Easy: Find if Path Exists, Flood Fill, Number of Provinces
- Medium: Number of Islands, Course Schedule, Rotting Oranges, Clone Graph, Network Delay Time
- Hard: Word Ladder, Alien Dictionary, Swim in Rising Water, Min Cost to Connect All Points

---

## PART 10 — DYNAMIC PROGRAMMING (26 pages) [CORE]

**Prerequisites:** Part 5 (recursion/recursion tree), Part 2A (arrays as DP tables), Part 9E.3 (Floyd-Warshall as DP-on-graph, cross-referenced).

**Universal Framework — every DP problem in this book is taught through:**
```
SC  → State + Choice            (what varies? what do I decide at each step?)
↓
RBR → Recurrence + Base Case + Recursion  (write the brute-force recursive relation first)
↓
MTS → Memoization → Tabulation → Space Optimization  (the only 3-step upgrade path allowed)
```

```
10.1  The SC→RBR→MTS Framework, worked once in full detail (Fibonacci → Climbing Stairs) (2 pg)
10.2  1D DP (House Robber, Climbing Stairs variants)         (2 pg)
10.3  2D DP on Grids (Unique Paths, Min Path Sum)             (2 pg)
10.4  Knapsack Family (0/1, unbounded, subset-sum, partition) (3 pg)
10.5  Longest Common Subsequence / Edit Distance Family        (3 pg)
10.6  Interval DP (Matrix Chain, Burst Balloons)                (2 pg)
10.7  Digit DP (conceptual + template)                            (2 pg)
10.8  Bitmask DP (TSP-style, reuses Part 1.7)                      (2 pg)
10.9  Tree DP (reuses 6D.4, House Robber III, Diameter-as-DP)       (2 pg)
10.10 DP on Graphs (reuses 9E.3, Longest Increasing Path)            (2 pg)
10.11 State Machine DP (Buy/Sell Stock family with cooldown/fee)      (2 pg)
10.12 Pattern Recognition Master Table + Decision Tree                  (2 pg)
```
**AHA:** "Every 'optimize/count/can-you' problem over a sequence/grid/graph is DP if — and only if — you can define an SC (state+choice) where subproblems overlap. If subproblems DON'T overlap, it's Divide & Conquer, not DP; if there's no 'choice', it's just a formula."

**Problem Roadmap:**
- Easy: Climbing Stairs, House Robber, Min Cost Climbing Stairs
- Medium: Coin Change, LCS, Unique Paths, Partition Equal Subset Sum, Longest Increasing Subsequence
- Hard: Edit Distance, Burst Balloons, Regular Expression Matching, Longest Increasing Path in Matrix

---

## PART 11 — GREEDY ALGORITHMS (8 pages)

**Prerequisites:** Part 2D (sorting), Part 10 (contrast greedy vs DP — greedy is taught AFTER DP specifically so the "why greedy fails here, DP works" comparison lands).

```
11.1  Greedy Mental Model & the Exchange Argument (proof sketch, not full proof)  (2 pg)
11.2  Interval Scheduling / Activity Selection                                     (2 pg)
11.3  Greedy on Arrays (Jump Game, Gas Station)                                     (2 pg)
11.4  Greedy vs DP Decision Tree (when greedy's local choice is provably optimal)     (2 pg)
```
**AHA:** "Greedy is DP with a proof that you never need to look back — the moment you can't prove that, fall back to Part 10's SC→RBR→MTS."

**Problem Roadmap:**
- Easy: Assign Cookies, Lemonade Change
- Medium: Jump Game, Gas Station, Non-overlapping Intervals, Partition Labels
- Hard: Candy, Minimum Number of Taps to Water a Garden

---

## PART 12 — STAFF-LEVEL ADVANCED STRUCTURES & DESIGN-ADJACENT DSA (10 pages) [STAFF]

**Prerequisites:** Parts 6–10 in full (this module composes prior structures rather than introducing new primitives).

```
12.1  LRU Cache (HashMap + Doubly Linked List composition)          (2 pg)
12.2  LFU Cache (frequency buckets + LRU-per-bucket)                 (2 pg)
12.3  Rate Limiter Data Structures (sliding window counters, token bucket as a DSA problem) (2 pg)
12.4  Sparse Table / Sqrt Decomposition (static range queries, contrast with Segment Tree 6E.2) (2 pg)
12.5  Trie + Design: Autocomplete System at Scale (composing 8.6 + 7.4 top-K)           (2 pg)
```
**AHA:** "At Staff level, the interview stops testing 'do you know a structure' and starts testing 'can you compose two structures to satisfy two constraints at once' (e.g., O(1) access AND O(1) recency)."

**Problem Roadmap:**
- Medium: Design HashMap, Design Circular Queue, Insert Delete GetRandom O(1)
- Hard: LRU Cache, LFU Cache, Design Search Autocomplete System, Design Twitter

---

## PART 13 — INTERVIEW META-LAYER & MASTER REVISION (6 pages)

**Prerequisites:** the entire book.

```
13.1  Master Pattern Index — every keyword across all 13 parts mapped to its technique (2 pg)
13.2  Cross-Topic AHA Compendium — every "AHA" callout from Parts 1–12, collected  (1 pg)
13.3  Mock Interview Communication Templates (clarify → approach → complexity → code → test) (1 pg)
13.4  45-Minute Interview Timing Budget (how many minutes per phase, by difficulty)  (1 pg)
13.5  One-Page Master Cheat Sheet (every template, one line each, final page of the book) (1 pg)
```

---

## DEPENDENCY GRAPH (topological order — build in this exact sequence)

```
Part 0 (Orientation)
   ↓
Part 1 (Math/Bits) ────────────────────────────┐
   ↓                                            │ (feeds Trie 8.7-8.8, DP 10.8)
Part 2 (Arrays/Strings/2-Ptr/BinSearch/Sort) ───┼───────────────┐
   ↓                                            │               │(feeds Heap 7, Segment Tree 6E)
Part 3 (Linked Lists)                            │               │
   ↓                                            │               │
Part 4 (Stacks/Queues) ── feeds recursion§5.7 ──┘               │
   ↓                                                             │
Part 5 (Recursion/Backtracking) ── feeds Trees§6, Trie§8, Graph§9│
   ↓                                                             │
Part 6 (Trees, incl. Segment Tree/BIT) ◄─────────────────────────┘
   ↓
Part 7 (Heaps) ── feeds Graph§9E (Dijkstra/Prim)
   ↓
Part 8 (Trie) ── feeds Part 9 (DFS-skeleton reuse), Part 1 (bit trie)
   ↓
Part 9 (Graphs) ── feeds Part 10 (DP-on-graph 10.10, Floyd-Warshall→DP)
   ↓
Part 10 (Dynamic Programming)
   ↓
Part 11 (Greedy) ── explicitly contrasted against Part 10
   ↓
Part 12 (Staff-Level Composition) ── requires Parts 3,6,7,8,10 simultaneously
   ↓
Part 13 (Meta-Layer / Master Revision)
```

---

## CROSS-CUTTING SPECIAL REQUIREMENTS (as specified) — WHERE THEY LIVE

| Requirement | Location |
|---|---|
| Edge List / Adjacency Matrix / Adjacency List / Grid Graph / Tree→Graph / Node Graph / Reverse Graph / Directed / Undirected / Weighted / Unweighted / Sparse / Dense | Part 9A (9A.1–9A.6) |
| Visited / Parent / Distance / Cost / Direction / Indegree / Outdegree arrays | Part 9B |
| DFS / BFS / Multi-Source BFS | Part 9C |
| Cycle Detection / Topological Sort / Union-Find | Part 9D |
| Dijkstra / Bellman-Ford / Floyd-Warshall | Part 9E |
| Prim / Kruskal | Part 9F |
| Tree Traversal / Construction / DFS / BFS / BST / AVL overview / Balanced / Diameter / Height / Path Sum / LCA / Serialization / Deserialization / Tree Patterns | Part 6A–6E |
| Array Traversal / Insertion / Deletion / Reverse / Rotation / Prefix / Suffix / Difference Array / Coordinate Compression / Matrix / Simulation / Searching / Sorting relation | Part 2A, 2C, 2D |
| DP: SC → RBR → MTS framework, applied to every DP problem | Part 10 (framework stated in 10.1, reapplied in every subsequent sub-topic) |
| Trie: Node Design / Insert / Search / StartsWith / Delete / Bit Trie / Wildcard / Autocomplete / Word Search / Maximum XOR | Part 8 (8.1–8.8) |

---

## HOW ANOTHER AI SHOULD USE THIS BLUEPRINT

1. Generate **one Part at a time**, in the exact dependency order above — never skip ahead.
2. For every numbered sub-topic (e.g. `9C.1 DFS`), instantiate the **full 26-node tree** from Section 0, at the page-fraction budget given.
3. Reuse the **AHA lines already written for each Part** verbatim where noted — they are cross-referenced deliberately (e.g. the DFS-skeleton AHA in Part 9 must literally reuse Part 5's and Part 8's wording) so the reader recognizes the pattern across modules.
4. Every Problem Roadmap (Easy/Medium/Hard) must cite real, well-known problems — do not invent problems.
5. Maintain the visual/box design system (color-coded AHA/Mistake/Tip/Template/Complexity cards, icons, print-safe A4 CSS) established in the standalone Trie handbook edition — this blueprint assumes that same visual system scales across all 13 parts.
6. Total output must land at ≈190–200 A4 pages; use the per-part and per-topic page budgets above as hard ceilings, not suggestions — if a topic overflows its budget, cut prose, not diagrams/tables/code.

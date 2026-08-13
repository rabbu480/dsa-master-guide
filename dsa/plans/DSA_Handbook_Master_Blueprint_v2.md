# MASTER BLUEPRINT — v2
## The Complete FAANG/Staff-Level Java DSA Engineering Handbook
### Target: ~195–200 A4 pages · Java only · Zero → Staff Engineer
### Supersedes v1 — incorporates: mentoring teaching flow, template appendix, mandatory comparisons, graph construction pipeline, problem-evolution chains, FAANG roadmap tags, print-safe styling.

---

## 0. WHAT CHANGED SINCE v1 (read this first)

| # | Change | Why |
|---|---|---|
| 1 | New 20-node **teaching flow** replaces the old 26-node reference tree | Code now comes near the end, not the start. Intuition is built before syntax. |
| 2 | New **Appendix A: Master Template Library** (10 pages) | Templates are defined ONCE, canonically. Chapters *reference* them, never redefine them — this also reclaims pages for teaching. |
| 3 | **Comparison Table** is now a mandatory node in every topic's tree, not an occasional extra | Interviewers constantly ask "why this over that" — the book now always answers it. |
| 4 | Graph module restructured around a strict **pipeline**: Input Format → Conversion → Representation → Helper Arrays → Template Reference → Algorithm | You must never reach for DFS/BFS before the graph is actually built in memory. |
| 5 | **Problem Evolution** is now mandatory per topic — problems are taught as chains, never in isolation | Mirrors how real interview loops escalate (Two Sum → Two Sum II → 3Sum → 4Sum → k-Sum). |
| 6 | **FAANG Roadmap block** added per topic: NeetCode 150 tag, company frequency (Google/Meta/Amazon/Microsoft/Uber), Top 5 must-solve, revision priority | Turns the book into a prioritized study plan, not just a reference. |
| 7 | **Print system locked**: white page background, black body text, high-contrast tables, dark theme reserved *only* for code blocks | Guarantees black-and-white print legibility while keeping code readable. |
| 8 | Page budget rebalanced to ~199 pages after adding the 10-page Template Appendix (savings came from no longer re-printing full template code in every chapter) | Keeps the book inside the 190–200 page ceiling. |

---

## 1. TEACHING FLOW (replaces the v1 26-node tree — apply to EVERY topic in the book)

This is the mandatory reading order for every topic, sized to sub-page density. **Never start with code.**

```
Topic
├── 1.  WHY                        — what breaks / what's slow / what's impossible without this
├── 2.  Problem It Solves           — the concrete pain point, stated as a mini-scenario
├── 3.  Mental Model                 — one clean metaphor a Staff Engineer would sketch on a whiteboard
├── 4.  Visualization                 — the diagram FIRST, before any explanation of mechanics
├── 5.  Internal Working                — what actually happens, step by step, narrated over the diagram
├── 6.  Memory Layout                    — how it actually sits in the JVM (objects/pointers vs contiguous array)
├── 7.  Construction                      — how you actually build one from scratch
├── 8.  Input Conversion                   — how FAANG problems hand you raw input → how you shape it into this structure
├── 9.  Template Reference                  — "see Appendix A, Template #N" — never redefined inline
├── 10. Dry Run                              — a full hand-traced example, every variable shown per step
├── 11. Debugging                             — how this breaks in practice, and how you'd catch it with prints/debugger
├── 12. Common Mistakes                        — ranked by real interview frequency
├── 13. Complexity                              — time/space, best/avg/worst, per operation, WHY (not just what)
├── 14. Comparison Table                         — this structure/algorithm vs its nearest alternative(s) — MANDATORY
├── 15. AHA Moments                               — the 1–3 insights that make this "click" permanently
├── 16. Interview Discussion                       — how to talk through this out loud in 60 seconds
├── 17. Follow-Ups                                  — what a Staff-level interviewer asks once you solve it
├── 18. Problem Evolution                            — the chain this problem belongs to (what changed / why / template reused / what it feeds into)
├── 19. FAANG Roadmap                                 — NeetCode 150 tag · Google/Meta/Amazon/Microsoft/Uber frequency · Top 5 must-solve · revision priority
└── 20. Revision & Cheat Sheet                          — 60-second recap, exam-day one-glance box
```

**Rule:** nodes 9 (Template Reference) and 19 (FAANG Roadmap) are structurally new — they turn every chapter into a pointer into two shared systems (the Template Library and the Roadmap tracker) instead of a self-contained silo.

---

## 2. PRINT & VISUAL SYSTEM (binding constraint on every page generated later)

| Element | Rule |
|---|---|
| Page background | Pure white (#ffffff) — never gray, never dark |
| Body text | Near-black (#1a1a1a+), high contrast, print-safe at 11–12px |
| Tables | High-contrast header row, thin borders, alternating light-gray stripe only (never mid-gray or color-only distinction — must survive black-and-white printing) |
| Color-coded cards (AHA/Mistake/Tip/etc.) | Colors used only as accents (left border + soft tint); all card text remains black so meaning survives grayscale printing |
| Code blocks | The ONE place a dark theme is allowed (dark background, light monospace text) — improves syntax-highlight legibility and visually separates "read this" from "this is copy-paste code" |
| Diagrams | Unicode/HTML only, black lines on white, no image assets |
| Icons | Used as small inline glyphs next to card titles only — never as decoration that carries meaning color alone must not carry |

This system applies uniformly across all 14 parts (13 content parts + Template Appendix) generated later in HTML.

---

## 3. APPENDIX A — MASTER TEMPLATE LIBRARY (10 pages) [NEW — referenced, never re-defined]

Canonical, copy-paste-safe Java, written once. Every chapter's node 9 ("Template Reference") points here by number.

```
A.1   DFS — Recursive                         A.17  Sliding Window (fixed + variable)
A.2   DFS — Iterative (explicit stack)         A.18  Prefix Sum
A.3   Tree DFS (pre/in/post, recursive+iter)    A.19  Difference Array
A.4   Grid DFS (4-dir / 8-dir, visited grid)     A.20  Monotonic Stack
A.5   Graph DFS (adjacency list, visited[])       A.21  Monotonic Queue
A.6   Trie DFS (wildcard + collect-words)          A.22  Heap (min/max idiom, PQ comparator)
A.7   Backtracking DFS (choose/explore/un-choose)   A.23  Union-Find (path compression + rank)
A.8   Memoized DFS (top-down DP)                      A.24  Dijkstra (heap-based)
A.9   BFS (queue-based)                                A.25  Bellman-Ford (edge relaxation)
A.10  Level-Order BFS (level tracking)                   A.26  Prim's Algorithm
A.11  Multi-Source BFS                                     A.27  Kruskal's Algorithm
A.12  Topological Sort — BFS (Kahn's)                        A.28  Segment Tree (build/query/update)
A.13  Binary Search — Exact                                    A.29  Fenwick / BIT (update/prefix query)
A.14  Binary Search — Lower Bound                                A.30  Trie (insert/search/startsWith/delete)
A.15  Binary Search — Upper Bound                                  A.31  Dynamic Programming Skeleton (SC→RBR→MTS, all 3 stages side by side)
A.16  Binary Search on Answer (monotonic predicate)
```

Each template entry gets: signature + full Java code + a 1-line "when to reach for this" + its complexity — **no dry run, no theory** (that lives in the chapter that references it). This appendix is the single source of truth; chapters may show a *problem-specific delta* on top of a template, but never re-paste the base template.

---

## 4. MANDATORY COMPARISON TABLES (node 14 in every relevant topic)

These are non-optional and must appear at the exact chapter listed:

| Comparison | Lives in |
|---|---|
| DFS vs BFS | Part 9C.4 |
| Recursive vs Iterative (DFS/traversal) | Part 5.1 / Part 6A.2 |
| Adjacency List vs Adjacency Matrix vs Edge List | Part 9A (dedicated comparison page) |
| Trie vs HashMap | Part 8 (opening motivation page) |
| BST vs Heap | Part 7.7 |
| Segment Tree vs Fenwick Tree | Part 6E (dedicated comparison page) |
| Memoization vs Tabulation (vs Space-Optimized) | Part 10.1 (inside the SC→RBR→MTS framework page) |
| Sliding Window vs Two Pointers | Part 2B (dedicated comparison page) |
| Prim vs Kruskal | Part 9F (dedicated comparison page) |
| Dijkstra vs Bellman-Ford (vs Floyd-Warshall) | Part 9E (dedicated comparison page) |
| Union-Find vs DFS (for connectivity/cycle detection) | Part 9D.3 |
| Greedy vs DP | Part 11.4 |
| Array vs Linked List (memory/access tradeoffs) | Part 3.7 |
| Stack-based vs Queue-based traversal | Part 4.7 |

Each comparison table uses the same fixed column schema for consistency:
`Aspect | Option A | Option B | (Option C) | When to choose`

---

## 5. GRAPH CONSTRUCTION PIPELINE (Part 9 restructure — mandatory order, never skipped)

No algorithm (DFS/BFS/Dijkstra/etc.) may be taught until the graph actually exists in memory. Every graph sub-module follows this exact pipeline:

```
Input Format          (how the problem hands you the graph: pairs, matrix, strings, grid)
   ↓
Conversion              (raw input → chosen representation, shown as Java code deltas only)
   ↓
Representation           (Edge List / Adjacency List / Adjacency Matrix / Grid / etc.)
   ↓
Helper Arrays              (which of visited/parent/distance/cost/indegree/outdegree/direction/color you need, and why)
   ↓
Template Reference          (pointer into Appendix A — A.5, A.9, A.11, A.12, A.23, A.24...)
   ↓
Algorithm                    (the actual technique, taught via Teaching Flow nodes 1–20)
```

### 9A. Representation Layer (10 pages) — expanded from v1
```
9A.0  Input Formats & Conversion Pipeline (overview page — how to recognize which input format you were given) (1 pg)
9A.1  Edge List                        (1 pg)
9A.2  Adjacency List                   (1 pg)
9A.3  Adjacency Matrix                 (1 pg)
9A.4  Comparison Page — Edge List vs Adjacency List vs Adjacency Matrix (mandatory, see §4) (1 pg)
9A.5  Grid Graph (2D grid as implicit graph, direction arrays introduced here)  (1 pg)
9A.6  Tree → Graph, Node Graph (LeetCode Node class)  (1 pg)
9A.7  Reverse Graph                     (1 pg)
9A.8  Directed vs Undirected Graph       (1 pg)
9A.9  Weighted vs Unweighted, Sparse vs Dense  (1 pg)
```

### 9B. Helper Arrays (4 pages) — now includes color[]
```
9B.1  Visited Array & Parent Array (path reconstruction)         (1 pg)
9B.2  Distance Array & Cost Array                                  (1 pg)
9B.3  Direction Array (grid dx/dy) & Indegree/Outdegree Arrays        (1 pg)
9B.4  Color Array (white/gray/black 3-state DFS coloring for directed-cycle detection) (1 pg)
```
**Decision rule taught here:** *visited[]* alone is enough for undirected connectivity; you need *color[]* the moment the graph is **directed** and you're checking cycles, because "visited but currently on the recursion stack" (gray) is a different state than "fully finished" (black).

### 9C. Traversal (4 pages — shorter than v1: template code lives in Appendix now)
```
9C.1  DFS — concept, dry run, when to reach for it (references A.5) (1 pg)
9C.2  BFS — concept, dry run (references A.9, A.10)                (1 pg)
9C.3  Multi-Source BFS — concept, dry run (references A.11)          (1 pg)
9C.4  Comparison Page — DFS vs BFS (mandatory, see §4)                 (1 pg)
```

### 9D. Structural Algorithms (6 pages)
```
9D.1  Cycle Detection — Directed (color[]) & Undirected (parent[])  (2 pg)
9D.2  Topological Sort — Kahn's (BFS, A.12) + DFS-based               (2 pg)
9D.3  Union-Find (A.23) + Comparison Page: Union-Find vs DFS (§4)      (2 pg)
```

### 9E. Shortest Path Family (7 pages)
```
9E.1  Dijkstra (A.24)                (2 pg)
9E.2  Bellman-Ford (A.25)             (2 pg)
9E.3  Floyd-Warshall (DP-on-graph, forward ref Part 10) (2 pg)
9E.4  Comparison Page — Dijkstra vs Bellman-Ford vs Floyd-Warshall (§4) (1 pg)
```

### 9F. Minimum Spanning Tree (3 pages)
```
9F.1  Prim's Algorithm (A.26)           (1 pg)
9F.2  Kruskal's Algorithm (A.27)        (1 pg)
9F.3  Comparison Page — Prim vs Kruskal (§4) (1 pg)
```

### 9G. Problem Evolution, Roadmap & Pattern Recognition (2 pages)
```
9G.1  Graph Problem Evolution Chains (see §6 below) + Master Decision Tree (1 pg)
9G.2  FAANG Roadmap (NeetCode tags, company frequency, Top 5, revision priority) (1 pg)
```

**Part 9 new total: 32 pages** (was 30 in v1 — the increase is intentional: dedicated representation + comparison pages were mandated).

---

## 6. PROBLEM EVOLUTION CHAINS (node 18 in Teaching Flow — mandatory per topic)

Every chain answers 4 fixed questions at each link: **What changed? Why? Which template is reused? What does it feed into?**

Canonical chains this book commits to (each lives inside its topic's node 18, and is aggregated once more in Part 13):

```
ARRAYS / TWO POINTERS
Two Sum (hashmap) → Two Sum II (sorted, two-pointer) → 3Sum (fix one + two-pointer) → 4Sum (fix two + two-pointer) → k-Sum (recursive generalization)
  Reused template: Two Pointers (A.17-adjacent) · Feeds into: subset-sum-family in Part 10.4

BINARY SEARCH
Binary Search (exact) → Search Insert Position (lower bound) → Search in Rotated Sorted Array (modified predicate) → Find Minimum in Rotated Array → Split Array Largest Sum (binary search ON THE ANSWER)
  Reused template: A.13→A.16 progression · Feeds into: DP-on-answer hybrids in Part 10

DFS / GRAPH
Number of Islands (grid DFS) → Max Area of Island (DFS + aggregation) → Number of Provinces (adjacency matrix DFS) → Course Schedule (directed cycle DFS) → Course Schedule II (DFS + topological order)
  Reused template: A.4 → A.5 → A.12 · Feeds into: Alien Dictionary (topological + tie-breaking)

TRIE
Implement Trie (208) → Replace Words (648, early-stop search) → Design Add and Search Words (211, wildcard DFS) → Word Search II (212, Trie+Backtracking) → Maximum XOR of Two Numbers (Bit Trie)
  Reused template: A.30 → A.6 → A.7 · Feeds into: Search Autocomplete System (Part 12.5)

DYNAMIC PROGRAMMING
Climbing Stairs (1D) → House Robber (1D with choice) → House Robber II (circular constraint) → House Robber III (Tree DP) → Coin Change (unbounded knapsack) → Edit Distance (2D LCS-family)
  Reused template: A.31 (SC→RBR→MTS at every link) · Feeds into: Regular Expression Matching (Hard-tier 2D DP)

SLIDING WINDOW
Best Time to Buy/Sell Stock (single pass) → Longest Substring Without Repeating Characters (variable window) → Minimum Window Substring (variable window + frequency map) → Sliding Window Maximum (monotonic deque)
  Reused template: A.17 → A.21 · Feeds into: Task Scheduler (Part 7 heap + cooldown window)
```

Every other topic's node 18 must build an analogous chain of 3–6 problems using this exact 4-question format — no topic may present problems as an unordered list.

---

## 7. FAANG ROADMAP TAGGING SYSTEM (node 19 in Teaching Flow — mandatory per topic)

Fixed schema applied at the end of every topic and re-aggregated in Part 13:

```
NeetCode 150:      [Yes/No — which category]
Google:            [●●●○○ frequency dots, 1–5]
Meta:              [●●●○○]
Amazon:            [●●●○○]
Microsoft:         [●●●○○]
Uber:              [●●●○○]
Top 5 Must-Solve:  [exact 5 problem names, ordered by ROI]
Revision Priority: [P0 = re-solve weekly / P1 = re-solve monthly / P2 = read-only refresher]
```

Frequency dots are qualitative (derived from well-known public interview-experience aggregation, not scraped live data) and are clearly labeled in the book's intro as *directional guidance*, not exact statistics — this is stated once in Part 0 so every topic page can use the shorthand without re-explaining it.

Part 13 aggregates every topic's roadmap block into one **Master Priority Matrix** (P0 items across the whole book, sorted by company-frequency, single table, 2 pages).

---

## 8. UPDATED PART-LEVEL PAGE BUDGET (Total ≈ 199 pages)

| Part | Title | v1 Pages | v2 Pages | Change |
|---|---|---|---|---|
| 0 | Orientation & How to Use This Book | 4 | 4 | — (now also defines frequency-dot convention) |
| 1 | Complexity, Math & Bit Foundations | 10 | 10 | — |
| 2 | Arrays, Strings & Searching | 30 | 28 | −2 (template code moved to Appendix) |
| 3 | Linked Lists | 10 | 9 | −1 |
| 4 | Stacks, Queues & Monotonic Structures | 10 | 9 | −1 |
| 5 | Recursion & Backtracking | 12 | 11 | −1 |
| 6 | Trees (incl. Segment Tree / BIT) | 24 | 22 | −2 |
| 7 | Heaps & Priority Queues | 8 | 7 | −1 |
| 8 | Trie | 12 | 11 | −1 |
| 9 | Graphs | 30 | 32 | +2 (dedicated representation + comparison pages) |
| 10 | Dynamic Programming | 26 | 24 | −2 |
| 11 | Greedy Algorithms | 8 | 7 | −1 |
| 12 | Staff-Level Advanced Structures | 10 | 9 | −1 |
| 13 | Interview Meta-Layer & Master Revision | 6 | 6 | — (now includes Master Priority Matrix) |
| **A** | **Master Template Library (NEW)** | — | **10** | +10 |
| | **TOTAL** | **200** | **199** | |

Net effect: pages did not need to grow to absorb the new requirements — moving template code into Appendix A funded the new comparison pages, evolution chains, and roadmap blocks without breaking the 190–200 ceiling.

---

## 9. UPDATED DEPENDENCY GRAPH (unchanged order, Appendix A inserted as a standing reference available from Part 5 onward)

```
Part 0 (Orientation, incl. frequency-dot & teaching-flow conventions)
   ↓
Part 1 (Math/Bits)
   ↓
Part 2 (Arrays/Strings/2-Ptr/BinSearch/Sort)
   ↓
Part 3 (Linked Lists)
   ↓
Part 4 (Stacks/Queues)
   ↓
Part 5 (Recursion/Backtracking) ──── Appendix A becomes active reference from here on ───┐
   ↓                                                                                     │
Part 6 (Trees, incl. Segment Tree/BIT)                                                    │
   ↓                                                                                      │
Part 7 (Heaps)                                                                             │
   ↓                                                                                        │
Part 8 (Trie)                                                                                │
   ↓                                                                                          │
Part 9 (Graphs — full construction pipeline, §5)  ◄───────────────────────────────────────────┘
   ↓
Part 10 (Dynamic Programming — SC→RBR→MTS, references A.31 throughout)
   ↓
Part 11 (Greedy — explicitly contrasted against Part 10 via §4 comparison page)
   ↓
Part 12 (Staff-Level Composition — composes Parts 3,6,7,8,10 simultaneously)
   ↓
Part 13 (Meta-Layer — aggregates every Problem Evolution chain + FAANG Roadmap into master matrices)
```

---

## 10. TRACEABILITY — WHERE EVERY NEW REQUIREMENT LIVES

| Requirement (this revision) | Location |
|---|---|
| Teaching flow (WHY → ... → Revision, code near the end) | §1, applied to all 13 parts |
| Master Template Library, referenced not redefined | Appendix A (§3) |
| Mandatory comparison tables | §4 table + dedicated pages inside Parts 2, 3, 4, 6, 7, 8, 9, 10, 11 |
| Graph construction pipeline (input→conversion→representation→helpers→template→algorithm) | §5 / Part 9 full restructure |
| Dedicated graph representation pages (Edge List, Adjacency List, Adjacency Matrix, Grid, Tree→Graph, Node Graph, Reverse Graph, Weighted, Directed) | Part 9A.0–9A.9 |
| Helper arrays incl. color[] | Part 9B.1–9B.4 |
| Problem Evolution chains | §6 + node 18 in every topic |
| FAANG Roadmap (NeetCode 150, company frequency, Top 5, revision priority) | §7 + node 19 in every topic + Part 13 Master Priority Matrix |
| Print-safe, white-background, high-contrast styling; dark theme only for code | §2 (binding on all future HTML generation) |
| Pattern-derivation goal, AHA-optimized, 190–200 page ceiling | Reflected in §1 node 15 (AHA Moments), and enforced by §8 budget table |

---

## 11. HOW ANOTHER AI SHOULD USE THIS BLUEPRINT (updated)

1. Generate **Appendix A first**, in isolation — it has no prerequisites and every later part cites it by template number.
2. Generate remaining Parts **in the exact dependency order** in §9 — never skip ahead.
3. For every numbered sub-topic, instantiate the **20-node Teaching Flow** (§1) at its page-fraction budget — code (node 9) must be a *pointer + delta*, never a full re-paste of Appendix A.
4. Every topic MUST include: at least one Comparison Table (§4), one Problem Evolution chain (§6), and one FAANG Roadmap block (§7) — these are structural requirements, not optional flourishes.
5. Apply the print/visual system in §2 uniformly — white page background and high-contrast tables everywhere, dark theme reserved exclusively for code blocks.
6. Maintain the page budget in §8 as a hard ceiling; if a topic overflows, cut prose — never cut diagrams, comparison tables, or the dry run.
7. Optimize every page for **AHA-per-square-inch**, not coverage-per-square-inch — if a concept can be taught with one sharp diagram instead of three paragraphs, use the diagram.

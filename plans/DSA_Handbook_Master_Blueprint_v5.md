# MASTER BLUEPRINT — v5
## The Complete FAANG/Staff-Level Java DSA Engineering Handbook
### Two books, now with a Pattern DNA Library · Java only · Zero → Staff Engineer
### Supersedes v4 — adds: a "Pattern DNA" card, applied once per core pattern (~28–30 patterns), as a new Book 2 section sitting between the problem entries and the indexes.

---

## 0. WHAT CHANGED IN THIS REVISION

| # | Change | Why |
|---|---|---|
| 1 | New **Pattern DNA Library** — one DNA card per core pattern (DFS, BFS, Two Pointers, Union-Find, Dijkstra, DP, etc.) | Problem cards teach "solve this one problem." Pattern DNA cards teach "understand this whole family" — parentage, children, reusable state, and failure modes at the *pattern* level, not the problem level. |
| 2 | Placed as **Book 2, new Section 2**, between Section 1 (problem entries) and the old Section 2 (indexes, now Section 3) | It's a recognition/lineage tool — belongs with revision material, not with concept teaching. |
| 3 | Deliberate structural mirror with Book 1's Appendix A | Appendix A = **HOW** (canonical Java code, no theory). Pattern DNA Library = **WHY / WHEN / WHERE THIS CAME FROM** (lineage, recognition, failure modes, no code). Every pattern now has exactly two homes: its code in Book 1, its DNA in Book 2. |
| 4 | Book 2 grows from ~100 → ~113 pages to fit ~28–30 DNA cards at readable density | Flagged explicitly below — same honesty pattern as prior revisions: I'm not shrinking existing content to force a page count. |

---

## 1. THE PATTERN DNA CARD — EXACT FORMAT (verbatim fields, as specified)

One card per **pattern** (not per problem — a pattern like "Sliding Window" covers dozens of problems already detailed individually in Book 2 Section 1).

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                          PATTERN DNA
                    [ Pattern Name, e.g. "Sliding Window" ]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PARENT PATTERN
  Which bigger pattern does this belong to?
  e.g. Sliding Window ← Two Pointers ← Array Traversal

CHILDREN PATTERNS
  Which patterns evolve from this?
  e.g. Sliding Window → Monotonic Deque Window → Variable Window + Frequency Map

REUSABLE IDEAS
  What concepts are reused across the whole family?
  e.g. "expand-then-shrink invariant," "amortized O(1) pointer movement"

INPUT SHAPE
  Array / String / Grid / Tree / Graph / Node / Edge
  (which raw shapes this pattern is typically applied to)

RECOGNITION SIGNALS
  What words in the problem statement should trigger this?
  e.g. "contiguous subarray," "longest substring," "at most k distinct"

DECISION TREE
  If X → Use ...
  Else if Y → Use ...
  (a short, forkable if/else chain distinguishing this pattern from its siblings)

REUSABLE STATE
  Which of these does this pattern typically carry?
  visited[] · parent[] · distance[] · prefix[] · dp[] · stack[] · queue[] · heap[]
  (checked/marked explicitly per pattern — most patterns use 1–3 of these, never all)

FAILURE MODES
  Top 3 reasons people fail problems in this pattern family.

INTERVIEW FOLLOW-UP
  The single most common next question an interviewer asks once this pattern is solved.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Rule:** Pattern DNA cards contain zero Java code and zero step-by-step problem solutions — those live in Appendix A (Book 1) and the problem cards (Book 2 Section 1), respectively. A DNA card is pure lineage + recognition + failure analysis.

---

## 2. WHICH PATTERNS GET A DNA CARD (~29 cards — mirrors Appendix A's 31 templates, grouped)

```
DFS FAMILY
  1. DFS (Recursive & Iterative, unified card)
  2. Tree DFS
  3. Grid DFS
  4. Graph DFS
  5. Trie DFS
  6. Backtracking DFS
  7. Memoized DFS (Top-Down DP)

BFS FAMILY
  8. BFS (incl. Level-Order)
  9. Multi-Source BFS
  10. Topological Sort (BFS / Kahn's)

SEARCH FAMILY
  11. Binary Search (Exact / Lower Bound / Upper Bound, unified card)
  12. Binary Search on Answer

TWO-POINTER FAMILY
  13. Two Pointers
  14. Sliding Window

ARRAY-STATE FAMILY
  15. Prefix Sum
  16. Difference Array
  17. Monotonic Stack
  18. Monotonic Queue

HEAP FAMILY
  19. Heap / Top-K
  20. K-Way Merge

GRAPH-ALGORITHM FAMILY
  21. Union-Find
  22. Dijkstra
  23. Bellman-Ford
  24. Prim / Kruskal (MST, unified card)

STRUCTURE FAMILY
  25. Segment Tree / Fenwick Tree (unified card)
  26. Trie (core structure)

DP FAMILY
  27. Dynamic Programming (SC→RBR→MTS, the umbrella card all DP problems point back to)

GREEDY & BITS FAMILY
  28. Greedy (Exchange Argument)
  29. Bit Manipulation / Bitmask
```

Each numbered entry above corresponds 1:1 to an Appendix A template (or a small cluster of them, where a "unified card" spans multiple A.# numbers, e.g. card #11 spans A.13–A.15). This 1:1 mirroring is intentional — a reader flipping between books always finds "the code" and "the DNA" under matching names.

---

## 3. UPDATED BOOK 2 STRUCTURE (Pattern DNA Library inserted as new Section 2)

```
Front Matter
  0.1  How To Use This Book                                                (1 pg)
  0.2  Template Quick-Reference Index (name/number/signature/complexity, no code) (2 pg)

Section 1 — Problem Entries, Grouped By Topic (~152 problems, ~78 pg)
  [unchanged from v4 — includes Commented Algorithm Steps before Template Used]

Section 2 — PATTERN DNA LIBRARY  ← NEW (~29 cards, ~15 pg)
  2.1  DFS Family              (7 cards, ~4 pg)
  2.2  BFS Family               (3 cards, ~2 pg)
  2.3  Search Family              (2 cards, ~1 pg)
  2.4  Two-Pointer Family           (2 cards, ~1 pg)
  2.5  Array-State Family            (4 cards, ~2 pg)
  2.6  Heap Family                     (2 cards, ~1 pg)
  2.7  Graph-Algorithm Family            (4 cards, ~2 pg)
  2.8  Structure Family                    (2 cards, ~1 pg)
  2.9  DP Family                             (1 card, ~0.5 pg — the umbrella card is denser, gets its own full page)
  2.10 Greedy & Bits Family                    (2 cards, ~1 pg)

Section 3 — The Seven Indexes (was Section 2, ~12 pg)  [unchanged from v4]
  3.1 By Topic · 3.2 By Pattern (now cross-links to Section 2 DNA cards) · 3.3 By Difficulty ·
  3.4 By Company · 3.5 By NeetCode Order · 3.6 By Revision Priority · 3.7 By Interview Frequency

Section 4 — Top Problems At A Glance, One Page Per Topic (was Section 3, ~13 pg)  [unchanged from v4]

Back Matter
  5.1  3-Hour Pre-Interview Cram Sequence (now also walks through relevant DNA cards, not just glance pages) (1 pg)
```

**Section 3.2 ("By Pattern" index) update:** each row now gains one more column — `DNA Card #` — pointing to the Section 2 card. Schema becomes:
`Problem | Topic | Difficulty | Template (A.#) | DNA Card (2.#) | Page#`

---

## 4. UPDATED BOOK 2 PAGE BUDGET

| Section | Pages (v4) | Pages (v5) | Change |
|---|---|---|---|
| Front Matter | 3 | 3 | — |
| Section 1 — Problem Entries | 78 | 78 | — |
| **Section 2 — Pattern DNA Library** | — | **15** | **+15 (new)** |
| Section 3 — Seven Indexes (was Section 2) | 12 | 12 | — (one new column added, negligible page cost) |
| Section 4 — Glance Pages (was Section 3) | 13 | 13 | — |
| Back Matter | 1 | 1 | — |
| **Book 2 Total** | **~100** | **~113** | **+13 net** |

Book 1 is untouched by this revision — still ~199 pages. **Combined total moves from ≈299 → ≈312 pages.** As with the last two revisions, I'm flagging this rather than quietly shrinking Section 1 or the glance pages to force Book 2 back to exactly 100 — the Pattern DNA Library is dense, high-value content and deserves real space. If you'd rather hold the line at ~100 pages for Book 2, the lever is combining more patterns into "unified cards" (e.g., folding all 7 DFS-family cards into 3–4 broader cards) rather than cutting fields from each card.

---

## 5. TRACEABILITY — WHAT'S NEW / WHAT MOVED

| Item | v4 Location | v5 Location |
|---|---|---|
| Problem entries (Section 1) | Book 2, Section 1 | unchanged |
| **Pattern DNA Library** | did not exist | **NEW — Book 2, Section 2** |
| Seven Indexes | Book 2, Section 2 | Book 2, **Section 3** (renumbered) |
| Glance Pages | Book 2, Section 3 | Book 2, **Section 4** (renumbered) |
| "By Pattern" index | Section 2.2, no DNA link | Section 3.2, **now links to DNA Card #** |
| Cram Sequence (back matter) | walks glance pages only | now **also walks relevant DNA cards** |
| Appendix A (template code) | Book 1 only | unchanged — still Book 1 only; DNA cards never contain code |

---

## 6. HOW ANOTHER AI SHOULD USE THIS BLUEPRINT (final, cumulative)

1. Build **Book 1** completely first (unchanged order from v4) — Appendix A's 31 template numbers must be frozen before anything in Book 2 begins.
2. Build **Book 2 front matter**, then **Section 1 (problem entries)** — unchanged process from v4, including Commented Algorithm Steps before Template Used in every card.
3. Build **Book 2 Section 2 (Pattern DNA Library)** next, using the 1:1 family grouping in §2 above. Each DNA card's "Parent Pattern" / "Children Patterns" fields must be internally consistent with the Problem Evolution chains already established in Book 1 (§6 of the v2 blueprint) — do not invent new lineage that contradicts what Book 1 already taught.
4. Build **Section 3 (indexes)** by mechanically sorting Section 1 + cross-linking Section 2 — the new `DNA Card #` column in the "By Pattern" index must point to a card that actually exists in Section 2.
5. Build **Section 4 (glance pages)** and the **back matter cram sequence** last, since the cram sequence needs both the glance pages and the DNA cards to already exist to reference them correctly.
6. Maintain the identical print/visual system across both books (white background, high-contrast tables, dark theme reserved for code) — Pattern DNA cards are non-code, so they follow the same light-card-with-colored-accent-border system as every other non-code box in the handbook (AHA/Mistake/Tip/etc. styling), not the dark code-block styling.
7. Treat ~199 pages (Book 1) and ~113 pages (Book 2) as the new hard ceilings; if Book 2 overflows, merge DNA cards into broader "unified cards" before cutting any of the 9 mandated DNA fields.

---

## 7. QUALITY RULE (binding on all generation from this point forward)

> **Never sacrifice understanding for page count.** If a page-budget conflict occurs, compress wording, remove repetition, or merge closely related examples — but never remove Mental Models, Visualizations, Dry Runs, AHA Moments, Comparison Tables, Pattern DNA, or Commented Algorithm Steps.

This overrides every prior "if it overflows, compress X" instruction anywhere in this blueprint — the elements named above are permanently protected. Page ceilings are soft; these seven elements are not.

**Generation status:** blueprint is now locked. Proceeding to actual content generation, starting with Book 1 — Appendix A (Master Template Library), per the build order in §6/§11 above, since both books' cross-references depend on its numbering being frozen first.

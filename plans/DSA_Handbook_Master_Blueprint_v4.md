# MASTER BLUEPRINT — v4
## The Complete FAANG/Staff-Level Java DSA Engineering Handbook
### Now split into TWO printable books · Java only · Zero → Staff Engineer
### Supersedes v3 — adds: two-book split (Learning Handbook ~200pg / Master Problem Handbook ~100pg), and a repositioned "Commented Algorithm Steps" field in every problem card.

---

## 0. WHAT CHANGED IN THIS REVISION

| # | Change | Why |
|---|---|---|
| 1 | Single ~301-page book split into **Book 1 (Learning, ~199 pg)** and **Book 2 (Master Problem Handbook, ~100 pg)** | Two physical books are more usable: Book 1 for study sessions, Book 2 as a standalone pocket-sized cram book before an on-site. |
| 2 | Every problem card gets a new **Commented Algorithm Steps** section, repositioned to appear **before** the Template Reference | Forces active recall — the reader must attempt to reconstruct the implementation logic before being told which canonical template it maps to. |
| 3 | Appendix A (full Java template code) stays in **Book 1 only** | Book 1 owns "templates," per your own split description. |
| 4 | Book 2 gains a new **Template Quick-Reference Index** (front matter) — template name + number + one-line signature + complexity, **no code** | Lets Book 2 function as a standalone cram book without needing Book 1 open, while actual code remains single-sourced in Book 1. |
| 5 | Every cross-reference between the two books now uses a stable citation format: `[Book 1, Part X.Y]` and `[A.N]` | Since they're now separate physical documents, references must be unambiguous without page numbers (which differ per print run). |

---

## 1. BOOK 1 — LEARNING HANDBOOK (~199 pages)

**Purpose:** concepts, templates, comparisons, AHA moments, teaching flow — zero to Staff Engineer, in dependency order.
**Contains:** Parts 0–12, Part 13 (renumbered Interview Meta-Layer), Appendix A.
**Does NOT contain:** the Master Problem Library, its 7 indexes, or the glance pages — those are entirely in Book 2.

```
Part 0   Orientation                                          4 pg
Part 1   Complexity, Math & Bit Foundations                   10 pg
Part 2   Arrays, Strings & Searching                           28 pg
Part 3   Linked Lists                                            9 pg
Part 4   Stacks, Queues & Monotonic Structures                    9 pg
Part 5   Recursion & Backtracking                                  11 pg
Part 6   Trees (incl. Segment Tree / BIT)                            22 pg
Part 7   Heaps & Priority Queues                                       7 pg
Part 8   Trie                                                            11 pg
Part 9   Graphs                                                            32 pg
Part 10  Dynamic Programming                                                24 pg
Part 11  Greedy Algorithms                                                    7 pg
Part 12  Staff-Level Advanced Structures & Design-Adjacent DSA                  9 pg
Part 13  Interview Meta-Layer & Master Revision (was Part 14 in v3)               6 pg
Appendix A  Master Template Library (full Java code, A.1–A.31)                      10 pg
                                                                    BOOK 1 TOTAL ≈ 199 pg
```

Everything else about Book 1 is **unchanged from v2/v3**: the 20-node Teaching Flow (§1 of v2), the white-background/high-contrast print system (§2 of v2), mandatory comparison tables (§4 of v2), the graph construction pipeline (§5 of v2), and Problem Evolution chains (§6 of v2) all still apply exactly as specified — this revision only touches the book *split* and the *problem card* format (which lives in Book 2).

Part 13 (Interview Meta-Layer) closes Book 1 with: Master Pattern Index, Cross-Topic AHA Compendium, Mock Interview Communication Templates, 45-Minute Timing Budget, One-Page Master Cheat Sheet — exactly as in v2/v3, with one addition: its Master Pattern Index (13.1) now explicitly says *"for the full problem-level index, see Book 2, Section 2.2 — By Pattern"* rather than pretending to be self-contained.

---

## 2. BOOK 2 — MASTER PROBLEM HANDBOOK (~100 pages)

**Purpose:** revise 150+ problems in a few hours, without needing Book 1 or LeetCode open.
**Contains:** everything formerly in v3's Part 13, promoted to its own book, plus a new front-matter Template Quick-Reference Index.

```
Front Matter
  0.1  How To Use This Book (cram-session workflow: index → glance page → card → done) (1 pg)
  0.2  Template Quick-Reference Index (all 31 templates: name, number, 1-line signature,
       complexity — NO code, just enough to jog memory; full code lives in Book 1 App. A) (2 pg)

Section 1 — Problem Entries, Grouped By Topic (~152 problems, ~78 pg)
  1.1  Arrays & Strings                              (~20 problems, ~10 pg)
  1.2  Two Pointers / Sliding Window / Binary Search   (~15 problems, ~8 pg)
  1.3  Linked List                                      (~10 problems, ~5 pg)
  1.4  Stacks / Queues / Monotonic                        (~10 problems, ~5 pg)
  1.5  Recursion / Backtracking                             (~10 problems, ~5 pg)
  1.6  Trees                                                   (~15 problems, ~8 pg)
  1.7  Heaps                                                      (~8 problems, ~4 pg)
  1.8  Trie                                                          (~8 problems, ~4 pg)
  1.9  Graphs                                                          (~20 problems, ~10 pg)
  1.10 Dynamic Programming                                                (~20 problems, ~10 pg)
  1.11 Greedy                                                                (~8 problems, ~4 pg)
  1.12 Staff-Level / Design                                                     (~8 problems, ~4 pg)

Section 2 — The Seven Indexes (~12 pg)
  2.1  By Topic            2.5  By NeetCode Order
  2.2  By Pattern           2.6  By Revision Priority
  2.3  By Difficulty         2.7  By Interview Frequency
  2.4  By Company (Google, Meta, Amazon, Microsoft, Uber, Netflix, Apple, Airbnb, Datadog, Snowflake)

Section 3 — Top Problems At A Glance, One Page Per Topic (~13 pg)
  (Arrays, Two Pointers/Sliding Window/Binary Search, Linked List, Stacks/Queues,
   Recursion/Backtracking, Trees, Heaps, Trie, Graphs, DP, Greedy, Staff-Level,
   + 1 Cross-Topic Capstone page)

Back Matter
  4.1  3-Hour Pre-Interview Cram Sequence (how to walk the whole book in one sitting) (1 pg)

                                                            BOOK 2 TOTAL ≈ 100 pg
```

---

## 3. UPDATED MANDATORY PER-PROBLEM CARD FORMAT (replaces the v3 card — this is the only structural content change besides the book split)

**What changed:** a new **Commented Algorithm Steps** section is inserted **between Mental Model and Template Used** — i.e. strictly *before* the reader is told which canonical template applies. This is deliberate: the reader should be able to attempt writing the solution from these steps alone, then check themselves against the template reference.

`Commented Algorithm Steps` differs from a generic step list — each line is written like an annotated pseudocode comment (naming the actual variables/structures you'd use), not high-level prose. It stops just short of Java syntax.

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  [Problem Name]                                    LC #[___]
  Difficulty: [Easy/Medium/Hard]   NeetCode Category: [_____]
  Frequency:  Google ●●●○○  Meta ●●●○○  Amazon ●●●○○
              Microsoft ●●●○○  Uber ●●●○○
  Pattern: [_____]     Topic: [_____]     Prereqs: [_____, _____]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

QUESTION SUMMARY (3–6 lines, original wording, never copied from LeetCode)

RECOGNITION
  Keywords: [...]      Constraints: [...]      Input Shape: [...]

MENTAL MODEL (one paragraph — the intuition, not the mechanics)

COMMENTED ALGORITHM STEPS  ← NEW, positioned BEFORE the template reveal
  1. [initialize ___ to track ___]
  2. [iterate over ___, at each step check ___]
  3. [when condition ___ holds, update ___ / branch into ___]
  4. [base case: ___ → return ___]
  5. [combine/aggregate results via ___]
  (numbered, implementation-level, comment-style — NOT prose, NOT Java syntax;
   dense enough that a reader could translate this directly into code themselves)

TEMPLATE USED → See Book 1, Appendix A, Template #[A.N — name]
  (revealed only now — after the reader has already reasoned through the steps above)

DRY RUN (mini example, every key variable traced)

COMPLEXITY
  Time: O(...)   Space: O(...)   Why: [one line]

COMMON MISTAKES (top 2–4, ranked by frequency)

VARIATIONS
  ← Previous problem in chain: [...]
  → Next problem in chain: [...]
  Full evolution chain: [cross-referenced to originating Book 1 Part/section]

AHA MOMENT (the one insight that unlocks it)

REVISION NOTES (max 5 bullets)

[If this problem's code differs from the cited Appendix A template:
 show ONLY the delta — a few modified lines, clearly marked "DELTA FROM A.N"
 — this is the ONLY place actual code syntax may appear in Book 2]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Hard rule (unchanged):** Java code is never duplicated in Book 2 outside of an explicit delta block. The Commented Algorithm Steps section is deliberately code-adjacent but not code — it's the bridge between "I understand this" and "I could type this."

---

## 4. CROSS-BOOK REFERENCING CONVENTION

Because Book 1 and Book 2 are now physically separate, all references use stable, print-run-independent citations rather than page numbers:

| From | To | Citation format | Example |
|---|---|---|---|
| Book 2 problem card | Book 1 template code | `See Book 1, Appendix A, Template #A.N` | `See Book 1, Appendix A, Template #A.5 — Graph DFS` |
| Book 2 problem card | Book 1 concept chapter | `See Book 1, Part X.Y` | `See Book 1, Part 9C.1 — DFS` |
| Book 1 Part 13 (Meta-Layer) | Book 2 indexes/glance pages | `See Book 2, Section Z.Z` | `See Book 2, Section 2.2 — By Pattern` |
| Book 2 index tables | Book 2 problem cards | internal page number (same book, safe to use) | `p. 34` |

---

## 5. UPDATED FULL PAGE BUDGET (both books)

| Book | Contents | Pages |
|---|---|---|
| **Book 1 — Learning Handbook** | Parts 0–13 + Appendix A | **≈199** |
| **Book 2 — Master Problem Handbook** | Front matter + Sections 1–3 + back matter | **≈100** |
| **Combined** | | **≈299** |

(Combined total is effectively unchanged from v3's ≈301 — this revision is a *repackaging*, not a scope change, aside from the small Template Quick-Reference Index added to Book 2's front matter.)

---

## 6. TRACEABILITY — WHAT MOVED WHERE

| Item | v3 Location | v4 Location |
|---|---|---|
| Parts 0–12 (all concept teaching) | Single book | Book 1, unchanged |
| Appendix A (template code) | Single book | Book 1 only |
| Part 13 Interview Meta-Layer | Single book, Part 14 | Book 1, Part 13 (renumbered) |
| Master Problem Library (152 problems) | Single book, Part 13 | Book 2, Section 1 |
| 7 Indexes | Single book, Part 13.2 | Book 2, Section 2 |
| Top Problems at a Glance (13 pages) | Single book, Part 13.3 | Book 2, Section 3 |
| Template Quick-Reference Index (no code) | did not exist | **NEW** — Book 2 front matter §0.2 |
| Commented Algorithm Steps field | did not exist | **NEW** — every problem card, positioned before Template Used |
| 3-Hour Cram Sequence | did not exist | **NEW** — Book 2 back matter §4.1 |

---

## 7. HOW ANOTHER AI SHOULD USE THIS BLUEPRINT (final, cumulative)

1. Build **Book 1** completely first, in the dependency order from v2/v3 (Appendix A can be generated alongside Part 5 onward, since it's referenced from there). Book 1 must be fully finished and its Template numbering (A.1–A.31) and Part numbering (0–13) frozen before starting Book 2 — Book 2's citations depend on these numbers being stable.
2. Build **Book 2**'s front matter (Template Quick-Reference Index) by summarizing Appendix A's signatures only — never re-deriving new templates.
3. Build **Book 2 Section 1** (problem cards) using the updated card format in §3 above — Commented Algorithm Steps before Template Used, in every single entry, no exceptions.
4. Build **Book 2 Section 2** (7 indexes) by mechanically sorting Section 1's entries — introduce no new facts.
5. Build **Book 2 Section 3** (glance pages) as a compression of Sections 1–2.
6. Every cross-book reference must use the citation format in §4 — never a bare page number pointing into the other book.
7. Maintain the identical print/visual system (white background, high-contrast tables, dark theme only for code) across both books, so they read as one coherent series despite being separate physical documents.
8. Treat ≈199 pages (Book 1) and ≈100 pages (Book 2) as hard ceilings for each book independently — if either overflows, compress prose first, never drop an index, a glance page, or a Commented Algorithm Steps section.

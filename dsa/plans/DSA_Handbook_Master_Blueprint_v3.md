# MASTER BLUEPRINT — v3
## The Complete FAANG/Staff-Level Java DSA Engineering Handbook
### New Target: ~300 A4 pages (revised up from 199 — see §0 rationale) · Java only · Zero → Staff Engineer
### Supersedes v2 — adds: mandatory Master Problem Library (150+ problems, 7 indexes, per-topic glance pages) as a new Part 13, ahead of the final revision chapter.

---

## 0. WHY THE PAGE CEILING CHANGED (read this first)

v2 targeted ~199 pages under a "teach concepts + light roadmap" scope. This revision adds a **mandatory, fully-fielded Master Problem Library** covering 150+ problems, each with 18 required fields, plus 7 independent cross-indexes and 13 per-topic "at a glance" pages.

Doing this at real density (not a thin stub) costs approximately:

| Component | Est. Pages |
|---|---|
| ~152 problem entries, dense card format, ~0.5 page avg (2/page) | ~76 |
| 7 cross-indexes (Topic, Pattern, Difficulty, Company, NeetCode Order, Revision Priority, Interview Frequency) | ~12 |
| 13 "Top Problems at a Glance" pages (one per topic) | ~13 |
| Intro / how-to-use-this-library page | ~1 |
| **New Part 13 subtotal** | **~102** |

Added to v2's 199 pages (with the old Part 13 renumbered Part 14), the honest total is **≈300 pages**.

**Decision taken (default, applied below):** raise the target to ~300 pages so the Problem Library keeps its full mandated depth.
**Alternative (not applied, noted for the record):** keep ~200 pages by cutting each problem card to ~6 fields (Name/LC#/Difficulty/Pattern/Template ref/one-line AHA) — this fits in ~35 pages total but stops being a "revise without needing LeetCode" resource, which contradicts the stated final goal. This blueprint does **not** take that shortcut.

---

## 1. UPDATED BOOK STRUCTURE (Parts, in build order)

Everything from v2 (§1 Teaching Flow, §2 Print System, §3 Appendix A Templates, §4 Comparison Tables, §5 Graph Pipeline, §6 Problem Evolution Chains, §7 FAANG Roadmap tags) is **unchanged and still binding**. This document only adds the new Part 13 and renumbers what follows.

```
Part 0   Orientation                                    4 pg
Part 1   Complexity, Math & Bit Foundations             10 pg
Part 2   Arrays, Strings & Searching                    28 pg
Part 3   Linked Lists                                    9 pg
Part 4   Stacks, Queues & Monotonic Structures            9 pg
Part 5   Recursion & Backtracking                         11 pg
Part 6   Trees (incl. Segment Tree / BIT)                   22 pg
Part 7   Heaps & Priority Queues                             7 pg
Part 8   Trie                                                 11 pg
Part 9   Graphs                                                32 pg
Part 10  Dynamic Programming                                    24 pg
Part 11  Greedy Algorithms                                       7 pg
Part 12  Staff-Level Advanced Structures & Design-Adjacent DSA     9 pg
Part 13  MASTER PROBLEM LIBRARY  ← NEW                             102 pg
Part 14  Interview Meta-Layer & Master Revision (was Part 13)         6 pg
Appendix A  Master Template Library                                    10 pg
                                                            TOTAL ≈ 301 pg
```

Part 13 sits exactly where requested: **after all concept teaching (Parts 0–12), before the final revision chapter (now Part 14).**

---

## 2. PART 13 — MASTER PROBLEM LIBRARY — INTERNAL STRUCTURE

### 13.0 How To Use This Library (1 page)
- What it is FOR: "revise 150+ problems in a few hours without opening LeetCode."
- How entries map back to chapters (each entry cites its originating Part/section).
- How the 7 indexes work together (topic index for structured study, frequency index for last-minute triage).
- Legend for frequency stars, revision-priority codes (P0/P1/P2), and template reference notation (`A.#`).

### 13.1 Problem Entries, Grouped By Topic (≈152 problems, ≈76 pages)

Grouping mirrors the book's own Part order, so a reader who just finished Part 9 (Graphs) can immediately drill Graph problems here without hunting:

```
13.1.1  Arrays & Strings              (~20 problems, ~10 pg)
13.1.2  Two Pointers / Sliding Window / Binary Search  (~15 problems, ~8 pg)
13.1.3  Linked List                    (~10 problems, ~5 pg)
13.1.4  Stacks / Queues / Monotonic      (~10 problems, ~5 pg)
13.1.5  Recursion / Backtracking          (~10 problems, ~5 pg)
13.1.6  Trees                              (~15 problems, ~8 pg)
13.1.7  Heaps                                (~8 problems, ~4 pg)
13.1.8  Trie                                   (~8 problems, ~4 pg)
13.1.9  Graphs                                   (~20 problems, ~10 pg)
13.1.10 Dynamic Programming                        (~20 problems, ~10 pg)
13.1.11 Greedy                                        (~8 problems, ~4 pg)
13.1.12 Staff-Level / Design                            (~8 problems, ~4 pg)
```
(≈152 problems total, ≈77 pages — matches the §0 estimate.)

### MANDATORY PER-PROBLEM CARD FORMAT (applies to every one of the ~152 entries)

Fixed field order — no entry may omit or reorder these:

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

TEMPLATE USED → See Appendix A, Template #[A.N — name]

STEP-BY-STEP ALGORITHM (numbered steps, prose — no code here)
  1. ...
  2. ...

DRY RUN (mini example, every key variable traced)

COMPLEXITY
  Time: O(...)   Space: O(...)   Why: [one line]

COMMON MISTAKES (top 2–4, ranked by frequency)

VARIATIONS
  ← Previous problem in chain: [...]
  → Next problem in chain: [...]
  Full evolution chain: [see §6-style chain, cross-referenced to originating Part]

AHA MOMENT (the one insight that unlocks it)

REVISION NOTES (max 5 bullets)

[If this problem's code differs from the cited Appendix A template:
 show ONLY the delta — a few modified lines, clearly marked "DELTA FROM A.N"]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Hard rule:** Java code is never duplicated here. Every entry ends its Template Used line with `"See Appendix A, Template #A.N"`; a delta block appears only if the problem meaningfully diverges from the canonical template (e.g., Word Search II's `node.word = null` dedup step on top of A.7 Backtracking DFS).

### 13.2 The Seven Indexes (≈12 pages)

Each index is a single dense table (not cards) pointing back to the Part 13.1 page where the full entry lives. Fixed column schema per index:

```
13.2.1  By Topic            → Problem | LC# | Pattern | Difficulty | Page#
13.2.2  By Pattern           → Problem | Topic | Difficulty | Template (A.#) | Page#
13.2.3  By Difficulty          → Problem | Topic | Pattern | Frequency | Page#
13.2.4  By Company               → Problem | Topic | Pattern | Difficulty | Page#
                                    (one sub-table per company: Google, Meta, Amazon,
                                     Microsoft, Uber, Netflix, Apple, Airbnb, Datadog, Snowflake)
13.2.5  By NeetCode Order          → follows NeetCode 150's own sequence exactly, 1:1
13.2.6  By Revision Priority         → grouped under P0 / P1 / P2 headers
13.2.7  By Interview Frequency        → grouped under ★★★★★ down to ★☆☆☆☆ headers
```
Each index page is a pure lookup table — no re-explanation of the problem, only the routing columns above plus the page number where the full card lives.

### 13.3 "Top Problems At A Glance" — One Page Per Topic (13 pages)

One dense summary table per topic (Arrays, Two Pointers/Sliding Window/Binary Search, Linked List, Stacks/Queues, Recursion/Backtracking, Trees, Heaps, Trie, Graphs, DP, Greedy, Staff-Level, plus one Cross-Topic Capstone page) — designed so **that single page alone** lets a reader review the whole topic in under 5 minutes.

Fixed schema (exactly as specified):

```
Problem | Pattern | Template | Difficulty | Frequency | Status | Comments
```

Example (Graphs — reproduced from spec, this exact table ships in the book):

| Problem | Pattern | Template | Difficulty | Frequency | Status | Comments |
|---|---|---|---|---|---|---|
| Number of Islands | DFS | A.5 | Easy | ★★★★★ | Core | |
| Course Schedule | Topo Sort | A.12 | Medium | ★★★★★ | Must Know | |
| Clone Graph | DFS | A.5 | Medium | ★★★★☆ | Core | |
| Network Delay Time | Dijkstra | A.24 | Medium | ★★★★★ | Must Know | |

"Status" uses a small fixed vocabulary: `Core` / `Must Know` / `Good to Know` / `Bonus` — kept consistent across all 13 glance pages so the reader's eye pattern-matches instantly regardless of topic.

---

## 3. RENUMBERED PART 14 (was Part 13 in v2) — NO CONTENT CHANGE

`Interview Meta-Layer & Master Revision` keeps its v2 content (Master Pattern Index, Cross-Topic AHA Compendium, Mock Interview Templates, Timing Budget, One-Page Master Cheat Sheet) — 6 pages, unchanged — but now also gains one explicit cross-link: its "Master Pattern Index" (14.1) references Part 13's "By Pattern" index (13.2.2) instead of duplicating it, keeping the two systems in sync rather than forked.

---

## 4. UPDATED FULL PAGE BUDGET TABLE

| Part | Title | Pages |
|---|---|---|
| 0 | Orientation | 4 |
| 1 | Complexity, Math & Bit Foundations | 10 |
| 2 | Arrays, Strings & Searching | 28 |
| 3 | Linked Lists | 9 |
| 4 | Stacks, Queues & Monotonic Structures | 9 |
| 5 | Recursion & Backtracking | 11 |
| 6 | Trees (incl. Segment Tree / BIT) | 22 |
| 7 | Heaps & Priority Queues | 7 |
| 8 | Trie | 11 |
| 9 | Graphs | 32 |
| 10 | Dynamic Programming | 24 |
| 11 | Greedy Algorithms | 7 |
| 12 | Staff-Level Advanced Structures | 9 |
| 13 | **Master Problem Library (NEW)** | **102** |
| 14 | Interview Meta-Layer & Master Revision | 6 |
| A | Master Template Library (Appendix) | 10 |
| | **TOTAL** | **≈301** |

---

## 5. TRACEABILITY — WHERE EVERY NEW REQUIREMENT LIVES

| Requirement (this revision) | Location |
|---|---|
| Master Problem Library section, positioned before final revision chapter | Part 13, placed immediately before Part 14 |
| Per-problem mandatory format (18 fields, no code duplication) | §2, "Mandatory Per-Problem Card Format" |
| ~150+ problems covering the whole book | Part 13.1.1–13.1.12, grouped by originating topic |
| By Topic index | 13.2.1 |
| By Pattern index | 13.2.2 |
| By Difficulty index | 13.2.3 |
| By Company index (incl. Netflix, Apple, Airbnb, Datadog, Snowflake beyond the core 5) | 13.2.4 |
| By NeetCode Order index | 13.2.5 |
| By Revision Priority index | 13.2.6 |
| By Interview Frequency index | 13.2.7 |
| "Top Problems at a Glance" per topic, 5-minute revision page | 13.3 (13 pages, fixed 7-column schema) |
| Templates referenced not re-duplicated | Every card's "Template Used" line + optional delta block, per Appendix A (v2 §3) |
| Handbook serves both learning (zero→Staff) and rapid pre-interview revision | Parts 0–12 (learning) + Part 13 (revision library) + Part 14 (final compression) |

---

## 6. HOW ANOTHER AI SHOULD USE THIS BLUEPRINT (final, cumulative)

1. Build **Appendix A** first (no prerequisites).
2. Build **Parts 0–12** in strict dependency order (unchanged from v2), applying the 20-node Teaching Flow, mandatory comparison tables, graph construction pipeline, problem-evolution chains, and FAANG roadmap tags throughout.
3. Build **Part 13 (Master Problem Library)** only after Parts 0–12 exist — every entry must cite the Part/section it originated from, and every entry's "Template Used" and "Variations" fields must be consistent with what was already taught (no new templates or chains invented here).
4. Build the **7 indexes (13.2)** by mechanically sorting Part 13.1's entries — these must never introduce facts not already present in the entries themselves.
5. Build the **13 glance pages (13.3)** last, as a compression of Part 13.1 + 13.2 — each must be independently sufficient for a 5-minute topic review.
6. Build **Part 14** referencing Part 13 rather than duplicating it.
7. Maintain the print/visual system (white background, high-contrast tables, dark theme reserved for code) across all of this new content, identical to Parts 0–12.
8. Treat the ~301-page total as the new ceiling — if it overflows, compress the per-problem "Question Summary" and "Dry Run" fields first (they're the most compressible), never drop an index or a glance page.

import glob
import os
import re

html_files = sorted(glob.glob("F:/dsa/bookfinal/*.html"))

utilities_map = {
    "Topic02": "UTILITIES & CONVERSIONS: Arrays.stream(), toArray(), char[], StringBuilder, getOrDefault(), computeIfAbsent()",
    "Topic03": "UTILITIES & CONVERSIONS: Array element swap, reverse(arr, left, right), partition(arr, pivot)",
    "Topic04": "UTILITIES & CONVERSIONS: Window frequency int[128], expand/shrink loop, atMost(K) - atMost(K-1)",
    "Topic05": "UTILITIES & CONVERSIONS: Safe mid = lo + (hi - lo) / 2, lowerBound(), upperBound(), feasible(mid)",
    "Topic06": "UTILITIES & CONVERSIONS: ListNode, reverseList(), findMiddle(), Dummy Sentinel node",
    "Topic07": "UTILITIES & CONVERSIONS: ArrayDeque push/pop/peek, Monotonic Stack maintainer",
    "Topic08": "UTILITIES & CONVERSIONS: ArrayDeque offer/poll, Circular Queue modulo (i + 1) % N, Monotonic Deque",
    "Topic09": "UTILITIES & CONVERSIONS: PriorityQueue comparators (a,b)->Integer.compare(a,b), Collections.reverseOrder()",
    "Topic10": "UTILITIES & CONVERSIONS: TreeNode, Pre/In/Postorder helpers, BFS level queue snapshot, checkHeight()",
    "Topic11": "UTILITIES & CONVERSIONS: TrieNode[26], isEnd, insert(), search(), startsWith()",
    "Topic12": "UTILITIES & CONVERSIONS: buildGraph(edges), DIR4/DIR8, isValid(r,c), UnionFind class",
    "Topic13": "UTILITIES & CONVERSIONS: Choose-Explore-Undo template, List<T> path, boolean[] used",
    "Topic14": "UTILITIES & CONVERSIONS: Memoization array fill -1, Tabulation dp[n+1][m+1], prev/curr space optimization",
    "Topic15": "UTILITIES & CONVERSIONS: Arrays.sort(intervals, (a,b)->Integer.compare(a[1],b[1])), maxReach tracker",
    "Topic16": "UTILITIES & CONVERSIONS: Sort by start time, Overlap check (last.end >= curr.start), Sweep Line diff array",
    "Topic17": "UTILITIES & CONVERSIONS: n & (n-1) clear lowest bit, n & -n isolate bit, (sub-1) & mask bitmask iteration",
    "Topic18": "UTILITIES & CONVERSIONS: gcd(a,b), lcm(a,b), Sieve of Eratosthenes int[], pow(x,n) fast exponentiation",
    "Topic19": "UTILITIES & CONVERSIONS: SegmentTree tree[4*N], Fenwick BIT tree[N+1], Sparse Table st[N][LOG]"
}

print("Checking Utilities & Conversions coverage across all topics:")
for f in html_files:
    fname = os.path.basename(f)
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        content = fp.read()
    
    topic_key = None
    for key in utilities_map:
        if key in fname:
            topic_key = key
            break
            
    has_utils = ("UTILITIES" in content.upper() or "CONVERSION" in content.upper())
    print(f"{fname:38s} | Has Utilities/Conversions: {str(has_utils):5s}")

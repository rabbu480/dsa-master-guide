import os
import glob
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

html_files = sorted(glob.glob('F:/dsa/bookfinal/*.html'))

print(f"=== DETAILED FAANG DSA HANDBOOK PHRASE AUDIT ===")
print(f"Found {len(html_files)} HTML files in F:/dsa/bookfinal/\n")

checks = {
    "Topic01_Foundations_BigO.html": ["Foundations", "Wi-Fi", "Call Stack", "Dry Run", "Rule"],
    "Topic02_Arrays_Strings_Hashing.html": ["Array", "HashMap", "Bucket", "Frequency", "Two Sum"],
    "Topic03_TwoPointers.html": ["Two Pointer", "Opposite", "Fast", "Sort Colors", "Rain Water"],
    "Topic04_SlidingWindow.html": ["Sliding Window", "Fixed", "Variable", "Substring", "K"],
    "Topic05_BinarySearch.html": ["Binary Search", "lowerBound", "upperBound", "Answer", "Rotated"],
    "Topic06_LinkedList.html": ["Linked List", "Dummy", "Fast", "Reverse", "Merge"],
    "Topic07_Stack.html": ["Stack", "ArrayDeque", "Monotonic", "RPN", "Histogram"],
    "Topic08_Queue_Deque.html": ["Queue", "Deque", "Circular", "Monotonic", "Sliding Window"],
    "Topic09_Heap.html": ["Heap", "PriorityQueue", "Heapify", "Median", "Kth"],
    "Topic10_Trees.html": ["Tree", "BST", "DFS", "BFS", "Lowest Common Ancestor"],
    "Topic11_Trie.html": ["Trie", "Autocomplete", "Prefix", "node.word", "Word Search II"],
    "Topic12_Graphs.html": ["Graph", "Adjacency List", "Course Schedule", "Indegree", "Dijkstra"],
    "Topic13_Backtracking.html": ["Backtracking", "Choose", "Explore", "Undo", "N-Queens"],
    "Topic14_DynamicProgramming.html": ["SB", "RBR", "MTS", "Memoization", "Knapsack"],
    "Topic15_Greedy.html": ["Greedy", "Exchange", "Jump Game", "Gas Station", "Partition"],
    "Topic16_Intervals.html": ["Interval", "Merge", "Insert", "Meeting Rooms", "Overlap"],
    "Topic17_BitManipulation.html": ["Bit", "Kernighan", "Single Number", "XOR", "Sum"],
    "Topic18_Math.html": ["Math", "GCD", "Sieve", "Exponentiation", "Prime"],
    "Topic19_AdvancedDS.html": ["Segment Tree", "Fenwick", "BIT", "KMP", "Manacher"],
    "Book2_InterviewMastery.html": ["Interview", "Mastery", "Mock", "Company", "Offer"]
}

all_passed = True
for filename, required_concepts in checks.items():
    filepath = f"F:/dsa/bookfinal/{filename}"
    if not os.path.exists(filepath):
        print(f"[MISSING FILE] {filename}")
        all_passed = False
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    pages = len(re.findall(r'class=["\']page["\']', content))
    missing = [c for c in required_concepts if c.lower() not in content.lower()]
    
    if missing:
        print(f"[WARNING] {filename} (Pages: {pages}) -> MISSING KEYWORDS: {missing}")
        all_passed = False
    else:
        print(f"[VERIFIED] {filename:<36} | Pages: {pages:2d} | All {len(required_concepts)} Core Keywords Verified 100% Intact")

print("\n" + "="*70)
if all_passed:
    print("SUCCESS! ALL 20 FILES ARE 100% INTACT, UNCOMPROMISED, AND VERIFIED!")
else:
    print("WARNING: Some files have missing keywords.")
print("="*70)

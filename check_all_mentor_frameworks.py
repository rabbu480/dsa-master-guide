import os
from bs4 import BeautifulSoup

html_files = [
    ('Topic01_Foundations_BigO.html', 'Foundations & Big-O'),
    ('Topic02_Arrays_Strings_Hashing.html', 'Arrays, Strings & Hashing'),
    ('Topic03_TwoPointers.html', 'Two Pointers'),
    ('Topic04_SlidingWindow.html', 'Sliding Window'),
    ('Topic05_BinarySearch.html', 'Binary Search'),
    ('Topic06_LinkedList.html', 'Linked List'),
    ('Topic07_Stack.html', 'Stack'),
    ('Topic08_Queue_Deque.html', 'Queue & Deque'),
    ('Topic09_Heap.html', 'Heap (Priority Queue)'),
    ('Topic10_Trees.html', 'Trees & BST'),
    ('Topic11_Trie.html', 'Trie (Prefix Tree)'),
    ('Topic12_Graphs.html', 'Graphs'),
    ('Topic13_Backtracking.html', 'Backtracking'),
    ('Topic14_DynamicProgramming.html', 'Dynamic Programming'),
    ('Topic15_Greedy.html', 'Greedy Algorithms'),
    ('Topic16_Intervals.html', 'Intervals'),
    ('Topic17_BitManipulation.html', 'Bit Manipulation'),
    ('Topic18_Math.html', 'Mathematics'),
    ('Topic19_AdvancedDS.html', 'Advanced Data Structures'),
    ('Book2_InterviewMastery.html', 'Book 2: Interview Mastery')
]

base_dir = 'F:/dsa/bookfinal'

print("=== MENTOR FRAMEWORK VERIFICATION AUDIT ===")
for filename, title in html_files:
    filepath = os.path.join(base_dir, filename)
    if not os.path.exists(filepath):
        print(f"[MISSING] {filename}")
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Key framework checks
    has_story = 'STORY' in content.upper() or 'REAL-WORLD' in content.upper() or 'PHASE 1' in content.upper()
    has_aha = 'AHA' in content.upper() or '💡' in content
    has_decision_tree = 'DECISION TREE' in content.upper() or 'dt-grid' in content
    has_cheat_sheet = 'SUMMARY' in content.upper() or 'CHECKLIST' in content.upper()
    
    print(f"File: {filename:35s} | Story: {'YES' if has_story else 'NO '} | Aha: {'YES' if has_aha else 'NO '} | DecisionTree: {'YES' if has_decision_tree else 'NO '} | CheatSheet: {'YES' if has_cheat_sheet else 'NO '}")

print("=" * 65)

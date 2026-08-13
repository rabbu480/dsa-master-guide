import os
import glob
import re

files_to_fix = [
    'Topic02_Arrays_Strings_Hashing.html',
    'Topic03_TwoPointers.html',
    'Topic04_SlidingWindow.html',
    'Topic06_LinkedList.html',
    'Topic07_Stack.html',
    'Topic08_Queue_Deque.html',
    'Topic09_Heap.html',
    'Topic10_Trees.html',
    'Topic11_Trie.html',
    'Topic12_Graphs.html',
    'Topic13_Backtracking.html',
    'Topic14_DynamicProgramming.html',
    'Topic15_Greedy.html',
    'Topic16_Intervals.html',
    'Topic17_BitManipulation.html',
    'Topic18_Math.html',
    'Topic19_AdvancedDS.html'
]

for filename in files_to_fix:
    filepath = os.path.join('F:/dsa/bookfinal', filename)
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Reset font sizes in CSS rules
    content = content.replace('font-size: 10.8px;', 'font-size: 11px;')
    content = content.replace('font-size: 0.65rem;', 'font-size: 0.68rem;')
    content = content.replace('font-size: 0.56rem;', 'font-size: 0.65rem;')
    content = content.replace('font-size: 0.70rem;', 'font-size: 0.72rem;')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("=== ENHANCED READABILITY FONT SIZES COMPLETE ===")

import os
import glob
import re

files_to_fix = [
    'Topic06_LinkedList.html',
    'Topic07_Stack.html',
    'Topic09_Heap.html',
    'Topic12_Graphs.html',
    'Topic13_Backtracking.html'
]

# Let's inspect Topic06_LinkedList.html structure first
with open('F:/dsa/bookfinal/Topic06_LinkedList.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("Topic06 size:", len(text))

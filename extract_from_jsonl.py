import os
import json
import re

jsonl_path = r'C:\Users\rabba\.gemini\antigravity\brain\f64b8896-da84-4ec4-81a1-c7cef11336dc\.system_generated\logs\transcript.jsonl'

keywords = {
    'Topic06_LinkedList.html': ['Linked List', 'ListNode', 'reverseList'],
    'Topic07_Stack.html': ['Stack Masterclass', 'MinStack', 'evalRPN'],
    'Topic09_Heap.html': ['Heap Masterclass', 'PriorityQueue', 'KthLargest'],
    'Topic12_Graphs.html': ['Graph Masterclass', 'numIslands', 'validTree'],
    'Topic13_Backtracking.html': ['Backtracking Masterclass', 'subsets', 'permute']
}

print(f"Reading {jsonl_path}...")
with open(jsonl_path, 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

print(f"Read {len(lines)} lines from transcript.jsonl.")

for fname, kw_list in keywords.items():
    best_html = ""
    for line in lines:
        if all(kw in line for kw in kw_list):
            # Find html snippets
            matches = re.findall(r'<!DOCTYPE html>[\s\S]*?</html>', line)
            if not matches:
                # Find html chunks inside json string
                matches = re.findall(r'<!DOCTYPE html>.*?</html>', line)
            for m in matches:
                if len(m) > len(best_html):
                    best_html = m
    if best_html:
        # Unescape unicode
        try:
            best_html = json.loads(f'"{best_html}"')
        except:
            best_html = best_html.replace('\\n', '\n').replace('\\"', '"').replace('\\\\', '\\')
            
        out_path = os.path.join('F:/dsa/bookfinal', fname)
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(best_html)
        print(f"SUCCESS! Restored {fname} ({len(best_html)} bytes)")
    else:
        print(f"No match for {fname}")

print("=== TRANSCRIPT EXTRACTION COMPLETE ===")

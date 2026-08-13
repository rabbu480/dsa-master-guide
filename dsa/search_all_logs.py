import os
import glob
import re
import json

files_needed = {
    'Topic06_LinkedList.html': None,
    'Topic07_Stack.html': None,
    'Topic09_Heap.html': None,
    'Topic12_Graphs.html': None,
    'Topic13_Backtracking.html': None
}

log_files = glob.glob(r'C:\Users\rabba\.gemini\antigravity\brain\**\*.jsonl', recursive=True) + \
            glob.glob(r'C:\Users\rabba\.gemini\antigravity\brain\**\*.log', recursive=True) + \
            glob.glob(r'C:\Users\rabba\.gemini\antigravity\brain\**\*.txt', recursive=True)

print(f"Searching across {len(log_files)} log files...")

for log_path in log_files:
    try:
        with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
            text = f.read()
        for fname in list(files_needed.keys()):
            if fname in text:
                pattern = rf'Topic 06: Linked List Masterclass|Topic 07: Stack Masterclass|Topic 09: Heap Masterclass|Topic 12: Graph Masterclass|Topic 13: Backtracking Masterclass'
                # Find html string blocks containing DOCTYPE html
                matches = re.findall(r'<!DOCTYPE html>[\s\S]*?</html>', text)
                for m in matches:
                    for target_fn in list(files_needed.keys()):
                        topic_title = target_fn.split('_')[1].replace('.html','')
                        if topic_title.lower() in m.lower():
                            if not files_needed[target_fn] or len(m) > len(files_needed[target_fn]):
                                files_needed[target_fn] = m
                                print(f"Found match for {target_fn} in {os.path.basename(log_path)}! Length: {len(m)}")
    except Exception as e:
        pass

for fname, code in files_needed.items():
    if code:
        out_path = os.path.join('F:/dsa/bookfinal', fname)
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(code)
        print(f"Restored {fname}!")
    else:
        print(f"Could not find transcript for {fname}")

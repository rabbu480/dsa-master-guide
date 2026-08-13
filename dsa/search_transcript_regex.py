import os
import json
import re

transcript_path = r'C:\Users\rabba\.gemini\antigravity\brain\f64b8896-da84-4ec4-81a1-c7cef11336dc\.system_generated/logs/transcript.jsonl'

files_needed = {
    'Topic06_LinkedList.html': None,
    'Topic07_Stack.html': None,
    'Topic09_Heap.html': None,
    'Topic12_Graphs.html': None,
    'Topic13_Backtracking.html': None
}

with open(transcript_path, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

for fname in files_needed.keys():
    # Look for TargetFile: ...fname ... CodeContent: ...
    pattern = rf'"TargetFile":"[^"]*{fname}"[\s\S]*?"CodeContent":"([\s\S]*?)"'
    matches = re.findall(pattern, text)
    if matches:
        # Get longest match
        best = max(matches, key=len)
        # Unescape json
        try:
            cleaned = json.loads(f'"{best}"')
            files_needed[fname] = cleaned
            print(f"FOUND {fname}! Length: {len(cleaned)}")
        except Exception as e:
            files_needed[fname] = best.replace('\\n', '\n').replace('\\"', '"').replace('\\\\', '\\')
            print(f"FOUND (raw) {fname}! Length: {len(files_needed[fname])}")

for fname, code in files_needed.items():
    if code:
        out_path = os.path.join('F:/dsa/bookfinal', fname)
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(code)
        print(f"Restored {fname}!")

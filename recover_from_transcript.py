import os
import json
import re

transcript_path = r'C:\Users\rabba\.gemini\antigravity\brain\f64b8896-da84-4ec4-81a1-c7cef11336dc\.system_generated\logs\transcript.jsonl'

files_needed = [
    'Topic06_LinkedList.html',
    'Topic07_Stack.html',
    'Topic09_Heap.html',
    'Topic12_Graphs.html',
    'Topic13_Backtracking.html'
]

found = {}

print("Searching transcript for original file writes...")
with open(transcript_path, 'r', encoding='utf-8', errors='ignore') as f:
    for line in f:
        for fname in files_needed:
            if fname not in found and fname in line and 'CodeContent' in line:
                try:
                    data = json.loads(line)
                    # Search tool calls
                    tool_calls = data.get('tool_calls', [])
                    for tc in tool_calls:
                        args = tc.get('args', {})
                        if args.get('TargetFile', '').endswith(fname) and 'CodeContent' in args:
                            code = args['CodeContent']
                            if len(code) > 10000:
                                found[fname] = code
                                print(f"FOUND {fname} in transcript! Length: {len(code)}")
                except Exception as e:
                    pass

for fname, code in found.items():
    out_path = os.path.join('F:/dsa/bookfinal', fname)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(code)
    print(f"Restored {fname} to F:/dsa/bookfinal/")

print("=== RECOVERY FROM TRANSCRIPT COMPLETE ===")

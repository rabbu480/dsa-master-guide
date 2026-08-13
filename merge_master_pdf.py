import os
import fitz

pdf_files = [
    'F:/dsa/bookfinal/Topic01_Foundations_BigO.pdf',
    'F:/dsa/bookfinal/Topic02_Arrays_Strings_Hashing.pdf',
    'F:/dsa/bookfinal/Topic03_TwoPointers.pdf',
    'F:/dsa/bookfinal/Topic04_SlidingWindow.pdf',
    'F:/dsa/bookfinal/Topic05_BinarySearch.pdf',
    'F:/dsa/bookfinal/Topic06_LinkedList.pdf',
    'F:/dsa/bookfinal/Topic07_Stack.pdf',
    'F:/dsa/bookfinal/Topic08_Queue_Deque.pdf',
    'F:/dsa/bookfinal/Topic09_Heap.pdf',
    'F:/dsa/bookfinal/Topic10_Trees.pdf',
    'F:/dsa/bookfinal/Topic11_Trie.pdf',
    'F:/dsa/bookfinal/Topic12_Graphs.pdf',
    'F:/dsa/bookfinal/Topic13_Backtracking.pdf',
    'F:/dsa/bookfinal/Topic14_DynamicProgramming.pdf',
    'F:/dsa/bookfinal/Topic15_Greedy.pdf',
    'F:/dsa/bookfinal/Topic16_Intervals.pdf',
    'F:/dsa/bookfinal/Topic17_BitManipulation.pdf',
    'F:/dsa/bookfinal/Topic18_Math.pdf',
    'F:/dsa/bookfinal/Topic19_AdvancedDS.pdf',
    'F:/dsa/bookfinal/Book2_InterviewMastery.pdf'
]

master_doc = fitz.open()
for f in pdf_files:
    if os.path.exists(f):
        d = fitz.open(f)
        master_doc.insert_pdf(d)
        print(f"[{len(d):2d} pages] Added {os.path.basename(f)}")
        d.close()

out_path = 'F:/dsa/bookfinal/FAANG_DSA_Master_Handbook.pdf'
master_doc.save(out_path)
print("=" * 55)
print("MASTER PDF SUCCESSFULLY MERGED!")
print(f"Path       : {out_path}")
print(f"Total Pages: {len(master_doc)}")
print(f"File Size  : {round(os.path.getsize(out_path)/(1024*1024), 2)} MB")
print("=" * 55)

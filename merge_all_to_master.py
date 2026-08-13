import os, glob, subprocess, fitz

book_dir = r"F:\dsa\bookfinal"
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

html_files = [
    'Topic01_Foundations_BigO.html',
    'Topic02_Arrays_Strings_Hashing.html',
    'Topic03_TwoPointers.html',
    'Topic04_SlidingWindow.html',
    'Topic05_BinarySearch.html',
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
    'Topic19_AdvancedDS.html',
    'Book2_InterviewMastery.html'
]

master_doc = fitz.open()

print(f"{'Topic File':<35} | {'PDF Pages':<10} | {'Status':<10}")
print("-" * 60)

for h_name in html_files:
    h_path = os.path.join(book_dir, h_name)
    pdf_path = h_path.replace(".html", ".pdf")
    
    if os.path.exists(pdf_path):
        d = fitz.open(pdf_path)
        pages = len(d)
        master_doc.insert_pdf(d)
        d.close()
        print(f"{h_name:<35} | {pages:<10} | OK")
    else:
        print(f"{h_name:<35} | Missing    | ERROR")

master_pdf = os.path.join(book_dir, "FAANG_DSA_Master_Handbook.pdf")
if os.path.exists(master_pdf):
    os.remove(master_pdf)
    
master_doc.save(master_pdf)
master_pages = len(master_doc)
doc_size = round(os.path.getsize(master_pdf) / (1024 * 1024), 2)
master_doc.close()

print("=" * 60)
print(f"MASTER HANDBOOK PDF MERGED SUCCESSFULLY!")
print(f"Path        : {master_pdf}")
print(f"Total Pages : {master_pages} pages")
print(f"File Size   : {doc_size} MB")
print("=" * 60)

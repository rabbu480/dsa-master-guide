import subprocess
import os
import fitz

html_files = [
    'F:/dsa/bookfinal/Topic01_Foundations_BigO.html',
    'F:/dsa/bookfinal/Topic02_Arrays_Strings_Hashing.html',
    'F:/dsa/bookfinal/Topic03_TwoPointers.html',
    'F:/dsa/bookfinal/Topic04_SlidingWindow.html',
    'F:/dsa/bookfinal/Topic05_BinarySearch.html',
    'F:/dsa/bookfinal/Topic06_LinkedList.html',
    'F:/dsa/bookfinal/Topic07_Stack.html',
    'F:/dsa/bookfinal/Topic08_Queue_Deque.html',
    'F:/dsa/bookfinal/Topic09_Heap.html',
    'F:/dsa/bookfinal/Topic10_Trees.html',
    'F:/dsa/bookfinal/Topic11_Trie.html',
    'F:/dsa/bookfinal/Topic12_Graphs.html',
    'F:/dsa/bookfinal/Topic13_Backtracking.html',
    'F:/dsa/bookfinal/Topic14_DynamicProgramming.html',
    'F:/dsa/bookfinal/Topic15_Greedy.html',
    'F:/dsa/bookfinal/Topic16_Intervals.html',
    'F:/dsa/bookfinal/Topic17_BitManipulation.html',
    'F:/dsa/bookfinal/Topic18_Math.html',
    'F:/dsa/bookfinal/Topic19_AdvancedDS.html',
    'F:/dsa/bookfinal/Book2_InterviewMastery.html'
]

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
if not os.path.exists(chrome_path):
    chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

print(f"Using Chrome path: {chrome_path}")

master_doc = fitz.open()

for html in html_files:
    pdf_out = html.replace('.html', '.pdf')
    cmd = [
        chrome_path,
        '--headless',
        '--disable-gpu',
        '--no-pdf-header-footer',
        f'--print-to-pdf={pdf_out}',
        html
    ]
    subprocess.run(cmd, check=True)
    if os.path.exists(pdf_out):
        d = fitz.open(pdf_out)
        print(f"[{len(d):2d} PDF Pages] Generated {os.path.basename(pdf_out)}")
        master_doc.insert_pdf(d)
        d.close()

out_path = 'F:/dsa/bookfinal/FAANG_DSA_Master_Handbook.pdf'
master_doc.save(out_path)
print("=" * 55)
print("MASTER PDF SUCCESSFULLY MERGED!")
print(f"File Path : {out_path}")
print(f"Total Pages: {len(master_doc)}")
print(f"File Size : {round(os.path.getsize(out_path)/(1024*1024), 2)} MB")
print("=" * 55)

import subprocess
import glob
import os
import fitz
from bs4 import BeautifulSoup

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

print("=== A4 PAGE FIT AUDIT: HTML DIV COUNT VS GENERATED PDF PAGE COUNT ===")
mismatches = []

for html in html_files:
    basename = os.path.basename(html)
    with open(html, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
    div_count = len(soup.find_all("div", class_="page"))

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
    d = fitz.open(pdf_out)
    pdf_count = len(d)
    d.close()

    status = "MATCH [OK]" if div_count == pdf_count else "MISMATCH [FIX]"
    print(f"{basename:40s} | HTML Pages: {div_count:2d} | PDF Pages: {pdf_count:2d} | {status}")
    if div_count != pdf_count:
        mismatches.append((basename, div_count, pdf_count))

print("=" * 70)
if not mismatches:
    print("ALL HTML PAGES FIT PERFECTLY ON A4 PRINTABLE PAGES (1:1 EXACT MATCH)!")
else:
    print(f"FOUND {len(mismatches)} MISMATCHES NEEDING PADDING/CSS ADJUSTMENTS.")

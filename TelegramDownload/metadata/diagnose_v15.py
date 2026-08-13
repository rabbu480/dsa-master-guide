import os
from bs4 import BeautifulSoup
import re

v10_dir = r"C:\Users\rabba\Downloads\TelegramDownload\metadata\v10"

with open(r"C:\Users\rabba\Downloads\TelegramDownload\metadata\diag.txt", "w", encoding="utf-8") as out:
    out.write("--- Sudoku ---\n")
    with open(os.path.join(v10_dir, '1.Array&Hashing_Final.html'), 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        sudoku = soup.find(string=re.compile('36\. Valid Sudoku'))
        if sudoku:
            tr = sudoku.find_parent('tr')
            if tr: out.write(tr.prettify() + "\n")
            
    out.write("\n--- List <-> Array ---\n")
    list_arr = soup.find(string=re.compile('List ↔ Array'))
    if list_arr:
        parent = list_arr.find_parent('div')
        if parent:
            out.write(parent.parent.prettify() + "\n")

    out.write("\n--- TIPS & REMINDERS ---\n")
    tips = soup.find(string=re.compile('TIPS & REMINDERS'))
    if tips:
        out.write(tips.parent.prettify() + "\n")

    out.write("\n--- COMMON HASHMAP METHODS ---\n")
    hashmap = soup.find(string=re.compile('COMMON HASHMAP METHODS'))
    if hashmap:
        out.write(hashmap.parent.prettify() + "\n")
        
    out.write("\n--- Graphs Boxes ---\n")
    with open(os.path.join(v10_dir, '9.Graphs_Final.html'), 'r', encoding='utf-8') as f:
        soup2 = BeautifulSoup(f.read(), 'html.parser')
        boxes = soup2.find_all('div', class_='section-box')
        out.write(f"Number of section-box in Graphs: {len(boxes)}\n")
        if len(boxes) == 0:
            divs = soup2.find_all('div', style=re.compile('border|background'))
            for d in divs[:3]:
                out.write(str(d.get('class', [])) + " " + str(d.get('style', '')) + "\n")

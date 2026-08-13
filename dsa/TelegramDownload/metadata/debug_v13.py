import os
import re
from bs4 import BeautifulSoup

v13_dir = r"C:\Users\rabba\Downloads\TelegramDownload\metadata\v13"
path = os.path.join(v13_dir, '1.Array&Hashing_Final.html')

with open(path, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

print("--- Checking '4 GROUPING / BUCKETING' ---")
el1 = soup.find(string=re.compile('4 GROUPING / BUCKETING'))
if el1:
    print(el1.parent)
    print(el1.parent.parent)

print("\n--- Checking 'HashSet<E> (Unique Elements)' ---")
el2 = soup.find(string=re.compile('HashSet<E> \(Unique Elements\)'))
if el2:
    print(el2.parent)
    print(el2.parent.parent)

print("\n--- Checking 'MOST USED IN INTERVIEWS' ---")
el3 = soup.find(string=re.compile('MOST USED IN INTERVIEWS'))
if el3:
    print(el3.parent)
    print(el3.parent.parent)


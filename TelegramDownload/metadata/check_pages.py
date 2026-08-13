import os
from bs4 import BeautifulSoup

path = r'C:\Users\rabba\Downloads\TelegramDownload\metadata\1.Array&Hashing_Final.html'
with open(path, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')
    pages = soup.find_all('div', class_='page')
    print('Number of .page divs:', len(pages))
    for i, p in enumerate(pages):
        header = p.find('h1')
        print(f'Page {i+1} header:', header.text.strip() if header else 'None')

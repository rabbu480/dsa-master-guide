import os
from bs4 import BeautifulSoup

path = r'C:\Users\rabba\Downloads\TelegramDownload\metadata\v11\1.Array&Hashing_Final.html'
with open(path, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

sections = soup.find_all('div', class_='section-header')
print('Sections found:')
for i, s in enumerate(sections):
    print(f'{i+1}. {s.text.strip()}')

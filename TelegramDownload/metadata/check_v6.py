from bs4 import BeautifulSoup
import sys

def check():
    with open(r'C:\Users\rabba\Downloads\TelegramDownload\metadata\v6\10.Heaps_Final.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        
    pages = soup.find_all('div', class_='page')
    print(f'Total pages: {len(pages)}')
    for i, p in enumerate(pages):
        h = p.find('div', class_='page-number')
        txt = h.get_text() if h else 'None'
        headers = [x.get_text() for x in p.find_all('h1')]
        print(f'Page {i+1} marked as {txt}, Headers: {headers}')

if __name__ == '__main__':
    check()

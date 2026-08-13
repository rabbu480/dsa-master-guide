from bs4 import BeautifulSoup

def check():
    with open(r'C:\Users\rabba\Downloads\TelegramDownload\metadata\v6\10.Heaps_Final.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        
    examples = soup.find_all('div', string=lambda s: s and 'EXAMPLES' in s)
    for ex in examples:
        parent = ex.parent
        print(parent.get_text(separator=' | ', strip=True))

if __name__ == '__main__':
    check()

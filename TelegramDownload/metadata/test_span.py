from bs4 import BeautifulSoup
with open(r'C:\Users\rabba\Downloads\TelegramDownload\metadata\v3\10.Heaps_Final.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')
span_all = soup.find_all(class_=lambda x: x and 'span-all' in x)
print(f'Heaps has {len(span_all)} span-all boxes.')

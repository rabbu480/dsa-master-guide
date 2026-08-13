import os
from bs4 import BeautifulSoup
v3_dir = r'C:\Users\rabba\Downloads\TelegramDownload\metadata\v3'
for fname in os.listdir(v3_dir):
    if not fname.endswith('.html'): continue
    with open(os.path.join(v3_dir, fname), 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    boxes = soup.find_all('div', class_=lambda x: x and ('section-box' in x or 'box-' in x))
    span_all_boxes = soup.find_all(class_=lambda x: x and 'span-all' in x)
    print(f'{fname}: {len(boxes)} boxes, {len(span_all_boxes)} span-all.')

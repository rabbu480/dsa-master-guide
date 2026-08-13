import re
from bs4 import BeautifulSoup
with open(r'C:\Users\rabba\Downloads\TelegramDownload\metadata\9.Graphs_Final.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

all_boxes = soup.find_all('div', class_='section-box')
in_cols = []
outside_cols = []
for box in all_boxes:
    parent = box.parent
    if parent and parent.get('class') and ('col-left' in parent.get('class') or 'col-right' in parent.get('class')):
        in_cols.append(box)
    else:
        outside_cols.append(box)

print(f"Boxes inside cols: {len(in_cols)}")
print(f"Boxes outside cols: {len(outside_cols)}")

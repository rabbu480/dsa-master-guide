import re
with open(r'C:\Users\rabba\Downloads\TelegramDownload\metadata\6.Binary_Search_Final.html', 'r', encoding='utf-8') as f:
    content = f.read()
# Split by '<div class="page">'
parts = content.split('<div class="page">')
for i, p in enumerate(parts[1:]): # skip the first part before the first page
    print(f'Page {i+1} length: {len(p)}')
    print(f'Page {i+1} snippet: {p[:200].strip()}')
    print('-'*40)

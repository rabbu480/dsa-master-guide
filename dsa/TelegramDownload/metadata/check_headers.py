import re
with open(r'C:\Users\rabba\Downloads\TelegramDownload\metadata\1.Array&Hashing_Final.html', 'r', encoding='utf-8') as f:
    content = f.read()

pages = content.split('<div class="page">')
for i, p in enumerate(pages[1:]):
    headers = re.findall(r'<div class="section-header"[^>]*>(.*?)</div>', p, re.DOTALL)
    print(f'Page {i+1} headers:')
    for h in headers:
        text = re.sub(r'<[^>]+>', '', h).strip()
        print('  ' + text)

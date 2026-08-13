import os
import re
from bs4 import BeautifulSoup

v12_dir = r"C:\Users\rabba\Downloads\TelegramDownload\metadata\v12"

with open(r"C:\Users\rabba\Downloads\TelegramDownload\metadata\summary.txt", "w", encoding="utf-8") as out:
    def summarize(fname):
        out.write(f"\\n=== {fname} ===\\n")
        with open(os.path.join(v12_dir, fname), 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
        
        headers = [h.text.strip() for h in soup.find_all(re.compile('^h[1-3]$'))]
        out.write("Headers: " + str(headers[:10]) + "\\n")
        
        section_titles = [s.text.strip() for s in soup.find_all('div', class_='section-header')]
        out.write("Sections: " + str(section_titles[:10]) + "\\n")

    for f in os.listdir(v12_dir):
        if f.endswith('_Final.html') and 'Array' not in f:
            summarize(f)

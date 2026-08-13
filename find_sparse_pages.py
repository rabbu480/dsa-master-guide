import glob
import os
import re

files = sorted(glob.glob("F:/dsa/bookfinal/*.html"))

for f in files:
    fname = os.path.basename(f)
    if fname == "index.html":
        continue
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        html = fp.read()
    
    # Split by <div class="page"
    pages = html.split('<div class="page"')
    sparse_list = []
    
    for i, p in enumerate(pages[1:], 1):
        # Count words / text length in this page
        # strip tags
        text_only = re.sub(r'<[^>]+>', ' ', p[:p.find('</div><!-- end') if '</div><!-- end' in p else len(p)])
        lines = [l.strip() for l in text_only.split('\n') if l.strip()]
        word_count = len(text_only.split())
        
        if word_count < 120:
            sparse_list.append((i, word_count, len(lines)))
            
    if sparse_list:
        print(f"{fname:38s} | Total: {len(pages)-1:2d} pages | Sparse (<120 words): {sparse_list}")

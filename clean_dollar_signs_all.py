import re
import glob
import os

html_files = glob.glob('F:/dsa/bookfinal/*.html')

print(f"Cleaning raw '$' LaTeX math symbols across {len(html_files)} HTML files...")

def clean_text(text):
    # Replace $O(...) $ with O(...)
    text = re.sub(r'\$O\(([^$]+)\)\$', r'O(\1)', text)
    # Replace $N$ or $M$ or single variable math
    text = re.sub(r'\$([A-Za-z0-9_\-\+\\\ \.\,\/]+)\$', r'\1', text)
    # Clean remaining stray \log, \times, \le, \ge, etc.
    text = text.replace('\\log_2', 'log₂')
    text.replace('\\log', 'log')
    text = text.replace('\\times', '×')
    text = text.replace('\\le', '<=')
    text = text.replace('\\ge', '>=')
    text = text.replace('\\implies', '=>')
    return text

cleaned_count = 0
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = clean_text(content)
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        cleaned_count += 1
        print(f"Cleaned raw math '$' symbols in: {os.path.basename(filepath)}")

print(f"Done! Cleaned math '$' symbols in {cleaned_count} files.")

import os
import glob
import re

V17_DIR = r"F:\dsa\v17"
V18_DIR = r"F:\dsa\v18"

def clean_html(content):
    # 1. Remove all <style>...</style> blocks completely
    content = re.sub(r'<style>.*?</style>', '', content, flags=re.DOTALL)
    
    # 2. Remove all inline style="..." attributes
    content = re.sub(r'\s*style="[^"]*"', '', content)
    
    # 3. Inject our new clean header pointing to style.css
    # We will find the <head> tag and replace everything inside it up to </head>
    clean_head = """<head>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
    <title>FAANG DSA Cheat Sheet</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Fira+Code&display=swap" rel="stylesheet"/>
    <link rel="stylesheet" href="assets/style.css"/>
</head>"""
    
    content = re.sub(r'<head>.*?</head>', clean_head, content, flags=re.DOTALL)
    return content

def main():
    if not os.path.exists(V18_DIR):
        os.makedirs(V18_DIR)
        
    v17_files = glob.glob(os.path.join(V17_DIR, "*.html"))
    for file_path in v17_files:
        filename = os.path.basename(file_path)
        print(f"Refactoring {filename}...")
        
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            html_content = f.read()
            
        cleaned_html = clean_html(html_content)
        
        # Save to V18
        out_path = os.path.join(V18_DIR, filename.replace('_Final', ''))
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_html)
            
        # Check size difference
        orig_size = os.path.getsize(file_path)
        new_size = os.path.getsize(out_path)
        print(f"  -> Reduced from {orig_size//1024}KB to {new_size//1024}KB")

if __name__ == "__main__":
    main()

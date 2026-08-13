import os, sys, shutil, subprocess, fitz

sys.stdout.reconfigure(encoding='utf-8')

src_file = r"F:\dsa\bookfinal - Copy\Topic11_Trie_3.html"
dst_file = r"F:\dsa\bookfinal\Topic11_Trie.html"
pdf_out = r"F:\dsa\bookfinal\Topic11_Trie.pdf"

shutil.copyfile(src_file, dst_file)
print("Successfully copied Topic11_Trie_3.html to", dst_file)

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

if os.path.exists(pdf_out): os.remove(pdf_out)

cmd = [chrome_path, '--headless', '--disable-gpu', '--no-pdf-header-footer', f'--print-to-pdf={pdf_out}', dst_file]
subprocess.run(cmd, check=True)

doc = fitz.open(pdf_out)
print("==========================================")
print(f"Generated Topic 11 PDF Page Count: {len(doc)} pages")
print("==========================================")

for i in range(len(doc)):
    page = doc[i]
    text = page.get_text()
    t_clean = text[:70].replace('\n', ' ')
    print(f"Page {i+1} has {len(text)} chars: {t_clean}")

doc.close()

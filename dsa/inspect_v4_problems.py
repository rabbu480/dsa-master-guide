import re

for topic in ["Topic03_TwoPointers.html", "Topic11_Trie.html"]:
    fpath = f"F:/dsa/bookfinal - Copy/v4/bookfinal/{topic}"
    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
        html = f.read()
    
    print(f"=== {topic} in v4 ===")
    # Find all prow blocks or problem titles
    prows = re.findall(r'<div class=["\']prow["\'][\s\S]*?</div>\s*</div>\s*</div>', html)
    print(f"Found {len(prows)} prow blocks in {topic}.")
    
    titles = re.findall(r'class=["\']ptitle["\'][^>]*>(.*?)</div>', html)
    for i, t in enumerate(titles, 1):
        print(f"  Problem {i}: {t.strip()}")
    print("\n")

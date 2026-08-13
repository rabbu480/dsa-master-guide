import re, sys

sys.stdout.reconfigure(encoding='utf-8')

for topic in ["Topic03_TwoPointers.html", "Topic11_Trie.html"]:
    fpath = f"F:/dsa/bookfinal - Copy/v4/bookfinal/{topic}"
    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
        html = f.read()
    
    print(f"=== {topic} Pages 8 & 9 in v4 ===")
    pages = re.split(r'<!-- PAGE \d+:', html)[1:]
    if len(pages) >= 9:
        p8 = pages[7]
        p9 = pages[8]
        print("Page 8 snippet:")
        print(p8[:600])
        print("\nPage 9 snippet:")
        print(p9[:600])
    print("\n")

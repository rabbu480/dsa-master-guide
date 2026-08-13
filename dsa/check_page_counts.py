import glob
import os
from bs4 import BeautifulSoup

html_files = sorted(glob.glob("F:/dsa/bookfinal/*.html"))

total_pages = 0
print("=== FAANG DSA HANDBOOK PAGE COUNT CHECK ===")
for filepath in html_files:
    filename = os.path.basename(filepath)
    with open(filepath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
    pages = soup.find_all("div", class_="page")
    num_pages = len(pages)
    total_pages += num_pages
    print(f"{filename:42s} : {num_pages:2d} Pages")

print("=" * 45)
print(f"TOTAL HANDBOOK PAGES: {total_pages}")

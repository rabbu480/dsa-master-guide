import glob, os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

v4_dir = r"F:\dsa\bookfinal - Copy\v4\bookfinal"
v4_files = sorted(glob.glob(os.path.join(v4_dir, "Topic*.html")))

print(f"{'Filename':<35} | {'v4 Pages':<10}")
print("-" * 50)

for fpath in v4_files:
    bname = os.path.basename(fpath)
    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
        html = f.read()
    pages = re.split(r'<!-- PAGE \d+:', html)[1:]
    print(f"{bname:<35} | {len(pages):<10}")

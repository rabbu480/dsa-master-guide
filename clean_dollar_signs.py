import glob
import re
import os

html_files = glob.glob("F:/dsa/bookfinal/*.html")

for filepath in html_files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Clean up LaTeX math $...$ delimiters
    # Replace $O(...) $ with O(...)
    cleaned = re.sub(r'\$O\((.*?)\)\$', r'O(\1)', content)
    cleaned = re.sub(r'\$([0-9A-Za-z_\\\+\-\*\/\^ \(\)]+)\$', r'\1', cleaned)
    cleaned = cleaned.replace("\\le", "<=")
    cleaned = cleaned.replace("\\ge", ">=")
    cleaned = cleaned.replace("\\alpha", "alpha")
    cleaned = cleaned.replace("\\cdot", "·")
    cleaned = cleaned.replace("\\approx", "≈")
    cleaned = cleaned.replace("\\to", "->")
    cleaned = cleaned.replace("\\rightarrow", "->")

    if cleaned != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(cleaned)
        print(f"Cleaned math dollar signs in {os.path.basename(filepath)}")

print("Dollar sign cleanup complete!")

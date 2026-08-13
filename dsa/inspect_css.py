import re

for filename in ["Topic01_Foundations_BigO.html", "Topic02_Arrays_Strings_Hashing.html", "Topic03_TwoPointers.html"]:
    filepath = f"F:/dsa/bookfinal/{filename}"
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        html = f.read()
    
    print(f"=== {filename} ===")
    # Print body style, .page style, and @media print style
    m_body = re.search(r'body\s*\{[^}]*\}', html)
    m_page = re.search(r'\.page\s*\{[^}]*\}', html)
    m_print = re.search(r'@media print\s*\{[\s\S]*?\n\}', html)
    
    if m_body: print("BODY:", m_body.group(0))
    if m_page: print("PAGE:", m_page.group(0))
    if m_print: print("PRINT:", m_print.group(0))
    print("\n")

import re

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'<div class=["\']page["\']', text)
print("TOPIC 03 PAGE DIV MATCHES:", len(matches))

# Let's count page headers
ph_matches = re.findall(r'<div class=["\']ph["\']', text)
print("TOPIC 03 PH HEADER MATCHES:", len(ph_matches))

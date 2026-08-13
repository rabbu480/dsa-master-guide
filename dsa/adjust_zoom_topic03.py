import re

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace zoom: 0.76 with zoom: 0.73 in print CSS
text = text.replace('zoom: 0.76;', 'zoom: 0.73;')

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("=== ADJUSTED ZOOM TO 0.73 IN TOPIC 03 ===")

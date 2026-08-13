import re

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Make CSS print zoom 0.65 in Topic 03 CSS rule
text = re.sub(r'zoom:\s*0\.76;', 'zoom: 0.65;', text)

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("=== SET PRINT ZOOM TO 0.65 IN TOPIC 03 ===")

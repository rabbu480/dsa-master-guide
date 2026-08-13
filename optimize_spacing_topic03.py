import re

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Make pre, code, table, box slightly more compact in Topic03 CSS so Chrome fits into 5 pages!
text = text.replace('font-size: 11px;', 'font-size: 10px;')
text = text.replace('line-height: 1.36;', 'line-height: 1.28;')
text = text.replace('font-size: 0.70rem;', 'font-size: 0.65rem;')
text = text.replace('font-size: 0.76rem;', 'font-size: 0.70rem;')
text = text.replace('font-size: 0.75rem;', 'font-size: 0.70rem;')
text = text.replace('font-size: 0.78rem;', 'font-size: 0.72rem;')
text = text.replace('font-size: 0.80rem;', 'font-size: 0.75rem;')
text = text.replace('font-size: 0.88rem;', 'font-size: 0.80rem;')

text = text.replace('padding: 10px 12px;', 'padding: 5px 8px;')
text = text.replace('padding: 8px 10px;', 'padding: 4px 6px;')
text = text.replace('margin-bottom: 12px;', 'margin-bottom: 6px;')
text = text.replace('margin-bottom: 14px;', 'margin-bottom: 6px;')

with open('F:/dsa/bookfinal/Topic03_TwoPointers.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("=== OPTIMIZED COMPACTNESS FOR TOPIC 03 ===")

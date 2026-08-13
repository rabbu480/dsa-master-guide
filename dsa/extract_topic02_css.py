import re
with open('F:/dsa/bookfinal/Topic02_Arrays_Strings_Hashing.html', 'r', encoding='utf-8') as f:
    t = f.read()
# Extract the @media print block
m = re.search(r'@page[\s\S]*?(?=</style>)', t)
if m:
    print(m.group(0)[:3000])
print("\n\n--- Page div count ---")
print(len(re.findall('<div class="page">', t)))

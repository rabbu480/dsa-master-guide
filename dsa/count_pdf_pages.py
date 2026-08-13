with open('F:/dsa/bookfinal/Topic03_TwoPointers.pdf', 'rb') as f:
    content = f.read()

# Count /Page type dictionary entries 
count1 = content.count(b'/Type /Page\n')
count2 = content.count(b'/Type/Page\n')
count3 = content.count(b'/Type /Page\r')
count4 = content.count(b'/Type/Page\r')
print(f'PDF page objects: {count1 + count2 + count3 + count4}')

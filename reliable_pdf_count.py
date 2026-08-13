import os, datetime

pdf_path = r'F:\dsa\bookfinal\Topic03_TwoPointers.pdf'
stat = os.stat(pdf_path)
print(f"PDF file size: {stat.st_size} bytes")
print(f"PDF last modified: {datetime.datetime.fromtimestamp(stat.st_mtime)}")

with open(pdf_path, 'rb') as f:
    content = f.read()

# Check count of /Page dictionary entries (most reliable method)
import re
count = len(re.findall(rb'/Type\s*/Page\b', content))
print(f"PDF /Type /Page objects: {count}")

# Also check via /Pages 
pages_count = re.search(rb'/Count\s+(\d+)', content)
if pages_count:
    print(f"PDF /Count value: {pages_count.group(1).decode()}")

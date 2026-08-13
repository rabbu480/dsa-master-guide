import re

with open('F:/dsa/bookfinal/Topic06_LinkedList.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace main layout container nesting if broken
# Check how many <div class="page"> are in text
pages = text.split('<div class="page">')
print("Topic06 page count:", len(pages) - 1)

# Ensure each page starts with <div class="page"> and ends with </div>
parts = text.split('<div class="page">')
header = parts[0]
page_bodies = parts[1:]

cleaned_pages = []
for p in page_bodies:
    # Find matching body before next page or end of main-content
    body = p.split('</div>\n\n<div class="page">')[0]
    # Remove tail closing divs if present
    body = re.sub(r'</div>\s*</div>\s*</div>\s*</body>[\s\S]*$', '', body)
    cleaned_pages.append('<div class="page">\n' + body.strip() + '\n</div>')

new_doc = header + "\n\n".join(cleaned_pages) + "\n\n</div>\n</div>\n</div>\n</body>\n</html>"

with open('F:/dsa/bookfinal/Topic06_LinkedList.html', 'w', encoding='utf-8') as f:
    f.write(new_doc)

print("Topic06 nesting fixed!")

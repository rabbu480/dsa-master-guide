import re

filepath = 'F:/dsa/bookfinal/Topic05_BinarySearch.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix pattern: move rule-box before the closing </div> of the page wrapper
# Pattern in file: </div> \n\n <div class="rule-box...</div> \n </div>
pattern = r'(\s*</div>\s*)(<div class="rule-box[^>]*>.*?</div>)(\s*</div>)'

def fix_nesting(match):
    rule_box = match.group(2)
    return f"\n            {rule_box}\n        </div>"

content = re.sub(pattern, fix_nesting, content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed Topic 05 inner div nesting successfully!")

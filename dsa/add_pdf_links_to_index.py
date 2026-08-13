import re

with open('F:/dsa/bookfinal/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace all card-actions blocks to include both Open HTML and Open PDF buttons with target="_blank"
def fix_card_actions(match):
    topic_match = re.search(r'href="(Topic\d+_[^"]+\.html|Book2_[^"]+\.html)"', match.group(0))
    if topic_match:
        html_file = topic_match.group(1)
        pdf_file = html_file.replace('.html', '.pdf')
        return f'''<div class="card-actions">
                <a href="{html_file}" class="card-btn btn-html" target="_blank">📖 Open HTML</a>
                <a href="{pdf_file}" class="card-btn btn-pdf" target="_blank">📄 Open PDF</a>
            </div>'''
    return match.group(0)

new_html = re.sub(r'<div class="card-actions">[\s\S]*?</div>', fix_card_actions, html)

with open('F:/dsa/bookfinal/index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("=== ADDED DEDICATED PDF HYPERLINKS WITH TARGET=_BLANK TO INDEX.HTML ===")

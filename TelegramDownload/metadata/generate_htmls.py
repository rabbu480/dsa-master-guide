import os
import glob
import markdown
import re
from bs4 import BeautifulSoup

base_dir = r"C:\Users\rabba\Downloads\TelegramDownload\metadata"
topics = [
    "1.Array&Hashing",
    "6.Binary_Search",
    "8.Trees",
    "9.Graphs",
    "10.Heaps"
]

css = """
<style>
    :root {
        --bg-color: #0f172a;
        --card-bg: #1e293b;
        --text-main: #f8fafc;
        --text-muted: #94a3b8;
        --accent: #38bdf8;
        --accent-secondary: #f59e0b;
        --accent-tertiary: #10b981;
        --border-color: #334155;
    }
    body {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        background-color: var(--bg-color);
        color: var(--text-main);
        line-height: 1.6;
        margin: 0;
        padding: 40px;
    }
    .page-title {
        text-align: center;
        font-size: 3rem;
        font-weight: 800;
        color: var(--accent);
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 50px;
        border-bottom: 2px solid var(--border-color);
        padding-bottom: 20px;
    }
    /* Masonry / Multi-column layout */
    .masonry {
        column-count: 2;
        column-gap: 30px;
    }
    @media (max-width: 1000px) {
        .masonry { column-count: 1; }
    }
    /* Cards for each section */
    .card {
        background: var(--card-bg);
        border: 1px solid var(--border-color);
        border-radius: 12px;
        padding: 24px;
        margin-bottom: 30px;
        break-inside: avoid;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.2);
    }
    .card > h2 {
        margin-top: 0;
        color: #fff;
        font-size: 1.5rem;
        border-left: 5px solid var(--accent-secondary);
        padding-left: 12px;
        margin-bottom: 20px;
    }
    h1, h3, h4, h5, h6 {
        color: var(--accent);
        margin-top: 24px;
        margin-bottom: 16px;
    }
    h1 { font-size: 2em; }
    h3 { font-size: 1.25em; border-bottom: 1px solid var(--border-color); padding-bottom: 8px;}
    p, ul, ol {
        color: #e2e8f0;
        margin-bottom: 16px;
    }
    li {
        margin-bottom: 8px;
    }
    strong {
        color: var(--accent-secondary);
        font-weight: 700;
    }
    em {
        color: var(--text-muted);
    }
    pre {
        background-color: #020617;
        border: 1px solid var(--border-color);
        border-radius: 8px;
        padding: 16px;
        overflow-x: auto;
        font-family: 'Fira Code', monospace;
        font-size: 0.9em;
        margin-bottom: 16px;
    }
    code {
        background-color: #020617;
        color: #a5b4fc;
        padding: 2px 6px;
        border-radius: 4px;
        font-family: 'Fira Code', monospace;
        font-size: 0.9em;
    }
    pre code {
        background-color: transparent;
        padding: 0;
    }
    table {
        width: 100%;
        border-collapse: collapse;
        margin-bottom: 20px;
        background: #0f172a;
        border-radius: 8px;
        overflow: hidden;
    }
    th {
        background: #2563eb;
        color: white;
        text-align: left;
        padding: 12px 16px;
        font-weight: 600;
    }
    td {
        padding: 12px 16px;
        border-bottom: 1px solid var(--border-color);
    }
    tr:last-child td { border-bottom: none; }
    blockquote {
        border-left: 4px solid var(--accent-tertiary);
        background: #1e293b;
        padding: 16px 20px;
        margin: 0 0 20px 0;
        border-radius: 0 8px 8px 0;
        font-style: italic;
    }
    img {
        max-width: 100%;
        border-radius: 8px;
        margin-bottom: 16px;
    }
    .page-indicator {
        text-align: center;
        font-size: 0.9rem;
        color: var(--text-muted);
        margin: 40px 0;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* PRINT STYLES */
    @media print {
        body { background: white; color: black; padding: 0; margin: 0; }
        .page-title { color: black; border-bottom: 2px solid #ccc; }
        .card { background: white; border: 1px solid #ccc; box-shadow: none; break-inside: avoid; }
        .card > h2 { color: black; border-left-color: #3b82f6; }
        h1, h3, h4 { color: black; }
        strong { color: #d97706; }
        pre { background: #f1f5f9; border: 1px solid #ccc; }
        code { color: #b91c1c; background: #f1f5f9; }
        table { border: 1px solid #ccc; background: white; }
        th { background: #3b82f6; color: white; }
        tr:nth-child(even) td { background: #f8fafc; }
        .masonry { column-count: 2; column-gap: 20px; }
        .page-break { page-break-before: always; }
        .page-indicator { display: none; }
    }
</style>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=Fira+Code&display=swap" rel="stylesheet">
"""

html_template = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{title}</title>
    {css}
</head>
<body>
    <h1 class="page-title">{title}</h1>
    {content}
</body>
</html>
"""

def extract_number(filename):
    basename = os.path.basename(filename)
    match = re.search(r'^(\d+)\.', basename)
    if match:
        return int(match.group(1))
    return 9999

for topic in topics:
    topic_dir = os.path.join(base_dir, topic)
    if not os.path.exists(topic_dir):
        continue
        
    md_files = glob.glob(os.path.join(topic_dir, "*.md"))
    md_files.sort(key=extract_number)
    
    if not md_files:
        continue
        
    print(f"Processing {topic} ({len(md_files)} files)...")
    
    # We will build a single beautifulSoup tree and then restructure it
    combined_md = ""
    for md_file in md_files:
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()
            # If the md file starts with # Title, we might want to downgrade it to h2
            # because we already have a master title.
            # But let's just parse it as is first.
            combined_md += content + "\n\n<!-- PAGE_BREAK -->\n\n"
            
    # Convert all markdown to html
    raw_html = markdown.markdown(combined_md, extensions=['fenced_code', 'tables'])
    
    soup = BeautifulSoup(raw_html, 'html.parser')
    
    # We want to group everything under an <h2> into a .card div.
    # If there are <h1> elements, we can treat them similarly or just turn them into h2
    for h1 in soup.find_all('h1'):
        h1.name = 'h2'
        
    # We will construct a new soup
    new_soup = BeautifulSoup('<div class="masonry"></div>', 'html.parser')
    masonry = new_soup.div
    
    current_card = None
    
    # Iterate over all top level elements in the body
    for element in list(soup.children):
        if element.name is None: 
            # NavigableString
            if str(element).strip() == "":
                continue
            if current_card:
                current_card.append(element.extract())
            else:
                pass # skip loose text at top
        elif str(element).strip() == "<!-- PAGE_BREAK -->":
            # Just ignore page breaks inside the masonry, the cards will flow naturally.
            # Or add a visual indicator
            indicator = new_soup.new_tag('div', attrs={'class':'page-indicator'})
            indicator.string = "--- Next Page ---"
            if current_card:
                current_card.append(indicator)
        elif element.name == 'h2':
            # Create a new card
            current_card = new_soup.new_tag('div', attrs={'class': 'card'})
            masonry.append(current_card)
            current_card.append(element.extract())
        else:
            if current_card:
                current_card.append(element.extract())
            else:
                # If there's content before any h2, wrap it in a card too
                current_card = new_soup.new_tag('div', attrs={'class': 'card'})
                masonry.append(current_card)
                current_card.append(element.extract())

    final_html = html_template.format(
        title=topic.replace("_", " "),
        css=css,
        content=str(new_soup)
    )
    
    output_file = os.path.join(base_dir, f"{topic}.html")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(final_html)
        
    print(f"Created {output_file}")

print("All HTML files generated with beautiful layout successfully.")

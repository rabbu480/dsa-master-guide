import re

toc_configs = {
    "Topic02_Arrays_Strings_Hashing.html": [
        ("02.0 Arrays & Strings", "#page1"),
        ("02.0 HashMap Internals", "#page2"),
        ("02.0 Pattern Recognition", "#page3"),
        ("02.1 Contains Dup & Anagram", "#page4"),
        ("02.1 Two Sum & Group Anagrams", "#page5"),
        ("02.1 Top K & Product Array", "#page6"),
        ("02.1 Valid Sudoku & Encode", "#page7"),
        ("02.1 Longest Consecutive", "#page8"),
        ("02.2 Edge Cases & Failures", "#page9"),
        ("02.3 Master Revision Sheet", "#page10"),
    ],
    "Topic03_TwoPointers.html": [
        ("03.0 Two Pointers Found", "#page1"),
        ("03.1 Opposite Direction", "#page2"),
        ("03.2 Same Direction", "#page3"),
        ("03.3 Dutch National Flag", "#page4"),
        ("03.4 Recognition Matrix", "#page5"),
        ("03.5 Valid Palindrome & 2Sum", "#page6"),
        ("03.5 Remove Dup & Move Zeroes", "#page7"),
        ("03.5 Merge Sorted Array", "#page8"),
        ("03.5 Three Sum & Sort Colors", "#page9"),
        ("03.5 String Compression", "#page10"),
        ("03.5 Container Water & Rain", "#page11"),
        ("03.6 Master Revision Sheet", "#page12"),
    ],
    "Topic04_SlidingWindow.html": [
        ("04.0 Sliding Window Found", "#page1"),
        ("04.1 Fixed Size Window", "#page2"),
        ("04.2 Variable Size Window", "#page3"),
        ("04.3 Frequency Array Win", "#page4"),
        ("04.4 Recognition Matrix", "#page5"),
        ("04.5 Buy/Sell Stock & Subarray", "#page6"),
        ("04.5 Longest Substring & Rep", "#page7"),
        ("04.5 Permutation & Anagrams", "#page8"),
        ("04.5 Fruit Baskets & Subarray", "#page9"),
        ("04.5 Min Window Substring", "#page10"),
        ("04.5 Subarrays K Distinct", "#page11"),
        ("04.6 Master Revision Sheet", "#page12"),
    ],
    "Topic05_BinarySearch.html": [
        ("05.0 BS Foundation", "#page1"),
        ("05.1 Classic & Boundary", "#page2"),
        ("05.3 Answer & 2D Matrix", "#page3"),
        ("05.6 Recognition & Toolkit", "#page4"),
        ("05.7 Easy NeetCode Suite", "#page5"),
        ("05.7 2D Matrix & Rotated", "#page6"),
        ("05.7 Min Rotated & Koko", "#page7"),
        ("05.7 Find Peak & Time Value", "#page8"),
        ("05.7 Split Array & Median", "#page9"),
        ("05.8 Master Revision Sheet", "#page10"),
    ]
}

css_to_add = """
    /* Sticky Sidebar Layout */
    .app-layout {
        display: grid;
        grid-template-columns: 220px 1fr;
        gap: 20px;
        align-items: start;
    }

    .toc-sidebar {
        position: sticky;
        top: 60px;
        background: white;
        border: 2px solid #3b82f6;
        border-radius: 8px;
        padding: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }
    [data-theme="dark"] .toc-sidebar { background: #1e293b; border-color: #38bdf8; }

    .toc-title { font-weight: 900; font-size: 0.85rem; color: #1e3a8a; margin-bottom: 8px; text-transform: uppercase; border-bottom: 2px solid #3b82f6; padding-bottom: 4px; }
    [data-theme="dark"] .toc-title { color: #38bdf8; }
    .toc-list { list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 4px; }
    .toc-link { color: #334155; text-decoration: none; font-weight: 700; font-size: 0.75rem; padding: 3px 6px; border-radius: 4px; display: block; transition: all 0.2s; }
    [data-theme="dark"] .toc-link { color: #cbd5e1; }
    .toc-link:hover { background: #2563eb; color: white; }

    .main-content { min-width: 0; }
"""

for filename, sections in toc_configs.items():
    filepath = f"F:/dsa/bookfinal/{filename}"
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if "toc-sidebar" in content:
        print(f"Skipping {filename}, already has toc-sidebar")
        continue

    # Add CSS
    content = content.replace("</style>", css_to_add + "\n</style>")
    
    # Add print rule to hide sidebar
    content = content.replace(".top-nav, .back-to-top { display: none !important; }", ".top-nav, .back-to-top, .toc-sidebar { display: none !important; }\n        .app-layout { display: block !important; }")
    content = content.replace(".top-nav { display: none !important; }", ".top-nav, .toc-sidebar { display: none !important; }\n        .app-layout { display: block !important; }")

    # Build Sidebar HTML
    toc_items_html = "\n".join([f'            <li><a href="{link}" class="toc-link">{title}</a></li>' for title, link in sections])
    sidebar_html = f"""<div class="app-layout">
    <!-- Sticky Table of Contents Sidebar -->
    <div class="toc-sidebar">
        <div class="toc-title">📋 SECTIONS</div>
        <ul class="toc-list">
{toc_items_html}
        </ul>
    </div>

    <!-- Main Content Pages -->
    <div class="main-content">"""

    # Insert after <div class="container">
    content = content.replace('<div class="container">', '<div class="container">\n' + sidebar_html, 1)

    # Insert closing tags before floating back-to-top button or script
    if '<!-- Floating Back to Top Button -->' in content:
        content = content.replace('<!-- Floating Back to Top Button -->', '    </div> <!-- end .main-content -->\n</div> <!-- end .app-layout -->\n\n<!-- Floating Back to Top Button -->')
    elif '<script>' in content:
        content = content.replace('<script>', '    </div> <!-- end .main-content -->\n</div> <!-- end .app-layout -->\n\n<script>')
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Successfully added sticky TOC sidebar to {filename}!")

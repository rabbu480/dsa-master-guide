import glob
import re

files = glob.glob('F:/dsa/bookfinal/*.html')

toc_script = """
<script>
    function toggleTheme() {
        document.body.getAttribute('data-theme') === 'dark' ? document.body.removeAttribute('data-theme') : document.body.setAttribute('data-theme', 'dark');
    }
    function toggleSidebar() {
        const layout = document.getElementById('appLayout') || document.querySelector('.app-layout');
        const btn = document.querySelector('.shrink-btn span');
        if (layout) {
            layout.classList.toggle('shrunk');
            if (btn) {
                btn.innerText = layout.classList.contains('shrunk') ? '➕ Expand' : '➖ Shrink';
            }
        }
    }
</script>
"""

css_patch = """
    .app-layout {
        display: grid;
        grid-template-columns: 240px 1fr;
        gap: 15px;
        align-items: start;
        transition: grid-template-columns 0.3s ease;
    }
    .app-layout.shrunk {
        grid-template-columns: 60px 1fr;
    }
    .toc-sidebar {
        position: sticky;
        top: 60px;
        background: white;
        border: 2px solid #3b82f6;
        border-radius: 8px;
        padding: 10px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        transition: all 0.3s ease;
        overflow: hidden;
    }
    [data-theme="dark"] .toc-sidebar { background: #1e293b; border-color: #38bdf8; }
    .toc-header-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 2px solid #3b82f6;
        padding-bottom: 4px;
        margin-bottom: 8px;
    }
    .toc-title { font-weight: 900; font-size: 0.82rem; color: #1e3a8a; text-transform: uppercase; margin: 0; }
    [data-theme="dark"] .toc-title { color: #38bdf8; }
    .shrink-btn {
        background: #e0e7ff;
        color: #1e40af;
        border: 1px solid #93c5fd;
        border-radius: 4px;
        padding: 2px 6px;
        font-size: 0.68rem;
        font-weight: 800;
        cursor: pointer;
    }
    .shrink-btn:hover { background: #2563eb; color: white; }
    .app-layout.shrunk .toc-title, .app-layout.shrunk .toc-text { display: none; }
    .app-layout.shrunk .toc-sidebar { padding: 6px; text-align: center; }
"""

updated_count = 0
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    # 1. Add id="appLayout" to app-layout if missing
    content = content.replace('<div class="app-layout">', '<div class="app-layout" id="appLayout">')
    
    # 2. Add shrink-btn inside toc-sidebar
    if 'shrink-btn' not in content:
        content = re.sub(
            r'<div class="toc-title">\s*📋 SECTIONS\s*</div>',
            '<div class="toc-header-bar"><span class="toc-title">📋 SECTIONS</span><button class="shrink-btn" onclick="toggleSidebar()"><span class="toc-text">➖ Shrink</span></button></div>',
            content
        )
    
    # 3. Add top nav button if missing
    if 'Expand/Shrink TOC' not in content:
        content = re.sub(
            r'(<button class="nav-btn" onclick="toggleTheme\(\)">[^<]*</button>)',
            r'\1\n        <button class="nav-btn" onclick="toggleSidebar()">↕️ Expand/Shrink TOC</button>',
            content
        )
    
    # 4. Inject CSS patch if missing
    if '.app-layout.shrunk' not in content:
        content = content.replace('</style>', f'{css_patch}\n</style>')
        
    # 5. Inject JS script if toggleSidebar missing
    if 'function toggleSidebar()' not in content:
        content = re.sub(r'<script>\s*function toggleTheme\(\).*?</script>', toc_script, content, flags=re.DOTALL)
    
    with open(f, 'w', encoding='utf-8') as fp:
        fp.write(content)
    updated_count += 1

print(f'Successfully updated {updated_count} HTML files with Expand/Shrink TOC sidebar functionality!')

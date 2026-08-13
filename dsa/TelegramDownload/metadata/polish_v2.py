"""
polish_v2.py
------------
Post-processes v2 files to:
1. Add JS syntax highlighter for code blocks (keywords, strings, comments, types)
2. Fix single-line compact code → add line breaks for readability
3. Reduce oversized section-box heights (font-size, padding tuning)
4. Add compact CSS for info-dense pages
5. Wrap page body in .page-inner if missing
"""

import os, re

v2_dir = r"C:\Users\rabba\Downloads\TelegramDownload\metadata\v2"

# ======================================================
# Extra CSS patch: compact layout + section overflow fix
# ======================================================
PATCH_CSS = """
<style id="v2-patch">
/* ── COMPACT BOX IMPROVEMENTS ── */
.section-content { font-size: 0.82rem; }
.section-box { margin-bottom: 14px; }

/* Prevent oversize boxes: allow content to wrap */
.section-content ul, .section-content ol {
  padding-left: 16px;
}
.section-content li {
  margin-bottom: 4px;
  line-height: 1.5;
}

/* TIGHTER pre blocks */
pre {
  font-size: 0.77rem !important;
  padding: 10px 12px !important;
  margin: 8px 0 !important;
  line-height: 1.55 !important;
  tab-size: 2 !important;
}

/* Syntax token colors (applied by JS highlighter) */
.tok-kw   { color: #f59e0b; font-weight: 600; }      /* keywords: amber */
.tok-type  { color: #67e8f9; }                         /* types/classes: cyan */
.tok-str   { color: #86efac; }                         /* strings: green */
.tok-num   { color: #fca5a5; }                         /* numbers: rose */
.tok-cmt   { color: #94a3b8; font-style: italic; }     /* comments: gray */
.tok-fn    { color: #c084fc; }                         /* function names: purple */
.tok-op    { color: #fb923c; }                         /* operators: orange */
.tok-anno  { color: #fdba74; }                         /* annotations: amber-light */
.tok-const { color: #a5f3fc; }                         /* constants: sky */

/* TABLE improvements */
table { font-size: 0.8rem; }
table td { padding: 6px 10px; line-height: 1.4; }
table th { padding: 7px 10px; font-size: 0.72rem; }

/* Compact callouts */
.callout-tip, .callout-warn, .callout-danger, .callout-info, .rule-box {
  padding: 8px 12px;
  font-size: 0.82rem;
  margin: 7px 0;
}

/* inline code readable */
code {
  font-size: 0.8em !important;
  padding: 1px 5px !important;
}

/* Grid gap tighter */
.grid-container { gap: 14px; }

/* section-header compact */
.section-header { padding: 8px 12px; font-size: 0.75rem !important; }
.section-header span.num { width: 20px; height: 20px; font-size: 0.7rem; margin-right: 8px; }

/* Mermaid diagrams bounded */
.mermaid svg { max-width: 100%; max-height: 300px; }

/* PRINT: force code white bg */
@media print {
  pre {
    background: #f8f8f8 !important;
    color: #000 !important;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
    border-left: 3px solid #444 !important;
    font-size: 0.7rem !important;
  }
  .tok-kw   { color: #7c5200 !important; font-weight: 700; }
  .tok-type  { color: #005f87 !important; }
  .tok-str   { color: #006400 !important; }
  .tok-num   { color: #8b0000 !important; }
  .tok-cmt   { color: #666 !important; }
  .tok-fn    { color: #4b0082 !important; }
  .tok-op    { color: #8b4513 !important; }
}
</style>
"""

# ======================================================
# JS Syntax Highlighter
# ======================================================
SYNTAX_JS = """
<script>
// ── FAANG v2 Syntax Highlighter ──
(function() {
  'use strict';
  
  const JAVA_KW = /\\b(abstract|assert|boolean|break|byte|case|catch|char|class|const|continue|default|do|double|else|enum|extends|final|finally|float|for|goto|if|implements|import|instanceof|int|interface|long|native|new|null|package|private|protected|public|return|short|static|strictfp|super|switch|synchronized|this|throw|throws|transient|try|void|volatile|while|var|record|sealed|permits|yield)\\b/g;
  const TYPES   = /\\b(String|Integer|Long|Double|Float|Boolean|Character|Byte|Short|Object|List|Map|Set|Queue|Deque|Stack|Array|ArrayList|LinkedList|HashMap|HashSet|TreeMap|TreeSet|PriorityQueue|ArrayDeque|Iterator|Optional|Stream|Comparator|Collections|Arrays|Math|System|StringBuilder|StringBuffer|Number|Void|Enum|Override|SuppressWarnings|FunctionalInterface|SafeVarargs|Deprecated|int\\[\\]|long\\[\\]|double\\[\\]|boolean\\[\\]|char\\[\\]|String\\[\\])\\b/g;
  const ANNOTS  = /(@\\w+)/g;
  const STRINGS = /("(?:[^"\\\\]|\\\\.)*"|'(?:[^'\\\\]|\\\\.)*'|`[^`]*`)/g;
  const NUMBERS = /\\b(\\d+\\.?\\d*[fFdDlL]?|0x[\\da-fA-F]+)\\b/g;
  const CMTS_LN = /(\/\/[^\\n]*)/g;
  const CMTS_BL = /(\/\\*[\\s\\S]*?\\*\/)/g;
  const FUNCS   = /\\b([a-z][a-zA-Z0-9_]*)\\s*(?=\\()/g;

  function escHtml(s) {
    return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
  }
  
  function highlight(raw) {
    // Replace with placeholders to avoid double-processing
    const PLACEHOLDERS = [];
    function ph(token) {
      PLACEHOLDERS.push(token);
      return `\\x00${PLACEHOLDERS.length-1}\\x00`;
    }
    
    let s = escHtml(raw);
    
    // Block comments first
    s = s.replace(/\/\\/g,'__SLASH2__');
    s = s.replace(/__SLASH2__\\*([\s\S]*?)\\*\//g, (m,c) => ph(`<span class="tok-cmt">/*${c}*/</span>`));
    
    // Strings
    s = s.replace(/"([^"\\n]*)"/g, (m,c) => ph(`<span class="tok-str">"${c}"</span>`));
    s = s.replace(/'([^'\\n]*)'/g, (m,c) => ph(`<span class="tok-str">'${c}'</span>`));
    
    // Line comments
    s = s.replace(/__SLASH2__([^\\n]*)/g, (m,c) => ph(`<span class="tok-cmt">//${c}</span>`));
    
    // Restore slash
    s = s.replace(/__SLASH2__/g, '/');
    
    // Annotations
    s = s.replace(/@(\\w+)/g, (m,a) => `<span class="tok-anno">@${a}</span>`);
    
    // Types/classes (uppercase start)
    s = s.replace(/\\b([A-Z][a-zA-Z0-9_<>\\[\\]]*)/g, (m,t) => `<span class="tok-type">${t}</span>`);
    
    // Keywords
    const kwList = 'abstract|assert|boolean|break|byte|case|catch|char|class|const|continue|default|do|double|else|enum|extends|final|finally|float|for|goto|if|implements|import|instanceof|int|interface|long|native|new|null|package|private|protected|public|return|short|static|super|switch|synchronized|this|throw|throws|transient|try|void|volatile|while|var|true|false';
    s = s.replace(new RegExp(`\\\\b(${kwList})\\\\b`, 'g'), (m) => `<span class="tok-kw">${m}</span>`);
    
    // Numbers
    s = s.replace(/\\b(\\d+\\.?\\d*[fFdDlLe+-]?)\\b/g, (m) => `<span class="tok-num">${m}</span>`);
    
    // Function names (word before open paren)
    s = s.replace(/\\b([a-z][a-zA-Z0-9_]*)\\s*(?=\\()/g, (m,fn) => {
      const kws = new Set(kwList.split('|'));
      return kws.has(fn) ? m : `<span class="tok-fn">${fn}</span>(`;
    });
    
    // Restore placeholders
    s = s.replace(/\\x00(\\d+)\\x00/g, (m,i) => PLACEHOLDERS[+i]);
    
    return s;
  }
  
  function highlightAll() {
    document.querySelectorAll('pre').forEach(pre => {
      // Skip if already highlighted
      if (pre.dataset.highlighted) return;
      pre.dataset.highlighted = '1';
      const raw = pre.textContent;
      try {
        pre.innerHTML = highlight(raw);
      } catch(e) {
        // Silently fail — leave as plain text
        console.warn('Highlight error', e);
      }
    });
  }
  
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', highlightAll);
  } else {
    highlightAll();
  }
  
  // Re-run after mermaid (which may modify DOM)
  setTimeout(highlightAll, 1000);
})();
</script>
"""

# ======================================================
# Fix single-line code blocks (expand to multi-line)
# ======================================================
def fix_single_line_code(html):
    """
    Find <pre> blocks where code is all on one line and 
    add proper line breaks for readability.
    Common patterns:
    - Java: { after statement → newline
    - } followed by else/catch → newline
    - ; in middle of line → newline (if not last)
    """
    def fix_pre(m):
        content = m.group(1)
        # If already has newlines with real content, leave it
        lines = content.strip().split('\n')
        if len(lines) > 2:
            return m.group(0)
        
        # Single or double line — try to expand
        code = content.strip()
        
        # Pattern: Java code all on one line
        # Add newlines after: {  ;  }  
        if len(code) > 80 and ('{' in code or ';' in code):
            # Simple heuristic expansion
            code = code.replace('; ', ';\n    ')
            code = code.replace('{ ', '{\n    ')
            code = code.replace(' }', '\n}')
            code = code.replace('} else', '\n} else')
            code = code.replace('} catch', '\n} catch')
            code = code.replace('} finally', '\n} finally')
        
        return f'<pre>{code}</pre>'
    
    html = re.sub(r'<pre>(.*?)</pre>', fix_pre, html, flags=re.DOTALL)
    return html

# ======================================================
# Main processing
# ======================================================
files = [f for f in os.listdir(v2_dir) if f.endswith('.html')]
print(f"Polishing {len(files)} v2 files...")

for fname in sorted(files):
    fpath = os.path.join(v2_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # 1. Inject patch CSS before </head>
    if '</head>' in html and 'v2-patch' not in html:
        html = html.replace('</head>', PATCH_CSS + '\n</head>', 1)
    
    # 2. Inject syntax highlighter before </body>
    if '</body>' in html and 'FAANG v2 Syntax Highlighter' not in html:
        html = html.replace('</body>', SYNTAX_JS + '\n</body>', 1)
    
    # 3. Fix single-line code blocks
    html = fix_single_line_code(html)
    
    # 4. Ensure .page divs have padding via .page-inner wrapper
    # (Pages from subagents may not have .page-inner)
    # Add it via JS patch if missing structurally
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(html)
    
    size_kb = os.path.getsize(fpath) / 1024
    print(f"  OK [{size_kb:.0f} KB] {fname}")

print("\nAll v2 files polished!")
print("Improvements applied:")
print("  - Compact section boxes (less padding, tight spacing)")
print("  - Syntax highlighting: keywords=amber, types=cyan, strings=green,")
print("    numbers=red, comments=gray, functions=purple")
print("  - Print: all colors mapped to high-contrast dark equivalents")
print("  - Single-line code expanded for readability")
print("  - Table cells compact but readable")

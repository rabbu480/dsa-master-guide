import os
import re

base_dir = r"C:\Users\rabba\Downloads\TelegramDownload\metadata\9.Graphs"
output_file = r"C:\Users\rabba\Downloads\TelegramDownload\metadata\9.Graphs_Final.html"

html_wrapper_start = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Graphs (FAANG Cheat Sheet)</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Fira+Code&display=swap" rel="stylesheet">
    <script type="module">
      import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
      mermaid.initialize({ 
          startOnLoad: true, 
          theme: 'base',
          themeVariables: {
              primaryColor: '#ffffff',
              primaryTextColor: '#000000',
              primaryBorderColor: '#3b82f6',
              lineColor: '#cbd5e1',
              fontFamily: 'Inter'
          }
      });
    </script>
    <style>
        :root {
            --primary: #1e3a8a;
            --secondary: #3b82f6;
            --green: #10b981;
            --red: #ef4444;
            --text-dark: #1e293b;
            --bg-light: #f8fafc;
            --border-color: #cbd5e1;
            --warning-bg: #fffbeb;
            --warning-border: #f59e0b;
        }
        body {
            font-family: 'Inter', sans-serif;
            background-color: #e2e8f0;
            color: var(--text-dark);
            margin: 0;
            padding: 20px;
            font-size: 14px;
        }
        .page {
            background: white;
            max-width: 1100px;
            margin: 0 auto 40px auto;
            padding: 40px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
            border-radius: 8px;
            page-break-after: always;
        }
        .header-top { display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid var(--primary); padding-bottom: 10px; margin-bottom: 20px; }
        .header-top h1 { margin: 0; font-size: 2.5rem; color: var(--primary); font-weight: 900; }
        .header-top .page-number { background: var(--primary); color: white; padding: 5px 15px; border-radius: 20px; font-weight: bold; }
        .grid-container { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
        .section-box { border: 1px solid var(--primary); border-radius: 6px; overflow: hidden; margin-bottom: 20px; background: white; }
        .section-header { background: var(--primary); color: white; padding: 8px 15px; font-weight: 700; font-size: 1.1rem; display: flex; align-items: center; }
        .section-header span.num { background: white; color: var(--primary); border-radius: 50%; width: 24px; height: 24px; display: inline-flex; align-items: center; justify-content: center; margin-right: 10px; font-size: 0.9rem; }
        .section-content { padding: 15px; }
        ul { margin: 0; padding-left: 20px; }
        li { margin-bottom: 8px; }
        .flex-row { display: flex; justify-content: space-between; gap: 20px; }
        .flex-col { flex: 1; text-align: center; }
        table { width: 100%; border-collapse: collapse; font-size: 0.9rem; }
        table th, table td { border: 1px solid var(--border-color); padding: 8px; text-align: left; }
        table th { background: #f1f5f9; }
        pre, code {
            background: #ffffff !important;
            color: #1e293b !important;
            border: 1px solid #cbd5e1;
            padding: 10px;
            border-radius: 4px;
            font-family: 'Fira Code', monospace;
            font-size: 0.85rem;
            margin: 10px 0;
            overflow-x: auto;
            display: block;
        }
        code { display: inline; padding: 2px 6px; border: none; }
        .rule-box { background: var(--warning-bg); border: 1px solid var(--warning-border); border-left: 5px solid var(--warning-border); padding: 10px 15px; margin-top: 10px; }
        .mermaid { display: flex; justify-content: center; margin: 10px 0; }
        @media print {
            body { background: white; padding: 0; }
            .page { box-shadow: none; border: none; margin: 0; padding: 20px 0; max-width: 100%; }
            pre, code { background: #ffffff !important; color: #000000 !important; border: 1px solid #ccc; }
        }
    </style>
</head>
<body>
"""

html_wrapper_end = """
</body>
</html>
"""

final_content = html_wrapper_start

for i in range(1, 29):
    file_path = os.path.join(base_dir, f"{i}.html")
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            final_content += f.read() + "\n"
    else:
        print(f"WARNING: Missing {file_path}")

final_content += html_wrapper_end

with open(output_file, "w", encoding="utf-8") as f:
    f.write(final_content)

size_kb = os.path.getsize(output_file) / 1024
print(f"Successfully generated {output_file} ({size_kb:.1f} KB)")

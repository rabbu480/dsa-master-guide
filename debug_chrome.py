import subprocess, os

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
html = 'F:/dsa/bookfinal/Topic03_TwoPointers.html'
pdf_out = 'F:/dsa/bookfinal/Topic03_test.pdf'
cmd = [chrome_path, '--headless', '--disable-gpu', '--no-pdf-header-footer', f'--print-to-pdf={pdf_out}', html]
result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
print('returncode:', result.returncode)
print('stdout:', result.stdout[:200])
print('stderr:', result.stderr[:500])
print('exists:', os.path.exists(pdf_out))

with open(r'C:\Users\rabba\Downloads\TelegramDownload\metadata\v0\10.Heaps_Final.html', 'r', encoding='utf-8') as f:
    content = f.read()
print('Length:', len(content))
print('Has <style:', '<style' in content)
pos = content.find('<style')
print('First style pos:', pos)
if pos >= 0:
    print('Context:', repr(content[pos:pos+100]))
# Also check what HTML entities might be causing issues
print('\nFirst 500 chars:')
print(repr(content[:200]))

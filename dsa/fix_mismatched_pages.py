import re

# 1. Fix Book2_InterviewMastery.html: Change print zoom to 0.63
with open('F:/dsa/bookfinal/Book2_InterviewMastery.html', 'r', encoding='utf-8') as f:
    b2_html = f.read()

b2_html = re.sub(r'zoom:\s*0\.\d+;', 'zoom: 0.63;', b2_html)
with open('F:/dsa/bookfinal/Book2_InterviewMastery.html', 'w', encoding='utf-8') as f:
    f.write(b2_html)
print("Updated Book2_InterviewMastery.html print zoom to 0.63")

# 2. Fix Topic16_Intervals.html: Change print zoom to 0.76 or check page breaks
with open('F:/dsa/bookfinal/Topic16_Intervals.html', 'r', encoding='utf-8') as f:
    t16_html = f.read()

t16_html = re.sub(r'zoom:\s*0\.\d+;', 'zoom: 0.75;', t16_html)
with open('F:/dsa/bookfinal/Topic16_Intervals.html', 'w', encoding='utf-8') as f:
    f.write(t16_html)
print("Updated Topic16_Intervals.html print zoom to 0.75")

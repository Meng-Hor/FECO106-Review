import re

filepath = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Title
html = html.replace('Interactive Learning', 'FECO106 Algorithm III')

# Replace Subtitle
html = html.replace('Master your knowledge with dynamically generated quizzes and curated study materials.', 'Mid-Term Review')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated hero section text")

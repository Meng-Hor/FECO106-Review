import re

filepath = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\quiz.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the text-gray-600 class with nothing so it inherits the rich text-main color
old_p = r'<p class="text-gray-600 mb-8 leading-relaxed">'
new_p = r'<p class="mb-8 leading-relaxed font-medium">'

html = html.replace(old_p, new_p)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated modal paragraph text color")

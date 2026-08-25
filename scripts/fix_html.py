import re

html_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('<body class="bg-gray-50 text-gray-800 font-sans min-h-screen">', '<body>')
content = content.replace(
    '<div class="max-w-4xl mx-auto px-4 py-8">', 
    '<div class="decor-wrapper">\n        <div class="decor-circle"></div>\n        <div class="decor-square"></div>\n        <div class="decor-triangle"></div>\n        <div class="max-w-4xl mx-auto px-4 py-8 relative z-10">'
)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML fixed.")

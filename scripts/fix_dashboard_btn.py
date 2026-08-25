import re

filepath = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\quiz.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# Add the standard padding to the Back to Dashboard button
html = html.replace('class="btn-primary w-full max-w-sm mx-auto"', 'class="btn-primary px-6 py-3 w-full max-w-sm mx-auto"')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)

print("Fixed Back to Dashboard button padding")

import re

path = r'C:\Users\Ly Meng Hor ING\Documents\Lesson-Review\web\feco106.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix desktop links
html = html.replace('href="index.html#dashboard"', 'href="#dashboard"')
html = html.replace('href="index.html#pdf-container"', 'href="#pdf-container"')

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated links in feco106.html")

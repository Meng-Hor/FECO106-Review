import re

path = r'C:\Users\Ly Meng Hor ING\Documents\Lesson-Review\web\quiz.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix desktop and mobile links
html = html.replace('href="index.html#dashboard"', 'href="feco106.html#dashboard"')
html = html.replace('href="index.html#pdf-container"', 'href="feco106.html#pdf-container"')

# Fix JS redirect for "Dashboard" button on completion screen
html = html.replace("window.location.href = 'index.html';", "window.location.href = 'feco106.html';")

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated links in quiz.html")

import re

html_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\quiz.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Add rounded corners to the quiz complete image
old_img = r'<img src="quiz_complete.png" alt="Quiz Complete Celebration" class="w-48 h-auto mx-auto mb-6 drop-shadow-md">'
new_img = r'<img src="quiz_complete.png" alt="Quiz Complete Celebration" class="w-48 h-auto mx-auto mb-6 drop-shadow-md rounded-2xl">'
html = html.replace(old_img, new_img)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Added rounded corners to celebration image")

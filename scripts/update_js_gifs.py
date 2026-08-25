import re

quiz_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\quiz.html'
with open(quiz_path, 'r', encoding='utf-8') as f:
    html = f.read()

old_results = r'''const availableGifs = \[1, 2, 3, 4, 6, 7, 8, 9, 10\];'''
new_results = '''const availableGifs = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21];'''

html = html.replace(old_results, new_results)

with open(quiz_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated Javascript to include all 20 GIFs")

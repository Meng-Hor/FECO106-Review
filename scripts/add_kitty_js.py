import re

quiz_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\quiz.html'
with open(quiz_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the array with one that includes custom_13
old_results = r'''const availableGifs = \[.*?\];'''
new_array = "const availableGifs = ['assets/gifs/custom_1.gif', 'assets/gifs/custom_4.gif', 'assets/gifs/custom_5.gif', 'assets/gifs/custom_6.gif', 'assets/gifs/custom_7.gif', 'assets/gifs/custom_8.gif', 'assets/gifs/custom_9.gif', 'assets/gifs/custom_10.gif', 'assets/gifs/custom_11.gif', 'assets/gifs/custom_12.gif', 'assets/gifs/custom_13.gif'];"

html = re.sub(old_results, new_array, html)

with open(quiz_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Added custom_13.gif to the JS array")

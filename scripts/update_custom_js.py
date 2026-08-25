import re

quiz_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\quiz.html'
with open(quiz_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Generate the new array string
new_array = "const availableGifs = [" + ", ".join([f"'assets/gifs/custom_{i}.gif'" for i in range(1, 12)]) + "];"

old_results = r'''const availableGifs = \[.*?\];'''

html = re.sub(old_results, new_array, html)

with open(quiz_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated Javascript to use the new Custom Keyword GIF collection")

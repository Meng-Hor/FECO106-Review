import re

css_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace .option-btn:hover with .option-btn:not(:disabled):hover
css = css.replace('.option-btn:hover {', '.option-btn:not(:disabled):hover {')

# Also fix it for dark mode if it exists
css = css.replace('.option-btn:hover {', '.option-btn:not(:disabled):hover {')

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Fixed option hover logic for disabled buttons")

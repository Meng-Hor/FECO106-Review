import re

css_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the @media (prefers-color-scheme: dark) block with data-color-mode selectors
# We'll use regex to find the start of the @media block and replace it.

old_media_start = r'@media \(prefers-color-scheme: dark\) \{'
new_media_start = r'''/* =========================================
   DARK MODE
   ========================================= */'''

css = re.sub(old_media_start, new_media_start, css)

# Replace the inner selectors
css = css.replace(':root, :root[data-theme="aura"] {', ':root[data-color-mode="dark"], :root[data-color-mode="dark"][data-theme="aura"] {')
css = css.replace(':root[data-theme="sunset"] {', ':root[data-color-mode="dark"][data-theme="sunset"] {')
css = css.replace(':root[data-theme="glacial"] {', ':root[data-color-mode="dark"][data-theme="glacial"] {')

# Remove the closing brace of the @media query
# It's right before the * { selector
css = css.replace('}\n\n* {', '\n* {')

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated styles.css to use data-color-mode")

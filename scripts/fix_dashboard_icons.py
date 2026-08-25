import re

css_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Add dynamic text classes
new_classes = '''
/* Dynamic Theme Text Classes */
.text-theme-primary { color: var(--primary-color) !important; }
.group:hover .group-hover\\:text-theme-primary { color: var(--primary-color) !important; }

.text-theme-danger { color: var(--danger-color) !important; }
.group:hover .group-hover\\:text-theme-danger { color: var(--danger-color) !important; }
'''

if 'Dynamic Theme Text Classes' not in css:
    css += new_classes
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)

filepath = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace hardcoded tailwind colors in dashboard JS
html = html.replace('text-purple-500', 'text-theme-primary')
html = html.replace('group-hover:text-purple-600', 'group-hover:text-theme-primary')

html = html.replace('text-red-500', 'text-theme-danger')
html = html.replace('group-hover:text-red-600', 'group-hover:text-theme-danger')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)

print("Optimized dashboard icons to use dynamic theme colors")

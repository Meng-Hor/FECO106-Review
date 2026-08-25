import re

# 1. Clean up index.html
filepath = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# Remove group-hover:scale-110 and transition-transform from icons
html = html.replace('group-hover:scale-110 transition-transform', '')
html = html.replace('group-hover:scale-110', '')

# Remove group-hover:text-... and transition-colors from text
html = html.replace('group-hover:text-theme-primary', '')
html = html.replace('group-hover:text-theme-danger', '')
html = html.replace('transition-colors', '')

# Clean up empty classes or double spaces left behind
html = html.replace('  ', ' ')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Refine CSS
css_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

old_hover = r'\.btn-secondary:hover \{\s*background: var\(--card-item-hover\);\s*transform: translateY\(-4px\);\s*border-color: var\(--primary-color\);\s*box-shadow: 0 12px 24px var\(--water-shadow\);\s*\}'
new_hover = '''.btn-secondary:hover {
    background: var(--card-item-hover);
    transform: translateY(-2px);
    border-color: var(--primary-color);
    box-shadow: 0 8px 20px var(--water-shadow);
}'''

css = re.sub(old_hover, new_hover, css)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Removed exaggerated hover effects")

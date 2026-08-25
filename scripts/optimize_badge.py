import re

css_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

old_badge = r'\.option-badge \{\s*background: var\(--nav-bg\);\s*color: var\(--text-main\);\s*border: 1px solid var\(--glass-border\);\s*\}'
new_badge = '''.option-badge {
    background: var(--text-main);
    color: var(--bg-base) !important;
    border: none;
    box-shadow: 0 2px 8px var(--water-shadow);
}'''

css = re.sub(old_badge, new_badge, css)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Optimized option badge contrast")

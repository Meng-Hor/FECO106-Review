import re

css_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

old_badge = r'\.option-badge \{\s*background: var\(--primary-color\);\s*color: white !important;\s*border: none;\s*box-shadow: 0 2px 8px var\(--water-shadow\);\s*transition: all 0\.3s ease;\s*\}\s*\.correct \.option-badge \{\s*background: white !important;\s*color: var\(--success-color\) !important;\s*\}\s*\.incorrect \.option-badge \{\s*background: white !important;\s*color: var\(--danger-color\) !important;\s*\}'

new_badge = '''.option-badge {
    background: var(--text-main);
    color: var(--bg-base) !important;
    border: none;
    box-shadow: 0 2px 8px var(--water-shadow);
}'''

css = re.sub(old_badge, new_badge, css)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Reverted option badge to the high-contrast monochromatic design")

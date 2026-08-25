import re

css_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

old_badge = r'\.option-badge \{\s*background: var\(--text-main\);\s*color: var\(--bg-base\) !important;\s*border: none;\s*box-shadow: 0 2px 8px var\(--water-shadow\);\s*\}'
new_badge = '''.option-badge {
    background: var(--primary-color);
    color: white !important;
    border: none;
    box-shadow: 0 2px 8px var(--water-shadow);
    transition: all 0.3s ease;
}

.correct .option-badge {
    background: white !important;
    color: var(--success-color) !important;
}

.incorrect .option-badge {
    background: white !important;
    color: var(--danger-color) !important;
}'''

css = re.sub(old_badge, new_badge, css)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Optimized option badge to use theme primary colors and adaptive states")

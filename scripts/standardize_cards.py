import re

css_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

old_btn = r'\.btn-secondary \{\s*background: var\(--card-item-bg\);\s*color: var\(--text-main\) !important;\s*border-radius: 1rem;\s*font-weight: 600;\s*border: 1px solid var\(--glass-border\);\s*box-shadow: 0 4px 12px var\(--card-item-shadow\);\s*transition: all 0\.3s cubic-bezier\(0\.34, 1\.56, 0\.64, 1\);\s*\}\s*\.btn-secondary:hover \{\s*background: var\(--card-item-hover\);\s*transform: translateY\(-2px\);\s*border-color: var\(--primary-color\);\s*box-shadow: 0 8px 20px var\(--water-shadow\);\s*\}'

new_btn = '''.btn-secondary {
    background: var(--nav-bg);
    backdrop-filter: blur(24px) saturate(180%);
    -webkit-backdrop-filter: blur(24px) saturate(180%);
    color: var(--text-main) !important;
    border-radius: 1.5rem;
    font-weight: 600;
    border: 1px solid var(--glass-border);
    box-shadow: 0 8px 32px 0 var(--water-shadow), inset 0 1px 1px 0 var(--option-inset), inset 0 0 0 1px var(--glass-border);
    transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}
.btn-secondary:hover {
    background: var(--card-item-hover);
    transform: translateY(-2px);
    border-color: var(--primary-color);
    box-shadow: 0 12px 40px 0 var(--water-shadow), inset 0 1px 1px 0 var(--option-inset), inset 0 0 0 1px var(--primary-color);
}'''

css = re.sub(old_btn, new_btn, css)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Standardized dashboard cards to match header aesthetic")

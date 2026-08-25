import re

css_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Add the new variables
css = re.sub(r'(--nav-btn-hover: .*?;)', r'\1\n    --card-item-bg: rgba(255, 255, 255, 0.95);\n    --card-item-hover: #FFFFFF;\n    --card-item-shadow: rgba(0, 0, 0, 0.06);', css, count=3)

def inject_dark_mode_vars(match):
    block = match.group(0)
    block = re.sub(r'(--nav-btn-hover: .*?;)', r'\1\n    --card-item-bg: rgba(0, 0, 0, 0.25);\n    --card-item-hover: rgba(0, 0, 0, 0.4);\n    --card-item-shadow: rgba(0, 0, 0, 0.3);', block)
    return block
css = re.sub(r'/\* Dark mode for.*?\}', inject_dark_mode_vars, css, flags=re.DOTALL)


# Update the .btn-secondary class
old_secondary = r'\.btn-secondary \{.*?(?=\/\* Danger Button \*\/)'
new_secondary = '''.btn-secondary {
    background: var(--card-item-bg);
    color: var(--text-main) !important;
    border-radius: 1rem;
    font-weight: 600;
    border: 1px solid var(--glass-border);
    box-shadow: 0 4px 12px var(--card-item-shadow);
    transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
}
.btn-secondary:hover {
    background: var(--card-item-hover);
    transform: translateY(-4px);
    border-color: var(--primary-color);
    box-shadow: 0 12px 24px var(--water-shadow);
}
'''

css = re.sub(old_secondary, new_secondary, css, flags=re.DOTALL)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated .btn-secondary to stand out from the card background")

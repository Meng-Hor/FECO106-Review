import re

css_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

spring_transition = 'transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);'

# Replace standard button transitions
css = re.sub(r'\.btn-primary \{\n.*?transition: all 0\.2s ease;', lambda m: m.group(0).replace('transition: all 0.2s ease;', spring_transition), css, flags=re.DOTALL)
css = re.sub(r'\.btn-danger \{\n.*?transition: all 0\.2s ease;', lambda m: m.group(0).replace('transition: all 0.2s ease;', spring_transition), css, flags=re.DOTALL)
css = re.sub(r'\.btn-success \{\n.*?transition: all 0\.2s ease;', lambda m: m.group(0).replace('transition: all 0.2s ease;', spring_transition), css, flags=re.DOTALL)
css = re.sub(r'\.btn-secondary \{\n.*?transition: all 0\.25s cubic-bezier\(0\.4, 0, 0\.2, 1\);', lambda m: m.group(0).replace('transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);', spring_transition), css, flags=re.DOTALL)

# Replace option btn and stat card transitions
css = re.sub(r'\.option-btn \{\n.*?transition: all 0\.3s cubic-bezier\(0\.4, 0, 0\.2, 1\);', lambda m: m.group(0).replace('transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);', spring_transition), css, flags=re.DOTALL)
css = re.sub(r'\.stat-card \{\n.*?transition: all 0\.3s cubic-bezier\(0\.4, 0, 0\.2, 1\);', lambda m: m.group(0).replace('transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);', spring_transition), css, flags=re.DOTALL)
css = re.sub(r'\.nav-btn \{\n.*?transition: all 0\.2s cubic-bezier\(0\.4, 0, 0\.2, 1\);', lambda m: m.group(0).replace('transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);', spring_transition), css, flags=re.DOTALL)

# Standardize stat-card float distance to -2px instead of -3px
css = css.replace('transform: translateY(-3px);', 'transform: translateY(-2px);')

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Standardized hover physics across all UI components")

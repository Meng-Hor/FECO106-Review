import re

css_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Update Light Mode Variables (Opacity Increase)
css = re.sub(r'--glass-bg: linear-gradient\(135deg, rgba\(255, 255, 255, 0\.6\), rgba\(255, 255, 255, 0\.2\)\);', '--glass-bg: linear-gradient(135deg, rgba(255, 255, 255, 0.85), rgba(255, 255, 255, 0.5));', css)
css = re.sub(r'--nav-bg: rgba\(255, 255, 255, 0\.4\);', '--nav-bg: rgba(255, 255, 255, 0.7);', css)

# Update Dark Mode Variables (Opacity Increase)
css = re.sub(r'--glass-bg: linear-gradient\(135deg, rgba\(30, 41, 59, 0\.5\), rgba\(15, 23, 42, 0\.2\)\);', '--glass-bg: linear-gradient(135deg, rgba(30, 41, 59, 0.85), rgba(15, 23, 42, 0.6));', css)
css = re.sub(r'--nav-bg: rgba\(15, 23, 42, 0\.5\);', '--nav-bg: rgba(15, 23, 42, 0.75);', css)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Increased glass opacity in CSS")

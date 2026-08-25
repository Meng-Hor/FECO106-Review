import re

for path in [
    r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\index.html',
    r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\quiz.html',
]:
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Remove hover:rotate-12 from mode-toggle button
    html = html.replace(
        'class="nav-btn w-8 h-8 sm:w-10 sm:h-10 rounded-lg sm:rounded-xl flex items-center justify-center focus:outline-none shadow-sm transition-transform hover:rotate-12"',
        'class="nav-btn w-8 h-8 sm:w-10 sm:h-10 rounded-lg sm:rounded-xl flex items-center justify-center focus:outline-none shadow-sm"'
    )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Fixed mode-toggle hover in {path}")

# Add a CSS spin animation to styles.css instead
css_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

spin_css = """
/* Mode toggle: click-only spin that auto-resets */
@keyframes spin-once {
    0%   { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}
#mode-toggle.spinning {
    animation: spin-once 0.4s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
}
"""
css += spin_css

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)
print("Added spin-once animation to styles.css")

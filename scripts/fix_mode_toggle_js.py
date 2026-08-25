import re

for path in [
    r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\index.html',
    r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\quiz.html',
]:
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find the modeToggle click listener and add spin class
    old_click = "modeToggle.addEventListener('click', () => {"
    new_click = """modeToggle.addEventListener('click', () => {
        modeToggle.classList.add('spinning');
        modeToggle.addEventListener('animationend', () => modeToggle.classList.remove('spinning'), { once: true });"""

    html = html.replace(old_click, new_click)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Added spin animation trigger to {path}")

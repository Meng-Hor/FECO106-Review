import re

def standardize_header(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Change nav border radius from full pill to standard card radius (rounded-3xl which is 1.5rem)
    html = html.replace('nav class="max-w-6xl mx-auto rounded-[2rem] md:rounded-full', 'nav class="max-w-6xl mx-auto rounded-3xl')

    # 2. Revert buttons from perfectly circular (rounded-full) back to the standard squircle (rounded-xl)
    html = html.replace('nav-btn w-10 h-10 rounded-full', 'nav-btn w-10 h-10 rounded-xl')
    html = html.replace('select id="theme-selector" class="nav-btn text-sm font-medium rounded-full', 'select id="theme-selector" class="nav-btn text-sm font-medium rounded-xl')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

standardize_header(r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\index.html')
standardize_header(r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\quiz.html')


# Update CSS to match the standard
css_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Fix the hardcoded white inset shadow on the nav
old_nav_css = r'box-shadow: 0 10px 40px -10px var\(--water-shadow\), inset 0 1px 1px rgba\(255,255,255,0.2\) !important;'
new_nav_css = r'box-shadow: 0 8px 32px 0 var(--water-shadow), inset 0 1px 1px 0 var(--option-inset), inset 0 0 0 1px var(--glass-border) !important;'
css = re.sub(old_nav_css, new_nav_css, css)

# Change the .nav-link tabs to use rounded-lg instead of rounded-full (pill)
old_link_css = r'border-radius: 9999px; /\* Pill tabs \*/'
new_link_css = r'border-radius: 0.75rem; /* Standard rounded tabs */'
css = re.sub(old_link_css, new_link_css, css)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Standardized header styling to match other components")

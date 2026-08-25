import re

css_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Update the Nav CSS classes to use dynamic theme variables
old_nav_css = r'''\.nav-link \{.*?\.nav-btn:hover \{.*?\}'''

new_nav_css = '''.nav-link {
    padding: 0.4rem 0.75rem;
    border-radius: 0.5rem;
    color: var(--text-muted) !important;
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}
.nav-link:hover {
    background: var(--nav-hover-bg);
    color: var(--primary-color) !important;
    transform: scale(1.05);
}

.nav-btn {
    background: var(--nav-btn-bg) !important;
    color: var(--primary-color) !important;
    border: 1px solid var(--glass-border) !important;
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}
.nav-btn:hover {
    background: var(--nav-btn-hover) !important;
    transform: scale(1.05);
}'''

css = re.sub(old_nav_css, new_nav_css, css, flags=re.DOTALL)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)


def fix_html_classes(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Remove hardcoded text-gray-600 and hover:text-purple-600 from nav links
    html = html.replace('text-gray-600 hover:text-purple-600 ', '')

    # Remove hardcoded border-purple-200/50 and text-purple-600 from nav buttons
    html = html.replace('border border-purple-200/50 text-purple-600 ', '')
    html = html.replace('text-purple-600 border border-purple-200/50 ', '')
    html = html.replace('border border-purple-200/50', '')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

fix_html_classes(r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\index.html')
fix_html_classes(r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\quiz.html')

print("Dynamic theme colors applied to Header UI")

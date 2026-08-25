import re

css_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Add new CSS variables for nav interactions
# Insert into light mode
css = re.sub(r'(--nav-bg: .*?;)', r'\1\n    --nav-hover-bg: rgba(0, 0, 0, 0.05);\n    --nav-btn-bg: rgba(255, 255, 255, 0.5);\n    --nav-btn-hover: rgba(255, 255, 255, 0.8);', css, count=3)

# Insert into dark mode
css = re.sub(r'(--nav-bg: .*?;)', r'\1\n    --nav-hover-bg: rgba(255, 255, 255, 0.1);\n    --nav-btn-bg: rgba(255, 255, 255, 0.1);\n    --nav-btn-hover: rgba(255, 255, 255, 0.2);', css)


# Add new CSS classes at the bottom
new_classes = '''
/* Premium Nav Hover Effects */
.nav-link {
    padding: 0.4rem 0.75rem;
    border-radius: 0.5rem;
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}
.nav-link:hover {
    background: var(--nav-hover-bg);
    transform: scale(1.05);
}

.nav-btn {
    background: var(--nav-btn-bg) !important;
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}
.nav-btn:hover {
    background: var(--nav-btn-hover) !important;
    transform: scale(1.05);
}
'''
css += new_classes

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)


def update_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update Nav Links
    old_link = r'class="text-gray-600 hover:text-purple-600 font-medium transition-colors flex items-center"'
    new_link = 'class="nav-link text-gray-600 hover:text-purple-600 font-medium flex items-center"'
    html = html.replace(old_link, new_link)

    # 2. Update Theme Selector
    old_theme_sel = r'class="bg-white/50 border border-purple-200/50 text-purple-600 text-sm rounded-lg focus:ring-purple-500 focus:border-purple-500 block p-2 backdrop-blur-sm cursor-pointer transition-colors hover:bg-white/80 outline-none"'
    new_theme_sel = 'class="nav-btn border border-purple-200/50 text-purple-600 text-sm rounded-lg focus:ring-purple-500 focus:border-purple-500 block p-2 backdrop-blur-sm cursor-pointer outline-none"'
    html = html.replace(old_theme_sel, new_theme_sel)

    # 3. Update Mode Toggle Button
    old_mode_btn = r'class="ml-2 w-10 h-10 rounded-lg flex items-center justify-center text-purple-600 bg-white/50 border border-purple-200/50 hover:bg-white/80 transition-colors focus:outline-none shadow-sm"'
    new_mode_btn = 'class="nav-btn ml-2 w-10 h-10 rounded-lg flex items-center justify-center text-purple-600 border border-purple-200/50 focus:outline-none shadow-sm"'
    html = html.replace(old_mode_btn, new_mode_btn)

    # 4. Update Logo Icon Background
    old_logo = r'class="w-10 h-10 rounded-lg overflow-hidden flex items-center justify-center shadow-sm border border-purple-200/50 bg-white/50 group-hover:bg-white/80 transition-colors"'
    new_logo = 'class="nav-btn w-10 h-10 rounded-lg overflow-hidden flex items-center justify-center shadow-sm border border-purple-200/50"'
    html = html.replace(old_logo, new_logo)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

update_html(r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\index.html')
update_html(r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\quiz.html')

print("Applied interactive hover effects to all header components")

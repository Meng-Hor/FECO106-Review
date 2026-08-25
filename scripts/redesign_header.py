import re

def redesign_header(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Transform nav into a floating pill container
    old_nav_start = r'<nav class="backdrop-blur-xl sticky top-0 z-50 shadow-sm">\s*<div class="max-w-5xl mx-auto px-4 sm:px-6 py-3 flex flex-col md:flex-row justify-between items-center gap-3 md:gap-0">'
    new_nav_start = '''<!-- Floating Pill Header -->
    <div class="px-4 pt-4 sm:pt-6 sticky top-0 z-50 transition-all">
        <nav class="max-w-6xl mx-auto rounded-[2rem] md:rounded-full px-4 sm:px-6 py-3 flex flex-col md:flex-row justify-between items-center gap-4 md:gap-0 border border-white/20">'''
    
    html = re.sub(old_nav_start, new_nav_start, html, flags=re.DOTALL)
    
    # We need to close the wrapping div after </nav>
    html = html.replace('</nav>', '</nav>\n    </div>')

    # 2. Make all buttons and icons fully rounded to match the pill aesthetic
    html = html.replace('class="nav-btn w-10 h-10 rounded-lg overflow-hidden flex items-center justify-center shadow-sm "',
                        'class="nav-btn w-10 h-10 rounded-full overflow-hidden flex items-center justify-center shadow-sm "')
    html = html.replace('class="nav-btn w-10 h-10 rounded-lg flex items-center justify-center focus:outline-none shadow-sm"',
                        'class="nav-btn w-10 h-10 rounded-full flex items-center justify-center focus:outline-none shadow-sm transition-transform hover:rotate-12"')
    html = html.replace('select id="theme-selector" class="nav-btn text-sm rounded-lg',
                        'select id="theme-selector" class="nav-btn text-sm font-medium rounded-full font-outfit px-3')

    # Ensure links are styled correctly (removing old text colors if they exist)
    html = html.replace('text-gray-600', '') 

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

redesign_header(r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\index.html')
redesign_header(r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\quiz.html')


# Update CSS for the new Pill Nav and Tabs
css_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace old Nav CSS
old_nav_css = r'/\* Premium Liquid Glass Nav \*/.*?\}'
new_nav_css = '''/* Premium Floating Pill Nav */
nav {
    background: var(--nav-bg) !important;
    backdrop-filter: blur(24px) saturate(180%) !important;
    -webkit-backdrop-filter: blur(24px) saturate(180%) !important;
    border: 1px solid var(--glass-border) !important;
    box-shadow: 0 10px 40px -10px var(--water-shadow), inset 0 1px 1px rgba(255,255,255,0.2) !important;
    transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
}'''
css = re.sub(old_nav_css, new_nav_css, css, flags=re.DOTALL)

# Replace Nav Links (Tabs) CSS
old_link_css = r'\.nav-link \{.*?\.nav-link:hover \{.*?\}'
new_link_css = '''.nav-link {
    padding: 0.5rem 1rem;
    border-radius: 9999px; /* Pill tabs */
    color: var(--text-muted) !important;
    transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}
.nav-link:hover {
    background: var(--nav-hover-bg);
    color: var(--primary-color) !important;
    transform: translateY(-2px);
    box-shadow: 0 4px 10px var(--water-shadow);
}'''
css = re.sub(old_link_css, new_link_css, css, flags=re.DOTALL)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Redesigned Header into a Floating Pill with rounded tabs")

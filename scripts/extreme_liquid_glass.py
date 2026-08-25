import re

css_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Enhance the liquid glass effect on all themes
# Aura
css = css.replace('--glass-bg: rgba(255, 255, 255, 0.7);', '--glass-bg: rgba(255, 255, 255, 0.35);')
css = css.replace('--glass-border: rgba(255, 255, 255, 1);', '--glass-border: rgba(255, 255, 255, 0.5);')
css = css.replace('--nav-bg: rgba(255, 255, 255, 0.7);', '--nav-bg: rgba(255, 255, 255, 0.35);')

# Sunset
css = css.replace('--glass-bg: rgba(255, 255, 255, 0.65);', '--glass-bg: rgba(255, 255, 255, 0.35);')
css = css.replace('--glass-border: rgba(255, 255, 255, 0.9);', '--glass-border: rgba(255, 255, 255, 0.5);')
css = css.replace('--nav-bg: rgba(255, 250, 245, 0.7);', '--nav-bg: rgba(255, 250, 245, 0.35);')

# Glacial
css = css.replace('--nav-bg: rgba(245, 255, 255, 0.7);', '--nav-bg: rgba(245, 255, 255, 0.35);')

# Dark Modes
css = css.replace('--glass-bg: rgba(30, 41, 59, 0.6);', '--glass-bg: rgba(15, 23, 42, 0.4);')
css = css.replace('--nav-bg: rgba(15, 23, 42, 0.7);', '--nav-bg: rgba(15, 23, 42, 0.4);')
css = css.replace('--glass-border: rgba(255, 255, 255, 0.05);', '--glass-border: rgba(255, 255, 255, 0.1);')

css = css.replace('--glass-bg: rgba(67, 20, 34, 0.6);', '--glass-bg: rgba(42, 14, 23, 0.4);')
css = css.replace('--nav-bg: rgba(42, 14, 23, 0.7);', '--nav-bg: rgba(42, 14, 23, 0.4);')

css = css.replace('--glass-bg: rgba(12, 74, 110, 0.6);', '--glass-bg: rgba(8, 47, 73, 0.4);')
css = css.replace('--nav-bg: rgba(8, 47, 73, 0.7);', '--nav-bg: rgba(8, 47, 73, 0.4);')


# Enhance the Card Container CSS for maximum liquid feel
old_card = r'''/\* Glassmorphism Cards \*/
\.card-container \{
    background: var\(--glass-bg\);
    backdrop-filter: blur\(30px\) saturate\(150%\);
    -webkit-backdrop-filter: blur\(30px\) saturate\(150%\);
    border: 1px solid var\(--glass-border\);
    border-radius: 1\.5rem;
    box-shadow: var\(--water-shadow\);
    transition: background 0\.5s ease, border-color 0\.5s ease;
\}'''

new_card = '''/* Glassmorphism Cards - True Liquid Effect */
.card-container {
    background: var(--glass-bg);
    backdrop-filter: blur(40px) saturate(200%);
    -webkit-backdrop-filter: blur(40px) saturate(200%);
    border: 1px solid var(--glass-border);
    border-radius: 1.5rem;
    box-shadow: var(--water-shadow), inset 0 1px 2px rgba(255, 255, 255, 0.3);
    transition: background 0.5s ease, border-color 0.5s ease;
}'''

css = re.sub(old_card, new_card, css)

# Make Nav Liquid
old_nav = r'''/\* Nav specific \*/
nav \{
    background: var\(--nav-bg\) !important;
    border-bottom: 1px solid var\(--glass-border\) !important;
    transition: background 0\.5s ease, border-color 0\.5s ease;
\}'''

new_nav = '''/* Nav specific - Liquid */
nav {
    background: var(--nav-bg) !important;
    backdrop-filter: blur(40px) saturate(200%) !important;
    -webkit-backdrop-filter: blur(40px) saturate(200%) !important;
    border-bottom: 1px solid var(--glass-border) !important;
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.05) !important;
    transition: background 0.5s ease, border-color 0.5s ease;
}'''

css = re.sub(old_nav, new_nav, css)


# Make option buttons liquid too!
old_option = r'''\.option-btn \{
    font-family: 'JetBrains Mono', monospace;
\}'''

new_option = '''.option-btn {
    font-family: 'JetBrains Mono', monospace;
    background: var(--glass-bg) !important;
    backdrop-filter: blur(20px) saturate(150%);
    border: 1px solid var(--glass-border) !important;
    transition: all 0.2s ease;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.02);
}
.option-btn:hover {
    background: rgba(255, 255, 255, 0.6) !important;
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
}'''

css = re.sub(old_option, new_option, css)


with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Applied Extreme Liquid Glass effect to CSS")

import re

css_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Update Light Mode Variables
css = re.sub(r'--glass-bg: .*?;', '--glass-bg: linear-gradient(135deg, rgba(255, 255, 255, 0.6), rgba(255, 255, 255, 0.2));', css)
css = re.sub(r'--nav-bg: .*?;', '--nav-bg: rgba(255, 255, 255, 0.4);', css)
css = re.sub(r'--glass-border: .*?;', '--glass-border: rgba(255, 255, 255, 0.5);', css)
css = re.sub(r'--water-shadow: .*?;', '--water-shadow: rgba(0, 0, 0, 0.08);', css)

# Update Dark Mode Variables (We need to specifically target the dark mode blocks)
def replace_in_dark_mode(match):
    block = match.group(0)
    block = re.sub(r'--glass-bg: .*?;', '--glass-bg: linear-gradient(135deg, rgba(30, 41, 59, 0.5), rgba(15, 23, 42, 0.2));', block)
    block = re.sub(r'--nav-bg: .*?;', '--nav-bg: rgba(15, 23, 42, 0.5);', block)
    block = re.sub(r'--glass-border: .*?;', '--glass-border: rgba(255, 255, 255, 0.08);', block)
    block = re.sub(r'--water-shadow: .*?;', '--water-shadow: rgba(0, 0, 0, 0.4);', block)
    return block

css = re.sub(r'/\* Dark mode for.*?\}', replace_in_dark_mode, css, flags=re.DOTALL)


# Update the Card Container with Premium Apple-style Glassmorphism
old_card = r'/\* Glassmorphism Cards.*?\}'
new_card = '''/* Premium Liquid Glass Cards */
.card-container {
    background: var(--glass-bg);
    backdrop-filter: blur(24px) saturate(180%);
    -webkit-backdrop-filter: blur(24px) saturate(180%);
    border: 1px solid var(--glass-border);
    border-radius: 1.5rem;
    box-shadow: 
        0 8px 32px 0 var(--water-shadow),
        inset 0 1px 1px 0 rgba(255, 255, 255, 0.4),
        inset 0 0 0 1px rgba(255, 255, 255, 0.1);
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}'''
css = re.sub(old_card, new_card, css, flags=re.DOTALL)


# Update Nav with Premium Glass
old_nav = r'/\* Nav specific.*?\}'
new_nav = '''/* Premium Liquid Glass Nav */
nav {
    background: var(--nav-bg) !important;
    backdrop-filter: blur(24px) saturate(180%) !important;
    -webkit-backdrop-filter: blur(24px) saturate(180%) !important;
    border-bottom: 1px solid var(--glass-border) !important;
    box-shadow: 0 4px 30px var(--water-shadow) !important;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}'''
css = re.sub(old_nav, new_nav, css, flags=re.DOTALL)


# Update Option Buttons
old_option = r'\.option-btn \{.*?\}'
new_option = '''.option-btn {
    font-family: 'JetBrains Mono', monospace;
    background: var(--glass-bg) !important;
    backdrop-filter: blur(16px) saturate(150%);
    border: 1px solid var(--glass-border) !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 2px 10px var(--water-shadow), inset 0 1px 1px 0 rgba(255, 255, 255, 0.3);
}'''
css = re.sub(old_option, new_option, css, flags=re.DOTALL)


with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Applied Premium Apple-style Liquid Glass effect")

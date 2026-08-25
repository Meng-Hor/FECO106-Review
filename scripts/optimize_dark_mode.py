import re

css_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Add adaptive variables for components that are hardcoded
var_inject = '''
    --option-hover-bg: rgba(255, 255, 255, 0.6);
    --option-inset: rgba(255, 255, 255, 0.3);
    --input-bg: rgba(255, 255, 255, 0.5);
    --input-focus-bg: rgba(255, 255, 255, 0.8);
    --input-border: rgba(255, 255, 255, 0.8);
    --input-focus-border: var(--primary-color);
    --scroll-thumb: rgba(0, 0, 0, 0.2);
    --scroll-thumb-hover: rgba(0, 0, 0, 0.4);
'''

dark_var_inject = '''
    --option-hover-bg: rgba(255, 255, 255, 0.1);
    --option-inset: rgba(255, 255, 255, 0.1);
    --input-bg: rgba(0, 0, 0, 0.2);
    --input-focus-bg: rgba(0, 0, 0, 0.4);
    --input-border: rgba(255, 255, 255, 0.1);
    --input-focus-border: var(--primary-color);
    --scroll-thumb: rgba(255, 255, 255, 0.2);
    --scroll-thumb-hover: rgba(255, 255, 255, 0.4);
'''

def inject_light_vars(match):
    block = match.group(0)
    block = block.replace('--water-shadow: rgba(0, 0, 0, 0.08);', '--water-shadow: rgba(0, 0, 0, 0.08);' + var_inject)
    return block

def inject_dark_vars(match):
    block = match.group(0)
    block = block.replace('--water-shadow: rgba(0, 0, 0, 0.4);', '--water-shadow: rgba(0, 0, 0, 0.4);' + dark_var_inject)
    return block

# Because we have multiple themes, we need to inject into ALL of them
# The clean_vars script guaranteed they all have --water-shadow
css = re.sub(r':root, :root\[data-theme="aura"\] \{.*?(?=\})', inject_light_vars, css, flags=re.DOTALL)
css = re.sub(r':root\[data-theme="sunset"\] \{.*?(?=\})', inject_light_vars, css, flags=re.DOTALL)
css = re.sub(r':root\[data-theme="glacial"\] \{.*?(?=\})', inject_light_vars, css, flags=re.DOTALL)

css = re.sub(r':root\[data-color-mode="dark"\], :root\[data-color-mode="dark"\]\[data-theme="aura"\] \{.*?(?=\})', inject_dark_vars, css, flags=re.DOTALL)
css = re.sub(r':root\[data-color-mode="dark"\]\[data-theme="sunset"\] \{.*?(?=\})', inject_dark_vars, css, flags=re.DOTALL)
css = re.sub(r':root\[data-color-mode="dark"\]\[data-theme="glacial"\] \{.*?(?=\})', inject_dark_vars, css, flags=re.DOTALL)


# 2. Update the hardcoded rules to use these variables
# Option hover
css = css.replace('background: rgba(255, 255, 255, 0.6) !important;', 'background: var(--option-hover-bg) !important;')
css = css.replace('inset 0 1px 1px 0 rgba(255, 255, 255, 0.3)', 'inset 0 1px 1px 0 var(--option-inset)')

# Textarea
css = css.replace('background: rgba(255, 255, 255, 0.5) !important;', 'background: var(--input-bg) !important;')
css = css.replace('border: 1px solid rgba(255, 255, 255, 0.8) !important;', 'border: 1px solid var(--input-border) !important;')
css = css.replace('background: rgba(255, 255, 255, 0.8) !important;', 'background: var(--input-focus-bg) !important;')
css = css.replace('border-color: rgba(200, 180, 160, 0.4) !important;', 'border-color: var(--input-focus-border) !important;')
css = css.replace('box-shadow: 0 0 0 3px rgba(139, 92, 70, 0.1) !important;', 'box-shadow: 0 0 0 3px var(--water-shadow) !important;')

# Scrollbar
css = css.replace('background: rgba(139, 92, 70, 0.3);', 'background: var(--scroll-thumb);')
css = css.replace('background: rgba(139, 92, 70, 0.5);', 'background: var(--scroll-thumb-hover);')

# Also fix the .card-container inset shadow which is hardcoded white
css = css.replace('inset 0 1px 1px 0 rgba(255, 255, 255, 0.4)', 'inset 0 1px 1px 0 var(--option-inset)')
css = css.replace('inset 0 0 0 1px rgba(255, 255, 255, 0.1)', 'inset 0 0 0 1px var(--glass-border)')


with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Optimized dark mode components by removing hardcoded light mode colors")

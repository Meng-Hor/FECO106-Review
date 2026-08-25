import re

css_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

old_gradient = r'\.theme-gradient-text \{\s*background: var\(--logo-gradient\);\s*-webkit-background-clip: text;\s*-webkit-text-fill-color: transparent;\s*background-clip: text;\s*color: transparent;\s*display: inline-block;\s*\}'
new_gradient = '''.theme-gradient-text {
    background: var(--logo-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    color: transparent;
    display: inline-block;
    padding-bottom: 0.15em;
    line-height: 1.1;
}'''

css = re.sub(old_gradient, new_gradient, css)

# In case it didn't have display: inline-block already (the regex above assumed it did)
if 'padding-bottom: 0.15em;' not in css:
    old_gradient_fallback = r'\.theme-gradient-text \{.*?\s*\}'
    new_gradient_fallback = '''.theme-gradient-text {
    background: var(--logo-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    color: transparent;
    display: inline-block;
    padding-bottom: 0.15em;
    line-height: 1.1;
}'''
    css = re.sub(old_gradient_fallback, new_gradient_fallback, css, flags=re.DOTALL)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Fixed gradient text clipping on descenders")

import re

css_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Add --logo-gradient variables
# Aura Light
css = re.sub(r'(--primary-color: #A78BFA;)', r'\1\n    --logo-gradient: linear-gradient(135deg, #8B5CF6, #F472B6);', css)
# Sunset Light
css = re.sub(r'(--primary-color: #FB923C;)', r'\1\n    --logo-gradient: linear-gradient(135deg, #EA580C, #F43F5E);', css)
# Glacial Light
css = re.sub(r'(--primary-color: #2DD4BF;)', r'\1\n    --logo-gradient: linear-gradient(135deg, #0D9488, #34D399);', css)

# Aura Dark
css = re.sub(r'(--primary-color: #8B5CF6;)', r'\1\n    --logo-gradient: linear-gradient(135deg, #A78BFA, #F9A8D4);', css)
# Sunset Dark
css = re.sub(r'(--primary-color: #F97316;)', r'\1\n    --logo-gradient: linear-gradient(135deg, #FB923C, #FDA4AF);', css)
# Glacial Dark
css = re.sub(r'(--primary-color: #14B8A6;)', r'\1\n    --logo-gradient: linear-gradient(135deg, #2DD4BF, #6EE7B7);', css)

# 2. Add .theme-gradient-text class
new_class = '''
.theme-gradient-text {
    background: var(--logo-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    color: transparent;
    display: inline-block;
}
'''
css += new_class

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)


def fix_html_header(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Make the FECO106 logo use the gradient text
    old_logo_text = r'<span class="font-outfit font-bold text-xl text-gray-800 tracking-tight">FECO106</span>'
    new_logo_text = r'<span class="font-outfit font-extrabold text-2xl theme-gradient-text tracking-tighter">FECO106</span>'
    html = html.replace(old_logo_text, new_logo_text)
    
    # What if it's already modified?
    old_logo_text_2 = r'<span class="font-outfit font-bold text-xl tracking-tight">FECO106</span>'
    html = html.replace(old_logo_text_2, new_logo_text)

    # Let's make the nav links use font-outfit too for a more premium look!
    old_links = r'class="nav-link font-medium flex items-center"'
    new_links = 'class="nav-link font-outfit font-bold tracking-wide flex items-center"'
    html = html.replace(old_links, new_links)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

fix_html_header(r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\index.html')
fix_html_header(r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\quiz.html')

print("Optimized header fonts and added dynamic theme gradients")

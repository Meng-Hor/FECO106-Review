import re

css_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Make danger colors significantly bolder so white text is highly readable!
# Aura Light Danger: #F472B6 (Pink 400) -> #DB2777 (Pink 600)
css = css.replace('--danger-color: #F472B6;', '--danger-color: #DB2777;')
css = css.replace('--danger-hover: #EC4899;', '--danger-hover: #BE185D;')

# Sunset Light Danger: #FB7185 (Rose 400) -> #E11D48 (Rose 600)
css = css.replace('--danger-color: #FB7185;', '--danger-color: #E11D48;')
css = css.replace('--danger-hover: #F43F5E;', '--danger-hover: #BE123C;')

# Glacial Light Danger: #F87171 (Red 400) -> #DC2626 (Red 600)
css = css.replace('--danger-color: #F87171;', '--danger-color: #DC2626;')
css = css.replace('--danger-hover: #EF4444;', '--danger-hover: #B91C1C;')

# For primary buttons too (Aura violet, Sunset coral, Glacial teal)
# Aura Light Primary: #A78BFA (Purple 400) -> #7C3AED (Violet 600)
css = css.replace('--primary-color: #A78BFA;', '--primary-color: #7C3AED;')
css = css.replace('--primary-hover: #8B5CF6;', '--primary-hover: #6D28D9;')

# Sunset Light Primary: #FB923C (Orange 400) -> #EA580C (Orange 600)
css = css.replace('--primary-color: #FB923C;', '--primary-color: #EA580C;')
css = css.replace('--primary-hover: #F97316;', '--primary-hover: #C2410C;')

# Glacial Light Primary: #2DD4BF (Teal 400) -> #0D9488 (Teal 600)
css = css.replace('--primary-color: #2DD4BF;', '--primary-color: #0D9488;')
css = css.replace('--primary-hover: #14B8A6;', '--primary-hover: #0F766E;')


# Make sure dark mode danger colors are bright enough against dark backgrounds
def fix_dark_mode(match):
    block = match.group(0)
    # Aura Dark Danger: #EC4899 -> #F472B6 (Brighter for dark mode)
    block = block.replace('--danger-color: #EC4899;', '--danger-color: #F472B6;')
    block = block.replace('--danger-hover: #F472B6;', '--danger-hover: #F9A8D4;')
    
    # Sunset Dark Danger: #E11D48 -> #FB7185
    block = block.replace('--danger-color: #E11D48;', '--danger-color: #FB7185;')
    block = block.replace('--danger-hover: #F43F5E;', '--danger-hover: #FDA4AF;')
    
    # Glacial Dark Danger: #EF4444 -> #F87171
    block = block.replace('--danger-color: #EF4444;', '--danger-color: #F87171;')
    block = block.replace('--danger-hover: #F87171;', '--danger-hover: #FCA5A5;')
    
    return block

css = re.sub(r'/\* Dark mode for.*?\}', fix_dark_mode, css, flags=re.DOTALL)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)


def fix_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Fix the errant </div>iv> typo
    html = html.replace('</div>iv>', '</div>')

    # Ensure the modal icon uses a solid high-contrast inline style or class
    # Replace style="color: var(--danger-color)" with something that works well
    # Since we darkened the danger colors, var(--danger-color) is perfect now.
    
    # But let's also remove text-gray-800 from the modal so it inherits perfectly
    html = html.replace('text-gray-800 mb-2 font-outfit', 'mb-2 font-outfit')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

fix_html(r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\quiz.html')

print("Optimized button contrast and fixed modal HTML")

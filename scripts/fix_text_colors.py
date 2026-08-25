import re

css_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Fix Sunset Light Mode text colors (was incorrectly using purple #581C87)
sunset_light_old = r'--text-main: #581C87;\s*--text-muted: #9CA3AF;'
sunset_light_new = '''--text-main: #431407; /* Orange 950 */
    --text-muted: #9A3412; /* Orange 700 */'''
css = re.sub(sunset_light_old, sunset_light_new, css)

# Fix Glacial Light Mode muted color to perfectly match the teal theme
glacial_light_old = r'--text-main: #064E3B;\s*--text-muted: #64748B;'
glacial_light_new = '''--text-main: #134E4A; /* Teal 950 */
    --text-muted: #0F766E; /* Teal 700 */'''
css = re.sub(glacial_light_old, glacial_light_new, css)

# Make sure Aura Light Mode is beautifully deep violet/slate
aura_light_old = r'--text-main: #334155;\s*--text-muted: #64748B;'
aura_light_new = '''--text-main: #1E1B4B; /* Indigo 950 */
    --text-muted: #4338CA; /* Indigo 700 */'''
css = re.sub(aura_light_old, aura_light_new, css)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Optimized light mode text colors to perfectly match their themes")

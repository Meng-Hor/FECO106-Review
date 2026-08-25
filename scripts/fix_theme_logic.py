import re

css_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Let's cleanly regenerate the entire variables section because my last script messed it up by doing dumb global string replaces.
themes_css = """@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@600;700;800&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500;600&display=swap');

/* =========================================
   THEME 1: PASTEL AURA (Default Light)
   ========================================= */
:root, :root[data-theme="aura"] {
    --bg-base: #FFFFFF;
    --bg-gradient: 
        radial-gradient(at 0% 0%, rgba(255, 212, 235, 0.9) 0px, transparent 60%),
        radial-gradient(at 100% 0%, rgba(212, 232, 255, 0.9) 0px, transparent 60%),
        radial-gradient(at 100% 100%, rgba(255, 245, 185, 0.9) 0px, transparent 60%),
        radial-gradient(at 0% 100%, rgba(212, 225, 255, 0.8) 0px, transparent 60%),
        radial-gradient(at 50% 50%, rgba(255, 255, 255, 1) 0px, transparent 80%);
    
    --glass-bg: rgba(255, 255, 255, 0.7);
    --glass-border: rgba(255, 255, 255, 1);
    --nav-bg: rgba(255, 255, 255, 0.7);
    --water-shadow: 0 12px 40px 0 rgba(160, 150, 180, 0.15);
    
    --text-main: #312E81;
    --text-muted: #6B7280;
    
    --primary-color: #A78BFA;
    --primary-hover: #8B5CF6;
    --danger-color: #F472B6;
    --danger-hover: #EC4899;
    --success-color: #34D399;
}

/* =========================================
   THEME 2: PEACH SUNSET (Light)
   ========================================= */
:root[data-theme="sunset"] {
    --bg-base: #FFFCF9;
    --bg-gradient: 
        radial-gradient(at 0% 0%, rgba(255, 223, 186, 0.9) 0px, transparent 60%),
        radial-gradient(at 100% 0%, rgba(255, 183, 178, 0.9) 0px, transparent 60%),
        radial-gradient(at 100% 100%, rgba(255, 250, 204, 0.9) 0px, transparent 60%),
        radial-gradient(at 0% 100%, rgba(255, 218, 193, 0.8) 0px, transparent 60%),
        radial-gradient(at 50% 50%, rgba(255, 255, 255, 1) 0px, transparent 80%);
    
    --glass-bg: rgba(255, 255, 255, 0.65);
    --glass-border: rgba(255, 255, 255, 0.9);
    --nav-bg: rgba(255, 250, 245, 0.7);
    --water-shadow: 0 12px 40px 0 rgba(180, 130, 100, 0.15);
    
    --text-main: #581C87;
    --text-muted: #9CA3AF;
    
    --primary-color: #FB923C;
    --primary-hover: #F97316;
    --danger-color: #FB7185;
    --danger-hover: #F43F5E;
    --success-color: #4ADE80;
}

/* =========================================
   THEME 3: GLACIAL MINT (Light)
   ========================================= */
:root[data-theme="glacial"] {
    --bg-base: #F8FFFF;
    --bg-gradient: 
        radial-gradient(at 0% 0%, rgba(186, 255, 234, 0.9) 0px, transparent 60%),
        radial-gradient(at 100% 0%, rgba(178, 240, 255, 0.9) 0px, transparent 60%),
        radial-gradient(at 100% 100%, rgba(224, 255, 245, 0.9) 0px, transparent 60%),
        radial-gradient(at 0% 100%, rgba(193, 230, 255, 0.8) 0px, transparent 60%),
        radial-gradient(at 50% 50%, rgba(255, 255, 255, 1) 0px, transparent 80%);
    
    --glass-bg: rgba(255, 255, 255, 0.65);
    --glass-border: rgba(255, 255, 255, 0.9);
    --nav-bg: rgba(245, 255, 255, 0.7);
    --water-shadow: 0 12px 40px 0 rgba(100, 160, 170, 0.15);
    
    --text-main: #064E3B;
    --text-muted: #64748B;
    
    --primary-color: #2DD4BF;
    --primary-hover: #14B8A6;
    --danger-color: #F87171;
    --danger-hover: #EF4444;
    --success-color: #34D399;
}

/* =========================================
   MANUAL DARK MODE
   ========================================= */
/* Dark mode for Pastel Aura */
:root[data-color-mode="dark"], :root[data-color-mode="dark"][data-theme="aura"] {
    --bg-base: #0F172A;
    --bg-gradient: 
        radial-gradient(at 0% 0%, rgba(139, 92, 246, 0.25) 0px, transparent 60%),
        radial-gradient(at 100% 0%, rgba(59, 130, 246, 0.25) 0px, transparent 60%),
        radial-gradient(at 100% 100%, rgba(236, 72, 153, 0.2) 0px, transparent 60%),
        radial-gradient(at 0% 100%, rgba(16, 185, 129, 0.15) 0px, transparent 60%);
    --glass-bg: rgba(30, 41, 59, 0.6);
    --glass-border: rgba(255, 255, 255, 0.05);
    --nav-bg: rgba(15, 23, 42, 0.7);
    --water-shadow: 0 12px 40px 0 rgba(0, 0, 0, 0.4);
    --text-main: #F8FAFC;
    --text-muted: #94A3B8;
    --primary-color: #8B5CF6; 
    --primary-hover: #A78BFA;
    --danger-color: #EC4899;  
    --danger-hover: #F472B6;
}

/* Dark mode for Peach Sunset */
:root[data-color-mode="dark"][data-theme="sunset"] {
    --bg-base: #2A0E17;
    --bg-gradient: 
        radial-gradient(at 0% 0%, rgba(225, 29, 72, 0.25) 0px, transparent 60%),
        radial-gradient(at 100% 0%, rgba(234, 88, 12, 0.25) 0px, transparent 60%),
        radial-gradient(at 100% 100%, rgba(245, 158, 11, 0.2) 0px, transparent 60%);
    --glass-bg: rgba(67, 20, 34, 0.6);
    --glass-border: rgba(255, 255, 255, 0.05);
    --nav-bg: rgba(42, 14, 23, 0.7);
    --water-shadow: 0 12px 40px 0 rgba(0, 0, 0, 0.4);
    --text-main: #FFF1F2;
    --text-muted: #FDA4AF;
    --primary-color: #F97316; 
    --primary-hover: #FB923C;
    --danger-color: #E11D48;  
    --danger-hover: #F43F5E;
}

/* Dark mode for Glacial Mint */
:root[data-color-mode="dark"][data-theme="glacial"] {
    --bg-base: #082F49;
    --bg-gradient: 
        radial-gradient(at 0% 0%, rgba(13, 148, 136, 0.25) 0px, transparent 60%),
        radial-gradient(at 100% 0%, rgba(2, 132, 199, 0.25) 0px, transparent 60%),
        radial-gradient(at 100% 100%, rgba(16, 185, 129, 0.2) 0px, transparent 60%);
    --glass-bg: rgba(12, 74, 110, 0.6);
    --glass-border: rgba(255, 255, 255, 0.05);
    --nav-bg: rgba(8, 47, 73, 0.7);
    --water-shadow: 0 12px 40px 0 rgba(0, 0, 0, 0.4);
    --text-main: #F0FDFB;
    --text-muted: #5EEAD4;
    --primary-color: #14B8A6; 
    --primary-hover: #2DD4BF;
    --danger-color: #EF4444;  
    --danger-hover: #F87171;
}"""

# Extract the rest of the CSS (fonts, buttons, body etc)
body_and_beyond_idx = css.find('\n* {')
if body_and_beyond_idx == -1:
    body_and_beyond_idx = css.find('* {')
rest_of_css = css[body_and_beyond_idx:]

new_css = themes_css + rest_of_css

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(new_css)

# Now fix the JavaScript in HTML to remove the smart OS default
def fix_js(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Replace the JS mode logic to strictly default to 'light'
    old_js = r'''// Load saved mode or OS preference
        let currentMode = localStorage\.getItem\('colorMode'\);
        if \(!currentMode\) \{
            currentMode = window\.matchMedia\('\(prefers-color-scheme: dark\)'\)\.matches \? 'dark' : 'light';
        \}'''
    
    new_js = '''// Load saved mode or default strictly to light
        let currentMode = localStorage.getItem('colorMode') || 'light';'''
    
    html = re.sub(old_js, new_js, html)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

fix_js(r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\index.html')
fix_js(r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\quiz.html')

print("Fixed CSS parsing bug and defaulted to light mode")

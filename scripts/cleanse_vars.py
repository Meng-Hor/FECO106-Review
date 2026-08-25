import re

css_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Generate the perfectly clean variables block
clean_vars = """@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@600;700;800&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500;600&display=swap');

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
    
    --glass-bg: linear-gradient(135deg, rgba(255, 255, 255, 0.85), rgba(255, 255, 255, 0.5));
    --glass-border: rgba(255, 255, 255, 0.5);
    --nav-bg: rgba(255, 255, 255, 0.7);
    --nav-hover-bg: rgba(0, 0, 0, 0.05);
    --nav-btn-bg: rgba(255, 255, 255, 0.5);
    --nav-btn-hover: rgba(255, 255, 255, 0.8);
    --card-item-bg: rgba(255, 255, 255, 0.95);
    --card-item-hover: #FFFFFF;
    --card-item-shadow: rgba(0, 0, 0, 0.06);
    --water-shadow: rgba(0, 0, 0, 0.08);
    
    --text-main: #312E81;
    --text-muted: #6B7280;
    
    --primary-color: #7C3AED;
    --logo-gradient: linear-gradient(135deg, #8B5CF6, #F472B6);
    --primary-hover: #6D28D9;
    --danger-color: #DB2777;
    --danger-hover: #BE185D;
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
    
    --glass-bg: linear-gradient(135deg, rgba(255, 255, 255, 0.85), rgba(255, 255, 255, 0.5));
    --glass-border: rgba(255, 255, 255, 0.5);
    --nav-bg: rgba(255, 255, 255, 0.7);
    --nav-hover-bg: rgba(0, 0, 0, 0.05);
    --nav-btn-bg: rgba(255, 255, 255, 0.5);
    --nav-btn-hover: rgba(255, 255, 255, 0.8);
    --card-item-bg: rgba(255, 255, 255, 0.95);
    --card-item-hover: #FFFFFF;
    --card-item-shadow: rgba(0, 0, 0, 0.06);
    --water-shadow: rgba(0, 0, 0, 0.08);
    
    --text-main: #581C87;
    --text-muted: #9CA3AF;
    
    --primary-color: #EA580C;
    --logo-gradient: linear-gradient(135deg, #EA580C, #F43F5E);
    --primary-hover: #C2410C;
    --danger-color: #E11D48;
    --danger-hover: #BE123C;
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
    
    --glass-bg: linear-gradient(135deg, rgba(255, 255, 255, 0.85), rgba(255, 255, 255, 0.5));
    --glass-border: rgba(255, 255, 255, 0.5);
    --nav-bg: rgba(255, 255, 255, 0.7);
    --nav-hover-bg: rgba(0, 0, 0, 0.05);
    --nav-btn-bg: rgba(255, 255, 255, 0.5);
    --nav-btn-hover: rgba(255, 255, 255, 0.8);
    --card-item-bg: rgba(255, 255, 255, 0.95);
    --card-item-hover: #FFFFFF;
    --card-item-shadow: rgba(0, 0, 0, 0.06);
    --water-shadow: rgba(0, 0, 0, 0.08);
    
    --text-main: #064E3B;
    --text-muted: #64748B;
    
    --primary-color: #0D9488;
    --logo-gradient: linear-gradient(135deg, #0D9488, #34D399);
    --primary-hover: #0F766E;
    --danger-color: #DC2626;
    --danger-hover: #B91C1C;
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
    --glass-bg: linear-gradient(135deg, rgba(30, 41, 59, 0.85), rgba(15, 23, 42, 0.6));
    --glass-border: rgba(255, 255, 255, 0.08);
    --nav-bg: rgba(15, 23, 42, 0.75);
    --nav-hover-bg: rgba(255, 255, 255, 0.1);
    --nav-btn-bg: rgba(255, 255, 255, 0.1);
    --nav-btn-hover: rgba(255, 255, 255, 0.2);
    --card-item-bg: rgba(0, 0, 0, 0.25);
    --card-item-hover: rgba(0, 0, 0, 0.4);
    --card-item-shadow: rgba(0, 0, 0, 0.3);
    --water-shadow: rgba(0, 0, 0, 0.4);
    
    --text-main: #F8FAFC;
    --text-muted: #94A3B8;
    
    --primary-color: #8B5CF6;
    --logo-gradient: linear-gradient(135deg, #A78BFA, #F9A8D4);
    --primary-hover: #A78BFA;
    --danger-color: #F472B6;
    --danger-hover: #F9A8D4;
    --success-color: #34D399;
}

/* Dark mode for Peach Sunset */
:root[data-color-mode="dark"][data-theme="sunset"] {
    --bg-base: #2A0E17;
    --bg-gradient: 
        radial-gradient(at 0% 0%, rgba(225, 29, 72, 0.25) 0px, transparent 60%),
        radial-gradient(at 100% 0%, rgba(234, 88, 12, 0.25) 0px, transparent 60%),
        radial-gradient(at 100% 100%, rgba(245, 158, 11, 0.2) 0px, transparent 60%);
    --glass-bg: linear-gradient(135deg, rgba(30, 41, 59, 0.85), rgba(15, 23, 42, 0.6));
    --glass-border: rgba(255, 255, 255, 0.08);
    --nav-bg: rgba(15, 23, 42, 0.75);
    --nav-hover-bg: rgba(255, 255, 255, 0.1);
    --nav-btn-bg: rgba(255, 255, 255, 0.1);
    --nav-btn-hover: rgba(255, 255, 255, 0.2);
    --card-item-bg: rgba(0, 0, 0, 0.25);
    --card-item-hover: rgba(0, 0, 0, 0.4);
    --card-item-shadow: rgba(0, 0, 0, 0.3);
    --water-shadow: rgba(0, 0, 0, 0.4);
    
    --text-main: #FFF1F2;
    --text-muted: #FDA4AF;
    
    --primary-color: #F97316;
    --logo-gradient: linear-gradient(135deg, #FB923C, #FDA4AF);
    --primary-hover: #FB923C;
    --danger-color: #FB7185;
    --danger-hover: #FDA4AF;
    --success-color: #4ADE80;
}

/* Dark mode for Glacial Mint */
:root[data-color-mode="dark"][data-theme="glacial"] {
    --bg-base: #082F49;
    --bg-gradient: 
        radial-gradient(at 0% 0%, rgba(13, 148, 136, 0.25) 0px, transparent 60%),
        radial-gradient(at 100% 0%, rgba(2, 132, 199, 0.25) 0px, transparent 60%),
        radial-gradient(at 100% 100%, rgba(16, 185, 129, 0.2) 0px, transparent 60%);
    --glass-bg: linear-gradient(135deg, rgba(30, 41, 59, 0.85), rgba(15, 23, 42, 0.6));
    --glass-border: rgba(255, 255, 255, 0.08);
    --nav-bg: rgba(15, 23, 42, 0.75);
    --nav-hover-bg: rgba(255, 255, 255, 0.1);
    --nav-btn-bg: rgba(255, 255, 255, 0.1);
    --nav-btn-hover: rgba(255, 255, 255, 0.2);
    --card-item-bg: rgba(0, 0, 0, 0.25);
    --card-item-hover: rgba(0, 0, 0, 0.4);
    --card-item-shadow: rgba(0, 0, 0, 0.3);
    --water-shadow: rgba(0, 0, 0, 0.4);
    
    --text-main: #F0FDFB;
    --text-muted: #5EEAD4;
    
    --primary-color: #14B8A6;
    --logo-gradient: linear-gradient(135deg, #2DD4BF, #6EE7B7);
    --primary-hover: #2DD4BF;
    --danger-color: #F87171;
    --danger-hover: #FCA5A5;
    --success-color: #34D399;
}
"""

start_idx = css.find("@import url('https://fonts.googleapis.com")
end_idx = css.find('\n* {')
if end_idx == -1: end_idx = css.find('* {')

new_css = clean_vars + css[end_idx:]

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(new_css)

print("Perfectly cleansed and synchronized all CSS variables!")

import re

css_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Completely rewrite the variable section and body to support dynamic themes and dark mode
themes_css = """@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@600;700;800&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500;600&display=swap');

/* =========================================
   THEME 1: PASTEL AURA (Default)
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
    
    --text-main: #312E81; /* Deep indigo */
    --text-muted: #6B7280;
    
    --primary-color: #A78BFA; /* Pastel violet */
    --primary-hover: #8B5CF6;
    --danger-color: #F472B6;  /* Pastel pink */
    --danger-hover: #EC4899;
    --success-color: #34D399; /* Pastel mint */
}

/* =========================================
   THEME 2: PEACH SUNSET
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
    
    --text-main: #581C87; /* Deep maroon/purple */
    --text-muted: #9CA3AF;
    
    --primary-color: #FB923C; /* Warm Coral */
    --primary-hover: #F97316;
    --danger-color: #FB7185;  /* Soft Rose */
    --danger-hover: #F43F5E;
    --success-color: #4ADE80; /* Soft Green */
}

/* =========================================
   THEME 3: GLACIAL MINT
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
    
    --text-main: #064E3B; /* Deep Forest Green */
    --text-muted: #64748B;
    
    --primary-color: #2DD4BF; /* Bright Teal */
    --primary-hover: #14B8A6;
    --danger-color: #F87171;  /* Soft Red */
    --danger-hover: #EF4444;
    --success-color: #34D399; /* Mint */
}

/* =========================================
   AUTO DARK MODE (Inverts the active theme)
   ========================================= */
@media (prefers-color-scheme: dark) {
    /* Dark mode for Pastel Aura */
    :root, :root[data-theme="aura"] {
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
    :root[data-theme="sunset"] {
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
    :root[data-theme="glacial"] {
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
    }
}

* {
    font-family: 'Inter', sans-serif;
}

h1, h2, h3, h4 {
    font-family: 'Outfit', sans-serif;
}

.btn-primary, .btn-secondary, .btn-danger, .option-btn, textarea, #time, #score-display {
    font-family: 'JetBrains Mono', monospace;
}

body {
    background-color: var(--bg-base);
    background-image: var(--bg-gradient);
    background-attachment: fixed;
    color: var(--text-main);
    min-height: 100vh;
    transition: background-color 0.5s ease, color 0.5s ease;
}

/* Glassmorphism Cards */
.card-container {
    background: var(--glass-bg);
    backdrop-filter: blur(30px) saturate(150%);
    -webkit-backdrop-filter: blur(30px) saturate(150%);
    border: 1px solid var(--glass-border);
    border-radius: 1.5rem;
    box-shadow: var(--water-shadow);
    transition: background 0.5s ease, border-color 0.5s ease;
}

/* Nav specific */
nav {
    background: var(--nav-bg) !important;
    border-bottom: 1px solid var(--glass-border) !important;
    transition: background 0.5s ease, border-color 0.5s ease;
}

/* Make sure text colors inherit properly */
.text-gray-800, .text-gray-700 { color: var(--text-main) !important; }
.text-gray-600, .text-gray-500 { color: var(--text-muted) !important; }
"""

# Replace everything from top up to Buttons section
css = re.sub(r'^.*?\.btn-primary \{', themes_css + '\n.btn-primary {', css, flags=re.DOTALL)

# Update Button Colors to use Variables
css = re.sub(r'\.btn-primary \{\n    background: #A78BFA;.*?box-shadow: 0 4px 15px rgba\(167, 139, 250, 0\.4\);\n\}',
             r'''.btn-primary {
    background: var(--primary-color);
    color: white !important;
    border-radius: 0.75rem;
    font-weight: 600;
    border: none;
    transition: all 0.2s ease;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15);
}''', css, flags=re.DOTALL)

css = re.sub(r'\.btn-primary:hover \{\n    background: #8B5CF6;.*?box-shadow: 0 6px 20px rgba\(139, 92, 246, 0\.5\);\n\}',
             r'''.btn-primary:hover {
    background: var(--primary-hover);
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.2);
}''', css, flags=re.DOTALL)

css = re.sub(r'\.btn-danger \{\n    background: #F472B6;.*?box-shadow: 0 4px 15px rgba\(244, 114, 182, 0\.4\);\n\}',
             r'''.btn-danger {
    background: var(--danger-color);
    color: white !important;
    border-radius: 0.75rem;
    font-weight: 600;
    border: none;
    transition: all 0.2s ease;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15);
}''', css, flags=re.DOTALL)

css = re.sub(r'\.btn-danger:hover \{\n    background: #EC4899;.*?box-shadow: 0 6px 20px rgba\(236, 72, 153, 0\.5\);\n\}',
             r'''.btn-danger:hover {
    background: var(--danger-hover);
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.2);
}''', css, flags=re.DOTALL)

css = re.sub(r'\.correct \{ \n    background: #34D399 !important;.*?\}',
             r'''.correct { 
    background: var(--success-color) !important; 
    color: white !important; 
    border: none !important;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15) !important;
}''', css, flags=re.DOTALL)

css = re.sub(r'\.incorrect \{ \n    background: #F472B6 !important;.*?\}',
             r'''.incorrect { 
    background: var(--danger-color) !important; 
    color: white !important; 
    border: none !important;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15) !important;
}''', css, flags=re.DOTALL)

# Secondary Buttons shouldn't clash in dark mode
css = re.sub(r'\.btn-secondary \{.*?\}',
             r'''.btn-secondary {
    background: var(--glass-bg);
    color: var(--text-main) !important;
    border-radius: 0.75rem;
    font-weight: 600;
    border: 1px solid var(--glass-border);
    transition: all 0.2s ease;
}''', css, flags=re.DOTALL)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated CSS with 3 themes and dark mode")

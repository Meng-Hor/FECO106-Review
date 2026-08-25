import re

css_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Update Body Background Gradient to Pastel Aura
new_body = '''body {
    background-color: #FFFFFF;
    background-image: 
        radial-gradient(at 0% 0%, rgba(255, 212, 235, 0.9) 0px, transparent 60%),
        radial-gradient(at 100% 0%, rgba(212, 232, 255, 0.9) 0px, transparent 60%),
        radial-gradient(at 100% 100%, rgba(255, 245, 185, 0.9) 0px, transparent 60%),
        radial-gradient(at 0% 100%, rgba(212, 225, 255, 0.8) 0px, transparent 60%),
        radial-gradient(at 50% 50%, rgba(255, 255, 255, 1) 0px, transparent 80%);
    background-attachment: fixed;
    color: var(--text-main);
    min-height: 100vh;
}'''
css = re.sub(r'body \{.*?min-height: 100vh;\n\}', new_body, css, flags=re.DOTALL)


# Update Variables for the Pastel Theme
new_vars = """:root {
    /* Pastel Aura Theme */
    --bg-vanilla: #FFFFFF;
    --water-shadow: 0 12px 40px 0 rgba(160, 150, 180, 0.15); /* Cooler, softer purple shadow */
    --glass-bg: rgba(255, 255, 255, 0.7); /* More transparent so pastel shows through */
    --glass-border: rgba(255, 255, 255, 1); 
    
    --primary-blue: rgba(167, 139, 250, 0.9); /* Vibrant pastel violet */
    --primary-hover: rgba(139, 92, 246, 1);
    
    --text-main: #312E81; /* Deep indigo text for contrast */
}"""
css = re.sub(r':root \{.*?\n\}', new_vars, css, flags=re.DOTALL)


# Update Primary Button (Violet)
new_primary = """.btn-primary {
    background: #A78BFA; /* Vibrant pastel violet */
    color: white !important;
    border-radius: 0.75rem;
    font-weight: 600;
    border: none;
    padding: 0.75rem 1.5rem;
    transition: all 0.2s ease;
    box-shadow: 0 4px 15px rgba(167, 139, 250, 0.4);
}
.btn-primary:hover {
    background: #8B5CF6;
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(139, 92, 246, 0.5);
}"""
css = re.sub(r'\.btn-primary \{.*?\.btn-primary:hover \{.*?\}', new_primary, css, flags=re.DOTALL)


# Update Danger Button (Soft Pink/Coral)
new_danger = """.btn-danger {
    background: #F472B6; /* Vibrant pastel pink */
    color: white !important;
    border-radius: 0.75rem;
    font-weight: 600;
    border: none;
    padding: 0.75rem 1.5rem;
    transition: all 0.2s ease;
    box-shadow: 0 4px 15px rgba(244, 114, 182, 0.4);
}
.btn-danger:hover {
    background: #EC4899;
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(236, 72, 153, 0.5);
}"""
css = re.sub(r'\.btn-danger \{.*?\.btn-danger:hover \{.*?\}', new_danger, css, flags=re.DOTALL)


# Update Correct Choice (Soft Mint Green)
css = re.sub(r'\.correct \{.*?\}',
             r'''.correct { 
    background: #34D399 !important; /* Pastel Emerald/Mint */
    color: white !important; 
    border: none !important;
    box-shadow: 0 4px 15px rgba(52, 211, 153, 0.4) !important;
}''', css, flags=re.DOTALL)

# Update Incorrect Choice (Matches Pink Danger)
css = re.sub(r'\.incorrect \{.*?\}',
             r'''.incorrect { 
    background: #F472B6 !important; /* Pastel Pink */
    color: white !important; 
    border: none !important;
    box-shadow: 0 4px 15px rgba(244, 114, 182, 0.4) !important;
}''', css, flags=re.DOTALL)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated CSS to Pastel Aura Theme")

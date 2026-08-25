import re

css_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# 1. 3D Pop-Up Cards
old_card = r'/\* Premium Liquid Glass Cards \*/.*?\}'
new_card = '''/* 3D Pop-up Liquid Glass Cards */
.card-container {
    background: var(--glass-bg);
    backdrop-filter: blur(24px) saturate(180%);
    -webkit-backdrop-filter: blur(24px) saturate(180%);
    border-radius: 1.5rem;
    
    /* 3D Beveled Glass Borders */
    border-top: 1px solid rgba(255, 255, 255, 0.7);
    border-left: 1px solid rgba(255, 255, 255, 0.4);
    border-right: 1px solid rgba(255, 255, 255, 0.1);
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    
    /* Extreme 3D Pop-out shadows */
    box-shadow: 
        0 20px 40px -10px var(--water-shadow),
        0 10px 20px -5px rgba(0, 0, 0, 0.05),
        inset 0 3px 5px 0 rgba(255, 255, 255, 0.5),
        inset 0 -2px 5px 0 rgba(0, 0, 0, 0.05);
        
    transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
}
.card-container:hover {
    transform: translateY(-5px);
    box-shadow: 
        0 30px 50px -10px var(--water-shadow),
        0 15px 25px -5px rgba(0, 0, 0, 0.1),
        inset 0 3px 5px 0 rgba(255, 255, 255, 0.6),
        inset 0 -2px 5px 0 rgba(0, 0, 0, 0.05);
}

:root[data-color-mode="dark"] .card-container {
    border-top: 1px solid rgba(255, 255, 255, 0.2);
    border-left: 1px solid rgba(255, 255, 255, 0.1);
    border-right: 1px solid rgba(255, 255, 255, 0.02);
    border-bottom: 1px solid rgba(255, 255, 255, 0.02);
    box-shadow: 
        0 20px 40px -10px var(--water-shadow),
        inset 0 2px 4px 0 rgba(255, 255, 255, 0.1),
        inset 0 -2px 4px 0 rgba(0, 0, 0, 0.2);
}'''
css = re.sub(old_card, new_card, css, flags=re.DOTALL)


# 2. Re-write all button styles to be 3D glass bubbles
old_buttons = r'\.btn-primary \{.*?(?=\.correct \{)'
new_buttons = '''.btn-primary {
    background: linear-gradient(135deg, var(--primary-color), var(--primary-hover));
    color: white !important;
    border-radius: 1rem;
    font-weight: 700;
    
    /* 3D Glass Pill Effect */
    border-top: 1px solid rgba(255, 255, 255, 0.6);
    border-left: 1px solid rgba(255, 255, 255, 0.4);
    border-right: 1px solid rgba(0, 0, 0, 0.1);
    border-bottom: 1px solid rgba(0, 0, 0, 0.2);
    
    box-shadow: 
        0 10px 20px -5px var(--water-shadow),
        inset 0 2px 3px rgba(255, 255, 255, 0.4),
        inset 0 -2px 4px rgba(0, 0, 0, 0.15);
        
    transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}
.btn-primary:hover {
    transform: translateY(-4px) scale(1.02);
    box-shadow: 
        0 15px 25px -5px var(--water-shadow),
        inset 0 2px 3px rgba(255, 255, 255, 0.6),
        inset 0 -2px 4px rgba(0, 0, 0, 0.2);
}

/* Secondary / Glass Buttons (Quiz Sets) */
.btn-secondary {
    background: var(--glass-bg);
    backdrop-filter: blur(16px) saturate(180%);
    color: var(--text-main) !important;
    border-radius: 1rem;
    font-weight: 700;
    
    border-top: 1px solid rgba(255, 255, 255, 0.8);
    border-left: 1px solid rgba(255, 255, 255, 0.5);
    border-right: 1px solid rgba(255, 255, 255, 0.1);
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    
    box-shadow: 
        0 10px 20px -5px var(--water-shadow),
        inset 0 2px 4px rgba(255, 255, 255, 0.5),
        inset 0 -2px 4px rgba(0, 0, 0, 0.05);
        
    transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}
.btn-secondary:hover {
    transform: translateY(-4px) scale(1.02);
    background: rgba(255, 255, 255, 0.8);
    border-color: var(--primary-color);
    box-shadow: 
        0 15px 30px -5px var(--water-shadow),
        inset 0 2px 4px rgba(255, 255, 255, 0.9);
}
:root[data-color-mode="dark"] .btn-secondary:hover {
    background: rgba(255, 255, 255, 0.2);
}

/* Danger Button */
.btn-danger {
    background: linear-gradient(135deg, var(--danger-color), var(--danger-hover));
    color: white !important;
    border-radius: 1rem;
    font-weight: 700;
    
    border-top: 1px solid rgba(255, 255, 255, 0.6);
    border-left: 1px solid rgba(255, 255, 255, 0.4);
    border-right: 1px solid rgba(0, 0, 0, 0.1);
    border-bottom: 1px solid rgba(0, 0, 0, 0.2);
    
    box-shadow: 
        0 10px 20px -5px var(--water-shadow),
        inset 0 2px 3px rgba(255, 255, 255, 0.4),
        inset 0 -2px 4px rgba(0, 0, 0, 0.15);
        
    transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}
.btn-danger:hover {
    transform: translateY(-4px) scale(1.02);
    box-shadow: 
        0 15px 25px -5px var(--water-shadow),
        inset 0 2px 3px rgba(255, 255, 255, 0.6),
        inset 0 -2px 4px rgba(0, 0, 0, 0.2);
}

/* MCQ Options */
.option-btn {
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    background: var(--glass-bg) !important;
    backdrop-filter: blur(16px) saturate(180%);
    border-radius: 1rem;
    
    border-top: 1px solid rgba(255, 255, 255, 0.7) !important;
    border-left: 1px solid rgba(255, 255, 255, 0.4) !important;
    border-right: 1px solid rgba(255, 255, 255, 0.1) !important;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1) !important;
    
    box-shadow: 
        0 8px 15px -5px var(--water-shadow),
        inset 0 2px 3px rgba(255, 255, 255, 0.4) !important;
        
    transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}
.option-btn:hover {
    transform: translateY(-3px) scale(1.01);
    background: rgba(255, 255, 255, 0.9) !important;
    border-color: var(--primary-color) !important;
    box-shadow: 
        0 12px 20px -5px var(--water-shadow),
        inset 0 2px 3px rgba(255, 255, 255, 0.8) !important;
}
:root[data-color-mode="dark"] .option-btn:hover {
    background: rgba(255, 255, 255, 0.2) !important;
}

'''
css = re.sub(old_buttons, new_buttons, css, flags=re.DOTALL)


# Fix Correct/Incorrect to match the 3D aesthetic
old_correct = r'\.correct \{.*?\}'
new_correct = '''.correct { 
    background: linear-gradient(135deg, var(--success-color), #059669) !important; 
    color: white !important; 
    border-top: 1px solid rgba(255,255,255,0.6) !important;
    border-left: 1px solid rgba(255,255,255,0.3) !important;
    border-bottom: 1px solid rgba(0,0,0,0.2) !important;
    border-right: 1px solid rgba(0,0,0,0.1) !important;
    box-shadow: 0 10px 20px -5px rgba(0,0,0,0.2), inset 0 2px 3px rgba(255,255,255,0.4) !important;
    transform: translateY(-2px) scale(1.02);
}'''
css = re.sub(old_correct, new_correct, css, flags=re.DOTALL)

old_incorrect = r'\.incorrect \{.*?\}'
new_incorrect = '''.incorrect { 
    background: linear-gradient(135deg, var(--danger-color), var(--danger-hover)) !important; 
    color: white !important; 
    border-top: 1px solid rgba(255,255,255,0.6) !important;
    border-left: 1px solid rgba(255,255,255,0.3) !important;
    border-bottom: 1px solid rgba(0,0,0,0.2) !important;
    border-right: 1px solid rgba(0,0,0,0.1) !important;
    box-shadow: 0 10px 20px -5px rgba(0,0,0,0.2), inset 0 2px 3px rgba(255,255,255,0.4) !important;
}'''
css = re.sub(old_incorrect, new_incorrect, css, flags=re.DOTALL)


with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Applied 3D Liquid Glass effect to all components")

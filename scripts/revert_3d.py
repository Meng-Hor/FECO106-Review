import re

py_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\scripts\3d_liquid_glass.py'
css_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\styles.css'

with open(py_path, 'r', encoding='utf-8') as f:
    py_code = f.read()

# Extract the new strings from the python script (which are now in the CSS)
# And replace them back with what they originally were!
# Wait, extracting from python string literals with regex is risky.
# Let's just manually redefine them here.

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# REVERT CARDS
new_card = r'/\* 3D Pop-up Liquid Glass Cards \*/.*?:root\[data-color-mode="dark"\] \.card-container \{.*?\}'
old_card = '''/* Premium Liquid Glass Cards */
.card-container {
    background: var(--glass-bg);
    backdrop-filter: blur(24px) saturate(180%);
    -webkit-backdrop-filter: blur(24px) saturate(180%);
    border: 1px solid var(--glass-border);
    border-radius: 1.5rem;
    box-shadow: 
        0 8px 32px 0 var(--water-shadow),
        inset 0 1px 1px 0 rgba(255, 255, 255, 0.4),
        inset 0 0 0 1px rgba(255, 255, 255, 0.1);
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}'''
css = re.sub(new_card, old_card, css, flags=re.DOTALL)

# REVERT BUTTONS
new_buttons = r'\.btn-primary \{.*?/\* MCQ Options \*/.*?\}'
old_buttons = '''.btn-primary {
    background: var(--primary-color);
    color: white !important;
    border-radius: 0.75rem;
    font-weight: 600;
    border: none;
    transition: all 0.2s ease;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15);
}
.btn-primary:hover {
    background: var(--primary-hover);
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.2);
}

/* Secondary / Glass Buttons (Quiz Sets) */
.btn-secondary {
    background: var(--glass-bg);
    color: var(--text-main) !important;
    border-radius: 0.75rem;
    font-weight: 600;
    border: 1px solid var(--glass-border);
    transition: all 0.2s ease;
}
.btn-secondary:hover {
    background: rgba(255, 255, 255, 1);
    transform: translateY(-3px);
    border-color: rgba(194, 110, 70, 0.3);
    box-shadow: 0 8px 25px rgba(194, 110, 70, 0.15);
}
.btn-secondary:hover {
    background: rgba(255, 255, 255, 0.2);
    transform: translateY(-3px);
    border-color: var(--primary-color);
    box-shadow: 0 8px 25px var(--water-shadow);
}

/* Danger Button */
.btn-danger {
    background: var(--danger-color);
    color: white !important;
    border-radius: 0.75rem;
    font-weight: 600;
    border: none;
    transition: all 0.2s ease;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15);
}
.btn-danger:hover {
    background: var(--danger-hover);
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.2);
}

/* MCQ Options */
.option-btn {
    font-family: 'JetBrains Mono', monospace;
    background: var(--glass-bg) !important;
    backdrop-filter: blur(16px) saturate(150%);
    border: 1px solid var(--glass-border) !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 2px 10px var(--water-shadow), inset 0 1px 1px 0 rgba(255, 255, 255, 0.3);
}'''
css = re.sub(new_buttons, old_buttons, css, flags=re.DOTALL)

# Re-fix the secondary hover bug (I accidentally restored my previous bug of having two hovers)
css = css.replace('''.btn-secondary:hover {
    background: rgba(255, 255, 255, 1);
    transform: translateY(-3px);
    border-color: rgba(194, 110, 70, 0.3);
    box-shadow: 0 8px 25px rgba(194, 110, 70, 0.15);
}
.btn-secondary:hover {
    background: rgba(255, 255, 255, 0.2);
    transform: translateY(-3px);
    border-color: var(--primary-color);
    box-shadow: 0 8px 25px var(--water-shadow);
}''', '''.btn-secondary:hover {
    background: var(--nav-btn-hover);
    transform: translateY(-3px);
    border-color: var(--primary-color);
    box-shadow: 0 8px 25px var(--water-shadow);
}''')


# REVERT CORRECT/INCORRECT
new_correct = r'\.correct \{.*?scale\(1\.02\);\n\}'
old_correct = '''.correct { 
    background: var(--success-color) !important; 
    color: white !important; 
    border: none !important;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15) !important;
}'''
css = re.sub(new_correct, old_correct, css, flags=re.DOTALL)

new_incorrect = r'\.incorrect \{.*?!important;\n\}'
old_incorrect = '''.incorrect { 
    background: var(--danger-color) !important; 
    color: white !important; 
    border: none !important;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15) !important;
}'''
css = re.sub(new_incorrect, old_incorrect, css, flags=re.DOTALL)

# Fix option hover
new_option_hover = r'\.option-btn:hover \{.*?:root\[data-color-mode="dark"\] \.option-btn:hover \{.*?\}'
old_option_hover = '''.option-btn:hover {
    background: rgba(255, 255, 255, 0.6) !important;
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
}'''
css = re.sub(new_option_hover, old_option_hover, css, flags=re.DOTALL)


with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Reverted to previous UI state")

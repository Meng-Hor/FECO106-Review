import re

# 1. Update CSS
css_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

new_classes = '''
.option-badge {
    background: var(--nav-bg);
    color: var(--text-main);
    border: 1px solid var(--glass-border);
}
.btn-success {
    background: var(--success-color);
    color: white !important;
    border-radius: 0.75rem;
    font-weight: 600;
    border: none;
    transition: all 0.2s ease;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15);
}
.btn-success:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.2);
}
'''

if '.btn-success' not in css:
    css = css + new_classes
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)


# 2. Clean quiz.html
html_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\quiz.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix option buttons generation
old_btn_class = r'btn.className = `option-btn w-full p-3 sm:p-4 text-left border rounded-lg bg-white/40 backdrop-blur-lg border border-gray-200/50 hover:bg-white/60 font-medium \$\{borderClasses\[idx\]\}`;'
new_btn_class = 'btn.className = `option-btn w-full p-3 sm:p-4 text-left font-medium rounded-lg flex items-center ${borderClasses[idx]}`;'

old_btn_html = r'btn.innerHTML = `<span class="mr-3 font-bold text-gray-800 bg-white px-3 py-1 rounded-md shadow-sm border border-gray-200 text-gray-700 backdrop-blur-sm">\$\{idx \+ 1\}</span> \$\{escapeHtml\(opt\)\}`;'
new_btn_html = 'btn.innerHTML = `<span class="option-badge mr-3 font-bold px-3 py-1 rounded-md shadow-sm backdrop-blur-sm">${idx + 1}</span> <span>${escapeHtml(opt)}</span>`;'

html = re.sub(old_btn_class, new_btn_class, html)
html = re.sub(old_btn_html, new_btn_html, html)


# Fix open-ended feedback container
old_feedback_container = r'<div id="answer-feedback" class="hidden mt-6 p-4 bg-white/40 backdrop-blur-lg border \n?border-gray-200/50 border rounded-lg">'
new_feedback_container = r'<div id="answer-feedback" class="hidden mt-6 p-5 card-container border rounded-xl">'
html = re.sub(old_feedback_container, new_feedback_container, html, flags=re.DOTALL)

# Fix open-ended feedback text
html = html.replace('<h4 class="font-bold text-gray-700 mb-2">Model Answer:</h4>', '<h4 class="font-bold mb-3">Model Answer:</h4>')
html = html.replace('<p id="model-answer-text" class="text-gray-600 mb-4"></p>', '<p id="model-answer-text" class="mb-5 leading-relaxed"></p>')

# Fix self-correct buttons
html = html.replace('class="px-6 py-2 btn-primary bg-green-500 px-6 py-2"', 'class="px-6 py-2 btn-success w-full sm:w-auto"')
html = html.replace('class="px-6 py-2 btn-primary bg-red-500 px-6 py-2"', 'class="px-6 py-2 btn-danger w-full sm:w-auto"')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Cleaned up quiz.html hardcoded colors completely")

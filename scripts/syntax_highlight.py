import re

# 1. Update quiz.html
quiz_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\quiz.html'
with open(quiz_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Add Highlight.js CDN links in the <head>
if 'highlight.js' not in html:
    head_injection = '''
    <!-- Highlight.js for Code Syntax Highlighting -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/tokyo-night-dark.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/cpp.min.js"></script>
</head>'''
    html = html.replace('</head>', head_injection)

# Update Javascript in loadQuestion
old_load = r'document\.getElementById\(\'question-text\'\)\.innerHTML = currentQuestion\.question;'
new_load = '''
        // Strip hardcoded inline styles and inject syntax highlighting classes
        let qHTML = currentQuestion.question;
        qHTML = qHTML.replace(/<pre style="[^"]*">/g, '<pre class="quiz-code-block">');
        qHTML = qHTML.replace(/<code>/g, '<code class="language-cpp">');
        
        document.getElementById('question-text').innerHTML = qHTML;
        
        // Trigger Highlight.js on the newly injected code blocks
        document.querySelectorAll('pre code').forEach((block) => {
            hljs.highlightElement(block);
        });
'''
html = html.replace(old_load, new_load)

with open(quiz_path, 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Add CSS for .quiz-code-block
css_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

if '.quiz-code-block' not in css:
    css_injection = '''
/* Custom Code Block Styling to override Highlight.js defaults and match Glassmorphism */
.quiz-code-block {
    background: rgba(15, 23, 42, 0.85) !important;
    backdrop-filter: blur(12px) saturate(180%);
    -webkit-backdrop-filter: blur(12px) saturate(180%);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 1rem;
    padding: 1.5rem !important;
    margin-top: 1.5rem;
    box-shadow: inset 0 1px 1px rgba(255, 255, 255, 0.1), 0 8px 24px rgba(0, 0, 0, 0.3);
    overflow-x: auto;
}

.quiz-code-block code {
    font-family: 'Fira Code', 'Courier New', Courier, monospace !important;
    font-size: 0.95rem;
    line-height: 1.5;
    background: transparent !important;
    padding: 0 !important;
}
'''
    css = css + css_injection

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Injected Highlight.js and glassmorphic code block styling")

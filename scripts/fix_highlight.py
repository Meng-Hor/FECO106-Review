import re

quiz_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\quiz.html'
with open(quiz_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix the malformed HTML tag
html = html.replace('class="text-xl sm:text-2xl font-semibold mb-6 style="color: var(--text-main)""', 'class="text-xl sm:text-2xl font-semibold mb-6" style="color: var(--text-main)"')

# 2. Inject Highlight.js into <head> if it's missing or if the previous injection was incomplete
if 'highlight.js/11.9.0' not in html:
    head_injection = '''
    <!-- Highlight.js for Code Syntax Highlighting -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/tokyo-night-dark.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/cpp.min.js"></script>
</head>'''
    html = html.replace('</head>', head_injection)

# 3. Update the loadQuestion Javascript logic
old_load = r'qText\.innerHTML = q\.question;'
new_load = '''
            // Strip hardcoded inline styles and inject syntax highlighting classes
            let qHTML = q.question;
            qHTML = qHTML.replace(/<pre style="[^"]*">/g, '<pre class="quiz-code-block">');
            qHTML = qHTML.replace(/<code>/g, '<code class="language-cpp">');
            
            qText.innerHTML = qHTML;
            
            // Trigger Highlight.js on the newly injected code blocks
            document.querySelectorAll('pre code').forEach((block) => {
                hljs.highlightElement(block);
            });
'''
html = re.sub(old_load, new_load, html)

with open(quiz_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Fixed syntax highlighting injection")

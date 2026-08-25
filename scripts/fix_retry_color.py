path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\quiz.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# Switch retry from btn-secondary to btn-success
html = html.replace(
    'id="retry-btn" class="btn-secondary px-6 py-3 w-full text-base rounded-xl shadow-lg transition-all flex items-center justify-center gap-2"',
    'id="retry-btn" class="btn-success px-6 py-3 w-full text-base rounded-xl shadow-lg transition-all flex items-center justify-center gap-2"'
)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Retry button now uses btn-success (theme-adaptive)")

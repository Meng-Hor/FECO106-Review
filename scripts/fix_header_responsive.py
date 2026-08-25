import re

def fix_header(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find the nav container
    nav_pattern = r'<nav[^>]*>.*?<div class="([^"]* flex [^"]*)">'
    match = re.search(nav_pattern, html, re.DOTALL)
    
    if match:
        old_classes = match.group(1)
        
        # We know it starts with max-w-5xl mx-auto
        # Let's completely replace it for clean code
        new_classes = "max-w-5xl mx-auto px-4 md:px-6 py-3 md:py-4 flex flex-col sm:flex-row justify-between items-center gap-3 sm:gap-0"
        
        html = html.replace(old_classes, new_classes)
        
    # Let's also make sure the link container scales its text slightly smaller on mobile
    html = html.replace('class="flex space-x-4 sm:space-x-6"', 'class="flex space-x-6 sm:space-x-8 text-sm sm:text-base"')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

fix_header(r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\index.html')
fix_header(r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\quiz.html')

print("Fixed header responsiveness")

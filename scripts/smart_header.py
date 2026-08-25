import re

def make_header_smart(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Add ID and explicit transition to the header wrapper
    old_wrapper = r'<div class="px-4 pt-4 sm:pt-6 sticky top-0 z-50 transition-all">'
    new_wrapper = r'<div id="smart-header" class="px-4 pt-4 sm:pt-6 sticky top-0 z-50" style="transition: transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);">'
    
    html = re.sub(old_wrapper, new_wrapper, html)

    # 2. Inject the javascript logic at the end of the file, just before </body>
    smart_header_js = '''
    <script>
        // Smart Header Logic
        let lastScrollY = window.scrollY;
        const header = document.getElementById('smart-header');
        window.addEventListener('scroll', () => {
            if (window.scrollY > lastScrollY && window.scrollY > 80) {
                // Scrolling down & past the top
                header.style.transform = 'translateY(-150%)';
            } else {
                // Scrolling up or at top
                header.style.transform = 'translateY(0)';
            }
            lastScrollY = window.scrollY;
        });
    </script>
'''
    # Check if we already injected it
    if 'Smart Header Logic' not in html:
        html = html.replace('</body>', f'{smart_header_js}</body>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)


make_header_smart(r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\index.html')
make_header_smart(r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\quiz.html')

print("Implemented smart auto-hiding header based on scroll behavior")

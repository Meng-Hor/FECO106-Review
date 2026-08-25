import re

def optimize_smart_header_again(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Replace the old Javascript logic
    old_js = r'// Smart Header Logic - Optimized for smoothness.*?ticking = false;\s*}\);'
    
    new_js = '''// Smart Header Logic - Intentional Scroll Reveal
        let lastScrollY = window.scrollY;
        let scrollUpDistance = 0;
        let ticking = false;
        
        const header = document.getElementById('smart-header');
        
        window.addEventListener('scroll', () => {
            if (!ticking) {
                window.requestAnimationFrame(() => {
                    const currentScrollY = window.scrollY;
                    const scrollDelta = currentScrollY - lastScrollY;
                    
                    if (scrollDelta > 0) {
                        // Scrolling DOWN
                        scrollUpDistance = 0; // Reset up-scroll counter
                        if (currentScrollY > 100) {
                            header.style.transform = 'translateY(-120%)';
                            header.style.opacity = '0';
                            header.style.pointerEvents = 'none';
                        }
                    } else if (scrollDelta < 0) {
                        // Scrolling UP
                        scrollUpDistance += Math.abs(scrollDelta);
                        
                        // Only reveal if the user intentionally scrolled up by more than 150px,
                        // OR if they have reached the absolute top of the page.
                        if (scrollUpDistance > 150 || currentScrollY < 100) {
                            header.style.transform = 'translateY(0)';
                            header.style.opacity = '1';
                            header.style.pointerEvents = 'auto';
                        }
                    }
                    
                    lastScrollY = currentScrollY;
                    ticking = false;
                });
                ticking = true;
            }
        }, { passive: true });'''
    
    html = re.sub(old_js, new_js, html, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

optimize_smart_header_again(r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\index.html')
optimize_smart_header_again(r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\quiz.html')

print("Implemented intentional scroll-up distance threshold")

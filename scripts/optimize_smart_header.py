import re

def optimize_smart_header(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Remove the bouncy transition from the header div and replace it with a smooth, linear ease
    old_wrapper = r'<div id="smart-header" class="px-4 pt-4 sm:pt-6 sticky top-0 z-50" style="transition: transform 0.4s cubic-bezier\(0.34, 1.56, 0.64, 1\);">'
    new_wrapper = r'<div id="smart-header" class="px-4 pt-4 sm:pt-6 sticky top-0 z-50" style="transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);">'
    html = re.sub(old_wrapper, new_wrapper, html)

    # 2. Replace the old Javascript logic with the optimized requestAnimationFrame logic
    old_js = r'// Smart Header Logic.*?lastScrollY = window\.scrollY;\s*}\);'
    
    new_js = '''// Smart Header Logic - Optimized for smoothness
        let lastScrollY = window.scrollY;
        let ticking = false;
        
        const header = document.getElementById('smart-header');
        
        window.addEventListener('scroll', () => {
            if (!ticking) {
                window.requestAnimationFrame(() => {
                    const currentScrollY = window.scrollY;
                    const scrollDelta = currentScrollY - lastScrollY;
                    
                    // Only trigger if scrolled more than 15px (prevents micro-jitters and headache-inducing flashes)
                    if (Math.abs(scrollDelta) > 15) {
                        if (scrollDelta > 0 && currentScrollY > 100) {
                            // Scrolling down
                            header.style.transform = 'translateY(-120%)';
                            header.style.opacity = '0';
                            header.style.pointerEvents = 'none';
                        } else {
                            // Scrolling up
                            header.style.transform = 'translateY(0)';
                            header.style.opacity = '1';
                            header.style.pointerEvents = 'auto';
                        }
                        lastScrollY = currentScrollY;
                    }
                    ticking = false;
                });
                ticking = true;
            }
        }, { passive: true });'''
    
    html = re.sub(old_js, new_js, html, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

optimize_smart_header(r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\index.html')
optimize_smart_header(r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\quiz.html')

print("Optimized smart header with smooth easing and scroll thresholds")

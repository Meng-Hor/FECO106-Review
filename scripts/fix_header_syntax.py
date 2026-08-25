import re

def fix_syntax_error(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find where the Smart Header Logic starts
    start_idx = html.find('// Smart Header Logic')
    if start_idx == -1: return

    # Find where the script ends
    end_idx = html.find('</script>\n</body>')
    if end_idx == -1: return

    # Completely replace everything from start_idx to end_idx
    clean_js = '''// Smart Header Logic - Fixed
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
                        
                        // Reveal if scrolled up intentionally, or near top
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
        }, { passive: true });
    '''
    
    html = html[:start_idx] + clean_js + html[end_idx:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

fix_syntax_error(r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\index.html')
fix_syntax_error(r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\quiz.html')

print("Fixed Javascript syntax error in smart header logic")

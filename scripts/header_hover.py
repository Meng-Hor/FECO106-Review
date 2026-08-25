import re

def add_mouse_hover_header(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find where the Smart Header Logic starts
    start_idx = html.find('// Smart Header Logic')
    if start_idx == -1: return

    # Find where the script ends
    end_idx = html.find('</script>\n</body>')
    if end_idx == -1: return

    # Completely replace everything from start_idx to end_idx
    clean_js = '''// Smart Header Logic - 300px Threshold & Top Hover Reveal
        let lastScrollY = window.scrollY;
        let scrollUpDistance = 0;
        let ticking = false;
        let isHoveringTop = false;
        
        const header = document.getElementById('smart-header');
        
        function showHeader() {
            header.style.transform = 'translateY(0)';
            header.style.opacity = '1';
            header.style.pointerEvents = 'auto';
        }

        function hideHeader() {
            if (window.scrollY > 100 && !isHoveringTop) {
                header.style.transform = 'translateY(-120%)';
                header.style.opacity = '0';
                header.style.pointerEvents = 'none';
            }
        }

        // 1. Mouse hover logic for desktop
        document.addEventListener('mousemove', (e) => {
            if (e.clientY < 90) {
                if (!isHoveringTop) {
                    isHoveringTop = true;
                    showHeader();
                }
            } else {
                if (isHoveringTop) {
                    isHoveringTop = false;
                    // Hide if we move mouse away, UNLESS we earned the header by scrolling up 300px
                    if (scrollUpDistance < 300 && window.scrollY > 100) {
                        hideHeader();
                    }
                }
            }
        });

        // 2. Scroll logic
        window.addEventListener('scroll', () => {
            if (!ticking) {
                window.requestAnimationFrame(() => {
                    const currentScrollY = window.scrollY;
                    const scrollDelta = currentScrollY - lastScrollY;
                    
                    if (scrollDelta > 0) {
                        // Scrolling DOWN
                        scrollUpDistance = 0; // Reset up-scroll counter
                        hideHeader();
                    } else if (scrollDelta < 0) {
                        // Scrolling UP
                        scrollUpDistance += Math.abs(scrollDelta);
                        
                        // Reveal if scrolled up intentionally by 300px, or near top
                        if (scrollUpDistance > 300 || currentScrollY < 100) {
                            showHeader();
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

add_mouse_hover_header(r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\index.html')
add_mouse_hover_header(r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\quiz.html')

print("Implemented 300px scroll threshold and top-hover reveal for header")

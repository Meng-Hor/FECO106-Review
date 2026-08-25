js_snippet = """
  <script>
    // Mobile Hamburger Menu Toggle
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    const hamburgerIcon = document.getElementById('hamburger-icon');
    if (mobileMenuBtn && mobileMenu) {
      mobileMenuBtn.addEventListener('click', () => {
        const isOpen = !mobileMenu.classList.contains('hidden');
        mobileMenu.classList.toggle('hidden');
        hamburgerIcon.className = isOpen ? 'fa-solid fa-bars text-sm' : 'fa-solid fa-xmark text-sm';
      });
      // Close menu on link click
      mobileMenu.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
          mobileMenu.classList.add('hidden');
          hamburgerIcon.className = 'fa-solid fa-bars text-sm';
        });
      });
    }
  </script>"""

import re

for path in [
    r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\index.html',
    r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\quiz.html',
]:
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Insert before </body>
    html = html.replace('</body>', js_snippet + '\n</body>')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Added hamburger JS to {path}")

import re

path = r'C:\Users\Ly Meng Hor ING\Documents\Lesson-Review\web\index.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

correct_js = """  <script>
    // Theme & Mode Logic
    const themeSelector = document.getElementById('theme-selector');
    const modeToggle = document.getElementById('mode-toggle');
    const modeIcon = document.getElementById('mode-icon');
    
    // Load saved theme
    const savedTheme = localStorage.getItem('selectedTheme') || 'aura';
    document.documentElement.setAttribute('data-theme', savedTheme);
    if (themeSelector) themeSelector.value = savedTheme;

    // Load saved mode or default strictly to light
    let currentMode = localStorage.getItem('colorMode') || 'light';
    document.documentElement.setAttribute('data-color-mode', currentMode);
    updateModeIcon();

    // Listen for Theme changes
    if (themeSelector) {
      themeSelector.addEventListener('change', (e) => {
        const newTheme = e.target.value;
        document.documentElement.setAttribute('data-theme', newTheme);
        localStorage.setItem('selectedTheme', newTheme);
      });
    }
    
    // Listen for Mode changes
    if (modeToggle) {
      modeToggle.addEventListener('click', () => {
        modeToggle.classList.add('spinning');
        modeToggle.addEventListener('animationend', () => modeToggle.classList.remove('spinning'), { once: true });
        currentMode = currentMode === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-color-mode', currentMode);
        localStorage.setItem('colorMode', currentMode);
        updateModeIcon();
      });
    }

    function updateModeIcon() {
      if (modeIcon) {
        if (currentMode === 'dark') {
          modeIcon.className = 'fa-solid fa-sun text-sm sm:text-base';
        } else {
          modeIcon.className = 'fa-solid fa-moon text-sm sm:text-base';
        }
      }
    }
  </script>"""

# Find the old script block
# It starts with <script>\n    // Theme Logic (shared with feco106.html)
old_script_pattern = re.compile(r'<script>\s*// Theme Logic \(shared with feco106\.html\).*?</script>', re.DOTALL)
html = old_script_pattern.sub(correct_js, html)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Fixed theme logic in index.html")

import re

quiz_path = r'C:\Users\Ly Meng Hor ING\Documents\Lesson-Review\web\quiz_networking.html'
with open(quiz_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove data.js from <head>
html = html.replace('<script src="sets/Networking_OSI_TCP_IP/data.js"></script>', '')

# 2. Fix the mess at the bottom
# The mess looks like:
# <script>\n        window.quizData = [];\n      </script>\n      </script>\n      </script>\n      <script>\n      const pdfData = ...
pattern = re.compile(r'<script>\s*window\.quizData = \[\];\s*</script>.*?(?=<script>\s*const pdfData)', re.DOTALL)
clean_bottom = """<script>
        window.quizData = [];
    </script>
    <script src="sets/Networking_OSI_TCP_IP/data.js"></script>
    """
html = pattern.sub(clean_bottom, html)

with open(quiz_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Fixed quiz_networking.html completely")

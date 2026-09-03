import re

# Fix data.js
data_path = r'C:\Users\Ly Meng Hor ING\Documents\Lesson-Review\web\sets\Networking_OSI_TCP_IP\data.js'
with open(data_path, 'r', encoding='utf-8') as f:
    data_content = f.read()

# Change "title" to "set"
data_content = data_content.replace('"title": "OSI and TCP/IP Model",', '"set": "OSI_and_TCP_IP_Model",')
with open(data_path, 'w', encoding='utf-8') as f:
    f.write(data_content)
print("Fixed data.js")

# Fix networking.html script section
html_path = r'C:\Users\Ly Meng Hor ING\Documents\Lesson-Review\web\networking.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# The mangled block starts at `<script>\n    window.quizData = [];\n    </script>`
# and ends right before `<script>\n    const pdfData = [];`
# Let's clean it up.
pattern = re.compile(r'<script>\s*window\.quizData = \[\];\s*</script>.*?<script>\s*const pdfData = \[\];', re.DOTALL)
clean_block = """<script>
      window.quizData = [];
    </script>
    <script src="sets/Networking_OSI_TCP_IP/data.js"></script>
    <script>
    const pdfData = [];"""

html = pattern.sub(clean_block, html)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed networking.html scripts")

# Let's also make sure quiz_networking.html's script section is correct (it might have been mangled too)
quiz_path = r'C:\Users\Ly Meng Hor ING\Documents\Lesson-Review\web\quiz_networking.html'
with open(quiz_path, 'r', encoding='utf-8') as f:
    quiz_html = f.read()

# Fix mangled script tags in quiz_networking.html
quiz_pattern = re.compile(r'(<script src="sets/.*?>\s*)+')
clean_quiz_script = '<script src="sets/Networking_OSI_TCP_IP/data.js"></script>\n    '
quiz_html = quiz_pattern.sub(clean_quiz_script, quiz_html)

# But wait, did I use the exact same broken regex before?
# Let's just find exactly where highlight.js ends and our script should go.
quiz_html = re.sub(
    r'<script src="https://cdnjs\.cloudflare\.com/ajax/libs/highlight\.js/11\.9\.0/languages/cpp\.min\.js"></script>.*?<script>\s*const quizData = window\.quizData;',
    r'<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/cpp.min.js"></script>\n    <script src="sets/Networking_OSI_TCP_IP/data.js"></script>\n    <script>\n        const quizData = window.quizData;',
    quiz_html,
    flags=re.DOTALL
)

with open(quiz_path, 'w', encoding='utf-8') as f:
    f.write(quiz_html)
print("Fixed quiz_networking.html scripts")

import re

quiz_path = r'C:\Users\Ly Meng Hor ING\Documents\Lesson-Review\web\quiz_networking.html'
with open(quiz_path, 'r', encoding='utf-8') as f:
    quiz_html = f.read()

# Strip out all the bad duplicate lines: <script src="sets/Networking_OSI_TCP_IP/data.js"></script>
quiz_html = re.sub(r'(<script src="sets/Networking_OSI_TCP_IP/data\.js"></script>\s*)+', '', quiz_html)

# Now inject exactly ONE back right after the highlight.js cpp.min.js script
clean_quiz_script = '<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/cpp.min.js"></script>\n    <script src="sets/Networking_OSI_TCP_IP/data.js"></script>\n'
quiz_html = quiz_html.replace('<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/cpp.min.js"></script>', clean_quiz_script)

with open(quiz_path, 'w', encoding='utf-8') as f:
    f.write(quiz_html)

print("Fixed quiz_networking.html script tags")

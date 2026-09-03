import os
import re
import shutil

# Paths
base_dir = r'C:\Users\Ly Meng Hor ING\Documents\Lesson-Review\web'
quiz_path = os.path.join(base_dir, 'quiz.html')
feco_quiz_path = os.path.join(base_dir, 'quiz_feco106.html')
net_quiz_path = os.path.join(base_dir, 'quiz_networking.html')
feco_html = os.path.join(base_dir, 'feco106.html')
net_html = os.path.join(base_dir, 'networking.html')

# 1. Rename quiz.html to quiz_feco106.html
shutil.copy(quiz_path, feco_quiz_path)

# 2. Update feco106.html to point to quiz_feco106.html
with open(feco_html, 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace("window.location.href = 'quiz.html?set=' + index;", "window.location.href = 'quiz_feco106.html?set=' + index;")
with open(feco_html, 'w', encoding='utf-8') as f:
    f.write(content)

# 3. Create quiz_networking.html
with open(quiz_path, 'r', encoding='utf-8') as f:
    quiz_content = f.read()

# Update title
quiz_content = quiz_content.replace('<title>FECO106: Mid-Term Review</title>', '<title>Networking: OSI and TCP/IP Review</title>')

# Update script sources to ONLY load networking data
script_pattern = re.compile(r'(<script src="sets/.*?>\s*)+')
new_script = '<script src="sets/Networking_OSI_TCP_IP/data.js"></script>\n    '
quiz_content = script_pattern.sub(new_script, quiz_content)

# Update the Back to Dashboard button redirect to go to networking.html instead of feco106.html
quiz_content = quiz_content.replace("window.location.href = 'feco106.html'", "window.location.href = 'networking.html'")
quiz_content = quiz_content.replace('href="feco106.html#dashboard"', 'href="networking.html#dashboard"')
quiz_content = quiz_content.replace('href="feco106.html#pdf-container"', 'href="networking.html#pdf-container"')

with open(net_quiz_path, 'w', encoding='utf-8') as f:
    f.write(quiz_content)

# 4. Update networking.html to point to quiz_networking.html
with open(net_html, 'r', encoding='utf-8') as f:
    net_content = f.read()
net_content = net_content.replace("window.location.href = 'quiz.html?set=' + index;", "window.location.href = 'quiz_networking.html?set=' + index;")
net_content = net_content.replace('href="#dashboard"', 'href="networking.html#dashboard"') # keep it absolute/relative to itself to be safe, or just "#dashboard"
with open(net_html, 'w', encoding='utf-8') as f:
    f.write(net_content)

# 5. Delete old quiz.html to avoid confusion
os.remove(quiz_path)

print("Quiz pages split successfully")

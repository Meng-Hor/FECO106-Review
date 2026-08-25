import re

def update_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    new_head = '<link rel="icon" type="image/png" href="dog_icon.png">\n    <title>GoodLuck :D</title>'
    html = re.sub(r'<title>.*?</title>', new_head, html)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

update_file(r'web\index.html')
update_file(r'web\quiz.html')
print("Updated head tags!")

import re

data_path = r'C:\Users\Ly Meng Hor ING\Documents\Lesson-Review\web\sets\Networking_OSI_TCP_IP\data.js'
with open(data_path, 'r', encoding='utf-8') as f:
    data_content = f.read()

# Change "correct" to "correctOption"
data_content = data_content.replace('"correct": ', '"correctOption": ')

with open(data_path, 'w', encoding='utf-8') as f:
    f.write(data_content)

print("Fixed data.js correctOption")

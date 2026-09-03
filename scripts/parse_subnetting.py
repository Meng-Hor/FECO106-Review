import os
import json
import re

file_path = r'C:\Users\Ly Meng Hor ING\Downloads\Telegram Desktop\IPv4 and Subnetting Exercises.md'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# The file has sections starting with "## Exercise N: Title"
# I will split it by "## Exercise "
exercises = re.split(r'## Exercise \d+:\s+', text)

# The first element is the preamble
preamble = exercises[0].strip()

questions = []
for ex in exercises[1:]:
    lines = ex.strip().split('\n')
    title = lines[0].strip()
    content = '\n'.join(lines[1:]).strip()
    
    questions.append({
        "type": "open_ended",
        "question": f"**{title}**\n\n{content}\n\n*(Use the scratchpad to work out your answer!)*",
        "correctAnswer": "This is an open-ended subnetting exercise. Self-grade based on your calculations.",
        "timeLimit": 120,
        "points": 1000
    })

quiz_data = {
    "set": "IPv4_and_Subnetting_Exercises",
    "questions": questions
}

js_content = f"window.quizData.push({json.dumps(quiz_data, indent=4)});"

out_dir = r'C:\Users\Ly Meng Hor ING\Documents\Lesson-Review\web\sets\Networking_IPv4_Subnetting'
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, 'data.js'), 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Created data.js for IPv4 subnetting")

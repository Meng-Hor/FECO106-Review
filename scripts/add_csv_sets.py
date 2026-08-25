import csv
import json
import os
import re

html_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\index.html'
material_dir = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\material'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'const quizData = (\[.*?\]);\s*const pdfData', content, re.DOTALL)
if not match:
    print("Could not find quizData")
    exit()

quiz_data = json.loads(match.group(1))

# Remove existing CSV sets if they accidentally remain
quiz_data = [s for s in quiz_data if not s['set'].startswith('Algorithm_III_Week_4_QuizGlow_')]

csv_sets = []

for filename in os.listdir(material_dir):
    if filename.endswith('.csv'):
        set_name = filename.replace('.csv', '')
        filepath = os.path.join(material_dir, filename)
        
        quiz_set = {
            "set": set_name,
            "questions": []
        }
        
        with open(filepath, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    q = {
                        "type": "mcq",
                        "question": row['Question Text'],
                        "timeLimit": row['Time Limit (seconds)'],
                        "points": row['Points'],
                        "options": [
                            row['Option 1 (Red)'],
                            row['Option 2 (Blue)'],
                            row['Option 3 (Yellow)'],
                            row['Option 4 (Green)']
                        ],
                        "correctOption": int(row['Correct Option Number (1-4)'])
                    }
                    quiz_set['questions'].append(q)
                except KeyError as e:
                    print("KeyError:", e, "in row:", row)
                    continue
        
        if quiz_set['questions']:
            csv_sets.append(quiz_set)

# Sort them so they are in order
csv_sets.sort(key=lambda x: x['set'])

# Insert CSV sets at the beginning
quiz_data = csv_sets + quiz_data

quiz_data_str = json.dumps(quiz_data, indent=4)
new_content = content[:match.start()] + f"const quizData = {quiz_data_str};\n        const pdfData" + content[match.end():]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Added CSV sets back into quizData!")

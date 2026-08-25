import json
import re

html_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the existing JSON
match = re.search(r'const quizData = (\[.*?\]);', content, re.DOTALL)
if match:
    quiz_data_str = match.group(1)
    quiz_data = json.loads(quiz_data_str)
    
    # New set
    new_set = {
        "set": "PDF_Set_1_Core_Concepts",
        "questions": [
            {
                "question": "A pointer stores an address. What does that address identify in a real program?",
                "timeLimit": "30",
                "points": "1000",
                "options": [
                    "The line number in the source code where the variable was defined",
                    "The exact location in the computer's memory (RAM) where a specific piece of data is stored",
                    "The file path on the hard drive where the program is saved",
                    "The logical size of the array it points to"
                ],
                "correctOption": 2
            },
            {
                "question": "What problem occurs if the owner finishes using allocated memory but never releases it?",
                "timeLimit": "30",
                "points": "1000",
                "options": [
                    "A syntax error during compilation",
                    "The pointer becomes NULL automatically",
                    "A memory leak occurs, potentially exhausting available memory",
                    "The memory is automatically garbage collected in C"
                ],
                "correctOption": 3
            },
            {
                "question": "Why is p dangling after free(a) even though p still contains an address?",
                "timeLimit": "30",
                "points": "1000",
                "options": [
                    "Because p was not declared as a pointer",
                    "Because free(a) deletes the variable p",
                    "Because the memory at that address has been returned to the system and is no longer valid",
                    "Because p automatically changes its address to 0"
                ],
                "correctOption": 3
            },
            {
                "question": "Why does a = NULL not automatically change p to NULL?",
                "timeLimit": "30",
                "points": "1000",
                "options": [
                    "They are separate variables; changing 'a' only changes 'a'",
                    "Because p is a constant pointer",
                    "Because NULL is not a valid address",
                    "Because p points to 'a' directly"
                ],
                "correctOption": 1
            },
            {
                "question": "Name the exact statements between which *p is valid.",
                "timeLimit": "30",
                "points": "1000",
                "options": [
                    "Between variable declaration and program exit",
                    "Between successful allocation (e.g., malloc) and deallocation (e.g., free)",
                    "Between fopen and fclose",
                    "Between main() and return 0;"
                ],
                "correctOption": 2
            }
        ]
    }
    
    # Check if already exists to avoid duplication
    if not any(s['set'] == new_set['set'] for s in quiz_data):
        quiz_data.append(new_set)
        
    new_quiz_data_str = json.dumps(quiz_data, indent=4)
    new_content = content.replace(f"const quizData = {quiz_data_str};", f"const quizData = {new_quiz_data_str};")
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print("Successfully updated index.html with the new PDF quiz set!")
else:
    print("Could not find quizData in index.html")

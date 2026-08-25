import json
import re

html_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'const quizData = (\[.*?\]);\s*const pdfData', content, re.DOTALL)
if not match:
    print("Could not find quizData")
    exit()

quiz_data = json.loads(match.group(1))

rev1 = next(s for s in quiz_data if s['set'] == 'Revision_Exercise_1')
rev2 = next(s for s in quiz_data if s['set'] == 'Revision_Exercise_2')

# Remove previously accidentally appended if any
rev1['questions'] = rev1['questions'][:12] # First 12 were correct
rev2['questions'] = rev2['questions'][:10] # First 10 were correct

# Add Revision 1 - Round 3 (Set 1)
rev1_missing_1 = [
    {
        "type": "mcq",
        "question": "Round 3 (Clue Match): A function overwrites its only owner pointer with a new address without freeing the old allocation.",
        "options": ["Memory Leak", "Dangling Pointer", "Invariant", "Whole-Record Swap"],
        "correctOption": 1
    },
    {
        "type": "mcq",
        "question": "Round 3 (Clue Match): After free(records), an alias still holds &records[2].",
        "options": ["Memory Leak", "Dangling Pointer", "Invariant", "Whole-Record Swap"],
        "correctOption": 2
    },
    {
        "type": "mcq",
        "question": "Round 3 (Clue Match): At every public operation boundary, 0 <= size && size <= capacity must be true.",
        "options": ["Memory Leak", "Dangling Pointer", "Invariant", "Whole-Record Swap"],
        "correctOption": 3
    },
    {
        "type": "mcq",
        "question": "Round 3 (Clue Match): A loader parses into temporary fields, rejects malformed/duplicate data, then stores once and increments size.",
        "options": ["Read - Validate - Commit", "Buffer Overrun", "Memory Leak", "Whole-Record Swap"],
        "correctOption": 1
    },
    {
        "type": "mcq",
        "question": "Round 3 (Clue Match): After sorting, each student ID remains attached to that student's name and score.",
        "options": ["Read - Validate - Commit", "Buffer Overrun", "Memory Leak", "Whole-Record Swap"],
        "correctOption": 4
    },
    {
        "type": "mcq",
        "question": "Round 3 (Clue Match): An insertion writes a[size] when size == capacity and growth was not performed.",
        "options": ["Read - Validate - Commit", "Buffer Overrun", "Memory Leak", "Whole-Record Swap"],
        "correctOption": 2
    }
]

# Add Revision 1 - Round 3 (Set 2)
rev1_missing_2 = [
    {
        "type": "mcq",
        "question": "Round 3 (Match): Malformed record",
        "options": ["Publish one fully validated record", "Confirm every formatted write", "Input missing required fields or containing unexpected extra data", "Move every field together during sorting"],
        "correctOption": 3
    },
    {
        "type": "mcq",
        "question": "Round 3 (Match): Duplicate ID",
        "options": ["A key already stored in the collection", "Confirm every formatted write", "Input missing required fields", "Move every field together"],
        "correctOption": 1
    },
    {
        "type": "mcq",
        "question": "Round 3 (Match): Whole-record swap",
        "options": ["Publish one fully validated record", "Move every field together during sorting", "A key already stored in the collection", "Confirm every formatted write"],
        "correctOption": 2
    },
    {
        "type": "mcq",
        "question": "Round 3 (Match): Commit",
        "options": ["Publish one fully validated record and then increase size", "Move every field together during sorting", "A key already stored in the collection", "Confirm every formatted write"],
        "correctOption": 1
    },
    {
        "type": "mcq",
        "question": "Round 3 (Match): Checked save",
        "options": ["Publish one fully validated record", "Move every field together during sorting", "Confirm every formatted write and the final close", "A key already stored in the collection"],
        "correctOption": 3
    }
]

# Add Revision 2 - Section C
rev2_missing = [
    {
        "type": "mcq",
        "question": "Section C (Match): Dangling Pointer",
        "options": ["A condition such as 0 <= size <= capacity", "An allocation remains unreachable", "A pointer still stores an address after the referred object has ended its lifetime", "Parse into temporary data, verify, then publish"],
        "correctOption": 3
    },
    {
        "type": "mcq",
        "question": "Section C (Match): Memory Leak",
        "options": ["A condition such as 0 <= size <= capacity", "An allocation remains unreachable because its owning address was lost", "A pointer still stores an address after lifetime ends", "Parse into temporary data, verify, then publish"],
        "correctOption": 2
    },
    {
        "type": "mcq",
        "question": "Section C (Match): Invariant",
        "options": ["A condition such as 0 <= size <= capacity that must remain true at defined boundaries", "An allocation remains unreachable", "A pointer still stores an address after lifetime ends", "Move every field of a record together"],
        "correctOption": 1
    },
    {
        "type": "mcq",
        "question": "Section C (Match): Read–Validate–Commit",
        "options": ["A condition such as 0 <= size <= capacity", "An allocation remains unreachable", "Move every field of a record together", "Parse into temporary data, verify completeness/ranges/uniqueness, then publish"],
        "correctOption": 4
    },
    {
        "type": "mcq",
        "question": "Section C (Match): Whole-Record Swap",
        "options": ["Move every field of a record together so field relationships remain intact during sorting", "An allocation remains unreachable", "A pointer still stores an address after lifetime ends", "Parse into temporary data, verify, then publish"],
        "correctOption": 1
    }
]

for q in rev1_missing_1 + rev1_missing_2:
    q['timeLimit'] = "30"
    q['points'] = "1000"
    rev1['questions'].append(q)

for q in rev2_missing:
    q['timeLimit'] = "30"
    q['points'] = "1000"
    rev2['questions'].append(q)

quiz_data_str = json.dumps(quiz_data, indent=4)
new_content = content[:match.start()] + f"const quizData = {quiz_data_str};\n        const pdfData" + content[match.end():]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully added all matching/duel sections!")

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

# Helper to format code blocks to look exactly like the PDF photos
def format_code(code_str):
    return f'<pre style="background-color: #1e1e1e; color: #d4d4d4; padding: 1rem; border-radius: 0.5rem; overflow-x: auto; font-family: monospace; font-size: 0.875rem; margin-top: 0.5rem; border: 1px solid #333; text-align: left;"><code>{code_str}</code></pre>'

rev_ex_1 = {
    "set": "Revision_Exercise_1",
    "questions": [
        {
            "type": "mcq",
            "question": "1. What is the output, x?" + format_code("int x = 6;\nint *p = &x;\nint *q = p;\n*q += 4;\np = NULL;\ncout << x;"),
            "timeLimit": "30",
            "points": "1000",
            "options": ["6", "10", "0", "Undefined behavior"],
            "correctOption": 2
        },
        {
            "type": "mcq",
            "question": "2. What is the output?" + format_code("char* tag = static_cast<char*>(malloc(4 * sizeof(*tag)));\ntag[0] = 'C';\ntag[1] = 'O';\ntag[2] = 'D';\ntag[3] = 'E';\ncout << tag << endl;"),
            "timeLimit": "30",
            "points": "1000",
            "options": ["Always prints CODE", "Always prints CODE followed by one space", "Behavior is undefined because no null terminator is stored", "malloc adds the terminator automatically"],
            "correctOption": 3
        },
        {
            "type": "mcq",
            "question": "3. What should be filled in the blank?" + format_code("// Request a larger memory block using a temporary pointer\nint* temp = static_cast<int*>(realloc(data, newCapacity * sizeof(*data)));\n// Check whether realloc() failed\nif (temp == nullptr) {\n    /* ? */\n}"),
            "timeLimit": "30",
            "points": "1000",
            "options": ["free(data); capacity=newCap;", "data=tmp; capacity=newCap;", "Return failure without changing data or capacity", "Set data=NULL and continue"],
            "correctOption": 3
        },
        {
            "type": "mcq",
            "question": "4. Evaluate the following shifting loop:" + format_code("// Shift elements one position to the right\nfor (int i = size; i > index; --i) {\n    data[i] = data[i - 1];\n}\n// Insert the new value\ndata[index] = value;\n// Update the logical size\n++size;"),
            "timeLimit": "30",
            "points": "1000",
            "options": ["Correct after capacity and index validation", "Must use i >= index", "Must start at size-1", "Must shift left"],
            "correctOption": 1
        },
        {
            "type": "mcq",
            "question": "5. What is true about hits?" + format_code("int main() {\n int data[8] = {3, 8, 13, 21};\n int size = 4;\n int capacity = 8;\n int hits = 0;\n for (int i = 0; i < capacity; ++i) {\n  if (data[i] == 0) {\n   ++hits;\n  }\n }\n cout << \"hits = \" << hits << endl;\n return 0;\n}"),
            "timeLimit": "30",
            "points": "1000",
            "options": ["hits is evidence about four stored values", "hits is 4, but the loop incorrectly treats unused slots as logical data", "hits is 0 because size is 4", "The loop writes beyond capacity"],
            "correctOption": 2
        },
        {
            "type": "mcq",
            "question": "6. What is the status of alias?" + format_code("int* data = static_cast<int*>(malloc(3 * sizeof(*data)));\nif (data == nullptr) { return 1; }\ndata[0] = 10; data[1] = 20; data[2] = 30;\nint* alias = &data[1];\nfree(data);"),
            "timeLimit": "30",
            "points": "1000",
            "options": ["alias remains valid because it is a different pointer", "alias becomes NULL automatically", "alias is dangling and must not be dereferenced", "only data[0] is released"],
            "correctOption": 3
        },
        {
            "type": "mcq",
            "question": "R2.1 Complete the blank: void setZero(int _____ p) { *p = 0; }",
            "timeLimit": "30",
            "points": "1000",
            "options": ["*", "&", "const", "[]"],
            "correctOption": 1
        },
        {
            "type": "mcq",
            "question": "R2.2 Complete the blank: Student *p = &s; cout << p_____score;",
            "timeLimit": "30",
            "points": "1000",
            "options": [".", "->", "*", "&"],
            "correctOption": 2
        },
        {
            "type": "mcq",
            "question": "R2.3 Complete the blank: FILE *fp = fopen(name, \"r\"); if (fp == _____) return false;",
            "timeLimit": "30",
            "points": "1000",
            "options": ["false", "0", "NULL", "-1"],
            "correctOption": 3
        },
        {
            "type": "mcq",
            "question": "R2.4 Complete the blank: int *tmp = (int*)realloc(data, newCap * _____);",
            "timeLimit": "30",
            "points": "1000",
            "options": ["sizeof(*data)", "sizeof(data)", "sizeof(newCap)", "sizeof(tmp)"],
            "correctOption": 1
        },
        {
            "type": "mcq",
            "question": "R2.5 Complete the blank: for (int i = size; i > index; _____i) a[i] = a[i-1];",
            "timeLimit": "30",
            "points": "1000",
            "options": ["++", "--", "+=", "*="],
            "correctOption": 2
        },
        {
            "type": "mcq",
            "question": "R2.6 Complete the blank: for (int i = index; i < size - 1; ++i) a[i] = a[i _____ 1];",
            "timeLimit": "30",
            "points": "1000",
            "options": ["+", "-", "*", "/"],
            "correctOption": 1
        }
    ]
}

rev_ex_2 = {
    "set": "Revision_Exercise_2",
    "questions": [
        {
            "type": "mcq",
            "question": "1. Trace the code and choose one best answer." + format_code("int score = 11;\nint *first = &score;\nint *second = first;\n*second = *first + 5;\ncout << score;"),
            "timeLimit": "30",
            "points": "1000",
            "options": ["11", "16", "the address of score", "undefined behavior"],
            "correctOption": 2
        },
        {
            "type": "mcq",
            "question": "2. Trace the code and choose one best answer." + format_code("int *data = (int*)malloc(3 * sizeof *data);\nint *tmp = (int*)realloc(data, 6 * sizeof *data);\nif (tmp != NULL) data = tmp;"),
            "timeLimit": "30",
            "points": "1000",
            "options": ["If realloc fails, data still refers to the original block", "realloc always frees the original block on failure", "tmp must replace data before checking", "The code zero-initializes the new slots"],
            "correctOption": 1
        },
        {
            "type": "mcq",
            "question": "3. Trace the code and choose one best answer." + format_code("int a[7] = {4, 9, 12};\nint size = 3, capacity = 7;\nfor (int i=0; i<size; ++i) cout << a[i] << \" \";"),
            "timeLimit": "30",
            "points": "1000",
            "options": ["4 9 12", "4 9 12 0 0 0 0", "Seven undefined values", "Nothing"],
            "correctOption": 1
        },
        {
            "type": "mcq",
            "question": "4. Trace the code and choose one best answer." + format_code("int a[6]={2,5,8,11}; int size=4; int index=1;\nfor(int i=size; i>index; --i) a[i]=a[i-1];\na[index]=3; ++size;"),
            "timeLimit": "30",
            "points": "1000",
            "options": ["[2,3,5,8,11]", "[2,5,3,8,11]", "[3,2,5,8,11]", "[2,3,8,11]"],
            "correctOption": 1
        },
        {
            "type": "mcq",
            "question": "5. Trace the code and choose one best answer." + format_code("int a[6]={7,14,21,28}; int size=4; int index=1;\nfor(int i=index; i<size-1; ++i) a[i]=a[i+1];\n--size;"),
            "timeLimit": "30",
            "points": "1000",
            "options": ["Logical array [7,21,28]", "Logical array [7,14,21]", "Logical array [14,21,28]", "size remains 4"],
            "correctOption": 1
        },
        {
            "type": "mcq",
            "question": "6. Complete the pointer parameter: void addOne(int _____ value) { ++(*value); }",
            "timeLimit": "30",
            "points": "1000",
            "options": ["*", "&", "const", "[]"],
            "correctOption": 1
        },
        {
            "type": "mcq",
            "question": "7. Given Student *current;, access its id field: current_____id",
            "timeLimit": "30",
            "points": "1000",
            "options": [".", "->", "*", "&"],
            "correctOption": 2
        },
        {
            "type": "mcq",
            "question": "8. Validate file opening: FILE *fp=fopen(path,\"r\"); if(fp==_____) return false;",
            "timeLimit": "30",
            "points": "1000",
            "options": ["false", "0", "NULL", "-1"],
            "correctOption": 3
        },
        {
            "type": "mcq",
            "question": "9. Complete the insertion bound: for(int i=size; i _____ index; --i) a[i]=a[i-1];",
            "timeLimit": "30",
            "points": "1000",
            "options": ["<", ">", "<=", ">="],
            "correctOption": 2
        },
        {
            "type": "mcq",
            "question": "10. Complete the deletion source: for(int i=index; i<size-1; ++i) a[i]=a[i _____ 1];",
            "timeLimit": "30",
            "points": "1000",
            "options": ["+", "-", "*", "/"],
            "correctOption": 1
        }
    ]
}

quiz_data = [s for s in quiz_data if s['set'] not in ('Revision_Exercise_1', 'Revision_Exercise_2')]
quiz_data.extend([rev_ex_1, rev_ex_2])

quiz_data_str = json.dumps(quiz_data, indent=4)
new_content = content[:match.start()] + f"const quizData = {quiz_data_str};\n        const pdfData" + content[match.end():]

# We need to make sure the innerHTML injection of q.question doesn't escape our HTML formatting!
# In index.html, qText.textContent = q.question; escapes HTML. We need to use innerHTML.
new_content = new_content.replace('qText.textContent = q.question;', 'qText.innerHTML = q.question;')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Added Revision Exercises with code blocks!")

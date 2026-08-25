window.quizData.push({
    "set": "Revision_Exercise_1",
    "questions": [
        {
            "type": "mcq",
            "question": "1. What is the output, x?<pre style=\"background-color: #1e1e1e; color: #d4d4d4; padding: 1rem; border-radius: 0.5rem; overflow-x: auto; font-family: monospace; font-size: 0.875rem; margin-top: 0.5rem; border: 1px solid #333; text-align: left;\"><code>int x = 6;\nint *p = &x;\nint *q = p;\n*q += 4;\np = NULL;\ncout << x;</code></pre>",
            "timeLimit": "30",
            "points": "1000",
            "options": [
                "6",
                "10",
                "0",
                "Undefined behavior"
            ],
            "correctOption": 2
        },
        {
            "type": "mcq",
            "question": "2. What is the output?<pre style=\"background-color: #1e1e1e; color: #d4d4d4; padding: 1rem; border-radius: 0.5rem; overflow-x: auto; font-family: monospace; font-size: 0.875rem; margin-top: 0.5rem; border: 1px solid #333; text-align: left;\"><code>char* tag = static_cast<char*>(malloc(4 * sizeof(*tag)));\ntag[0] = 'C';\ntag[1] = 'O';\ntag[2] = 'D';\ntag[3] = 'E';\ncout << tag << endl;</code></pre>",
            "timeLimit": "30",
            "points": "1000",
            "options": [
                "Always prints CODE",
                "Always prints CODE followed by one space",
                "Behavior is undefined because no null terminator is stored",
                "malloc adds the terminator automatically"
            ],
            "correctOption": 3
        },
        {
            "type": "mcq",
            "question": "3. What should be filled in the blank?<pre style=\"background-color: #1e1e1e; color: #d4d4d4; padding: 1rem; border-radius: 0.5rem; overflow-x: auto; font-family: monospace; font-size: 0.875rem; margin-top: 0.5rem; border: 1px solid #333; text-align: left;\"><code>// Request a larger memory block using a temporary pointer\nint* temp = static_cast<int*>(realloc(data, newCapacity * sizeof(*data)));\n// Check whether realloc() failed\nif (temp == nullptr) {\n    /* ? */\n}</code></pre>",
            "timeLimit": "30",
            "points": "1000",
            "options": [
                "free(data); capacity=newCap;",
                "data=tmp; capacity=newCap;",
                "Return failure without changing data or capacity",
                "Set data=NULL and continue"
            ],
            "correctOption": 3
        },
        {
            "type": "mcq",
            "question": "4. Evaluate the following shifting loop:<pre style=\"background-color: #1e1e1e; color: #d4d4d4; padding: 1rem; border-radius: 0.5rem; overflow-x: auto; font-family: monospace; font-size: 0.875rem; margin-top: 0.5rem; border: 1px solid #333; text-align: left;\"><code>// Shift elements one position to the right\nfor (int i = size; i > index; --i) {\n    data[i] = data[i - 1];\n}\n// Insert the new value\ndata[index] = value;\n// Update the logical size\n++size;</code></pre>",
            "timeLimit": "30",
            "points": "1000",
            "options": [
                "Correct after capacity and index validation",
                "Must use i >= index",
                "Must start at size-1",
                "Must shift left"
            ],
            "correctOption": 1
        },
        {
            "type": "mcq",
            "question": "5. What is true about hits?<pre style=\"background-color: #1e1e1e; color: #d4d4d4; padding: 1rem; border-radius: 0.5rem; overflow-x: auto; font-family: monospace; font-size: 0.875rem; margin-top: 0.5rem; border: 1px solid #333; text-align: left;\"><code>int main() {\n int data[8] = {3, 8, 13, 21};\n int size = 4;\n int capacity = 8;\n int hits = 0;\n for (int i = 0; i < capacity; ++i) {\n  if (data[i] == 0) {\n   ++hits;\n  }\n }\n cout << \"hits = \" << hits << endl;\n return 0;\n}</code></pre>",
            "timeLimit": "30",
            "points": "1000",
            "options": [
                "hits is evidence about four stored values",
                "hits is 4, but the loop incorrectly treats unused slots as logical data",
                "hits is 0 because size is 4",
                "The loop writes beyond capacity"
            ],
            "correctOption": 2
        },
        {
            "type": "mcq",
            "question": "6. What is the status of alias?<pre style=\"background-color: #1e1e1e; color: #d4d4d4; padding: 1rem; border-radius: 0.5rem; overflow-x: auto; font-family: monospace; font-size: 0.875rem; margin-top: 0.5rem; border: 1px solid #333; text-align: left;\"><code>int* data = static_cast<int*>(malloc(3 * sizeof(*data)));\nif (data == nullptr) { return 1; }\ndata[0] = 10; data[1] = 20; data[2] = 30;\nint* alias = &data[1];\nfree(data);</code></pre>",
            "timeLimit": "30",
            "points": "1000",
            "options": [
                "alias remains valid because it is a different pointer",
                "alias becomes NULL automatically",
                "alias is dangling and must not be dereferenced",
                "only data[0] is released"
            ],
            "correctOption": 3
        },
        {
            "type": "mcq",
            "question": "R2.1 Complete the blank: void setZero(int _____ p) { *p = 0; }",
            "timeLimit": "30",
            "points": "1000",
            "options": [
                "*",
                "&",
                "const",
                "[]"
            ],
            "correctOption": 1
        },
        {
            "type": "mcq",
            "question": "R2.2 Complete the blank: Student *p = &s; cout << p_____score;",
            "timeLimit": "30",
            "points": "1000",
            "options": [
                ".",
                "->",
                "*",
                "&"
            ],
            "correctOption": 2
        },
        {
            "type": "mcq",
            "question": "R2.3 Complete the blank: FILE *fp = fopen(name, \"r\"); if (fp == _____) return false;",
            "timeLimit": "30",
            "points": "1000",
            "options": [
                "false",
                "0",
                "NULL",
                "-1"
            ],
            "correctOption": 3
        },
        {
            "type": "mcq",
            "question": "R2.4 Complete the blank: int *tmp = (int*)realloc(data, newCap * _____);",
            "timeLimit": "30",
            "points": "1000",
            "options": [
                "sizeof(*data)",
                "sizeof(data)",
                "sizeof(newCap)",
                "sizeof(tmp)"
            ],
            "correctOption": 1
        },
        {
            "type": "mcq",
            "question": "R2.5 Complete the blank: for (int i = size; i > index; _____i) a[i] = a[i-1];",
            "timeLimit": "30",
            "points": "1000",
            "options": [
                "++",
                "--",
                "+=",
                "*="
            ],
            "correctOption": 2
        },
        {
            "type": "mcq",
            "question": "R2.6 Complete the blank: for (int i = index; i < size - 1; ++i) a[i] = a[i _____ 1];",
            "timeLimit": "30",
            "points": "1000",
            "options": [
                "+",
                "-",
                "*",
                "/"
            ],
            "correctOption": 1
        },
        {
            "type": "mcq",
            "question": "Round 3 (Clue Match): A function overwrites its only owner pointer with a new address without freeing the old allocation.",
            "options": [
                "Memory Leak",
                "Dangling Pointer",
                "Invariant",
                "Whole-Record Swap"
            ],
            "correctOption": 1,
            "timeLimit": "30",
            "points": "1000"
        },
        {
            "type": "mcq",
            "question": "Round 3 (Clue Match): After free(records), an alias still holds &records[2].",
            "options": [
                "Memory Leak",
                "Dangling Pointer",
                "Invariant",
                "Whole-Record Swap"
            ],
            "correctOption": 2,
            "timeLimit": "30",
            "points": "1000"
        },
        {
            "type": "mcq",
            "question": "Round 3 (Clue Match): At every public operation boundary, 0 <= size && size <= capacity must be true.",
            "options": [
                "Memory Leak",
                "Dangling Pointer",
                "Invariant",
                "Whole-Record Swap"
            ],
            "correctOption": 3,
            "timeLimit": "30",
            "points": "1000"
        },
        {
            "type": "mcq",
            "question": "Round 3 (Clue Match): A loader parses into temporary fields, rejects malformed/duplicate data, then stores once and increments size.",
            "options": [
                "Read - Validate - Commit",
                "Buffer Overrun",
                "Memory Leak",
                "Whole-Record Swap"
            ],
            "correctOption": 1,
            "timeLimit": "30",
            "points": "1000"
        },
        {
            "type": "mcq",
            "question": "Round 3 (Clue Match): After sorting, each student ID remains attached to that student's name and score.",
            "options": [
                "Read - Validate - Commit",
                "Buffer Overrun",
                "Memory Leak",
                "Whole-Record Swap"
            ],
            "correctOption": 4,
            "timeLimit": "30",
            "points": "1000"
        },
        {
            "type": "mcq",
            "question": "Round 3 (Clue Match): An insertion writes a[size] when size == capacity and growth was not performed.",
            "options": [
                "Read - Validate - Commit",
                "Buffer Overrun",
                "Memory Leak",
                "Whole-Record Swap"
            ],
            "correctOption": 2,
            "timeLimit": "30",
            "points": "1000"
        },
        {
            "type": "mcq",
            "question": "Round 3 (Match): Malformed record",
            "options": [
                "Publish one fully validated record",
                "Confirm every formatted write",
                "Input missing required fields or containing unexpected extra data",
                "Move every field together during sorting"
            ],
            "correctOption": 3,
            "timeLimit": "30",
            "points": "1000"
        },
        {
            "type": "mcq",
            "question": "Round 3 (Match): Duplicate ID",
            "options": [
                "A key already stored in the collection",
                "Confirm every formatted write",
                "Input missing required fields",
                "Move every field together"
            ],
            "correctOption": 1,
            "timeLimit": "30",
            "points": "1000"
        },
        {
            "type": "mcq",
            "question": "Round 3 (Match): Whole-record swap",
            "options": [
                "Publish one fully validated record",
                "Move every field together during sorting",
                "A key already stored in the collection",
                "Confirm every formatted write"
            ],
            "correctOption": 2,
            "timeLimit": "30",
            "points": "1000"
        },
        {
            "type": "mcq",
            "question": "Round 3 (Match): Commit",
            "options": [
                "Publish one fully validated record and then increase size",
                "Move every field together during sorting",
                "A key already stored in the collection",
                "Confirm every formatted write"
            ],
            "correctOption": 1,
            "timeLimit": "30",
            "points": "1000"
        },
        {
            "type": "mcq",
            "question": "Round 3 (Match): Checked save",
            "options": [
                "Publish one fully validated record",
                "Move every field together during sorting",
                "Confirm every formatted write and the final close",
                "A key already stored in the collection"
            ],
            "correctOption": 3,
            "timeLimit": "30",
            "points": "1000"
        }
    ]
});
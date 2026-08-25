window.quizData.push({
    "set": "Revision_Exercise_2",
    "questions": [
        {
            "type": "mcq",
            "question": "1. Trace the code and choose one best answer.<pre style=\"background-color: #1e1e1e; color: #d4d4d4; padding: 1rem; border-radius: 0.5rem; overflow-x: auto; font-family: monospace; font-size: 0.875rem; margin-top: 0.5rem; border: 1px solid #333; text-align: left;\"><code>int score = 11;\nint *first = &score;\nint *second = first;\n*second = *first + 5;\ncout << score;</code></pre>",
            "timeLimit": "30",
            "points": "1000",
            "options": [
                "11",
                "16",
                "the address of score",
                "undefined behavior"
            ],
            "correctOption": 2
        },
        {
            "type": "mcq",
            "question": "2. Trace the code and choose one best answer.<pre style=\"background-color: #1e1e1e; color: #d4d4d4; padding: 1rem; border-radius: 0.5rem; overflow-x: auto; font-family: monospace; font-size: 0.875rem; margin-top: 0.5rem; border: 1px solid #333; text-align: left;\"><code>int *data = (int*)malloc(3 * sizeof *data);\nint *tmp = (int*)realloc(data, 6 * sizeof *data);\nif (tmp != NULL) data = tmp;</code></pre>",
            "timeLimit": "30",
            "points": "1000",
            "options": [
                "If realloc fails, data still refers to the original block",
                "realloc always frees the original block on failure",
                "tmp must replace data before checking",
                "The code zero-initializes the new slots"
            ],
            "correctOption": 1
        },
        {
            "type": "mcq",
            "question": "3. Trace the code and choose one best answer.<pre style=\"background-color: #1e1e1e; color: #d4d4d4; padding: 1rem; border-radius: 0.5rem; overflow-x: auto; font-family: monospace; font-size: 0.875rem; margin-top: 0.5rem; border: 1px solid #333; text-align: left;\"><code>int a[7] = {4, 9, 12};\nint size = 3, capacity = 7;\nfor (int i=0; i<size; ++i) cout << a[i] << \" \";</code></pre>",
            "timeLimit": "30",
            "points": "1000",
            "options": [
                "4 9 12",
                "4 9 12 0 0 0 0",
                "Seven undefined values",
                "Nothing"
            ],
            "correctOption": 1
        },
        {
            "type": "mcq",
            "question": "4. Trace the code and choose one best answer.<pre style=\"background-color: #1e1e1e; color: #d4d4d4; padding: 1rem; border-radius: 0.5rem; overflow-x: auto; font-family: monospace; font-size: 0.875rem; margin-top: 0.5rem; border: 1px solid #333; text-align: left;\"><code>int a[6]={2,5,8,11}; int size=4; int index=1;\nfor(int i=size; i>index; --i) a[i]=a[i-1];\na[index]=3; ++size;</code></pre>",
            "timeLimit": "30",
            "points": "1000",
            "options": [
                "[2,3,5,8,11]",
                "[2,5,3,8,11]",
                "[3,2,5,8,11]",
                "[2,3,8,11]"
            ],
            "correctOption": 1
        },
        {
            "type": "mcq",
            "question": "5. Trace the code and choose one best answer.<pre style=\"background-color: #1e1e1e; color: #d4d4d4; padding: 1rem; border-radius: 0.5rem; overflow-x: auto; font-family: monospace; font-size: 0.875rem; margin-top: 0.5rem; border: 1px solid #333; text-align: left;\"><code>int a[6]={7,14,21,28}; int size=4; int index=1;\nfor(int i=index; i<size-1; ++i) a[i]=a[i+1];\n--size;</code></pre>",
            "timeLimit": "30",
            "points": "1000",
            "options": [
                "Logical array [7,21,28]",
                "Logical array [7,14,21]",
                "Logical array [14,21,28]",
                "size remains 4"
            ],
            "correctOption": 1
        },
        {
            "type": "mcq",
            "question": "6. Complete the pointer parameter: void addOne(int _____ value) { ++(*value); }",
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
            "question": "7. Given Student *current;, access its id field: current_____id",
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
            "question": "8. Validate file opening: FILE *fp=fopen(path,\"r\"); if(fp==_____) return false;",
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
            "question": "9. Complete the insertion bound: for(int i=size; i _____ index; --i) a[i]=a[i-1];",
            "timeLimit": "30",
            "points": "1000",
            "options": [
                "<",
                ">",
                "<=",
                ">="
            ],
            "correctOption": 2
        },
        {
            "type": "mcq",
            "question": "10. Complete the deletion source: for(int i=index; i<size-1; ++i) a[i]=a[i _____ 1];",
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
            "question": "Section C (Match): Dangling Pointer",
            "options": [
                "A condition such as 0 <= size <= capacity",
                "An allocation remains unreachable",
                "A pointer still stores an address after the referred object has ended its lifetime",
                "Parse into temporary data, verify, then publish"
            ],
            "correctOption": 3,
            "timeLimit": "30",
            "points": "1000"
        },
        {
            "type": "mcq",
            "question": "Section C (Match): Memory Leak",
            "options": [
                "A condition such as 0 <= size <= capacity",
                "An allocation remains unreachable because its owning address was lost",
                "A pointer still stores an address after lifetime ends",
                "Parse into temporary data, verify, then publish"
            ],
            "correctOption": 2,
            "timeLimit": "30",
            "points": "1000"
        },
        {
            "type": "mcq",
            "question": "Section C (Match): Invariant",
            "options": [
                "A condition such as 0 <= size <= capacity that must remain true at defined boundaries",
                "An allocation remains unreachable",
                "A pointer still stores an address after lifetime ends",
                "Move every field of a record together"
            ],
            "correctOption": 1,
            "timeLimit": "30",
            "points": "1000"
        },
        {
            "type": "mcq",
            "question": "Section C (Match): Read\u2013Validate\u2013Commit",
            "options": [
                "A condition such as 0 <= size <= capacity",
                "An allocation remains unreachable",
                "Move every field of a record together",
                "Parse into temporary data, verify completeness/ranges/uniqueness, then publish"
            ],
            "correctOption": 4,
            "timeLimit": "30",
            "points": "1000"
        },
        {
            "type": "mcq",
            "question": "Section C (Match): Whole-Record Swap",
            "options": [
                "Move every field of a record together so field relationships remain intact during sorting",
                "An allocation remains unreachable",
                "A pointer still stores an address after lifetime ends",
                "Parse into temporary data, verify, then publish"
            ],
            "correctOption": 1,
            "timeLimit": "30",
            "points": "1000"
        }
    ]
});
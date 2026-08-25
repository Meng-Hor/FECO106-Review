window.quizData.push({
    "set": "Algorithm_III_Week_4_QuizGlow_Set_1_Core_Concepts",
    "questions": [
        {
            "type": "mcq",
            "question": "What does a pointer variable store?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "An address",
                "A data type",
                "A file name",
                "An array size"
            ],
            "correctOption": 1
        },
        {
            "type": "mcq",
            "question": "Who must normally release a dynamically allocated block?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "Every alias",
                "The owner",
                "The compiler",
                "The last array element"
            ],
            "correctOption": 2
        },
        {
            "type": "mcq",
            "question": "What is p after free(a) if p still stores an address inside a?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "A new owner",
                "A NULL pointer",
                "A dangling pointer",
                "A valid array"
            ],
            "correctOption": 3
        },
        {
            "type": "mcq",
            "question": "After free(a); a = NULL;, what happens to alias p?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "It becomes NULL",
                "It owns new memory",
                "It becomes an integer",
                "It can remain dangling"
            ],
            "correctOption": 4
        },
        {
            "type": "mcq",
            "question": "When is *p valid after p = &a[1]?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "After assignment and before free(a)",
                "Only after free(a)",
                "Before p receives an address",
                "Whenever a is NULL"
            ],
            "correctOption": 1
        },
        {
            "type": "mcq",
            "question": "What does logical size represent in a dynamic array?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "The bytes in one element",
                "The number of meaningful elements",
                "The maximum possible index",
                "The number of freed slots"
            ],
            "correctOption": 2
        },
        {
            "type": "mcq",
            "question": "What does capacity represent?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "The number of valid records",
                "The last stored value",
                "The number of allocated element slots",
                "The number of pointers"
            ],
            "correctOption": 3
        },
        {
            "type": "mcq",
            "question": "Which dynamic-array invariant must always hold?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "capacity < size",
                "size is always positive",
                "size equals capacity",
                "0 <= size <= capacity"
            ],
            "correctOption": 4
        },
        {
            "type": "mcq",
            "question": "Which bound should a normal search use?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "i < size",
                "i <= capacity",
                "i < capacity",
                "i <= size"
            ],
            "correctOption": 1
        },
        {
            "type": "mcq",
            "question": "If capacity is 0, what is a valid first growth value?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "0",
                "1",
                "-1",
                "size - 1"
            ],
            "correctOption": 2
        },
        {
            "type": "mcq",
            "question": "Why store realloc's result in a temporary pointer?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "To clear every element",
                "To make size equal capacity",
                "To preserve the owner if resizing fails",
                "To avoid checking NULL"
            ],
            "correctOption": 3
        },
        {
            "type": "mcq",
            "question": "In which direction should insertion shift elements?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "From left to right",
                "From the middle outward",
                "No shifting is needed",
                "From right to left"
            ],
            "correctOption": 4
        },
        {
            "type": "mcq",
            "question": "In which direction should deletion shift later elements?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "From left to right",
                "From right to left",
                "From both ends",
                "In random order"
            ],
            "correctOption": 1
        },
        {
            "type": "mcq",
            "question": "Which insertion positions are valid for an array of logical size n?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "1 through n",
                "0 through n",
                "0 through n - 1 only",
                "1 through capacity"
            ],
            "correctOption": 2
        },
        {
            "type": "mcq",
            "question": "What is the main purpose of a Student struct?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "Allocate every file",
                "Replace all functions",
                "Keep related fields together",
                "Store only one score"
            ],
            "correctOption": 3
        },
        {
            "type": "mcq",
            "question": "Which expression accesses score through Student *p?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "p.score",
                "*p.score",
                "p-score",
                "p->score"
            ],
            "correctOption": 4
        },
        {
            "type": "mcq",
            "question": "What does const Student *p communicate?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "The function should not modify the record",
                "The pointer is always NULL",
                "The record must be freed",
                "The record has no fields"
            ],
            "correctOption": 1
        },
        {
            "type": "mcq",
            "question": "When should a parsed file record be committed?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "Immediately after fgets",
                "After all checks and capacity growth succeed",
                "Before checking duplicates",
                "Before parsing fields"
            ],
            "correctOption": 2
        },
        {
            "type": "mcq",
            "question": "What should a malformed input line do to accepted records?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "Delete the last record",
                "Increase size",
                "Leave them unchanged",
                "Reset capacity"
            ],
            "correctOption": 3
        },
        {
            "type": "mcq",
            "question": "What belongs in a strong technical explanation?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "Only the final output",
                "Only a definition",
                "A guess and a rewrite",
                "Claim, evidence, and consequence"
            ],
            "correctOption": 4
        }
    ]
});
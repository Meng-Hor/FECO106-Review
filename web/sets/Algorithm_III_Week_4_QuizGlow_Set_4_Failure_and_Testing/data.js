window.quizData.push({
    "set": "Algorithm_III_Week_4_QuizGlow_Set_4_Failure_and_Testing",
    "questions": [
        {
            "type": "mcq",
            "question": "Which test checks rejection of an index above the insertion range?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "Insert at size + 1",
                "Insert at size",
                "Insert at 0",
                "Search at size - 1"
            ],
            "correctOption": 1
        },
        {
            "type": "mcq",
            "question": "Which case exposes a broken zero-capacity growth policy?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "size=2, capacity=4, search",
                "size=0, capacity=0, insert at 0",
                "size=1, capacity=5, delete",
                "size=3, capacity=3, display"
            ],
            "correctOption": 2
        },
        {
            "type": "mcq",
            "question": "What does forced realloc failure test?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "Successful sorting",
                "Name formatting",
                "Owner and metadata preservation",
                "Normal file reading"
            ],
            "correctOption": 3
        },
        {
            "type": "mcq",
            "question": "Which case tests resizing and right shifting together?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "Search an empty array",
                "Delete the last element",
                "Read one valid record",
                "Insert in the middle of a full array"
            ],
            "correctOption": 4
        },
        {
            "type": "mcq",
            "question": "What does insertion at index 0 test most strongly?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "The maximum right shift",
                "A no-shift append",
                "The file close result",
                "A duplicate ID"
            ],
            "correctOption": 1
        },
        {
            "type": "mcq",
            "question": "What does insertion at index size represent?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "An invalid position",
                "Appending with no element shift",
                "Deleting the last element",
                "Searching capacity"
            ],
            "correctOption": 2
        },
        {
            "type": "mcq",
            "question": "After deleting the only element, what should size become?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "1",
                "capacity + 1",
                "0",
                "-1"
            ],
            "correctOption": 3
        },
        {
            "type": "mcq",
            "question": "What must an operation preserve when it rejects an invalid index?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "Only the error message",
                "A larger capacity",
                "A new owner",
                "Size, capacity, and existing values"
            ],
            "correctOption": 4
        },
        {
            "type": "mcq",
            "question": "What should code do when tmp == NULL after realloc?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "Return failure without committing changes",
                "Assign data = tmp and continue",
                "Increase size",
                "Free every alias"
            ],
            "correctOption": 1
        },
        {
            "type": "mcq",
            "question": "When should loading a valid record increase size?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "Before parsing",
                "After validation and capacity are ready",
                "Before duplicate checking",
                "After every rejected line"
            ],
            "correctOption": 2
        },
        {
            "type": "mcq",
            "question": "What state effect should a duplicate record line have?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "Replace the first record",
                "Increase size",
                "No change to accepted records",
                "Reduce capacity"
            ],
            "correctOption": 3
        },
        {
            "type": "mcq",
            "question": "How should the line 102|Sokha be handled?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "Accept with score 0",
                "Accept as two records",
                "Use Sokha as an ID",
                "Reject: the score is missing"
            ],
            "correctOption": 4
        },
        {
            "type": "mcq",
            "question": "Why parse an extra character after the expected fields?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "To detect unexpected trailing content",
                "To double capacity",
                "To close the file",
                "To free the record"
            ],
            "correctOption": 1
        },
        {
            "type": "mcq",
            "question": "Which ID passes the stated validation rule?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "0",
                "25",
                "-4",
                "A12"
            ],
            "correctOption": 2
        },
        {
            "type": "mcq",
            "question": "Which score is valid under the review rule?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "101",
                "-0.5",
                "100",
                "120"
            ],
            "correctOption": 3
        },
        {
            "type": "mcq",
            "question": "Why is a bounded name conversion important?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "It forces unique IDs",
                "It checks fclose",
                "It increases size",
                "It prevents writing past the name array"
            ],
            "correctOption": 4
        },
        {
            "type": "mcq",
            "question": "What normally happens if fopen uses r on a missing file?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "Opening fails",
                "A new file is created",
                "The file is truncated",
                "The program appends"
            ],
            "correctOption": 1
        },
        {
            "type": "mcq",
            "question": "Why can append mode be risky for a validated record file?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "It always deletes the file",
                "It may bypass full-file validation",
                "It prevents all writes",
                "It makes scores negative"
            ],
            "correctOption": 2
        },
        {
            "type": "mcq",
            "question": "What should a loading audit trail include?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "Only the final capacity",
                "Only accepted names",
                "Line, decision, reason, and counts",
                "Only the file mode"
            ],
            "correctOption": 3
        },
        {
            "type": "mcq",
            "question": "Why are boundary tests stronger than only normal cases?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "They guarantee no bugs",
                "They remove preconditions",
                "They avoid failure branches",
                "They can expose violated correctness properties"
            ],
            "correctOption": 4
        }
    ]
});
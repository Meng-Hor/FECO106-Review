window.quizData.push({
    "set": "Algorithm_III_Week_4_QuizGlow_Set_2_State_Tracing",
    "questions": [
        {
            "type": "mcq",
            "question": "If a[1] is 7 and *p += 5 where p = &a[1], what is a[1]?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "12",
                "7",
                "5",
                "The address changes"
            ],
            "correctOption": 1
        },
        {
            "type": "mcq",
            "question": "What is true immediately after free(a)?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "Only a is invalid",
                "Pointers into the old block are invalid",
                "All aliases become NULL",
                "The array keeps its lifetime"
            ],
            "correctOption": 2
        },
        {
            "type": "mcq",
            "question": "If p = &a[1] and *p = 20, what changes?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "p becomes 20",
                "a becomes NULL",
                "a[1] becomes 20",
                "capacity becomes 20"
            ],
            "correctOption": 3
        },
        {
            "type": "mcq",
            "question": "Why can a non-const pointer parameter modify caller data?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "It creates a separate file",
                "It disables dereferencing",
                "It always owns memory",
                "It refers to the caller's object"
            ],
            "correctOption": 4
        },
        {
            "type": "mcq",
            "question": "What must happen before writing into newly malloc'd memory?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "Check whether allocation succeeded",
                "Call free first",
                "Set every alias to NULL",
                "Reduce capacity"
            ],
            "correctOption": 1
        },
        {
            "type": "mcq",
            "question": "For size 3 and capacity 5, how many slots are unused?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "3",
                "2",
                "5",
                "8"
            ],
            "correctOption": 2
        },
        {
            "type": "mcq",
            "question": "What must happen before appending when size equals capacity?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "Increment size twice",
                "Search unused slots to capacity",
                "Grow capacity and confirm success",
                "Delete the last element"
            ],
            "correctOption": 3
        },
        {
            "type": "mcq",
            "question": "Insert 15 at index 1 into [10,20,30]. What is the result?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "[15,10,20,30]",
                "[10,20,15,30]",
                "[10,20,30,15]",
                "[10,15,20,30]"
            ],
            "correctOption": 4
        },
        {
            "type": "mcq",
            "question": "Delete index 1 from [10,15,20,30]. What remains logically?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "[10,20,30]",
                "[10,15,30]",
                "[15,20,30]",
                "[10,15,20]"
            ],
            "correctOption": 1
        },
        {
            "type": "mcq",
            "question": "After deletion, what is true of a value beyond the new size?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "It must be searched",
                "It is not a logical element",
                "It increases capacity",
                "It becomes the owner"
            ],
            "correctOption": 2
        },
        {
            "type": "mcq",
            "question": "Which insertion loop shifts safely for index k?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "for (i=0; i<k; i++)",
                "for (i=size; i<k; i--)",
                "for (i=size; i>k; i--)",
                "for (i=k; i>size; i++)"
            ],
            "correctOption": 3
        },
        {
            "type": "mcq",
            "question": "Which deletion condition stops at the new logical end?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "i <= capacity",
                "i > size",
                "i == capacity",
                "i < size - 1"
            ],
            "correctOption": 4
        },
        {
            "type": "mcq",
            "question": "If realloc returns NULL through tmp, what remains true?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "Original data, size, and capacity remain",
                "Original data is freed",
                "Size becomes zero",
                "Capacity is committed"
            ],
            "correctOption": 1
        },
        {
            "type": "mcq",
            "question": "What should findById return when it finds a matching record?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "A copied file",
                "The matching index",
                "The array capacity",
                "The record's score only"
            ],
            "correctOption": 2
        },
        {
            "type": "mcq",
            "question": "Inside updateScore(Student *s,...), how is score accessed?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "s.score",
                "score->s",
                "s->score",
                "s-score"
            ],
            "correctOption": 3
        },
        {
            "type": "mcq",
            "question": "When sorting students, what should be swapped?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "Only scores",
                "Only names",
                "Only IDs",
                "Complete Student objects"
            ],
            "correctOption": 4
        },
        {
            "type": "mcq",
            "question": "What does %29[^|] help protect?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "The name buffer boundary",
                "The score range",
                "The file mode",
                "The array capacity"
            ],
            "correctOption": 1
        },
        {
            "type": "mcq",
            "question": "If sscanf reports 2 fields when 3 are required, what follows?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "Commit it with defaults",
                "Reject the candidate",
                "Increase size",
                "Overwrite the prior record"
            ],
            "correctOption": 2
        },
        {
            "type": "mcq",
            "question": "How should a record with score 120 be handled?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "Accept it",
                "Clamp it silently",
                "Reject it",
                "Use it as capacity"
            ],
            "correctOption": 3
        },
        {
            "type": "mcq",
            "question": "When is a save operation successful?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "As soon as fopen is called",
                "After the first fprintf",
                "Whenever mode w is used",
                "After open, all writes, and close succeed"
            ],
            "correctOption": 4
        }
    ]
});
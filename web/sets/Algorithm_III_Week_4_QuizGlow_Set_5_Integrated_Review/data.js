window.quizData.push({
    "set": "Algorithm_III_Week_4_QuizGlow_Set_5_Integrated_Review",
    "questions": [
        {
            "type": "mcq",
            "question": "In a dynamic Student array, which pointer owns the allocation?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "The pointer responsible for calling free",
                "Every pointer to one record",
                "The file stream",
                "The last Student"
            ],
            "correctOption": 1
        },
        {
            "type": "mcq",
            "question": "What can happen to p = &records[2] after successful realloc?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "p becomes the owner automatically",
                "p may no longer identify valid storage",
                "p always becomes NULL",
                "The record becomes const"
            ],
            "correctOption": 2
        },
        {
            "type": "mcq",
            "question": "When capacity is 0, what new capacity supports the first insert?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "0",
                "size - 1",
                "1",
                "-1"
            ],
            "correctOption": 3
        },
        {
            "type": "mcq",
            "question": "What is the insertion precondition for index k?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "0 < k && k < size",
                "k == capacity",
                "k > size",
                "0 <= k && k <= size"
            ],
            "correctOption": 4
        },
        {
            "type": "mcq",
            "question": "What is the deletion precondition for index k?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "0 <= k && k < size",
                "0 <= k && k <= size",
                "k == capacity",
                "k > size"
            ],
            "correctOption": 1
        },
        {
            "type": "mcq",
            "question": "Which sequence correctly performs insertion?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "Write, increment, validate, grow, shift",
                "Validate, grow, shift, write, increment size",
                "Shift, free, write, parse, close",
                "Grow, increment, reject, write, shift"
            ],
            "correctOption": 2
        },
        {
            "type": "mcq",
            "question": "What must realloc failure preserve in the integrated manager?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "Only the requested value",
                "Only the error text",
                "Records, size, capacity, and owner",
                "A larger capacity"
            ],
            "correctOption": 3
        },
        {
            "type": "mcq",
            "question": "What should findById return when no ID matches?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "0",
                "capacity",
                "NULL Student",
                "-1"
            ],
            "correctOption": 4
        },
        {
            "type": "mcq",
            "question": "Why is a returned index useful for updating a record?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "It identifies the exact element in the collection",
                "It copies the entire file",
                "It changes the allocation owner",
                "It validates fclose"
            ],
            "correctOption": 1
        },
        {
            "type": "mcq",
            "question": "What preserves id-name-score relationships during sorting?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "Swapping only scores",
                "Swapping the whole Student object",
                "Sorting only names",
                "Reassigning all IDs"
            ],
            "correctOption": 2
        },
        {
            "type": "mcq",
            "question": "Which loading order protects accepted collection state?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "Commit, read, parse, validate, grow",
                "Grow, commit, close, parse, read",
                "Read, parse, validate, ensure capacity, commit",
                "Parse, commit, read, free, validate"
            ],
            "correctOption": 3
        },
        {
            "type": "mcq",
            "question": "Why build each candidate record in temporary variables?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "It removes the need for validation",
                "It guarantees unique memory addresses",
                "It automatically saves the file",
                "Only a complete valid candidate reaches the array"
            ],
            "correctOption": 4
        },
        {
            "type": "mcq",
            "question": "Assuming ID 101 is new, how should 101|Dara|78.5 be handled?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "Accept it",
                "Reject for missing score",
                "Reject for trailing data",
                "Use 78.5 as capacity"
            ],
            "correctOption": 1
        },
        {
            "type": "mcq",
            "question": "How should 104|Vannak|81|extra be handled?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "Accept four fields",
                "Reject for unexpected trailing data",
                "Accept and ignore all checks",
                "Use extra as a score"
            ],
            "correctOption": 2
        },
        {
            "type": "mcq",
            "question": "Which save sequence supports a truthful success message?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "Report, open, write, skip close",
                "Open, report, then write one record",
                "Open, write every record, close, then report",
                "Append, ignore errors, report"
            ],
            "correctOption": 3
        },
        {
            "type": "mcq",
            "question": "What is the safest cleanup rule for the dynamic record array?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "Every alias calls free",
                "Never call free",
                "Free after every search",
                "The owner frees the block exactly once"
            ],
            "correctOption": 4
        },
        {
            "type": "mcq",
            "question": "What should aliases do after the owner frees the array?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "Never dereference the old addresses",
                "Continue reading them",
                "Call realloc on them",
                "Treat them as new owners"
            ],
            "correctOption": 1
        },
        {
            "type": "mcq",
            "question": "Which evidence best proves a failed insert preserved invariants?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "A success message",
                "A before-and-after state trace with no changes",
                "A larger capacity",
                "A different test program"
            ],
            "correctOption": 2
        },
        {
            "type": "mcq",
            "question": "Which statement is evidence rather than a guess?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "The code looks wrong",
                "I think p is unsafe",
                "The block's lifetime ended at free(a)",
                "The output feels unusual"
            ],
            "correctOption": 3
        },
        {
            "type": "mcq",
            "question": "Which order matches the seven-step explanation sequence?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "Test, state, result, trace, failure, invariant, condition",
                "Claim, guess, compile, run, save, free, stop",
                "Precondition, output, style, file, pointer, name, score",
                "State, precond., invariant, trace, failure, test, conclude"
            ],
            "correctOption": 4
        }
    ]
});
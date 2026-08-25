window.quizData.push({
    "set": "PDF_Set_4_follow-ups_Failure_and_testing",
    "questions": [
        {
            "type": "open_ended",
            "question": "For size 4, name two invalid insertion indexes that test opposite boundaries.",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "-1 and 5."
        },
        {
            "type": "open_ended",
            "question": "What result should inserting into an empty zero-capacity array produce?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "It should successfully grow capacity (e.g. to 1), allocate memory, and insert the element at index 0."
        },
        {
            "type": "open_ended",
            "question": "After forced realloc failure, which four values or states should you compare?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "data (unchanged), size (unchanged), capacity (unchanged), and the returned result (failure)."
        },
        {
            "type": "open_ended",
            "question": "Why is inserting into the middle of a full array stronger than only appending?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "It tests if the right-shifting loop works correctly without losing elements."
        },
        {
            "type": "open_ended",
            "question": "How many elements move when inserting at index 0 into an array of size 5?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "All 5 elements move."
        },
        {
            "type": "open_ended",
            "question": "How many existing elements move when inserting at index size?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "Zero elements move."
        },
        {
            "type": "open_ended",
            "question": "After deleting the only element, must capacity also become zero?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "No, capacity remains unchanged. We don't typically shrink arrays on deletion."
        },
        {
            "type": "open_ended",
            "question": "How can you prove an invalid-index operation left the array unchanged?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "size, capacity, and the array contents are identical to before the operation."
        },
        {
            "type": "open_ended",
            "question": "Why should a failed resize return before executing the shift loop?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "Because if it fails, we have no space. Shifting would write out of bounds."
        },
        {
            "type": "open_ended",
            "question": "Which action is the final commit when loading a valid record?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "size++"
        },
        {
            "type": "open_ended",
            "question": "If a duplicate line is rejected, should the accepted/rejected counters change?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "The rejected counter should increase; accepted should not."
        },
        {
            "type": "open_ended",
            "question": "Which required field is absent from 102|Sokha?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "The score field is absent."
        },
        {
            "type": "open_ended",
            "question": "How does an extra %c help distinguish valid input from 104|Vannak|81|extra?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "It catches the extra data `|extra` which wouldn't fit into the expected 3 variables."
        },
        {
            "type": "open_ended",
            "question": "Why are zero and negative IDs rejected?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "IDs are typically positive integers; zero or negative IDs represent invalid or uninitialized states."
        },
        {
            "type": "open_ended",
            "question": "Give one value just below and one just above the valid score range.",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "-0.1 and 100.1 (assuming valid is 0.0 to 100.0)."
        },
        {
            "type": "open_ended",
            "question": "What could happen if an unbounded name is read into char name[30]?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "Buffer overflow: the name spills into adjacent memory, corrupting other variables or crashing."
        },
        {
            "type": "open_ended",
            "question": "How should the program distinguish a missing input file from an empty input file?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "fopen returning NULL means missing file. fopen succeeding but fgets immediately returning NULL means empty file."
        },
        {
            "type": "open_ended",
            "question": "When is append mode appropriate, and why may it be wrong for complete replacement?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "Append is fast for adding new records. It is wrong for replacements because old records aren't removed."
        },
        {
            "type": "open_ended",
            "question": "Why should an audit trail record the rejection reason, not only the line number?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "To diagnose *why* it failed (e.g., bad score vs missing pipe), enabling data correction."
        },
        {
            "type": "open_ended",
            "question": "Give a normal test that might pass even when the boundary behavior is incorrect.",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "Inserting at index 0 in an empty array (it doesn't shift, so it hides a broken shift loop)."
        }
    ]
});
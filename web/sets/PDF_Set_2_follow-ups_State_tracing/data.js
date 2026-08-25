window.quizData.push({
    "set": "PDF_Set_2_follow-ups_State_tracing",
    "questions": [
        {
            "type": "open_ended",
            "question": "Does *p += 5 change an address or a stored value? Show the state change.",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "Changes the stored value. `a[1]` increases by 5."
        },
        {
            "type": "open_ended",
            "question": "After free(a), which pointers become invalid: only a or every pointer into the block? Why?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "Every pointer into the block becomes invalid because the entire block is returned to the OS."
        },
        {
            "type": "open_ended",
            "question": "If p = &a[1], explain why assigning through *p changes a[1].",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "`p` holds the address of `a[1]`, so dereferencing `p` directly accesses `a[1]`."
        },
        {
            "type": "open_ended",
            "question": "Give an example of a function changing caller data through a pointer parameter.",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "void updateScore(Student *s) { s->score = 100; }"
        },
        {
            "type": "open_ended",
            "question": "What should the program do if malloc returns NULL?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "Handle the error gracefully by rejecting the operation or reporting failure."
        },
        {
            "type": "open_ended",
            "question": "For size 3 and capacity 5, should indexes 3 and 4 be displayed? Why?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "No. They are uninitialized or contain stale garbage data."
        },
        {
            "type": "open_ended",
            "question": "List the safe steps for appending when the collection is full.",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "1) Grow capacity. 2) Check for failure. 3) Update capacity variable. 4) Assign data array."
        },
        {
            "type": "open_ended",
            "question": "Trace the movements required to insert 15 at index 1 in [10,20,30].",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "30 moves to index 3, 20 moves to index 2. 15 is placed at index 1."
        },
        {
            "type": "open_ended",
            "question": "Trace deletion of index 1 from [10,15,20,30].",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "20 moves to index 1, 30 moves to index 2."
        },
        {
            "type": "open_ended",
            "question": "Why might the deleted value still appear in memory after size--?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "Because we only decremented `size`. We didn't clear the old memory slot."
        },
        {
            "type": "open_ended",
            "question": "For insertion at index 1 with size 3, what values does i take?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "i starts at 3, decreases to 2 (shifts 30 to index 3, 20 to index 2)."
        },
        {
            "type": "open_ended",
            "question": "Why does the deletion loop stop at size - 1?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "Because `size - 1` is the last valid element that needs to be shifted left."
        },
        {
            "type": "open_ended",
            "question": "Which assignment must not execute when tmp == NULL?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "data = tmp; and capacity *= 2;"
        },
        {
            "type": "open_ended",
            "question": "Why is returning an index more useful than returning only \"found\"?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "Because the index allows us to directly access, modify, or delete the specific element."
        },
        {
            "type": "open_ended",
            "question": "When would s.score be correct instead of s->score?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "When `s` is a struct value (e.g. Student s), not a pointer."
        },
        {
            "type": "open_ended",
            "question": "Give an example showing how swapping only scores corrupts student information.",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "Swapping scores between Dara(90) and Sokha(80) without swapping names gives Dara 80 and Sokha 90, corrupting both."
        },
        {
            "type": "open_ended",
            "question": "Why does %29[^|] use 29 when the name array has 30 characters?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "To leave room for the null terminator \\0 in a 30-character array."
        },
        {
            "type": "open_ended",
            "question": "Why should a two-field line not be accepted with a default third value?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "Because the line is malformed; guessing defaults compromises data integrity."
        },
        {
            "type": "open_ended",
            "question": "Are scores 0 and 100 valid? Explain the boundary rule.",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "Yes, if the rule is 0 <= score <= 100."
        },
        {
            "type": "open_ended",
            "question": "Why must fclose be checked even after every fprintf succeeds?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "Because buffered data might fail to write to the physical disk during `fclose`."
        }
    ]
});
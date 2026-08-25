window.quizData.push({
    "set": "PDF_Set_1_follow-ups_Core_concepts",
    "questions": [
        {
            "type": "open_ended",
            "question": "A pointer stores an address. What does that address identify in a real program?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "A specific location in memory (RAM)."
        },
        {
            "type": "open_ended",
            "question": "What problem occurs if the owner finishes using allocated memory but never releases it?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "A memory leak occurs, potentially exhausting available memory if repeated."
        },
        {
            "type": "open_ended",
            "question": "Why is p dangling after free(a) even though p still contains an address?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "The memory was returned to the system but `p` was not set to NULL."
        },
        {
            "type": "open_ended",
            "question": "Why does a = NULL not automatically change p to NULL?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "They are separate variables; changing `a` does not affect the copy of the address in `p`."
        },
        {
            "type": "open_ended",
            "question": "Name the exact statements between which *p is valid.",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "Between allocation (e.g. `malloc`) and deallocation (e.g. `free`)."
        },
        {
            "type": "open_ended",
            "question": "If size = 3, which array positions are meaningful?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "Indexes 0, 1, and 2."
        },
        {
            "type": "open_ended",
            "question": "Can capacity be larger than size? Give one example.",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "Yes. For example, allocated 10 items (capacity=10), but only filled 3 (size=3)."
        },
        {
            "type": "open_ended",
            "question": "Give one state that violates 0 <= size <= capacity and explain the danger.",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "State: size 5, capacity 3. Danger: Out of bounds memory access (buffer overflow)."
        },
        {
            "type": "open_ended",
            "question": "What could happen if searching continues to capacity instead of size?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "Searching uninitialized or stale memory, causing false positives."
        },
        {
            "type": "open_ended",
            "question": "Why does doubling capacity fail when capacity begins at zero?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "0 * 2 = 0. Capacity never grows."
        },
        {
            "type": "open_ended",
            "question": "Trace what happens to the original block when temporary realloc returns NULL.",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "The original block remains unchanged and is not freed."
        },
        {
            "type": "open_ended",
            "question": "What value could be lost if insertion shifted from left to right?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "The element being shifted to the right would overwrite the next element before it can move."
        },
        {
            "type": "open_ended",
            "question": "Why is left-to-right shifting safe during deletion?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "Because the element being overwritten is the one we want to delete."
        },
        {
            "type": "open_ended",
            "question": "Why is index size valid for insertion but invalid for normal element access?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "Because `size` points to the first empty slot at the end, valid for appending, but invalid for reading existing items."
        },
        {
            "type": "open_ended",
            "question": "What relationship could be lost if student IDs, names, and scores were stored separately?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "The logical association between a student's ID, name, and score."
        },
        {
            "type": "open_ended",
            "question": "Rewrite p->score without using the arrow operator.",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "(*p).score"
        },
        {
            "type": "open_ended",
            "question": "With const Student *p, what can and cannot the function change?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "The function can change the pointer itself, but cannot modify the struct it points to."
        },
        {
            "type": "open_ended",
            "question": "Name three checks required before committing a parsed record.",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "1) Format validation, 2) Business logic/range validation, 3) Capacity check."
        },
        {
            "type": "open_ended",
            "question": "If one malformed line is rejected, what collection state must remain unchanged?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "size, capacity, and all existing elements."
        },
        {
            "type": "open_ended",
            "question": "Explain \"p is dangling\" using claim, evidence, and consequence.",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "Claim: `p` is dangling. Evidence: memory is freed but `p` holds the old address. Consequence: dereferencing causes undefined behavior."
        }
    ]
});
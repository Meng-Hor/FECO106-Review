window.quizData.push({
    "set": "PDF_Set_3_follow-ups_Defect_diagnosis",
    "questions": [
        {
            "type": "open_ended",
            "question": "Repair capacity *= 2 so that zero capacity can grow.",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "capacity = (capacity == 0) ? 1 : capacity * 2;"
        },
        {
            "type": "open_ended",
            "question": "Give a concrete inconsistent state caused by updating capacity before successful resizing.",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "capacity says 10, but data only points to a block of 5, causing buffer overflow on index 6."
        },
        {
            "type": "open_ended",
            "question": "Show why direct assignment from realloc can create a memory leak.",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "If realloc fails, it returns NULL. `data = realloc(data...)` overwrites the only pointer to the original memory, leaking it."
        },
        {
            "type": "open_ended",
            "question": "What unsafe statement might execute if a failed realloc is not checked?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "Writing to data[size] (which is now NULL) causing a segmentation fault."
        },
        {
            "type": "open_ended",
            "question": "With size = 3 and index = 1, evaluate size < index. What happens to the loop?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "3 < 1 is false. The loop doesn't run."
        },
        {
            "type": "open_ended",
            "question": "Why should index validation occur before attempting allocation?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "To avoid wasting time/memory allocating if the operation is invalid anyway."
        },
        {
            "type": "open_ended",
            "question": "Give a state where data[index] = value writes outside allocated memory.",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "size = 5, capacity = 5, index = 5."
        },
        {
            "type": "open_ended",
            "question": "If size++ happens before allocation fails, which invariant or meaning is violated?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "Logical size is larger than physical capacity. `0 <= size <= capacity` is violated."
        },
        {
            "type": "open_ended",
            "question": "Give an example of a stale value in an unused slot causing a false search result.",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "Searching for 'Dara' might find an old deleted 'Dara' at index `size + 1` if the loop bound is `capacity`."
        },
        {
            "type": "open_ended",
            "question": "Which deletion indexes are valid when size is zero?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "None. You cannot delete from an empty array."
        },
        {
            "type": "open_ended",
            "question": "What could happen if both the owner and an alias call free?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "Double-free error, which crashes the program and corrupts the memory allocator."
        },
        {
            "type": "open_ended",
            "question": "How would you test whether repeated operations create a memory leak?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "Run the operation in a loop 10,000 times. If memory usage grows indefinitely, it's a leak."
        },
        {
            "type": "open_ended",
            "question": "Why is use-after-free dangerous even when the program sometimes prints the expected value?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "It accesses memory the program doesn't own. It might coincidentally hold the old value, but it can crash randomly later."
        },
        {
            "type": "open_ended",
            "question": "Give an example of partial corruption caused by parsing directly into records[size].",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "A malformed line overwrites the previous name/ID before failing, leaving partial garbage at records[size]."
        },
        {
            "type": "open_ended",
            "question": "Which operation becomes ambiguous if duplicate student IDs are accepted?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "Searching by ID, as it could return the wrong student."
        },
        {
            "type": "open_ended",
            "question": "What should a sorting swap contain to preserve record identity?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "The entire Student struct, so ID, name, and score stay together."
        },
        {
            "type": "open_ended",
            "question": "Explain the type error in p.score when p is Student *.",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "p is a pointer, so we must use -> instead of . to access fields."
        },
        {
            "type": "open_ended",
            "question": "Explain the type error in s->score when s is a Student object.",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "s is a struct, so we must use . instead of -> to access fields."
        },
        {
            "type": "open_ended",
            "question": "What happens to the old file immediately after opening it with \"w\"?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "It truncates the file to 0 bytes, erasing all existing contents."
        },
        {
            "type": "open_ended",
            "question": "Describe a safer replacement strategy than writing directly over the original file.",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "Write to a temporary file, check for success, then rename/replace the original file."
        }
    ]
});
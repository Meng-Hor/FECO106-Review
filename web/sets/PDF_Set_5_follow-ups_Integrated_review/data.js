window.quizData.push({
    "set": "PDF_Set_5_follow-ups_Integrated_review",
    "questions": [
        {
            "type": "open_ended",
            "question": "How can you identify the owner when several pointers reference the same dynamic array?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "The owner is the pointer originally assigned from malloc/realloc and responsible for calling free."
        },
        {
            "type": "open_ended",
            "question": "Why may an interior pointer become invalid after a successful realloc?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "realloc might move the block to a new address, making old interior pointers dangling."
        },
        {
            "type": "open_ended",
            "question": "After the first successful insertion from zero capacity, what are valid size and capacity values?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "size = 1, capacity = 1 (or whatever initial growth value is used, e.g., 2)."
        },
        {
            "type": "open_ended",
            "question": "Explain why insertion allows k == size.",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "Because k == size represents appending to the end of the array, which is valid."
        },
        {
            "type": "open_ended",
            "question": "Explain why deletion rejects k == size.",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "Because there is no element at index == size. Valid elements are 0 to size - 1."
        },
        {
            "type": "open_ended",
            "question": "At which step does insertion first modify the logical collection?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "Writing to data[index] modifies the physical array, but size++ officially modifies the logical collection."
        },
        {
            "type": "open_ended",
            "question": "Why must ownership be included in the state preserved after failed resizing?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "Because the original block is not freed. If we lose the pointer, we cause a memory leak."
        },
        {
            "type": "open_ended",
            "question": "Why is -1 a useful not-found result for an index-returning search?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "Array indexes are 0 or positive. -1 is out-of-bounds, making it a clear, unambiguous error signal."
        },
        {
            "type": "open_ended",
            "question": "Show how the returned index can be used to update a student's score.",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "index = findById(id); if (index != -1) data[index].score = newScore;"
        },
        {
            "type": "open_ended",
            "question": "What invariant must still hold after sorting Student records?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "The association between a student's ID, Name, and Score must remain intact."
        },
        {
            "type": "open_ended",
            "question": "At what point in the loading pipeline does untrusted text become official collection state?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "When it is successfully parsed, validated, and size++ is executed."
        },
        {
            "type": "open_ended",
            "question": "What temporary fields would you use when parsing a Student line?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "Temporary variables (e.g., int tmp_id, char tmp_name[30], float tmp_score)."
        },
        {
            "type": "open_ended",
            "question": "Before accepting 101|Dara|78.5, what must be checked besides its format?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "The logical rules (e.g., uniqueness of ID 101, and score 78.5 being between 0 and 100)."
        },
        {
            "type": "open_ended",
            "question": "If the loader silently ignores |extra, what validation promise is broken?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "The promise that malformed lines with extra garbage are rejected."
        },
        {
            "type": "open_ended",
            "question": "Why should the success message be printed only after fclose returns success?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "Because buffered data could fail to write during fclose. Success is only certain after it successfully closes."
        },
        {
            "type": "open_ended",
            "question": "How many times should the dynamic record block be freed, and by whom?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "Exactly once, by the owner pointer."
        },
        {
            "type": "open_ended",
            "question": "What could you do to aliases after freeing the owner to reduce accidental misuse?",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "Set the owner pointer to NULL so aliases reading it know it's freed."
        },
        {
            "type": "open_ended",
            "question": "Give a before-and-after state table that proves a failed insertion changed nothing.",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "Before: size=5, capacity=5, data=[A,B,C,D,E]. After: size=5, capacity=5, data=[A,B,C,D,E]."
        },
        {
            "type": "open_ended",
            "question": "Turn \"I think the pointer is unsafe\" into an evidence-based statement.",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "The pointer is unsafe because it accesses memory that was already freed, which is an invalid use-after-free."
        },
        {
            "type": "open_ended",
            "question": "Apply the seven-step explanation sequence to one failed insertion.",
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "1. Check bounds. 2. Verify capacity. 3. Realloc fails. 4. Restore state. 5. Reject operation. 6. Array unchanged. 7. Return failure."
        }
    ]
});
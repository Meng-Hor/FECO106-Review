window.quizData.push({
    "set": "Algorithm_III_Week_4_QuizGlow_Set_3_Defect_Diagnosis",
    "questions": [
        {
            "type": "mcq",
            "question": "Why is capacity *= 2 defective when capacity starts at 0?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "It keeps capacity at 0",
                "It makes capacity negative",
                "It frees data",
                "It doubles size"
            ],
            "correctOption": 1
        },
        {
            "type": "mcq",
            "question": "Why should capacity not change before realloc succeeds?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "Capacity must always be zero",
                "Failure would publish false metadata",
                "Size must change first",
                "realloc cannot return NULL"
            ],
            "correctOption": 2
        },
        {
            "type": "mcq",
            "question": "What can direct data = realloc(data, ...) lose on failure?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "The logical size",
                "The file stream",
                "The only pointer to the original block",
                "The struct definition"
            ],
            "correctOption": 3
        },
        {
            "type": "mcq",
            "question": "What defect occurs if realloc's result is never checked?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "The old block always grows",
                "Every alias becomes safe",
                "The file closes early",
                "Code may continue using NULL"
            ],
            "correctOption": 4
        },
        {
            "type": "mcq",
            "question": "Why does for(i=size; i<index; i--) fail for middle insertion?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "Its condition is initially false",
                "It shifts left correctly",
                "It increments i",
                "It checks file fields"
            ],
            "correctOption": 1
        },
        {
            "type": "mcq",
            "question": "When should an invalid insertion index be rejected?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "After size++",
                "Before resizing or shifting",
                "After overwriting data",
                "Only during saving"
            ],
            "correctOption": 2
        },
        {
            "type": "mcq",
            "question": "Why is writing data[index] before ensuring capacity unsafe?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "It always changes the ID",
                "It closes the file",
                "The write may be outside allocated storage",
                "It makes p const"
            ],
            "correctOption": 3
        },
        {
            "type": "mcq",
            "question": "Why must size++ wait until insertion succeeds?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "Capacity must equal zero",
                "The owner must become an alias",
                "Search must use capacity",
                "Failure must not publish a new logical element"
            ],
            "correctOption": 4
        },
        {
            "type": "mcq",
            "question": "What bug can occur when search loops to capacity?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "Unused slots may be treated as elements",
                "Valid elements are always skipped",
                "The block is automatically freed",
                "The file is truncated"
            ],
            "correctOption": 1
        },
        {
            "type": "mcq",
            "question": "Why must deletion reject an operation when size is 0?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "Capacity must be negative",
                "No valid element exists to remove",
                "The owner must be freed",
                "Every index is valid"
            ],
            "correctOption": 2
        },
        {
            "type": "mcq",
            "question": "Why should a borrowing alias not call free on the block?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "It cannot store an address",
                "It always equals NULL",
                "It does not own the allocation",
                "It is a struct object"
            ],
            "correctOption": 3
        },
        {
            "type": "mcq",
            "question": "What defect results when the owner never calls free?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "A valid append",
                "A bounded name",
                "A duplicate ID",
                "A memory leak"
            ],
            "correctOption": 4
        },
        {
            "type": "mcq",
            "question": "What is dereferencing p after its block was freed?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "Invalid use after free",
                "Safe read-only access",
                "A capacity check",
                "A file commit"
            ],
            "correctOption": 1
        },
        {
            "type": "mcq",
            "question": "Why parse into temporaries instead of records[size] directly?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "It makes every ID unique",
                "A bad line cannot partly corrupt collection state",
                "It removes the need for fgets",
                "It guarantees fopen"
            ],
            "correctOption": 2
        },
        {
            "type": "mcq",
            "question": "What defect occurs if a duplicate ID is committed?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "Capacity becomes zero",
                "The name buffer grows",
                "Record identity is no longer unique",
                "The owner becomes NULL"
            ],
            "correctOption": 3
        },
        {
            "type": "mcq",
            "question": "Why is swapping only scores during sorting wrong?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "It cannot change order",
                "It frees the array",
                "It rejects all files",
                "Scores become detached from student identities"
            ],
            "correctOption": 4
        },
        {
            "type": "mcq",
            "question": "Which operator is wrong for a Student *p?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "p.score",
                "p->score",
                "(*p).score",
                "p[0].score"
            ],
            "correctOption": 1
        },
        {
            "type": "mcq",
            "question": "Which operator is wrong for a Student object s?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "s.score",
                "s->score",
                "(&s)->score",
                "s.id"
            ],
            "correctOption": 2
        },
        {
            "type": "mcq",
            "question": "What danger does fopen(filename, \"w\") create?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "It reads without writing",
                "It guarantees atomic replacement",
                "It truncates the existing file",
                "It appends safely"
            ],
            "correctOption": 3
        },
        {
            "type": "mcq",
            "question": "Why is reporting success before fclose incorrect?",
            "timeLimit": "20",
            "points": "1000",
            "options": [
                "fclose changes every ID",
                "The array may gain capacity",
                "Pointers become const",
                "A close failure may still lose buffered data"
            ],
            "correctOption": 4
        }
    ]
});
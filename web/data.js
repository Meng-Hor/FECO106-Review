const quizData = [
  {
    "set": "Algorithm_III_Week_4_QuizGlow_Set_1_Core_Concepts",
    "questions": [
      {
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
  },
  {
    "set": "Algorithm_III_Week_4_QuizGlow_Set_2_State_Tracing",
    "questions": [
      {
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
  },
  {
    "set": "Algorithm_III_Week_4_QuizGlow_Set_3_Defect_Diagnosis",
    "questions": [
      {
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
  },
  {
    "set": "Algorithm_III_Week_4_QuizGlow_Set_4_Failure_and_Testing",
    "questions": [
      {
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
  },
  {
    "set": "Algorithm_III_Week_4_QuizGlow_Set_5_Integrated_Review",
    "questions": [
      {
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
  }
];
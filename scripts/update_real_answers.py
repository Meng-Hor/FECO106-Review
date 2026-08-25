import json
import re

html_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract existing JSON
match = re.search(r'const quizData = (\[.*?\]);', content, re.DOTALL)
if not match:
    print("Could not find quizData")
    exit()

quiz_data = json.loads(match.group(1))

answers = {
    1: "A specific location in memory (RAM).",
    2: "A memory leak occurs, potentially exhausting available memory if repeated.",
    3: "The memory was returned to the system but `p` was not set to NULL.",
    4: "They are separate variables; changing `a` does not affect the copy of the address in `p`.",
    5: "Between allocation (e.g. `malloc`) and deallocation (e.g. `free`).",
    6: "Indexes 0, 1, and 2.",
    7: "Yes. For example, allocated 10 items (capacity=10), but only filled 3 (size=3).",
    8: "State: size 5, capacity 3. Danger: Out of bounds memory access (buffer overflow).",
    9: "Searching uninitialized or stale memory, causing false positives.",
    10: "0 * 2 = 0. Capacity never grows.",
    11: "The original block remains unchanged and is not freed.",
    12: "The element being shifted to the right would overwrite the next element before it can move.",
    13: "Because the element being overwritten is the one we want to delete.",
    14: "Because `size` points to the first empty slot at the end, valid for appending, but invalid for reading existing items.",
    15: "The logical association between a student's ID, name, and score.",
    16: "(*p).score",
    17: "The function can change the pointer itself, but cannot modify the struct it points to.",
    18: "1) Format validation, 2) Business logic/range validation, 3) Capacity check.",
    19: "size, capacity, and all existing elements.",
    20: "Claim: `p` is dangling. Evidence: memory is freed but `p` holds the old address. Consequence: dereferencing causes undefined behavior.",
    21: "Changes the stored value. `a[1]` increases by 5.",
    22: "Every pointer into the block becomes invalid because the entire block is returned to the OS.",
    23: "`p` holds the address of `a[1]`, so dereferencing `p` directly accesses `a[1]`.",
    24: "void updateScore(Student *s) { s->score = 100; }",
    25: "Handle the error gracefully by rejecting the operation or reporting failure.",
    26: "No. They are uninitialized or contain stale garbage data.",
    27: "1) Grow capacity. 2) Check for failure. 3) Update capacity variable. 4) Assign data array.",
    28: "30 moves to index 3, 20 moves to index 2. 15 is placed at index 1.",
    29: "20 moves to index 1, 30 moves to index 2.",
    30: "Because we only decremented `size`. We didn't clear the old memory slot.",
    31: "i starts at 3, decreases to 2 (shifts 30 to index 3, 20 to index 2).",
    32: "Because `size - 1` is the last valid element that needs to be shifted left.",
    33: "data = tmp; and capacity *= 2;",
    34: "Because the index allows us to directly access, modify, or delete the specific element.",
    35: "When `s` is a struct value (e.g. Student s), not a pointer.",
    36: "Swapping scores between Dara(90) and Sokha(80) without swapping names gives Dara 80 and Sokha 90, corrupting both.",
    37: "To leave room for the null terminator \\0 in a 30-character array.",
    38: "Because the line is malformed; guessing defaults compromises data integrity.",
    39: "Yes, if the rule is 0 <= score <= 100.",
    40: "Because buffered data might fail to write to the physical disk during `fclose`.",
    41: "capacity = (capacity == 0) ? 1 : capacity * 2;",
    42: "capacity says 10, but data only points to a block of 5, causing buffer overflow on index 6.",
    43: "If realloc fails, it returns NULL. `data = realloc(data...)` overwrites the only pointer to the original memory, leaking it.",
    44: "Writing to data[size] (which is now NULL) causing a segmentation fault.",
    45: "3 < 1 is false. The loop doesn't run.",
    46: "To avoid wasting time/memory allocating if the operation is invalid anyway.",
    47: "size = 5, capacity = 5, index = 5.",
    48: "Logical size is larger than physical capacity. `0 <= size <= capacity` is violated.",
    49: "Searching for 'Dara' might find an old deleted 'Dara' at index `size + 1` if the loop bound is `capacity`.",
    50: "None. You cannot delete from an empty array.",
    51: "Double-free error, which crashes the program and corrupts the memory allocator.",
    52: "Run the operation in a loop 10,000 times. If memory usage grows indefinitely, it's a leak.",
    53: "It accesses memory the program doesn't own. It might coincidentally hold the old value, but it can crash randomly later.",
    54: "A malformed line overwrites the previous name/ID before failing, leaving partial garbage at records[size].",
    55: "Searching by ID, as it could return the wrong student.",
    56: "The entire Student struct, so ID, name, and score stay together.",
    57: "p is a pointer, so we must use -> instead of . to access fields.",
    58: "s is a struct, so we must use . instead of -> to access fields.",
    59: "It truncates the file to 0 bytes, erasing all existing contents.",
    60: "Write to a temporary file, check for success, then rename/replace the original file.",
    61: "-1 and 5.",
    62: "It should successfully grow capacity (e.g. to 1), allocate memory, and insert the element at index 0.",
    63: "data (unchanged), size (unchanged), capacity (unchanged), and the returned result (failure).",
    64: "It tests if the right-shifting loop works correctly without losing elements.",
    65: "All 5 elements move.",
    66: "Zero elements move.",
    67: "No, capacity remains unchanged. We don't typically shrink arrays on deletion.",
    68: "size, capacity, and the array contents are identical to before the operation.",
    69: "Because if it fails, we have no space. Shifting would write out of bounds.",
    70: "size++",
    71: "The rejected counter should increase; accepted should not.",
    72: "The score field is absent.",
    73: "It catches the extra data `|extra` which wouldn't fit into the expected 3 variables.",
    74: "IDs are typically positive integers; zero or negative IDs represent invalid or uninitialized states.",
    75: "-0.1 and 100.1 (assuming valid is 0.0 to 100.0).",
    76: "Buffer overflow: the name spills into adjacent memory, corrupting other variables or crashing.",
    77: "fopen returning NULL means missing file. fopen succeeding but fgets immediately returning NULL means empty file.",
    78: "Append is fast for adding new records. It is wrong for replacements because old records aren't removed.",
    79: "To diagnose *why* it failed (e.g., bad score vs missing pipe), enabling data correction.",
    80: "Inserting at index 0 in an empty array (it doesn't shift, so it hides a broken shift loop).",
    81: "The owner is the pointer originally assigned from malloc/realloc and responsible for calling free.",
    82: "realloc might move the block to a new address, making old interior pointers dangling.",
    83: "size = 1, capacity = 1 (or whatever initial growth value is used, e.g., 2).",
    84: "Because k == size represents appending to the end of the array, which is valid.",
    85: "Because there is no element at index == size. Valid elements are 0 to size - 1.",
    86: "Writing to data[index] modifies the physical array, but size++ officially modifies the logical collection.",
    87: "Because the original block is not freed. If we lose the pointer, we cause a memory leak.",
    88: "Array indexes are 0 or positive. -1 is out-of-bounds, making it a clear, unambiguous error signal.",
    89: "index = findById(id); if (index != -1) data[index].score = newScore;",
    90: "The association between a student's ID, Name, and Score must remain intact.",
    91: "When it is successfully parsed, validated, and size++ is executed.",
    92: "Temporary variables (e.g., int tmp_id, char tmp_name[30], float tmp_score).",
    93: "The logical rules (e.g., uniqueness of ID 101, and score 78.5 being between 0 and 100).",
    94: "The promise that malformed lines with extra garbage are rejected.",
    95: "Because buffered data could fail to write during fclose. Success is only certain after it successfully closes.",
    96: "Exactly once, by the owner pointer.",
    97: "Set the owner pointer to NULL so aliases reading it know it's freed.",
    98: "Before: size=5, capacity=5, data=[A,B,C,D,E]. After: size=5, capacity=5, data=[A,B,C,D,E].",
    99: "The pointer is unsafe because it accesses memory that was already freed, which is an invalid use-after-free.",
    100: "1. Check bounds. 2. Verify capacity. 3. Realloc fails. 4. Restore state. 5. Reject operation. 6. Array unchanged. 7. Return failure."
}

# Iterate through the sets and update the correct answers
q_num = 1
for s in quiz_data:
    if 'PDF_Set' in s['set']:
        for q in s['questions']:
            if q_num in answers:
                q['correctAnswer'] = answers[q_num]
            q_num += 1

quiz_data_str = json.dumps(quiz_data, indent=4)

# Replace in file
new_content = content[:match.start()] + f"const quizData = {quiz_data_str};" + content[match.end():]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Real answers updated!")

# Set 1 follow-ups: Core concepts - Answer Key

This document contains the AI-generated model answers for the open-ended questions found in the PDF material. 

**1. A pointer stores an address. What does that address identify in a real program?**
It identifies the exact location in the computer's memory (RAM) where a specific piece of data or an object is stored.

**2. What problem occurs if the owner finishes using allocated memory but never releases it?**
A memory leak occurs, meaning the memory remains occupied and cannot be reused by the system, potentially exhausting available memory if repeated over time.

**3. Why is p dangling after free(a) even though p still contains an address?**
The pointer `p` still holds the memory address, but the memory at that address has been returned to the operating system and is no longer valid or safe to access.

**4. Why does a = NULL not automatically change p to NULL?**
`a` and `p` are separate variables. Assigning NULL to `a` only changes the value stored in `a`, not the value stored in `p` (which is a separate copy of the original address).

**5. Name the exact statements between which *p is valid.**
`*p` is valid between the successful allocation of the memory it points to (e.g., via `malloc`) and the moment that memory is deallocated (e.g., via `free`).

**6. If size = 3, which array positions are meaningful?**
Indexes 0, 1, and 2 are meaningful (they are the valid logical elements).

**7. Can capacity be larger than size? Give one example.**
Yes. For example, an array might have allocated space for 10 elements (capacity = 10), but currently only stores 3 elements (size = 3).

**8. Give one state that violates 0 <= size <= capacity and explain the danger.**
State: `size = 5` and `capacity = 3`. Danger: The program believes it has 5 valid elements, but memory is only allocated for 3, leading to out-of-bounds memory access (buffer overflow) when accessing indexes 3 and 4.

**9. What could happen if searching continues to capacity instead of size?**
The search would process uninitialized memory or stale data left in the unused slots, potentially returning a false positive (finding a "ghost" element).

**10. Why does doubling capacity fail when capacity begins at zero?**
Because 0 multiplied by 2 is still 0. The capacity will never grow, causing allocations to fail or remain at size zero.

**11. Trace what happens to the original block when temporary realloc returns NULL.**
The original block remains intact and unchanged. It is not freed, and its original data is preserved.

**12. What value could be lost if insertion shifted from left to right?**
The element at the insertion index would overwrite the element immediately to its right before that right element could be moved, causing a cascading loss of the original data.

**13. Why is left-to-right shifting safe during deletion?**
During deletion, the element being overwritten is the one we want to remove (or one that has already been shifted left), so no needed data is lost.

**14. Why is index size valid for insertion but invalid for normal element access?**
For insertion, `index == size` means appending exactly at the end of the current logical elements. For normal access, valid indexes are 0 to `size - 1`, so accessing `index == size` reads garbage memory outside the logical array.

**15. What relationship could be lost if student IDs, names, and scores were stored separately?**
The logical connection between a specific student's ID, their name, and their score could easily become desynchronized (e.g., if one array is sorted but the others are not).

**16. Rewrite p->score without using the arrow operator.**
`(*p).score`

**17. With const Student *p, what can and cannot the function change?**
The function can change where the pointer `p` points to (if `p` itself is not const), but it cannot modify the contents of the `Student` struct that `p` points to.

**18. Name three checks required before committing a parsed record.**
1) Format validation (all fields parsed correctly). 
2) Business logic validation (e.g., scores in valid range, unique IDs). 
3) Capacity check (ensuring there is enough space in the array to store it).

**19. If one malformed line is rejected, what collection state must remain unchanged?**
The `size` of the collection, the `capacity` (unless it grew before the rejection), and all existing valid elements in the array must remain exactly as they were.

**20. Explain "p is dangling" using claim, evidence, and consequence.**
Claim: `p` is a dangling pointer. 
Evidence: The memory block `p` points to has been freed using `free()`, but `p` was not set to NULL. 
Consequence: Dereferencing `p` results in undefined behavior (like a crash or data corruption) because it accesses memory the program no longer owns.

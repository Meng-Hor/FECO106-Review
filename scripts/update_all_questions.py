import json
import re
import os

html_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# First, let's redefine the javascript logic in the HTML to support open-ended questions
# We will do this by replacing the entire script block and options container
# This is a bit complex with regex, so we'll rewrite the HTML structure from scratch
# using the existing data and adding the new PDF data.

# Extract existing CSV data
match = re.search(r'const quizData = (\[.*?\]);', content, re.DOTALL)
if match:
    quiz_data_str = match.group(1)
    quiz_data = json.loads(quiz_data_str)
    
    # Remove the previously added "PDF_Set_1_Core_Concepts" if it exists
    quiz_data = [s for s in quiz_data if s['set'] != 'PDF_Set_1_Core_Concepts']

pdf_questions_text = """
Set 1 follow-ups: Core concepts
1. A pointer stores an address. What does that address identify in a real program?
2. What problem occurs if the owner finishes using allocated memory but never releases it?
3. Why is p dangling after free(a) even though p still contains an address?
4. Why does a = NULL not automatically change p to NULL?
5. Name the exact statements between which *p is valid.
6. If size = 3, which array positions are meaningful?
7. Can capacity be larger than size? Give one example.
8. Give one state that violates 0 <= size <= capacity and explain the danger.
9. What could happen if searching continues to capacity instead of size?
10. Why does doubling capacity fail when capacity begins at zero?
11. Trace what happens to the original block when temporary realloc returns NULL.
12. What value could be lost if insertion shifted from left to right?
13. Why is left-to-right shifting safe during deletion?
14. Why is index size valid for insertion but invalid for normal element access?
15. What relationship could be lost if student IDs, names, and scores were stored separately?
16. Rewrite p->score without using the arrow operator.
17. With const Student *p, what can and cannot the function change?
18. Name three checks required before committing a parsed record.
19. If one malformed line is rejected, what collection state must remain unchanged?
20. Explain "p is dangling" using claim, evidence, and consequence.

Set 2 follow-ups: State tracing
21. Does *p += 5 change an address or a stored value? Show the state change.
22. After free(a), which pointers become invalid: only a or every pointer into the block? Why?
23. If p = &a[1], explain why assigning through *p changes a[1].
24. Give an example of a function changing caller data through a pointer parameter.
25. What should the program do if malloc returns NULL?
26. For size 3 and capacity 5, should indexes 3 and 4 be displayed? Why?
27. List the safe steps for appending when the collection is full.
28. Trace the movements required to insert 15 at index 1 in [10,20,30].
29. Trace deletion of index 1 from [10,15,20,30].
30. Why might the deleted value still appear in memory after size--?
31. For insertion at index 1 with size 3, what values does i take?
32. Why does the deletion loop stop at size - 1?
33. Which assignment must not execute when tmp == NULL?
34. Why is returning an index more useful than returning only "found"?
35. When would s.score be correct instead of s->score?
36. Give an example showing how swapping only scores corrupts student information.
37. Why does %29[^|] use 29 when the name array has 30 characters?
38. Why should a two-field line not be accepted with a default third value?
39. Are scores 0 and 100 valid? Explain the boundary rule.
40. Why must fclose be checked even after every fprintf succeeds?

Set 3 follow-ups: Defect diagnosis
41. Repair capacity *= 2 so that zero capacity can grow.
42. Give a concrete inconsistent state caused by updating capacity before successful resizing.
43. Show why direct assignment from realloc can create a memory leak.
44. What unsafe statement might execute if a failed realloc is not checked?
45. With size = 3 and index = 1, evaluate size < index. What happens to the loop?
46. Why should index validation occur before attempting allocation?
47. Give a state where data[index] = value writes outside allocated memory.
48. If size++ happens before allocation fails, which invariant or meaning is violated?
49. Give an example of a stale value in an unused slot causing a false search result.
50. Which deletion indexes are valid when size is zero?
51. What could happen if both the owner and an alias call free?
52. How would you test whether repeated operations create a memory leak?
53. Why is use-after-free dangerous even when the program sometimes prints the expected value?
54. Give an example of partial corruption caused by parsing directly into records[size].
55. Which operation becomes ambiguous if duplicate student IDs are accepted?
56. What should a sorting swap contain to preserve record identity?
57. Explain the type error in p.score when p is Student *.
58. Explain the type error in s->score when s is a Student object.
59. What happens to the old file immediately after opening it with "w"?
60. Describe a safer replacement strategy than writing directly over the original file.

Set 4 follow-ups: Failure and testing
61. For size 4, name two invalid insertion indexes that test opposite boundaries.
62. What result should inserting into an empty zero-capacity array produce?
63. After forced realloc failure, which four values or states should you compare?
64. Why is inserting into the middle of a full array stronger than only appending?
65. How many elements move when inserting at index 0 into an array of size 5?
66. How many existing elements move when inserting at index size?
67. After deleting the only element, must capacity also become zero?
68. How can you prove an invalid-index operation left the array unchanged?
69. Why should a failed resize return before executing the shift loop?
70. Which action is the final commit when loading a valid record?
71. If a duplicate line is rejected, should the accepted/rejected counters change?
72. Which required field is absent from 102|Sokha?
73. How does an extra %c help distinguish valid input from 104|Vannak|81|extra?
74. Why are zero and negative IDs rejected?
75. Give one value just below and one just above the valid score range.
76. What could happen if an unbounded name is read into char name[30]?
77. How should the program distinguish a missing input file from an empty input file?
78. When is append mode appropriate, and why may it be wrong for complete replacement?
79. Why should an audit trail record the rejection reason, not only the line number?
80. Give a normal test that might pass even when the boundary behavior is incorrect.

Set 5 follow-ups: Integrated review
81. How can you identify the owner when several pointers reference the same dynamic array?
82. Why may an interior pointer become invalid after a successful realloc?
83. After the first successful insertion from zero capacity, what are valid size and capacity values?
84. Explain why insertion allows k == size.
85. Explain why deletion rejects k == size.
86. At which step does insertion first modify the logical collection?
87. Why must ownership be included in the state preserved after failed resizing?
88. Why is -1 a useful not-found result for an index-returning search?
89. Show how the returned index can be used to update a student's score.
90. What invariant must still hold after sorting Student records?
91. At what point in the loading pipeline does untrusted text become official collection state?
92. What temporary fields would you use when parsing a Student line?
93. Before accepting 101|Dara|78.5, what must be checked besides its format?
94. If the loader silently ignores |extra, what validation promise is broken?
95. Why should the success message be printed only after fclose returns success?
96. How many times should the dynamic record block be freed, and by whom?
97. What could you do to aliases after freeing the owner to reduce accidental misuse?
98. Give a before-and-after state table that proves a failed insertion changed nothing.
99. Turn "I think the pointer is unsafe" into an evidence-based statement.
100. Apply the seven-step explanation sequence to one failed insertion.
"""

# Let's organize them into sets
pdf_sets = []
current_set = None

for line in pdf_questions_text.strip().split('\n'):
    line = line.strip()
    if not line:
        continue
    if line.startswith('Set '):
        current_set = {
            "set": "PDF_" + line.replace(' ', '_').replace(':', ''),
            "questions": []
        }
        pdf_sets.append(current_set)
    elif line[0].isdigit():
        q_text = line.split('.', 1)[1].strip()
        current_set['questions'].append({
            "type": "open_ended",
            "question": q_text,
            "timeLimit": "60",
            "points": "1000",
            "correctAnswer": "Model Answer: Check your understanding against the core concepts taught in class. (Self-graded)"
        })

quiz_data.extend(pdf_sets)

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FECO106 Mid-Term Review</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        .option-btn {{ transition: all 0.2s; }}
        .option-btn:hover:not(:disabled) {{ transform: translateY(-2px); box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); }}
        .correct {{ background-color: #22c55e !important; color: white !important; border-color: #22c55e !important; }}
        .incorrect {{ background-color: #ef4444 !important; color: white !important; border-color: #ef4444 !important; }}
        
        .opt-1 {{ border-left-width: 4px; border-left-color: #ef4444; }}
        .opt-2 {{ border-left-width: 4px; border-left-color: #3b82f6; }}
        .opt-3 {{ border-left-width: 4px; border-left-color: #eab308; }}
        .opt-4 {{ border-left-width: 4px; border-left-color: #22c55e; }}
    </style>
</head>
<body class="bg-gray-50 text-gray-800 font-sans min-h-screen">
    <div class="max-w-4xl mx-auto px-4 py-8">
        <header class="text-center mb-10">
            <h1 class="text-4xl font-bold text-blue-800 mb-2">FECO106 Mid-Term Review</h1>
            <p class="text-gray-600">Interactive Learning Platform</p>
        </header>

        <!-- Dashboard View -->
        <div id="dashboard" class="bg-white rounded-xl shadow-lg p-6">
            <h2 class="text-2xl font-semibold mb-6">Available Quiz Sets</h2>
            <div id="quiz-sets-container" class="grid gap-4 md:grid-cols-2 mb-8">
                <!-- Dynamically populated -->
            </div>
        </div>

        <!-- Quiz View -->
        <div id="quiz-view" class="hidden">
            <div class="bg-white rounded-xl shadow-lg p-6 mb-6 relative">
                <div class="flex justify-between items-center mb-6 border-b pb-4">
                    <div>
                        <h3 id="current-set-title" class="text-lg font-bold text-gray-700">Set Title</h3>
                        <p class="text-sm text-gray-500">Question <span id="current-question-num">1</span> of <span id="total-questions">10</span></p>
                    </div>
                    <div class="flex items-center gap-4">
                        <div class="text-right">
                            <p class="text-sm text-gray-500">Score</p>
                            <p id="current-score" class="text-xl font-bold text-blue-600">0</p>
                        </div>
                        <div class="w-16 h-16 rounded-full border-4 border-blue-500 flex items-center justify-center relative transition-colors duration-300">
                            <span id="time-left" class="text-xl font-bold">20</span>
                        </div>
                    </div>
                </div>

                <div class="mb-8">
                    <h2 id="question-text" class="text-2xl font-semibold mb-6 text-gray-800">Question text goes here?</h2>
                    
                    <div id="options-container" class="grid gap-4">
                        <!-- Options generated here -->
                    </div>
                    
                    <div id="open-ended-container" class="hidden">
                        <textarea id="open-ended-answer" rows="4" class="w-full p-4 border rounded-lg focus:ring-2 focus:ring-blue-500 mb-4" placeholder="Type your answer here..."></textarea>
                        <button id="reveal-btn" class="px-6 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 font-medium w-full">Reveal Answer</button>
                        
                        <div id="answer-feedback" class="hidden mt-6 p-4 bg-gray-50 border rounded-lg">
                            <h4 class="font-bold text-gray-700 mb-2">Model Answer:</h4>
                            <p id="model-answer-text" class="text-gray-600 mb-4"></p>
                            <div class="flex gap-4 justify-center">
                                <button id="self-correct-btn" class="px-6 py-2 bg-green-500 text-white rounded-lg hover:bg-green-600 font-medium">I Got It Right</button>
                                <button id="self-wrong-btn" class="px-6 py-2 bg-red-500 text-white rounded-lg hover:bg-red-600 font-medium">I Got It Wrong</button>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="flex justify-between items-center mt-8 border-t pt-4">
                    <button id="quit-btn" class="px-4 py-2 text-red-600 hover:bg-red-50 rounded-lg transition-colors font-medium">Quit Quiz</button>
                    <button id="next-btn" class="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors font-medium hidden shadow-md">Next Question</button>
                </div>
            </div>
        </div>

        <!-- Result View -->
        <div id="result-view" class="hidden bg-white rounded-xl shadow-lg p-8 text-center">
            <h2 class="text-3xl font-bold mb-4 text-gray-800">Quiz Completed!</h2>
            <div class="mb-8">
                <p class="text-gray-600 mb-2 text-lg">Your final score</p>
                <p id="final-score" class="text-5xl font-bold text-blue-600 drop-shadow-sm">0</p>
            </div>
            
            <div class="grid grid-cols-2 gap-4 max-w-sm mx-auto mb-8">
                <div class="bg-green-100 p-4 rounded-lg border border-green-200">
                    <p class="text-green-800 text-sm font-medium">Correct</p>
                    <p id="correct-count" class="text-3xl font-bold text-green-700">0</p>
                </div>
                <div class="bg-red-100 p-4 rounded-lg border border-red-200">
                    <p class="text-red-800 text-sm font-medium">Incorrect</p>
                    <p id="incorrect-count" class="text-3xl font-bold text-red-700">0</p>
                </div>
            </div>

            <button id="home-btn" class="px-8 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors font-semibold shadow-md">Back to Dashboard</button>
        </div>
    </div>

    <script>
        const quizData = {json.dumps(quiz_data)};

        let currentSetIndex = -1;
        let currentQuestionIndex = 0;
        let score = 0;
        let correctAnswers = 0;
        let timer;
        let timeLeft = 0;
        let isAnswered = false;
        
        const dashboard = document.getElementById('dashboard');
        const quizView = document.getElementById('quiz-view');
        const resultView = document.getElementById('result-view');
        const setsContainer = document.getElementById('quiz-sets-container');
        
        const setTitle = document.getElementById('current-set-title');
        const qNum = document.getElementById('current-question-num');
        const totalQ = document.getElementById('total-questions');
        const scoreEl = document.getElementById('current-score');
        const timeEl = document.getElementById('time-left');
        const qText = document.getElementById('question-text');
        
        const optionsContainer = document.getElementById('options-container');
        const openEndedContainer = document.getElementById('open-ended-container');
        const oeAnswer = document.getElementById('open-ended-answer');
        const revealBtn = document.getElementById('reveal-btn');
        const answerFeedback = document.getElementById('answer-feedback');
        const modelAnswerText = document.getElementById('model-answer-text');
        
        const nextBtn = document.getElementById('next-btn');
        const quitBtn = document.getElementById('quit-btn');
        
        function initDashboard() {{
            setsContainer.innerHTML = '';
            quizData.forEach((set, index) => {{
                const btn = document.createElement('button');
                const cleanName = set.set.replace(/_/g, ' ');
                btn.className = 'p-6 bg-white border-2 border-gray-100 rounded-xl hover:border-blue-500 hover:shadow-md transition-all text-left group';
                btn.innerHTML = `
                    <h3 class="text-lg font-bold text-gray-800 group-hover:text-blue-600 mb-2">${{cleanName}}</h3>
                    <p class="text-sm text-gray-500">${{set.questions.length}} questions</p>
                `;
                btn.onclick = () => startQuiz(index);
                setsContainer.appendChild(btn);
            }});
        }}
        
        function startQuiz(index) {{
            currentSetIndex = index;
            currentQuestionIndex = 0;
            score = 0;
            correctAnswers = 0;
            
            dashboard.classList.add('hidden');
            resultView.classList.add('hidden');
            quizView.classList.remove('hidden');
            
            setTitle.textContent = quizData[index].set.replace(/_/g, ' ');
            totalQ.textContent = quizData[index].questions.length;
            
            loadQuestion();
        }}
        
        function escapeHtml(unsafe) {{
            return String(unsafe).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;").replace(/'/g, "&#039;");
        }}

        function loadQuestion() {{
            const q = quizData[currentSetIndex].questions[currentQuestionIndex];
            isAnswered = false;
            
            qNum.textContent = currentQuestionIndex + 1;
            scoreEl.textContent = score;
            qText.textContent = q.question;
            
            timeLeft = parseInt(q.timeLimit) || 30;
            timeEl.textContent = timeLeft;
            timeEl.parentElement.classList.remove('border-red-500');
            timeEl.parentElement.classList.add('border-blue-500');
            
            clearInterval(timer);
            timer = setInterval(updateTimer, 1000);
            
            if (q.type === 'open_ended') {{
                optionsContainer.classList.add('hidden');
                openEndedContainer.classList.remove('hidden');
                oeAnswer.value = '';
                oeAnswer.disabled = false;
                revealBtn.classList.remove('hidden');
                answerFeedback.classList.add('hidden');
            }} else {{
                openEndedContainer.classList.add('hidden');
                optionsContainer.classList.remove('hidden');
                optionsContainer.innerHTML = '';
                const borderClasses = ['opt-1', 'opt-2', 'opt-3', 'opt-4'];
                
                q.options.forEach((opt, idx) => {{
                    const btn = document.createElement('button');
                    btn.className = `option-btn w-full p-4 text-left border rounded-lg bg-gray-50 hover:bg-gray-100 font-medium ${{borderClasses[idx]}}`;
                    btn.innerHTML = escapeHtml(opt);
                    btn.onclick = () => selectOption(idx + 1, btn);
                    optionsContainer.appendChild(btn);
                }});
            }}
            
            nextBtn.classList.add('hidden');
        }}
        
        function updateTimer() {{
            timeLeft--;
            timeEl.textContent = timeLeft;
            
            if (timeLeft <= 5) {{
                timeEl.parentElement.classList.remove('border-blue-500');
                timeEl.parentElement.classList.add('border-red-500');
            }}
            
            if (timeLeft <= 0) {{
                clearInterval(timer);
                if (quizData[currentSetIndex].questions[currentQuestionIndex].type === 'open_ended') {{
                    showModelAnswer();
                }} else {{
                    timeOutMCQ();
                }}
            }}
        }}

        // Open Ended Logic
        revealBtn.onclick = () => {{
            clearInterval(timer);
            showModelAnswer();
        }};

        function showModelAnswer() {{
            isAnswered = true;
            oeAnswer.disabled = true;
            revealBtn.classList.add('hidden');
            
            const q = quizData[currentSetIndex].questions[currentQuestionIndex];
            modelAnswerText.textContent = q.correctAnswer;
            answerFeedback.classList.remove('hidden');
        }}

        document.getElementById('self-correct-btn').onclick = () => {{
            const q = quizData[currentSetIndex].questions[currentQuestionIndex];
            const points = parseInt(q.points) || 1000;
            const maxTime = parseInt(q.timeLimit) || 30;
            const timeBonus = Math.floor(points * (Math.max(0, timeLeft) / maxTime) * 0.5);
            score += points + timeBonus;
            correctAnswers++;
            scoreEl.textContent = score;
            
            answerFeedback.classList.add('hidden');
            nextBtn.classList.remove('hidden');
        }};

        document.getElementById('self-wrong-btn').onclick = () => {{
            answerFeedback.classList.add('hidden');
            nextBtn.classList.remove('hidden');
        }};
        
        // MCQ Logic
        function timeOutMCQ() {{
            if (isAnswered) return;
            isAnswered = true;
            
            const q = quizData[currentSetIndex].questions[currentQuestionIndex];
            const correctIdx = q.correctOption - 1;
            
            const buttons = optionsContainer.children;
            for (let i = 0; i < buttons.length; i++) {{
                buttons[i].disabled = true;
                if (i === correctIdx) {{
                    buttons[i].classList.add('correct');
                }} else {{
                    buttons[i].classList.add('opacity-50');
                }}
            }}
            
            nextBtn.classList.remove('hidden');
        }}
        
        function selectOption(selectedOpt, btnElement) {{
            if (isAnswered) return;
            isAnswered = true;
            clearInterval(timer);
            
            const q = quizData[currentSetIndex].questions[currentQuestionIndex];
            const correctOpt = q.correctOption;
            const points = parseInt(q.points) || 1000;
            
            const buttons = optionsContainer.children;
            for (let i = 0; i < buttons.length; i++) {{
                buttons[i].disabled = true;
                if (i + 1 === correctOpt) {{
                    buttons[i].classList.add('correct');
                }} else {{
                    buttons[i].classList.add('opacity-50');
                }}
            }}
            
            if (selectedOpt === correctOpt) {{
                correctAnswers++;
                const maxTime = parseInt(q.timeLimit) || 30;
                const timeBonus = Math.floor(points * (timeLeft / maxTime) * 0.5);
                score += points + timeBonus;
                scoreEl.textContent = score;
            }} else {{
                btnElement.classList.remove('opacity-50');
                btnElement.classList.add('incorrect');
            }}
            
            nextBtn.classList.remove('hidden');
        }}
        
        nextBtn.onclick = () => {{
            currentQuestionIndex++;
            if (currentQuestionIndex < quizData[currentSetIndex].questions.length) {{
                loadQuestion();
            }} else {{
                showResults();
            }}
        }};
        
        quitBtn.onclick = () => {{
            clearInterval(timer);
            if(confirm('Are you sure you want to quit this quiz?')) {{
                showDashboard();
            }} else {{
                if(!isAnswered) timer = setInterval(updateTimer, 1000);
            }}
        }};
        
        function showResults() {{
            quizView.classList.add('hidden');
            resultView.classList.remove('hidden');
            
            document.getElementById('final-score').textContent = score;
            document.getElementById('correct-count').textContent = correctAnswers;
            const total = quizData[currentSetIndex].questions.length;
            document.getElementById('incorrect-count').textContent = total - correctAnswers;
        }}
        
        function showDashboard() {{
            quizView.classList.add('hidden');
            resultView.classList.add('hidden');
            dashboard.classList.remove('hidden');
        }}
        
        document.getElementById('home-btn').onclick = showDashboard;
        
        window.addEventListener('DOMContentLoaded', initDashboard);
    </script>
</body>
</html>
"""

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Added all 100 questions with open-ended self-grading support!")

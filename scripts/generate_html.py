import csv
import glob
import json
import os

path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term'
csv_files = glob.glob(os.path.join(path, '*.csv'))
pdf_files = glob.glob(os.path.join(path, '*.pdf'))

data = []
for file in csv_files:
    set_name = os.path.basename(file).replace('.csv', '')
    with open(file, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        questions = []
        for row in reader:
            questions.append({
                'question': row['Question Text'],
                'timeLimit': row['Time Limit (seconds)'],
                'points': row['Points'],
                'options': [row['Option 1 (Red)'], row['Option 2 (Blue)'], row['Option 3 (Yellow)'], row['Option 4 (Green)']],
                'correctOption': int(row['Correct Option Number (1-4)'])
            })
        data.append({
            'set': set_name,
            'questions': questions
        })

pdf_data = [{'name': os.path.basename(f), 'path': os.path.basename(f)} for f in pdf_files]

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
        
        .opt-1 {{ border-left-width: 4px; border-left-color: #ef4444; }} /* Red */
        .opt-2 {{ border-left-width: 4px; border-left-color: #3b82f6; }} /* Blue */
        .opt-3 {{ border-left-width: 4px; border-left-color: #eab308; }} /* Yellow */
        .opt-4 {{ border-left-width: 4px; border-left-color: #22c55e; }} /* Green */
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
            
            <h2 class="text-2xl font-semibold mb-6">Study Materials (PDFs)</h2>
            <div id="pdf-container" class="grid gap-4 md:grid-cols-2">
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
        const quizData = {json.dumps(data)};
        const pdfData = {json.dumps(pdf_data)};

        // State variables
        let currentSetIndex = -1;
        let currentQuestionIndex = 0;
        let score = 0;
        let correctAnswers = 0;
        let timer;
        let timeLeft = 0;
        let isAnswered = false;
        
        // DOM Elements
        const dashboard = document.getElementById('dashboard');
        const quizView = document.getElementById('quiz-view');
        const resultView = document.getElementById('result-view');
        const setsContainer = document.getElementById('quiz-sets-container');
        const pdfContainer = document.getElementById('pdf-container');
        
        const setTitle = document.getElementById('current-set-title');
        const qNum = document.getElementById('current-question-num');
        const totalQ = document.getElementById('total-questions');
        const scoreEl = document.getElementById('current-score');
        const timeEl = document.getElementById('time-left');
        const qText = document.getElementById('question-text');
        const optionsContainer = document.getElementById('options-container');
        const nextBtn = document.getElementById('next-btn');
        const quitBtn = document.getElementById('quit-btn');
        
        // Initialize dashboard
        function initDashboard() {{
            setsContainer.innerHTML = '';
            pdfContainer.innerHTML = '';
            
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

            if (pdfData.length === 0) {{
                pdfContainer.innerHTML = '<p class="text-gray-500">No PDF materials found.</p>';
            }} else {{
                pdfData.forEach((pdf) => {{
                    const link = document.createElement('a');
                    link.href = encodeURI(pdf.path);
                    link.target = '_blank';
                    link.className = 'p-6 bg-white border-2 border-gray-100 rounded-xl hover:border-red-500 hover:shadow-md transition-all text-left group flex items-center justify-between';
                    link.innerHTML = `
                        <h3 class="text-lg font-bold text-gray-800 group-hover:text-red-600 truncate mr-4">${{pdf.name}}</h3>
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-red-500 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                        </svg>
                    `;
                    pdfContainer.appendChild(link);
                }});
            }}
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
            return String(unsafe)
                 .replace(/&/g, "&amp;")
                 .replace(/</g, "&lt;")
                 .replace(/>/g, "&gt;")
                 .replace(/"/g, "&quot;")
                 .replace(/'/g, "&#039;");
        }}

        function loadQuestion() {{
            const q = quizData[currentSetIndex].questions[currentQuestionIndex];
            isAnswered = false;
            
            qNum.textContent = currentQuestionIndex + 1;
            scoreEl.textContent = score;
            qText.textContent = q.question;
            
            // Set timer
            timeLeft = parseInt(q.timeLimit) || 20;
            timeEl.textContent = timeLeft;
            timeEl.parentElement.classList.remove('border-red-500');
            timeEl.parentElement.classList.add('border-blue-500');
            
            clearInterval(timer);
            timer = setInterval(updateTimer, 1000);
            
            // Render options
            optionsContainer.innerHTML = '';
            const borderClasses = ['opt-1', 'opt-2', 'opt-3', 'opt-4'];
            
            q.options.forEach((opt, idx) => {{
                const btn = document.createElement('button');
                btn.className = `option-btn w-full p-4 text-left border rounded-lg bg-gray-50 hover:bg-gray-100 font-medium ${{borderClasses[idx]}}`;
                btn.innerHTML = escapeHtml(opt);
                btn.onclick = () => selectOption(idx + 1, btn);
                optionsContainer.appendChild(btn);
            }});
            
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
                timeOut();
            }}
        }}
        
        function timeOut() {{
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
                // Correct
                correctAnswers++;
                // Add points with time bonus
                const maxTime = parseInt(q.timeLimit) || 20;
                const timeBonus = Math.floor(points * (timeLeft / maxTime) * 0.5);
                score += points + timeBonus;
                scoreEl.textContent = score;
            }} else {{
                // Incorrect
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
        
        // Start
        window.addEventListener('DOMContentLoaded', initDashboard);
    </script>
</body>
</html>
"""

with open(os.path.join(path, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(html_content)

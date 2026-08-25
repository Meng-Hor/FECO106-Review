import re

html_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

keyboard_logic = """
        // --- KEYBOARD INTERACTIVITY ---
        document.addEventListener('keydown', (e) => {
            // Ignore if we are in the dashboard or result view
            if (quizView.classList.contains('hidden')) return;

            const q = quizData[currentSetIndex].questions[currentQuestionIndex];
            const isTyping = document.activeElement === oeAnswer;

            if (!isAnswered) {
                if (q.type === 'open_ended') {
                    // Reveal Answer
                    if (e.key === 'Enter' && (e.ctrlKey || e.shiftKey || !isTyping)) {
                        e.preventDefault();
                        revealBtn.click();
                    }
                } else {
                    // MCQ Selection
                    if (['1', '2', '3', '4'].includes(e.key)) {
                        e.preventDefault();
                        const idx = parseInt(e.key) - 1;
                        const btns = optionsContainer.querySelectorAll('.option-btn');
                        if (btns[idx]) btns[idx].click();
                    }
                }
            } else {
                // Answered State
                if (q.type === 'open_ended' && !answerFeedback.classList.contains('hidden')) {
                    // Self Grading
                    if (e.key === '1' || e.key.toLowerCase() === 'y' || e.key === 'ArrowLeft') {
                        e.preventDefault();
                        document.getElementById('self-correct-btn').click();
                    } else if (e.key === '2' || e.key.toLowerCase() === 'n' || e.key === 'ArrowRight') {
                        e.preventDefault();
                        document.getElementById('self-wrong-btn').click();
                    }
                } else {
                    // Next Question (works for both MCQ and after Self Grading)
                    if (e.key === 'Enter' || e.key === ' ') {
                        if (e.key === ' ') e.preventDefault();
                        nextBtn.click();
                    }
                }
            }
        });
"""

# Insert the logic right before the closing </script> tag at the end of the file.
content = content.replace('    </script>\n</body>', keyboard_logic + '\n    </script>\n</body>')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Keyboard interactivity added!")

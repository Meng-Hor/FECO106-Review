import re

path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\styles.css'
with open(path, 'r', encoding='utf-8') as f:
    css = f.read()

# Add mobile-specific overrides at the end of the file
mobile_css = """

/* ===== Mobile Responsive Overrides ===== */
@media (max-width: 640px) {
    /* Tighter option buttons on mobile */
    .option-btn {
        padding: 0.5rem 0.75rem !important;
        font-size: 0.8rem;
        border-radius: 0.625rem;
    }

    .option-badge {
        padding: 0.15rem 0.5rem !important;
        font-size: 0.75rem;
        min-width: 1.5rem;
        margin-right: 0.5rem !important;
    }

    /* Tighter primary/danger/secondary buttons */
    .btn-primary, .btn-danger, .btn-secondary {
        padding: 0.45rem 0.9rem;
        font-size: 0.8rem;
        border-radius: 0.625rem;
    }

    /* Tighter card padding globally */
    .card-container {
        border-radius: 1.25rem;
    }

    /* Compact quiz code block on mobile */
    .quiz-code-block {
        font-size: 0.72rem !important;
        padding: 0.75rem !important;
        border-radius: 0.5rem !important;
    }
}
"""

css += mobile_css

with open(path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Added mobile responsive CSS overrides to styles.css")

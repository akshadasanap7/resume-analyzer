# 🤖 AI-Powered Resume Screening & Candidate Ranking System

> Final Year DSML Project — Automates resume screening using Machine Learning, NLP & Web Development

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.x-black?style=flat-square&logo=flask)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange?style=flat-square&logo=scikit-learn)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## 🚀 Features

- 📋 Upload Job Description → auto-detects required skills
- 📁 Upload multiple resumes (PDF / DOCX)
- 🔍 Extracts Name, Email, Phone, Skills, Education, Experience
- 📊 Calculates ATS Score (out of 100) per candidate
- 🏆 Ranks candidates from best to least suitable
- 📈 Interactive dashboard with animated charts & analytics
- 🎨 Animated dark-theme UI with glassmorphism design

---

## 🧠 Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.x |
| Backend | Flask |
| NLP / ML | scikit-learn, regex |
| File Parsing | pdfplumber, python-docx |
| Visualization | Plotly |
| Frontend | HTML, CSS (Glassmorphism), JavaScript |

---

## 📁 Project Structure

```
resume-analyzer/
├── app.py                  # Flask backend & API routes
├── extractor.py            # NLP + ATS scoring engine
├── templates/
│   └── index.html          # HR Dashboard frontend
├── static/
│   └── style.css           # Animated dark theme CSS
├── requirements.txt        # Python dependencies
├── .gitignore
└── uploads/                # Auto-created on first run
```

---

## ⚙️ Setup & Run

```bash
# 1. Clone the repository
git clone https://github.com/akshadasanap7/resume-analyzer.git
cd resume-analyzer

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python app.py

# 4. Open browser
http://127.0.0.1:5000
```

---

## 📊 ATS Score Breakdown

| Criteria | Marks |
|---|---|
| Skills Match | 40 |
| Experience | 20 |
| Education | 15 |
| Projects | 15 |
| Certifications | 10 |
| **Total** | **100** |

---

## 🔄 System Workflow

```
HR uploads Job Description
        ↓
Auto-detect required skills
        ↓
HR uploads Resumes (PDF/DOCX)
        ↓
Text Extraction (pdfplumber / python-docx)
        ↓
NLP: Extract Name, Email, Skills, Experience, Education
        ↓
Resume vs JD Matching (Cosine Similarity)
        ↓
ATS Score Calculation (5 criteria)
        ↓
Candidate Ranking (highest → lowest)
        ↓
Animated Dashboard + Charts
```

---

## 🎨 UI Highlights

- 🌌 Animated gradient background with floating particles
- 🪟 Glassmorphism cards with blur effects
- 📊 Plotly charts with dark transparent theme
- 🏅 Gold / Silver / Bronze rank badges
- 📱 Fully responsive design

---

## 👩‍💻 Author

**Akshada Sanap** — Final Year DSML Student

---

## 📄 License

This project is licensed under the MIT License.

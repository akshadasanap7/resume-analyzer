# 🤖 AI-Powered Resume Screening & Candidate Ranking System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.x-000000?style=for-the-badge&logo=flask&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Charts-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-Frontend-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-Animated-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-00C851?style=for-the-badge)

**Final Year DSML Project** — An intelligent system that automates resume screening using Machine Learning, NLP, and Web Development to help HR teams rank candidates efficiently.

[🚀 Features](#-features) • [🧠 Tech Stack](#-tech-stack) • [📁 Project Structure](#-project-structure) • [⚙️ Setup](#️-setup--run) • [📊 ATS Scoring](#-ats-score-breakdown) • [🔄 Workflow](#-system-workflow) • [🎨 UI](#-ui-highlights)

</div>

---

## 📌 Problem Statement

When companies post a job opening, they receive **hundreds or thousands of resumes**. HR teams cannot manually read every resume — it is time-consuming, inconsistent, and error-prone.

This project solves that problem by building an **AI-powered system** that:
- Automatically reads and understands resumes
- Extracts key candidate information using NLP
- Compares each resume against the job description
- Calculates an ATS (Applicant Tracking System) compatibility score
- Ranks all candidates from most to least suitable
- Displays everything on an interactive visual dashboard

---

## 🎯 Objectives

| # | Objective |
|---|---|
| 1 | Accept PDF and DOCX resume uploads |
| 2 | Extract text from resumes automatically |
| 3 | Identify Name, Email, Phone, Skills, Education, Experience |
| 4 | Parse and analyze the Job Description |
| 5 | Match resume content against JD requirements |
| 6 | Calculate ATS score across 5 weighted criteria |
| 7 | Rank all candidates highest to lowest |
| 8 | Display results on an animated HR dashboard |

---

## 🚀 Features

- 📋 **Job Description Analysis** — paste any JD and auto-detect required skills instantly
- 📁 **Multi-Resume Upload** — drag & drop PDF / DOCX files, process multiple at once
- 🔍 **Smart Extraction** — extracts Name, Email, Phone, Skills, Education, Experience using NLP & regex
- 📊 **ATS Score** — calculates a score out of 100 based on 5 criteria
- 🏆 **Candidate Ranking** — sorts candidates from best to least suitable automatically
- 📈 **Analytics Dashboard** — interactive Plotly charts for score distribution and skill frequency
- 🎨 **Animated Dark UI** — glassmorphism design with floating particles and smooth transitions
- 📱 **Fully Responsive** — works on desktop, tablet, and mobile

---

## 🧠 Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| Language | Python 3.x | Core backend logic |
| Backend | Flask | Web server & REST API |
| NLP / ML | scikit-learn, regex | Text processing & similarity |
| File Parsing | pdfplumber, python-docx | Extract text from PDF & DOCX |
| Visualization | Plotly | Interactive charts |
| Frontend | HTML5, CSS3, JavaScript | Animated HR dashboard |
| Fonts | Google Fonts (Inter) | Clean modern typography |

---

## 📁 Project Structure

```
resume-analyzer/
│
├── app.py                  # Flask backend — all API routes
├── extractor.py            # NLP engine — extraction + ATS scoring
│
├── templates/
│   └── index.html          # HR Dashboard — frontend UI
│
├── static/
│   └── style.css           # Animated dark theme — glassmorphism CSS
│
├── requirements.txt        # All Python dependencies
├── .gitignore              # Ignored files (uploads, cache, venv)
├── README.md               # Project documentation
│
└── uploads/                # Auto-created on first run (resume files)
```

---

## ⚙️ Setup & Run

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/akshadasanap7/resume-analyzer.git
cd resume-analyzer

# 2. (Optional) Create virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

# 3. Install all dependencies
pip install -r requirements.txt

# 4. Run the Flask app
python app.py

# 5. Open in browser
http://127.0.0.1:5000
```

### Dependencies

```
flask
pdfplumber
python-docx
scikit-learn
plotly
pandas
werkzeug
```

---

## 📊 ATS Score Breakdown

The ATS score is calculated out of **100 marks** across 5 criteria:

| Criteria | Marks | Description |
|---|---|---|
| ✅ Skills Match | 40 | % of JD skills found in resume |
| 🎓 Education | 15 | Degree / qualification detected |
| 💼 Experience | 20 | Years of experience mentioned |
| 🛠️ Projects | 15 | Project section detected |
| 📜 Certifications | 10 | Certification keywords found |
| **Total** | **100** | |

### Score Interpretation

| Score Range | Rating | Color |
|---|---|---|
| 75 – 100 | 🟢 Excellent — Highly Recommended | Green |
| 50 – 74  | 🟡 Good — Worth Considering | Yellow |
| 0  – 49  | 🔴 Low — Not Recommended | Red |

---

## 🔄 System Workflow

```
┌─────────────────────────────────────┐
│         HR Opens Dashboard          │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│      Paste Job Description (JD)     │
│   → Auto-detect required skills     │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│     Upload Resumes (PDF / DOCX)     │
│     Drag & Drop — multiple files    │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│         Text Extraction             │
│   pdfplumber / python-docx          │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│         NLP Processing              │
│  Name, Email, Phone, Skills,        │
│  Education, Experience              │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│     Resume vs JD Matching           │
│     Skill overlap + match %         │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│      ATS Score Calculation          │
│   Skills(40) + Exp(20) + Edu(15)    │
│   + Projects(15) + Certs(10)        │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│      Candidate Ranking              │
│   🥇 Rank 1 → 🥈 Rank 2 → 🥉 ...  │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│    Animated Dashboard + Charts      │
│    Stats • Table • Plotly Graphs    │
└─────────────────────────────────────┘
```

---

## 🎨 UI Highlights

| Feature | Description |
|---|---|
| 🌌 Animated Background | Pulsing radial gradient blobs in purple, cyan, pink |
| ✨ Floating Particles | 30 colored particles rising continuously |
| 🪟 Glassmorphism Cards | `backdrop-filter: blur` with transparent borders |
| 🔢 Step Indicators | Active / Done states with smooth color transitions |
| 📂 Drag & Drop Zone | Animated bouncing icon, highlights on hover |
| 📊 Score Bars | Animated fill bars — green / yellow / red by score |
| 🏅 Rank Badges | Gold / Silver / Bronze styled circular badges |
| 📈 Plotly Charts | ATS score distribution + top skills frequency |
| 📱 Responsive | Mobile-friendly grid layout |

---

## 🧩 Modules Overview

### Module 1 — Resume Upload
Accepts PDF and DOCX files via drag & drop or file browser. Supports multiple files at once.

### Module 2 — Text Extraction
Uses `pdfplumber` for PDFs and `python-docx` for DOCX files to extract raw text from each resume.

### Module 3 — Information Extraction
Uses regex patterns to extract:
- **Name** — first non-empty line of resume
- **Email** — regex pattern matching
- **Phone** — Indian and international formats
- **Skills** — matched against a 50+ skill database
- **Education** — keyword detection (B.Tech, M.Tech, BCA, etc.)
- **Experience** — regex for "X years of experience"

### Module 4 — Skill Matching
Compares extracted resume skills against JD-detected skills and calculates match percentage.

### Module 5 — ATS Scoring
Weighted scoring across 5 criteria totalling 100 marks.

### Module 6 — Candidate Ranking
Sorts all candidates by ATS score (highest to lowest) and assigns Gold / Silver / Bronze badges.

### Module 7 — Dashboard
Displays stats, ranked table with score bars, matched/missing skill tags, and two Plotly charts.

---

## 🔮 Future Enhancements

- [ ] AI-generated interview questions based on candidate resume
- [ ] Resume improvement suggestions with missing skill recommendations
- [ ] Automatic cover letter generation
- [ ] Multi-language resume support
- [ ] BERT / Sentence Transformer embeddings for deeper semantic matching
- [ ] Export results to PDF / Excel report
- [ ] Email shortlisted candidates directly from dashboard
- [ ] Bias monitoring and explainable ATS scoring

---

## 👩‍💻 Author

**Akshada Sanap**
Final Year DSML (Data Science & Machine Learning) Student

---

## 📄 License

This project is licensed under the **MIT License** — free to use, modify, and distribute.

---

<div align="center">
⭐ If you found this project helpful, please give it a star on GitHub!
</div>

# 🤖 AI-Powered Resume Screening & Candidate Ranking System

A final-year DSML project that automates resume screening using **Machine Learning**, **NLP**, and **Web Development**.

## 🚀 Features
- Upload Job Description → auto-detects required skills
- Upload multiple resumes (PDF / DOCX)
- Extracts Name, Email, Phone, Skills, Education, Experience
- Calculates ATS Score (out of 100) per candidate
- Ranks candidates from best to least suitable
- Interactive dashboard with charts and analytics

## 🧠 Tech Stack
| Layer | Technology |
|---|---|
| Language | Python 3.x |
| Backend | Flask |
| NLP / ML | scikit-learn, regex |
| File Parsing | pdfplumber, python-docx |
| Visualization | Plotly |
| Frontend | HTML, CSS, JavaScript |

## 📁 Project Structure
```
resume/
├── app.py              # Flask backend
├── extractor.py        # NLP + ATS scoring engine
├── templates/
│   └── index.html      # HR Dashboard frontend
├── requirements.txt
└── uploads/            # Auto-created on first run
```

## ⚙️ Setup & Run

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the app
python app.py

# 3. Open browser
http://127.0.0.1:5000
```

## 📊 ATS Score Breakdown
| Criteria | Marks |
|---|---|
| Skills Match | 40 |
| Experience | 20 |
| Education | 15 |
| Projects | 15 |
| Certifications | 10 |

## 👩‍💻 Author
Akshada Sanap — Final Year DSML Project

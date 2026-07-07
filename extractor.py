import re
import pdfplumber
import docx
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

SKILLS_DB = [
    "python", "java", "javascript", "typescript", "c++", "c#", "go", "rust", "kotlin", "swift",
    "sql", "mysql", "postgresql", "mongodb", "redis", "sqlite",
    "react", "angular", "vue", "html", "css", "bootstrap", "tailwind",
    "flask", "fastapi", "django", "spring boot", "node.js", "express",
    "machine learning", "deep learning", "nlp", "computer vision", "tensorflow", "pytorch", "keras",
    "scikit-learn", "pandas", "numpy", "matplotlib", "seaborn", "plotly",
    "docker", "kubernetes", "aws", "azure", "gcp", "git", "linux",
    "power bi", "tableau", "excel", "spark", "hadoop",
    "communication", "teamwork", "leadership", "problem solving"
]

EDUCATION_KEYWORDS = ["b.tech", "b.e", "m.tech", "mca", "bca", "bsc", "msc", "phd", "bachelor", "master", "degree"]
EXPERIENCE_PATTERN = re.compile(r'(\d+\.?\d*)\s*(?:\+)?\s*years?\s*(?:of)?\s*(?:experience)?', re.IGNORECASE)
EMAIL_PATTERN = re.compile(r'[\w.+-]+@[\w-]+\.[a-z]{2,}', re.IGNORECASE)
PHONE_PATTERN = re.compile(r'(?:\+91[\s-]?)?[6-9]\d{9}|\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}')


def extract_text(file_path: str) -> str:
    if file_path.endswith(".pdf"):
        with pdfplumber.open(file_path) as pdf:
            return "\n".join(page.extract_text() or "" for page in pdf.pages)
    elif file_path.endswith(".docx"):
        doc = docx.Document(file_path)
        return "\n".join(p.text for p in doc.paragraphs)
    return ""


def extract_info(text: str) -> dict:
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    name = lines[0] if lines else "Unknown"
    email = next(iter(EMAIL_PATTERN.findall(text)), None)
    phone = next(iter(PHONE_PATTERN.findall(text)), None)
    text_lower = text.lower()
    skills = [s for s in SKILLS_DB if s in text_lower]
    education = [kw.upper() for kw in EDUCATION_KEYWORDS if kw in text_lower]
    exp_match = EXPERIENCE_PATTERN.search(text)
    experience = float(exp_match.group(1)) if exp_match else 0
    return {
        "name": name,
        "email": email,
        "phone": phone,
        "skills": skills,
        "education": education,
        "experience": experience,
    }


def calculate_ats_score(candidate: dict, jd_skills: list) -> dict:
    resume_skills = set(candidate["skills"])
    jd_set = set(s.lower() for s in jd_skills)
    matched = resume_skills & jd_set
    missing = jd_set - resume_skills

    skill_score = round((len(matched) / len(jd_set)) * 40) if jd_set else 0
    edu_score = 15 if candidate["education"] else 0
    exp = candidate["experience"]
    exp_score = 20 if exp >= 2 else (10 if exp >= 1 else 5)
    project_score = 15  # static; can be enhanced with project detection
    cert_score = 0      # placeholder for certification detection

    total = skill_score + edu_score + exp_score + project_score + cert_score

    return {
        "total": total,
        "breakdown": {
            "Skills Match": skill_score,
            "Education": edu_score,
            "Experience": exp_score,
            "Projects": project_score,
            "Certifications": cert_score,
        },
        "matched_skills": list(matched),
        "missing_skills": list(missing),
        "match_percent": round((len(matched) / len(jd_set)) * 100) if jd_set else 0,
    }


def extract_jd_skills(jd_text: str) -> list:
    jd_lower = jd_text.lower()
    return [s for s in SKILLS_DB if s in jd_lower]


def rank_candidates(candidates: list) -> list:
    return sorted(candidates, key=lambda x: x["ats"]["total"], reverse=True)

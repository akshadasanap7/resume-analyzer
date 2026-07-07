import os
import json
from flask import Flask, request, jsonify, render_template, session
from werkzeug.utils import secure_filename
from extractor import extract_text, extract_info, extract_jd_skills, calculate_ats_score, rank_candidates

app = Flask(__name__)
app.secret_key = "ats_secret_key"
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

ALLOWED_EXT = {"pdf", "docx"}

def allowed(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXT


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload_jd", methods=["POST"])
def upload_jd():
    jd_text = request.form.get("jd_text", "")
    if not jd_text:
        return jsonify({"error": "No job description provided"}), 400
    session["jd_text"] = jd_text
    session["jd_skills"] = extract_jd_skills(jd_text)
    return jsonify({"skills": session["jd_skills"]})


@app.route("/upload_resumes", methods=["POST"])
def upload_resumes():
    jd_skills = session.get("jd_skills", [])
    if not jd_skills:
        return jsonify({"error": "Upload job description first"}), 400

    files = request.files.getlist("resumes")
    if not files:
        return jsonify({"error": "No resumes uploaded"}), 400

    results = []
    for f in files:
        if not allowed(f.filename):
            continue
        filename = secure_filename(f.filename)
        path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        f.save(path)
        text = extract_text(path)
        info = extract_info(text)
        ats = calculate_ats_score(info, jd_skills)
        results.append({"filename": filename, **info, "ats": ats})

    ranked = rank_candidates(results)
    session["results"] = json.dumps(ranked, default=str)
    return jsonify(ranked)


@app.route("/results")
def results():
    data = session.get("results")
    if not data:
        return jsonify([])
    return jsonify(json.loads(data))


if __name__ == "__main__":
    app.run(debug=True)

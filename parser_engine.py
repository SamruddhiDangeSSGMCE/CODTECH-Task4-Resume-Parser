"""
Resume Parsing & Job Matching Engine
CodTech IT Solutions Internship - Task 4
Author: Samruddhi Dange
"""

import re
import io
from typing import Dict, List, Any
import pypdf
import docx
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Comprehensive Skill Taxonomy
SKILLS_TAXONOMY = [
    # Machine Learning & AI
    'Python', 'R', 'TensorFlow', 'PyTorch', 'Keras', 'Scikit-Learn', 'Pandas', 'NumPy',
    'Matplotlib', 'Seaborn', 'OpenCV', 'NLP', 'Computer Vision', 'Deep Learning',
    'Machine Learning', 'Data Science', 'Data Analysis', 'Feature Engineering',
    'Model Deployment', 'HuggingFace', 'Transformers', 'XGBoost', 'LightGBM',
    # Web & Cloud
    'FastAPI', 'Flask', 'Django', 'Streamlit', 'HTML', 'CSS', 'JavaScript', 'React',
    'Node.js', 'AWS', 'Azure', 'GCP', 'Docker', 'Kubernetes', 'CI/CD', 'Git', 'GitHub',
    # Databases & Big Data
    'SQL', 'MySQL', 'PostgreSQL', 'MongoDB', 'Redis', 'PySpark', 'Hadoop', 'Tableau', 'Power BI'
]

EDUCATION_DEGREES = [
    r'\bB\.?Tech\b', r'\bB\.?E\.?\b', r'\bB\.?Sc\b', r'\bB\.?C\.?A\b',
    r'\bM\.?Tech\b', r'\bM\.?E\.?\b', r'\bM\.?Sc\b', r'\bM\.?C\.?A\b',
    r'\bBachelor of Engineering\b', r'\bBachelor of Technology\b',
    r'\bMaster of Engineering\b', r'\bMaster of Science\b',
    r'\bPhD\b', r'\bPh\.?D\.?\b', r'\bDiploma\b'
]

class ResumeParser:
    """
    Extracts text, contact details, education, and technical skills from resumes.
    """
    @staticmethod
    def extract_text_from_pdf(file_bytes: bytes) -> str:
        text = ""
        reader = pypdf.PdfReader(io.BytesIO(file_bytes))
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
        return text

    @staticmethod
    def extract_text_from_docx(file_bytes: bytes) -> str:
        doc = docx.Document(io.BytesIO(file_bytes))
        return "\n".join([p.text for p in doc.paragraphs])

    @staticmethod
    def extract_text(file_bytes: bytes, filename: str) -> str:
        fname = filename.lower()
        if fname.endswith('.pdf'):
            return ResumeParser.extract_text_from_pdf(file_bytes)
        elif fname.endswith('.docx'):
            return ResumeParser.extract_text_from_docx(file_bytes)
        else:
            return file_bytes.decode('utf-8', errors='ignore')

    @staticmethod
    def extract_contact_info(text: str) -> Dict[str, Any]:
        # Email Extraction
        email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
        emails = re.findall(email_pattern, text)
        email = emails[0] if emails else "Not detected"

        # Phone Extraction
        phone_pattern = r'(?:(?:\+91|0091)[\s-]?)?[6-9]\d{9}|(?:\+?1[\s-]?)?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{4}'
        phones = re.findall(phone_pattern, text)
        phone = phones[0] if phones else "Not detected"

        # Candidate Name Extraction (heuristic: first non-empty line or title pattern)
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        name = "Candidate"
        for line in lines[:5]:
            if len(line.split()) in [2, 3, 4] and not any(char.isdigit() for char in line) and '@' not in line:
                name = line
                break

        return {
            "name": name,
            "email": email,
            "phone": phone
        }

    @staticmethod
    def extract_skills(text: str) -> List[str]:
        found_skills = set()
        text_lower = text.lower()
        for skill in SKILLS_TAXONOMY:
            # Word boundary regex search
            escaped = re.escape(skill.lower())
            if re.search(rf'(?:\b|\W){escaped}(?:\b|\W)', text_lower):
                found_skills.add(skill)
        return sorted(list(found_skills))

    @staticmethod
    def extract_education(text: str) -> List[str]:
        found_edu = set()
        for pattern in EDUCATION_DEGREES:
            matches = re.findall(pattern, text, re.IGNORECASE)
            for m in matches:
                found_edu.add(m.strip().replace('.', ''))
        return sorted(list(found_edu))

    @staticmethod
    def parse(file_bytes: bytes, filename: str) -> Dict[str, Any]:
        raw_text = ResumeParser.extract_text(file_bytes, filename)
        contacts = ResumeParser.extract_contact_info(raw_text)
        skills = ResumeParser.extract_skills(raw_text)
        education = ResumeParser.extract_education(raw_text)
        
        return {
            "name": contacts["name"],
            "email": contacts["email"],
            "phone": contacts["phone"],
            "skills": skills,
            "education": education,
            "word_count": len(raw_text.split()),
            "raw_text": raw_text
        }

class JobMatcher:
    """
    Computes semantic similarity and skill gap analysis between resume and job description.
    """
    @staticmethod
    def match(resume_text: str, resume_skills: List[str], job_description: str) -> Dict[str, Any]:
        if not job_description.strip():
            return {
                "match_score": 0.0,
                "matching_skills": [],
                "missing_skills": []
            }

        # TF-IDF Cosine Similarity
        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = vectorizer.fit_transform([resume_text, job_description])
        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
        match_score = round(float(similarity) * 100, 2)

        # Skill Matching
        job_skills = ResumeParser.extract_skills(job_description)
        matching_skills = [s for s in job_skills if s in resume_skills]
        missing_skills = [s for s in job_skills if s not in resume_skills]

        return {
            "match_score": match_score,
            "job_skills": job_skills,
            "matching_skills": matching_skills,
            "missing_skills": missing_skills
        }

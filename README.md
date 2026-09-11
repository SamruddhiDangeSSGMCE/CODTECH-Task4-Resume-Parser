# CODTECH Task 4: AI Resume Parser & Job Description Matcher

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![NLP](https://img.shields.io/badge/Domain-NLP%20%26%20Information%20Extraction-green.svg)
![Scikit-Learn](https://img.shields.io/badge/Library-Scikit--Learn-orange.svg)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)

## 📌 Project Overview
This repository contains **Task 4** of the **CodTech IT Solutions Internship** in the **Natural Language Processing & Artificial Intelligence** domain.

The objective is to build an intelligent Resume Parsing and Job Description Matching system. The system ingests resumes in multiple formats (PDF, DOCX, TXT), automatically extracts key candidate details (Name, Contact Email, Phone Number, Educational Qualifications, and Technical Skills), and computes a semantic match score against any target job description using TF-IDF vectorization and Cosine Similarity, along with an automated skill gap analysis.

---

## 👩‍💻 Intern Information
- **Name:** Samruddhi Dange
- **Intern ID:** CITS8515
- **Internship Program:** CodTech IT Solutions Internship
- **Domain:** Artificial Intelligence / Natural Language Processing
- **Task 4:** Resume Parser & Job Matcher

---

## 🚀 Key Features
- **Multi-Format Ingestion:** Supports `.pdf` (via `pypdf`), `.docx` (via `python-docx`), and plain `.txt`.
- **Information Extraction Pipeline:**
  - **Candidate Name:** Pattern and structural heuristic parsing.
  - **Email Extraction:** RFC-compliant regex pattern recognition.
  - **Phone Number Extraction:** Domestic and international telephone format extraction.
  - **Education Detection:** Recognizes degrees (B.E., B.Tech, M.Tech, B.Sc, M.Sc, PhD, etc.).
  - **Skills Extraction:** Domain-specific taxonomy covering AI/ML, Data Science, Web, Cloud, Databases, and DevOps.
- **Job Description Matcher & Gap Analysis:**
  - TF-IDF Vectorization and Cosine Similarity scoring.
  - Granular skill gap identification (Matching Skills vs. Missing / Recommended Skills).
- **Interactive Streamlit Web Dashboard:**
  - Upload custom resumes or test immediately with pre-loaded sample resumes.
  - Preset job descriptions for roles like *Machine Learning / AI Engineer*, *Data Science Intern*, and *Full Stack Developer*.
  - Export structured resume data directly as a formatted JSON document.

---

## 📁 Repository Structure
```
├── app.py                         # Streamlit interactive web application
├── parser_engine.py               # Core parsing, NLP, and matching engine
├── create_sample_resumes.py       # Script generating test PDF and TXT resumes
├── requirements.txt               # Package dependencies
├── .gitignore                     # Git ignore rules
├── README.md                      # Comprehensive project documentation
└── sample_resumes/                # Test resumes
    ├── samruddhi_dange_resume.pdf # Formatted PDF resume
    └── data_science_intern_resume.txt
```

---

## 💻 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/SamruddhiDangeSSGMCE/CODTECH-Task4-Resume-Parser.git
cd CODTECH-Task4-Resume-Parser
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Generate sample test resumes (Optional, pre-generated resumes included)
```bash
python create_sample_resumes.py
```

### 4. Launch Streamlit Web Application
```bash
streamlit run app.py
```
Open your browser at `http://localhost:8501`.

---

## 📜 License & Acknowledgments
Developed as part of the CodTech IT Solutions Internship.

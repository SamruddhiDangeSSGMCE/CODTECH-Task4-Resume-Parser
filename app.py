"""
Resume Parser & Job Description Matcher - Streamlit Web Dashboard
CodTech IT Solutions Internship - Task 4
Author: Samruddhi Dange
"""

import os
import json
import streamlit as st
import pandas as pd
from parser_engine import ResumeParser, JobMatcher

st.set_page_config(
    page_title="Resume Parser & Job Matcher | CodTech Task 4",
    page_icon="📄",
    layout="wide"
)

# Header & Branding
st.markdown("""
<div style="background: linear-gradient(135deg, #0F766E, #14B8A6); padding: 22px; border-radius: 12px; color: white; margin-bottom: 20px;">
    <h1 style="margin: 0; font-size: 2.2rem;">📄 AI Resume Parser & Job Matcher</h1>
    <p style="margin: 5px 0 0 0; opacity: 0.9; font-size: 1.05rem;">
        CodTech IT Solutions Internship • <b>Task 4: Natural Language Processing & Information Extraction</b>
    </p>
    <p style="margin: 3px 0 0 0; font-size: 0.9rem; opacity: 0.8;">
        Intern: <b>Samruddhi Dange</b> | Intern ID: <b>CITS8515</b> | Domain: <b>Artificial Intelligence & NLP</b>
    </p>
</div>
""", unsafe_allow_html=True)

SAMPLE_DIR = os.path.join(os.path.dirname(__file__), 'sample_resumes')

# Sidebar: Resume Source
st.sidebar.header("📁 Resume Source")
source_mode = st.sidebar.radio("Input Source:", ["Sample Resumes Library", "Upload New Resume"])

file_bytes = None
filename = ""

if source_mode == "Sample Resumes Library":
    sample_options = {
        "Samruddhi Dange - ML Intern (PDF)": "samruddhi_dange_resume.pdf",
        "Alex Morgan - Data Science (TXT)": "data_science_intern_resume.txt"
    }
    selected_sample = st.sidebar.selectbox("Choose a Sample Resume:", list(sample_options.keys()))
    sample_fname = sample_options[selected_sample]
    sample_path = os.path.join(SAMPLE_DIR, sample_fname)
    if os.path.exists(sample_path):
        with open(sample_path, 'rb') as f:
            file_bytes = f.read()
        filename = sample_fname
else:
    uploaded = st.sidebar.file_uploader("Upload Resume (PDF, DOCX, TXT):", type=['pdf', 'docx', 'txt'])
    if uploaded is not None:
        file_bytes = uploaded.read()
        filename = uploaded.name

# Job Description Presets
st.sidebar.markdown("---")
st.sidebar.header("💼 Target Job Description")
preset_jd = st.sidebar.selectbox(
    "Load Preset Role Description:",
    [
        "Custom Job Description",
        "Machine Learning / AI Engineer",
        "Data Science Intern",
        "Full Stack Developer"
    ]
)

PRESETS = {
    "Machine Learning / AI Engineer": (
        "Seeking a passionate Machine Learning / AI Engineer. The ideal candidate will build predictive models, "
        "deploy deep learning systems using PyTorch and TensorFlow, develop APIs using FastAPI or Flask, and containerize "
        "services using Docker. Strong background in Python, Scikit-Learn, Computer Vision, OpenCV, Git, and SQL is required."
    ),
    "Data Science Intern": (
        "Looking for a Data Science Intern. Responsibilities include exploratory data analysis, data cleaning with Pandas "
        "and NumPy, statistical modeling using Scikit-Learn, creating visualizations using Matplotlib, Seaborn, and Tableau, "
        "and presenting insights to technical teams. Proficiency in Python and SQL is essential."
    ),
    "Full Stack Developer": (
        "Hiring a Full Stack Developer proficient in HTML, CSS, JavaScript, React, Node.js, and Python. "
        "Experience with relational databases (PostgreSQL, MySQL), REST APIs, Docker, and CI/CD pipelines is preferred."
    )
}

default_jd_text = PRESETS.get(preset_jd, "")
job_desc_input = st.sidebar.text_area("Job Description Content:", value=default_jd_text, height=180)

# Main Application Body
if file_bytes is not None:
    parsed_info = ResumeParser.parse(file_bytes, filename)
    match_result = JobMatcher.match(parsed_info['raw_text'], parsed_info['skills'], job_desc_input)
    
    tab1, tab2, tab3 = st.tabs(["👤 Extracted Resume Profile", "🎯 Job Description Match Analysis", "📜 Raw Extracted Text"])
    
    with tab1:
        st.subheader("📋 Candidate Information Card")
        col_name, col_email, col_phone = st.columns(3)
        col_name.metric("Candidate Name", parsed_info['name'])
        col_email.metric("Email Address", parsed_info['email'])
        col_phone.metric("Phone Number", parsed_info['phone'])
        
        st.markdown("---")
        col_skills, col_edu = st.columns([3, 2])
        
        with col_skills:
            st.subheader(f"🛠️ Extracted Technical Skills ({len(parsed_info['skills'])})")
            if parsed_info['skills']:
                badges = " ".join([f"<span style='background-color:#E0F2FE;color:#0369A1;padding:5px 10px;margin:4px;border-radius:15px;display:inline-block;font-weight:600;'>{s}</span>" for s in parsed_info['skills']])
                st.markdown(badges, unsafe_allow_html=True)
            else:
                st.info("No standard skills detected.")
                
        with col_edu:
            st.subheader("🎓 Education & Degrees")
            if parsed_info['education']:
                for deg in parsed_info['education']:
                    st.success(f"• **{deg}**")
            else:
                st.write("Degree details not explicitly matched.")
            st.metric("Total Word Count", parsed_info['word_count'])

        st.markdown("---")
        # JSON Download Button
        json_str = json.dumps({
            "name": parsed_info['name'],
            "email": parsed_info['email'],
            "phone": parsed_info['phone'],
            "skills": parsed_info['skills'],
            "education": parsed_info['education'],
            "word_count": parsed_info['word_count']
        }, indent=2)
        st.download_button(
            label="💾 Download Parsed Resume JSON",
            data=json_str,
            file_name=f"{parsed_info['name'].replace(' ', '_')}_parsed.json",
            mime="application/json"
        )
        
    with tab2:
        st.subheader("🎯 Semantic Match & Gap Analysis")
        if job_desc_input.strip():
            c_score, c_stats = st.columns([1, 2])
            
            with c_score:
                st.markdown("#### Match Score")
                score = match_result['match_score']
                st.metric("TF-IDF Cosine Similarity", f"{score}%")
                st.progress(min(float(score / 100.0 * 2.5), 1.0)) # Scaled display
                if score > 15:
                    st.success("🟢 Strong Candidate Match")
                elif score > 8:
                    st.warning("🟡 Moderate Match")
                else:
                    st.error("🔴 Low Match")
                    
            with c_stats:
                st.markdown("#### Skill Gap Analysis")
                c_mat, c_mis = st.columns(2)
                
                with c_mat:
                    st.write(f"**Matching Skills ({len(match_result['matching_skills'])})**")
                    if match_result['matching_skills']:
                        for sk in match_result['matching_skills']:
                            st.markdown(f"✅ `<span style='color:green;font-weight:bold;'>{sk}</span>`", unsafe_allow_html=True)
                    else:
                        st.write("None")
                        
                with c_mis:
                    st.write(f"**Missing / Recommended Skills ({len(match_result['missing_skills'])})**")
                    if match_result['missing_skills']:
                        for sk in match_result['missing_skills']:
                            st.markdown(f"❌ `<span style='color:#DC2626;font-weight:bold;'>{sk}</span>`", unsafe_allow_html=True)
                    else:
                        st.write("No missing required skills!")
        else:
            st.info("Paste a Job Description in the sidebar to view semantic matching and skill gap analysis.")
            
    with tab3:
        st.subheader("📜 Extracted Raw Text")
        st.text_area("Plain Text Content", parsed_info['raw_text'], height=350)
else:
    st.info("👈 Please select a sample resume or upload a resume file from the sidebar to begin.")

"""
Generate sample resumes (PDF and TXT) for testing the Resume Parser
CodTech IT Solutions Internship - Task 4
Author: Samruddhi Dange
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf_resume(filepath: str):
    c = canvas.Canvas(filepath, pagesize=letter)
    width, height = letter
    
    # Title / Header
    c.setFont("Helvetica-Bold", 20)
    c.drawString(50, height - 50, "Samruddhi Dange")
    
    c.setFont("Helvetica", 10)
    c.drawString(50, height - 70, "Email: samruddhidangessgmce@gmail.com | Phone: +91-9876543210")
    c.drawString(50, height - 85, "LinkedIn: linkedin.com/in/samruddhidange | GitHub: github.com/SamruddhiDangeSSGMCE")
    
    c.setLineWidth(1)
    c.line(50, height - 95, width - 50, height - 95)
    
    # Summary
    c.setFont("Helvetica-Bold", 13)
    c.drawString(50, height - 120, "Professional Summary")
    c.setFont("Helvetica", 10)
    summary_text = (
        "Passionate Machine Learning Engineer & Data Science Intern with extensive experience in "
        "Python, Scikit-Learn, PyTorch, and TensorFlow. Skilled in designing scalable predictive models, "
        "Computer Vision systems, and interactive Streamlit web applications."
    )
    c.drawString(50, height - 140, summary_text[:95])
    c.drawString(50, height - 155, summary_text[95:])
    
    # Education
    c.setFont("Helvetica-Bold", 13)
    c.drawString(50, height - 185, "Education")
    c.setFont("Helvetica-Bold", 10)
    c.drawString(50, height - 205, "Bachelor of Engineering (B.E.) in Computer Science and Engineering")
    c.setFont("Helvetica-Oblique", 10)
    c.drawString(50, height - 220, "SSGMCE Shegaon | CGPA: 8.9 / 10.0 (2021 - 2025)")
    
    # Technical Skills
    c.setFont("Helvetica-Bold", 13)
    c.drawString(50, height - 250, "Technical Skills")
    c.setFont("Helvetica", 10)
    c.drawString(50, height - 270, "Languages & Libraries: Python, SQL, C++, HTML, CSS, JavaScript")
    c.drawString(50, height - 285, "AI / ML Frameworks: PyTorch, TensorFlow, Scikit-Learn, Pandas, NumPy, OpenCV, Keras")
    c.drawString(50, height - 300, "Web & Cloud Tools: Streamlit, FastAPI, Flask, Docker, Git, GitHub, MySQL, MongoDB")
    
    # Projects
    c.setFont("Helvetica-Bold", 13)
    c.drawString(50, height - 330, "Featured Projects")
    c.setFont("Helvetica-Bold", 10)
    c.drawString(50, height - 350, "1. Handwritten Digit Recognition System (PyTorch CNN & SVM)")
    c.setFont("Helvetica", 9)
    c.drawString(60, height - 365, "• Built a Deep Convolutional Neural Network achieving 99.44% test accuracy.")
    c.drawString(60, height - 378, "• Integrated dynamic preprocessing and multi-class probability visualization.")
    
    c.setFont("Helvetica-Bold", 10)
    c.drawString(50, height - 400, "2. Customer Segmentation Engine using K-Means")
    c.setFont("Helvetica", 9)
    c.drawString(60, height - 415, "• Analyzed customer spending behaviors using Elbow and Silhouette methods (k=5).")
    c.drawString(60, height - 428, "• Delivered automated marketing persona classification and interactive dashboard.")
    
    c.setFont("Helvetica-Bold", 10)
    c.drawString(50, height - 450, "3. Titanic Survival Prediction Web App")
    c.setFont("Helvetica", 9)
    c.drawString(60, height - 465, "• Trained Logistic Regression, Random Forest, and Gradient Boosting pipelines.")
    c.drawString(60, height - 478, "• Built real-time inference with probability gauges in Streamlit.")
    
    # Internship
    c.setFont("Helvetica-Bold", 13)
    c.drawString(50, height - 510, "Internship Experience")
    c.setFont("Helvetica-Bold", 10)
    c.drawString(50, height - 530, "CodTech IT Solutions - Machine Learning Intern")
    c.setFont("Helvetica-Oblique", 10)
    c.drawString(50, height - 545, "Duration: 4 Weeks | Domain: Artificial Intelligence & Machine Learning")
    c.setFont("Helvetica", 9)
    c.drawString(60, height - 560, "• Developed production-ready machine learning solutions, documentation, and web apps.")
    
    c.save()
    print(f"Generated PDF resume: {filepath}")

def generate_txt_resume(filepath: str):
    content = """Alex Morgan
Email: alex.morgan@techmail.com | Phone: +1-555-234-5678
Location: San Francisco, CA | GitHub: github.com/alexmorgan-dev

PROFESSIONAL SUMMARY:
Data Science Intern with foundational expertise in Python, SQL, Machine Learning, and Data Analysis. Proven ability to build predictive models with Scikit-Learn and deploy data dashboards with Streamlit and Flask.

EDUCATION:
B.Tech in Information Technology
National Institute of Technology (NIT) | 2020 - 2024

SKILLS:
• Programming: Python, SQL, R, JavaScript
• Data Science: Scikit-Learn, Pandas, NumPy, Matplotlib, Seaborn, Feature Engineering
• Machine Learning: Deep Learning, TensorFlow, NLP, XGBoost
• Tools: Git, GitHub, Docker, MySQL, Tableau

WORK EXPERIENCE:
Data Science Intern | Apex Analytics
June 2023 - December 2023
• Built customer churn prediction models using Scikit-Learn and XGBoost with 84% accuracy.
• Performed Exploratory Data Analysis (EDA) on 100,000+ customer records using Pandas.
• Designed real-time monitoring dashboards using Streamlit and Tableau.
"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Generated TXT resume: {filepath}")

if __name__ == '__main__':
    os.makedirs('sample_resumes', exist_ok=True)
    generate_pdf_resume(os.path.join('sample_resumes', 'samruddhi_dange_resume.pdf'))
    generate_txt_resume(os.path.join('sample_resumes', 'data_science_intern_resume.txt'))

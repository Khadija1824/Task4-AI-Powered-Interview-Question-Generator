import streamlit as st
import os
from src.generator import InterviewQuestionGenerator

st.set_page_config(page_title="AI Interview Question Generator", page_icon="🎯", layout="wide")

# Custom Styling
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    .stButton>button { width: 100%; background-color: #2563eb; color: white; border-radius: 6px; }
    .stButton>button:hover { background-color: #1d4ed8; }
    </style>
""", unsafe_allow_html=True)

st.title("🎯 AI-Powered Intern Interview Question Generator")
st.markdown("Generate custom technical & behavioral interview question sets tailored specifically to your candidate profiles and job descriptions.")

# Initialize generator
@st.cache_resource
def get_generator():
    return InterviewQuestionGenerator()

generator = get_generator()

# Load default sample text files if available
def load_file_content(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return ""

default_jd = load_file_content("data/sample_jd.txt")
default_candidate = load_file_content("data/sample_candidate.txt")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📄 Job Description")
    jd_input = st.text_area("Paste Job Description or Requirements:", value=default_jd, height=250)

with col2:
    st.subheader("👤 Candidate Profile / Resume Summary")
    candidate_input = st.text_area("Paste Candidate Background or Resume:", value=default_candidate, height=250)

if st.button("Generate Interview Pack"):
    if not jd_input.strip() or not candidate_input.strip():
        st.warning("Please provide both a job description and a candidate profile.")
    else:
        with st.spinner("Analyzing profile against job description and generating questions..."):
            result = generator.generate_questions(jd_input, candidate_input)
            
            if "error" in result:
                st.error(f"Generation failed: {result['error']}")
            else:
                st.success("Interview pack generated successfully!")
                
                # Display Candidate Fit Summary
                if "candidate_summary" in result:
                    st.info(f"**Candidate Fit Overview:** {result['candidate_summary']}")
                
                st.markdown("---")
                st.subheader("📋 Tailored Interview Question Set")
                
                for idx, q in enumerate(result.get("questions", []), 1):
                    q_type = q.get("type", "Technical")
                    badge_color = "green" if q_type == "Technical" else "blue"
                    
                    with st.expander(f"Q{idx}: [{q_type}] {q.get('focus_area', 'General')} — Click to expand"):
                        st.markdown(f"**Question:** {q.get('question')}")
                        st.markdown(f"**Evaluation Rubric / What to Look For:**\n> {q.get('evaluation_rubric')}")
# 🎯 AI-Powered Intern Interview Question Generator

An automated, role-specific technical and behavioral interview question generator designed for hiring managers and recruiters. This application leverages the Google Gemini API to analyze job descriptions and candidate resumes, generating targeted interview questions along with evaluation rubrics.

---

## 🚀 Features

* **AI-Driven Personalization:** Automatically extracts candidate skills, projects, and experiences to craft contextual technical questions.
* **Balanced Question Sets:** Generates a tailored mix of technical depth queries (frameworks, algorithms, system architecture) and behavioral scenario prompts.
* **Evaluation Rubrics:** Provides clear "what to look for" guidelines and expected answers for each question to assist interviewers.
* **Interactive Web Interface:** Built with Streamlit for a clean, responsive, and easy-to-use desktop experience.
* **JSON-Enforced Output:** Uses structured schema generation to ensure reliable, clean data parsing.

---

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **AI / LLM:** Google GenAI SDK (`gemini-2.5-flash`)
* **Frontend Dashboard:** Streamlit
* **Utilities:** Pydantic, Python-Dotenv

---
⚙️ Installation & Setup
1. Clone or Navigate to the Repository
Open your terminal in the project root directory.

2. Install Dependencies
Install all necessary Python packages using pip:

Bash
pip install -r requirements.txt
3. Configure Environment Variables
Create a .env file in the root directory of your project and add your Google Gemini API key:

Code snippet
GEMINI_API_KEY=your_actual_api_key_here
🏃‍♂️ Running the Application
Launch the Streamlit web app by running:

Bash
streamlit run app.py
Once the local server starts:

Open your browser and go to the local URL provided (typically http://localhost:8501).

Review or modify the pre-loaded Job Description and Candidate Profile text areas.

Click "Generate Interview Pack" to view the candidate fit analysis and tailored interview questions with evaluation rubrics.

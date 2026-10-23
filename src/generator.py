import os
import json
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

class InterviewQuestionGenerator:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        self.client = genai.Client(api_key=api_key) if api_key else genai.Client()
        self.model_name = 'gemini-2.5-flash'

    def generate_questions(self, job_description: str, candidate_profile: str, num_questions: int = 5) -> dict:
        prompt = f"""
        You are an expert technical recruiter and hiring manager at a tech firm. 
        Your task is to generate custom interview questions for an intern candidate based on the provided Job Description (JD) and Candidate Profile.

        JOB DESCRIPTION:
        {job_description}

        CANDIDATE PROFILE:
        {candidate_profile}

        INSTRUCTIONS:
        1. Generate a mix of technical questions (targeting specific skills/projects mentioned in the JD and profile) and behavioral questions.
        2. Tailor difficulty appropriately for an intern position (testing fundamentals, problem-solving, and project understanding).
        3. Provide an expected answer guideline or evaluation rubric for each question.
        4. Output valid JSON matching the following schema structure:
        {{
            "candidate_summary": "Brief 1-2 sentence summary of candidate fit",
            "questions": [
                {{
                    "type": "Technical" or "Behavioral",
                    "focus_area": "e.g., Machine Learning / Python / Teamwork",
                    "question": "The interview question text",
                    "evaluation_rubric": "What to look for in a good answer"
                }}
            ]
        }}
        """

        try:
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    temperature=0.4,
                ),
            )
            return json.loads(response.text)
        except Exception as e:
            return {"error": str(e)}
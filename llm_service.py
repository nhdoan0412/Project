from models import Resume


def extract_resume_from_text(text: str) -> Resume:
    """
    Simulated LLM extraction function. Replace with real Gemini + LangChain pipeline.
    """
    return Resume(
        name="John Doe",
        contact_number="+1-123-456-7890",
        email="john.doe@example.com",
        skills=["Python", "SQL", "Machine Learning"],
        educations=[{
            "institution": "University of Example",
            "start_date": "2015-09",
            "end_date": "2019-05",
            "location": "Boston, MA",
            "degree": "B.Sc in Computer Science"
        }],
        work_experiences=[{
            "company": "Tech Company Inc.",
            "start_date": "2019-06",
            "end_date": "2023-03",
            "location": "San Francisco, CA",
            "role": "Software Engineer"
        }],
        YoE="4 years"
    )



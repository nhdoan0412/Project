#from models import Resume
#
#
#def extract_resume_from_text(text: str) -> Resume:
#    """
#    Simulated LLM extraction function. Replace with real Gemini + LangChain pipeline.
#    """
#    return Resume(
#        name="John Doe",
#        contact_number="+1-123-456-7890",
#        email="john.doe@example.com",
#        skills=["Python", "SQL", "Machine Learning"],
#        educations=[{
#            "institution": "University of Example",
#            "start_date": "2015-09",
#            "end_date": "2019-05",
#            "location": "Boston, MA",
#            "degree": "B.Sc in Computer Science"
#        }],
#        work_experiences=[{
#            "company": "Tech Company Inc.",
#            "start_date": "2019-06",
#            "end_date": "2023-03",
#            "location": "San Francisco, CA",
#            "role": "Software Engineer"
#        }],
#        YoE="4 years"
#    )

import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.output_parsers import PydanticOutputParser
from models import Resume

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  # ✅ Correct model for API key
    temperature=0.2,
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    convert_system_message_to_human=True
)

def extract_resume_from_text(text: str) -> Resume:
    parser = PydanticOutputParser(pydantic_object=Resume)

    prompt = PromptTemplate(
        input_variables=["text"],
        template="""
You are a helpful assistant that extracts structured resume information from raw text.
Return the output in this exact JSON format:

{format_instructions}

Resume:
{text}
""",
        partial_variables={"format_instructions": parser.get_format_instructions()}
    )

    chain = prompt | llm | parser
    return chain.invoke({"text": text})

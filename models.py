from typing import List, Optional
from pydantic import BaseModel


class Education(BaseModel):
    institution: str
    start_date: str
    end_date: str
    location: str
    degree: str


class WorkExperience(BaseModel):
    company: str
    start_date: str
    end_date: str
    location: str
    role: str


class Resume(BaseModel):
    name: Optional[str]
    contact_number: Optional[str]
    email: Optional[str]
    skills: List[str] = []
    educations: List[Education] = []
    work_experiences: List[WorkExperience] = []
    YoE: Optional[str] = None  

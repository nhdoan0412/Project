from typing import List, Optional
from pydantic import BaseModel


class Education(BaseModel):
    institution: str
    start_date: Optional[str] = None  # ✅ allow missing dates
    end_date: Optional[str] = None
    location: Optional[str] = None
    degree: Optional[str] = None


class WorkExperience(BaseModel):
    company: str
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    location: Optional[str] = None
    role: Optional[str] = None


class Resume(BaseModel):
    name: Optional[str] = None
    contact_number: Optional[str] = None
    email: Optional[str] = None
    skills: List[str] = []
    educations: List[Education] = []
    work_experiences: List[WorkExperience] = []
    YoE: Optional[str] = None

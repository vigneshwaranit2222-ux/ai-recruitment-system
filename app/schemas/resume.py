from pydantic import BaseModel


class ResumeResponse(BaseModel):
    candidate_name: str
    skills: list[str]
    resume_text: str
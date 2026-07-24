from pydantic import BaseModel


class CandidateCreate(BaseModel):
    name: str
    skills: str
    experience: int
    projects: str
    resume_text: str


class CandidateResponse(BaseModel):
    id: int
    name: str
    skills: str
    experience: int
    projects: str
    resume_text: str

    class Config:
        from_attributes = True
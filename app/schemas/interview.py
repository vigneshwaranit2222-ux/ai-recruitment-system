from pydantic import BaseModel


class InterviewCreate(BaseModel):
    candidate_id: int
    communication: float
    problem_solving: float
    coding: float
    leadership: float


class InterviewResponse(BaseModel):
    id: int
    candidate_id: int
    communication: float
    problem_solving: float
    coding: float
    leadership: float
    overall_rating: float

    class Config:
        from_attributes = True
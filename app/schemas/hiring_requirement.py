from pydantic import BaseModel


class HiringRequirement(BaseModel):

    role: str

    skills: list[str]

    experience: int

    communication: str
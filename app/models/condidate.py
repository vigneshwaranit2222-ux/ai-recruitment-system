from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

from app.database.database import Base


class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100))

    skills = Column(Text)
class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True)

    name = Column(String(100))

    skills = Column(Text)

    experience = Column(Integer)

    salary_expectation = Column(Integer)

    location = Column(String(100))

    available = Column(String(20))

    projects = Column(Text)

    resume_text = Column(Text)
    experience = Column(Integer)

    projects = Column(Text)

    resume_text = Column(Text)
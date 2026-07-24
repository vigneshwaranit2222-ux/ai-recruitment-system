from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

from app.database.database import Base


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True)

    company_name = Column(String(200))

    role_name = Column(String(200))

    required_skills = Column(Text)

    required_experience = Column(Integer)

    job_description = Column(Text)
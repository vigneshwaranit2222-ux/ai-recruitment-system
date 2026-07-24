from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import ForeignKey

from app.database.database import Base


class Interview(Base):
    __tablename__ = "interviews"

    id = Column(Integer, primary_key=True)

    candidate_id = Column(
        Integer,
        ForeignKey("candidates.id")
    )

    communication = Column(Float)

    problem_solving = Column(Float)

    coding = Column(Float)

    leadership = Column(Float)

    overall_rating = Column(Float)
from sqlalchemy.orm import Session

from app.models.interview import Interview

from app.services.interview.score_calculator import (
    ScoreCalculator
)


class InterviewRepository:

    @staticmethod
    def create_interview(
        db: Session,
        interview_data
    ):

        overall_score = (
            ScoreCalculator.calculate_overall_score(
                interview_data.communication,
                interview_data.problem_solving,
                interview_data.coding,
                interview_data.leadership
            )
        )

        interview = Interview(
            candidate_id=interview_data.candidate_id,
            communication=interview_data.communication,
            problem_solving=interview_data.problem_solving,
            coding=interview_data.coding,
            leadership=interview_data.leadership,
            overall_rating=overall_score
        )

        db.add(interview)
        db.commit()
        db.refresh(interview)

        return interview

    @staticmethod
    def get_all_interviews(
        db: Session
    ):
        return db.query(Interview).all()
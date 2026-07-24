from sqlalchemy.orm import Session

from app.models.candidate import Candidate


class CandidateRepository:

    @staticmethod
    def create_candidate(
        db: Session,
        candidate_data
    ):

        candidate = Candidate(
            name=candidate_data.name,
            skills=candidate_data.skills,
            experience=candidate_data.experience,
            projects=candidate_data.projects,
            resume_text=candidate_data.resume_text
        )

        db.add(candidate)
        db.commit()
        db.refresh(candidate)

        return candidate

    @staticmethod
    def get_all_candidates(db: Session):

        return db.query(Candidate).all()

    @staticmethod
    def get_candidate_by_id(
        db: Session,
        candidate_id: int
    ):

        return (
            db.query(Candidate)
            .filter(Candidate.id == candidate_id)
            .first()
        )
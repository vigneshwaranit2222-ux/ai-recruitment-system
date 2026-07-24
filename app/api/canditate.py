from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.schemas.candidate_schema import CandidateCreate
from app.schemas.candidate_schema import CandidateResponse

from app.database.candidate_repository import CandidateRepository

router = APIRouter(
    prefix="/candidates",
    tags=["Candidates"]
)


@router.post(
    "/",
    response_model=CandidateResponse
)
def create_candidate(
    candidate: CandidateCreate,
    db: Session = Depends(get_db)
):

    return CandidateRepository.create_candidate(
        db,
        candidate
    )


@router.get(
    "/",
    response_model=list[CandidateResponse]
)
def get_candidates(
    db: Session = Depends(get_db)
):

    return CandidateRepository.get_all_candidates(db)


@router.get(
    "/{candidate_id}",
    response_model=CandidateResponse
)
def get_candidate(
    candidate_id: int,
    db: Session = Depends(get_db)
):

    return CandidateRepository.get_candidate_by_id(
        db,
        candidate_id
    )
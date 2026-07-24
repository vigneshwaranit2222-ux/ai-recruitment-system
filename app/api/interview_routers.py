from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.schemas.interview_schema import (
    InterviewCreate,
    InterviewResponse
)

from app.database.interview_repository import (
    InterviewRepository
)

router = APIRouter(
    prefix="/interviews",
    tags=["Interviews"]
)


@router.post(
    "/",
    response_model=InterviewResponse
)
def create_interview(
    interview: InterviewCreate,
    db: Session = Depends(get_db)
):

    return InterviewRepository.create_interview(
        db,
        interview
    )


@router.get(
    "/",
    response_model=list[InterviewResponse]
)
def get_interviews(
    db: Session = Depends(get_db)
):

    return InterviewRepository.get_all_interviews(
        db
    )
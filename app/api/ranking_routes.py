from fastapi import APIRouter

from app.services.matching.candidate_ranker import (
    CandidateRanker
)

router = APIRouter(
    prefix="/ranking",
    tags=["Ranking"]
)


@router.post("/rank")
def rank_candidates():

    sample_data = [

        {
            "candidate_name": "John",
            "final_score": 91.5
        },

        {
            "candidate_name": "Alex",
            "final_score": 87.2
        },

        {
            "candidate_name": "David",
            "final_score": 95.1
        }
    ]

    return (
        CandidateRanker.rank_candidates(
            sample_data
        )
    )
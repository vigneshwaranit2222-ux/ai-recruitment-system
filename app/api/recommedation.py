from fastapi import APIRouter

from app.services.embedding.embedding_service import (
    EmbeddingService
)

from app.services.matching.recommendation_engine import (
    RecommendationEngine
)

router = APIRouter(
    prefix="/recommendations",
    tags=["Recommendations"]
)


@router.post("/match")
def recommend_candidate(

    candidate_resume: str,
    company_jd: str,
    interview_score: float

):

    candidate_embedding = (
        EmbeddingService.generate_embedding(
            candidate_resume
        )
    )

    company_embedding = (
        EmbeddingService.generate_embedding(
            company_jd
        )
    )

    result = (
        RecommendationEngine.generate_recommendation(
            candidate_embedding,
            company_embedding,
            interview_score
        )
    )

    return result 
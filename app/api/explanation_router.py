from fastapi import APIRouter
import google.generativeai as genai

from app.services.llm.recommendation_explainer import (
    RecommendationExplainer
)

router = APIRouter(
    prefix="/explanation",
    tags=["AI Explanation"]
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

explainer = RecommendationExplainer(
    model
)


@router.post("/")
def explain_candidate():

    candidate = {
        "name": "John",
        "skills":
        "Python, FastAPI, LangChain, RAG, Docker",

        "experience": 2,

        "interview_score": 90,

        "similarity_score": 95,

        "final_score": 93
    }

    explanation = (
        explainer.generate_explanation(
            candidate
        )
    )

    return {
        "candidate": candidate["name"],
        "explanation": explanation
    }
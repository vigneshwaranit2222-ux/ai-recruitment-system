from fastapi import FastAPI

from app.api.candidate import router as candidate_router
from app.api.company import router as company_router
from app.api.interview_routes import router as interview_router
from app.api.llm_routes import router as llm_router
from app.api.ranking_routes import router as ranking_router
from app.api.Report_routes import router as report_router
from app.api.explanation_router import router as explanation_router
from app.schemas.company_schema import (
    CompanyCreate,
    CompanyResponse,
)

app = FastAPI(
    title="AI Recruitment System",
    version="1.0.0"
)

app.include_router(candidate_router)
app.include_router(company_router)
app.include_router(interview_router)
app.include_router(llm_router)
app.include_router(ranking_router)
app.include_router(report_router)
app.include_router(explanation_router)


@app.get("/")
def home():
    return {
        "message": "AI Recruitment Recommendation System Running"
    }
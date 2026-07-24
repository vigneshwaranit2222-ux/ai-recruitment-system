from fastapi import APIRouter

from app.services.llm.requirement_extractor import (
    RequirementExtractor
)

router = APIRouter(
    prefix="/llm",
    tags=["LLM"]
)


@router.post("/extract")
def extract_requirement(
    prompt: str
):

    result = (
        RequirementExtractor
        .extract_requirements(
            prompt
        )
    )

    return result
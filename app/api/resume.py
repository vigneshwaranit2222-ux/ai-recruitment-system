import os

from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from app.services.resume.resume_loader import (
    ResumeLoader
)

from app.services.resume.resume_cleaner import (
    ResumeCleaner
)

from app.services.resume.resume_parser import (
    ResumeParser
)

router = APIRouter(
    prefix="/resume",
    tags=["Resume Parsing"]
)


@router.post("/upload")
async def upload_resume(
    file: UploadFile = File(...)
):

    os.makedirs(
        "data/resumes",
        exist_ok=True
    )

    file_path = (
        f"data/resumes/{file.filename}"
    )

    with open(
        file_path,
        "wb"
    ) as buffer:

        buffer.write(
            await file.read()
        )

    raw_text = ResumeLoader.load_pdf(
        file_path
    )

    cleaned_text = (
        ResumeCleaner.clean_text(
            raw_text
        )
    )

    candidate_name = (
        ResumeParser.extract_name(
            cleaned_text
        )
    )

    skills = (
        ResumeParser.extract_skills(
            cleaned_text
        )
    )

    return {
        "candidate_name": candidate_name,
        "skills": skills,
        "resume_text": cleaned_text
    }
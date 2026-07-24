from fastapi import APIRouter

from app.reports.report_generator import (
    ReportGenerator
)

from app.reports.pdf_generator import (
    PDFGenerator
)

router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


@router.get("/generate")
def generate_report():

    report_data = (
        ReportGenerator.generate_report()
    )

    file_name = (
        "recruitment_report.pdf"
    )

    PDFGenerator.generate_pdf(
        report_data,
        file_name
    )

    return {
        "message":
        "Report Generated Successfully",

        "file":
        file_name
    }
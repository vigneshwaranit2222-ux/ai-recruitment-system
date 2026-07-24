from uuid import uuid4

from fastapi import APIRouter, status

from app.schemas.company_schema import (
    CompanyCreate,
    CompanyResponse
)

router = APIRouter(
    prefix="/v1/companies",
    tags=["Companies"]
)


@router.post(
    "",
    response_model=CompanyResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_company(
    company: CompanyCreate
):

    return CompanyResponse(
        id=uuid4(),
        tenant_id=uuid4(),
        name=company.name,
        website=company.website
    )
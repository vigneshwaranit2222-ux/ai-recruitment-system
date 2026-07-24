from uuid import UUID

from pydantic import BaseModel, ConfigDict


class CompanyCreate(BaseModel):
    name: str
    website: str | None = None


class CompanyResponse(BaseModel):
    id: UUID
    tenant_id: UUID
    name: str
    website: str | None = None

    model_config = ConfigDict(
        from_attributes=True
    )
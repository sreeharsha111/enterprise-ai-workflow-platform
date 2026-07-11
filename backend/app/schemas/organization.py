from pydantic import EmailStr
from app.schemas.common import BaseResponse
from uuid import UUID

class OrganizationCreateRequest(BaseResponse):
    organization_name: str
    company_email: EmailStr
    employee_size: str
    timezone: str

    admin_name: str
    admin_email: EmailStr
    password: str

class OrganizationResponse(BaseResponse):
    organization_id: UUID
    organization_code: str
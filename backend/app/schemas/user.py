from app.schemas.common import BaseResponse
from pydantic import EmailStr
from uuid import UUID

class UserCreateRequest(BaseResponse):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    organization_id: UUID

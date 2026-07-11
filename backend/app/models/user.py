from dataclasses import dataclass
from uuid import UUID
from app.enums.status import Status
from app.models.base_entity import BaseEntity

@dataclass
class User(BaseEntity):
    id: UUID
    first_name: str
    last_name: str
    role: str
    email: str
    password_hash: str
    organization_code: str
    status: Status
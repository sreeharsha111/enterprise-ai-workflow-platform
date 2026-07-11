from dataclasses import dataclass
from uuid import UUID

from app.enums.status import Status
from app.models.base_entity import BaseEntity


@dataclass
class Organization(BaseEntity):
    id: UUID
    organization_code: str
    organization_name: str
    company_email: str
    employee_size: str
    timezone: str
    status: Status
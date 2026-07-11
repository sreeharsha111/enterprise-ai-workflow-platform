from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class BaseEntity:
    created_at: datetime | None
    updated_at: datetime | None
    created_by: UUID | None
    updated_by: UUID | None
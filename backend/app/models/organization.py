from dataclasses import dataclass
from datetime import datetime
from sqlalchemy import Column, DateTime, Enum, Integer, String
from app.core.database import Base
# from uuid import UUID

from app.enums.status import Status
# from app.models.base_entity import BaseEntity


@dataclass
class Organization(Base):
    __tablename__ ="organizations"
    id = Column(String(36), primary_key=True, nullable=False)

    organization_code = Column(
        String(20),
        unique=True,
        nullable=False
    )

    organization_name = Column(
        String(255),
        nullable=False
    )

    company_email = Column(
        String(255),
        unique=True,
        nullable=False
    )

    employee_size = Column(
        Integer,
        nullable=False
    )

    timezone = Column(
        String(100),
        nullable=False
    )

    status = Column(
        Enum(Status),
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    updated_at = Column(
        DateTime,
        nullable=True
    )

    created_by = Column(
        String(36),
        nullable=True
    )

    updated_by = Column(
        String(36),
        nullable=True
    )
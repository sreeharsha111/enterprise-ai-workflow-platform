from datetime import datetime

from app.enums.status import Status
from app.models.organization import Organization
from app.repositories.organization_repository import OrganizationRepository
from app.utils.uuid_generator import UUIDGenerator
from app.schemas.organization import OrganizationCreateRequest
from app.utils.organization_code_generator import OrganizationCodeGenerator
from app.exceptions.organization_exceptions import (
    OrganizationAlreadyExistsException
)
from app.schemas.organization import OrganizationResponse
from app.core.constants import ORGANIZATION_CREATED

class OrganizationService:

    def __init__(self,repository):
        self.repository = repository
        
    def create(self, request: OrganizationCreateRequest):
        existing_organization = self.repository.get_by_company_email(request.company_email)

        if existing_organization:
            raise OrganizationAlreadyExistsException(
                "Organization already exists."
            )



        organization_id = UUIDGenerator.generate()
        # organization_code = f"ORG-{len(self.repository.organizations) + 1:06d}"
        organization_count = self.repository.count()
        organization_code = OrganizationCodeGenerator.generate(organization_count)

        new_organization = Organization(
            id=organization_id,
            organization_code=organization_code,
            organization_name=request.organization_name,
            company_email=request.company_email,
            employee_size=request.employee_size,
            timezone=request.timezone,
            # admin_name=request.admin_name,
            # admin_email=request.admin_email,
            status=Status.ACTIVE,
            created_at=datetime.utcnow(),
            updated_at=None,
            updated_by=None,
            created_by=None
        )

        saved_organization = self.repository.save(new_organization)
        return OrganizationResponse(
            success=True,
            message=ORGANIZATION_CREATED,
            organization_id=saved_organization.id,
            organization_code=saved_organization.organization_code
        )
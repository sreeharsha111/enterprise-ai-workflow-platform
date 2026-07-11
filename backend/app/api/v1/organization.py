from fastapi import APIRouter
from app.schemas.organization import (
    OrganizationCreateRequest,
    OrganizationResponse
)
from app.services.organization_service import OrganizationService
from app.repositories.organization_repository import OrganizationRepository

router = APIRouter(
    prefix="/api/v1/organizations",
    tags=["Organizations"]
)

repository = OrganizationRepository()
service = OrganizationService(repository)

@router.post("/",response_model=OrganizationResponse)
def create_organization(request: OrganizationCreateRequest):
    return service.create(request)
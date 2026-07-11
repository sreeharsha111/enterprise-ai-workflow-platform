from app.repositories.user_repository import UserRepository
from app.repositories.organization_repository import OrganizationRepository
class UserService:
    def __init(self):
        self.user_repository = UserRepository()
        self.organisation_repository = OrganizationRepository()

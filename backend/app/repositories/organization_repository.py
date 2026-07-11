from app.models.organization import Organization

class OrganizationRepository:

    def __init__(self):
        self.organizations = []
    
    def save(self, organization: Organization):
        self.organizations.append(organization)
        return organization

    def get_by_company_email(self,email: str):
        for organization in self.organizations:
            if organization.company_email == email:
                return organization
        return None
    def count(self) -> int:
        return len(self.organizations)
    
    def get_all(self):
        return self.organizations
    
    def get_by_code(self, organization_code: str):
        for organization in self.organizations:
            if organization.organization_code == organization_code:
                return organization

        return None
    
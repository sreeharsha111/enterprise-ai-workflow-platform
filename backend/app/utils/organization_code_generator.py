class OrganizationCodeGenerator:

    @staticmethod
    def generate(count: int) -> str:
        return f"ORG-{count + 1:06d}"
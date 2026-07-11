import uuid
from uuid import UUID


class UUIDGenerator:

    @staticmethod
    def generate() -> UUID:
        return uuid.uuid4()
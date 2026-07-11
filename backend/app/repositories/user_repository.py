class UserRepository:

    def __init__(self):
        self.users = []

    def save(self, user):
        ...

    def get_by_email(self, email):
        ...

    def count(self):
        ...
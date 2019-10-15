class User:
    def __init__(self):
        self.id = ''
        self.name = ''
        self.country = ''
        self.email = ''
        self.password = ''
        self.role = ''

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'country': self.country,
            'email': self.email,
            'password': self.password,
            'role': self.role
        }
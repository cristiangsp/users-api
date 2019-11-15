import re
import uuid

from users_api.exception.user import NameTooShort, PasswordTooShort, RoleNotValid, EmailNotValid

class User:
    ROLE_ADVERTISER = 'advertiser'
    ROLE_PUBLISHER  = 'publisher'

    def __init__(self, name, email, password, role, country):
        self.__assert_name_is_valid(name)
        self.__assert_password_is_valid(password)
        self.__assert_email_is_valid(email)
        self.__assert_role_is_valid(role)

        self.id = str(uuid.uuid4())
        self.name = name
        self.country = country
        self.email = email
        self.password = password
        self.role = role

    def __assert_name_is_valid(self, name):
        if (len(name) < 5):
            raise NameTooShort()

    def __assert_password_is_valid(self, password):
        if (len(password) < 8):
            raise PasswordTooShort()

    def __assert_email_is_valid(self, email):
        if not re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):            
            raise EmailNotValid()

    def __assert_role_is_valid(self, role):
        if not role in [User.ROLE_ADVERTISER, User.ROLE_PUBLISHER]:
            raise RoleNotValid()

    def has_budget(self):
        return self.role == User.ROLE_ADVERTISER

    def initial_budget(self):
        if (self.country == 'US'):
            return 10000
    
        return 1000

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'country': self.country,
            'email': self.email,
            'password': self.password,
            'role': self.role
        }
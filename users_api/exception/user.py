class NameTooShort(Exception):
    def __init__(self):
        self.message = "Name cannot be shorter than 5 characters"

class PasswordTooShort(Exception):
    def __init__(self):
        self.message = "Password cannot be shorter than 8 characters"

class EmailNotValid(Exception):
    def __init__(self):
        self.message = "Email must be valid"

class RoleNotValid(Exception):
    def __init__(self):
        self.message = "Role must be 'advertiser' or 'publisher'"

class AlreadyExists(Exception):
    def __init__(self):
        self.message = "User already exists"

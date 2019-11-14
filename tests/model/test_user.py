import json
import unittest

from users_api.model.user import User
from users_api.exception.user import NameTooShort, PasswordTooShort, RoleNotValid, EmailNotValid

class TestUser(unittest.TestCase):

    def test_user_constructor_creates_a_user_properly(self):
        user = User('Awesome name', 'dummy@email.com', 'dummy-password', 'publisher', 'US')
        self.assertEqual('Awesome name', user.name)
        self.assertEqual('dummy@email.com', user.email)
        self.assertEqual('dummy-password', user.password)
        self.assertEqual('publisher', user.role)
        self.assertEqual('US', user.country)

    def test_user_constructor_fails_with_an_invalid_email(self):
        with self.assertRaises(EmailNotValid):
            User('Awesome name', 'invalid-email', 'dummy-password', 'publisher', 'US')

    def test_user_constructor_fails_with_a_too_short_name(self):
        with self.assertRaises(NameTooShort):
            User('A', 'dummy@email.com', 'dummy-password', 'publisher', 'US')

    def test_user_constructor_fails_with_a_too_short_password(self):
        with self.assertRaises(PasswordTooShort):
            User('Awesome name', 'dummy@email.com', 'P', 'publisher', 'US')

    def test_user_constructor_fails_with_an_invalid_role(self):
        with self.assertRaises(RoleNotValid):
            User('Awesome name', 'dummy@email.com', 'dummy-password', 'invalid-role', 'US')


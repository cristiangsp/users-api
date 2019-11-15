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

    def test_publisher_does_not_have_budget(self):
        user = User('Awesome name', 'dummy@email.com', 'dummy-password', 'publisher', 'US')
        self.assertFalse(user.has_budget())

    def test_advertiser_does_have_budget(self):
        user = User('Awesome name', 'dummy@email.com', 'dummy-password', 'advertiser', 'US')
        self.assertTrue(user.has_budget())

    def test_publisher_does_not_have_budget(self):
        user = User('Awesome name', 'dummy@email.com', 'dummy-password', 'publisher', 'US')
        self.assertFalse(user.has_budget())

    def test_us_advertiser_has_10000_as_initial_budget(self):
        user = User('Awesome name', 'dummy@email.com', 'dummy-password', 'advertiser', 'US')
        self.assertEqual(10000, user.initial_budget())
    
    def test_non_us_advertiser_has_1000_as_initial_budget(self):
        user = User('Awesome name', 'dummy@email.com', 'dummy-password', 'advertiser', 'ES')
        self.assertEqual(1000, user.initial_budget())

import unittest
import uuid

from users_api.database import users_database, budget_database
from users_api.use_case.create_user import CreateUser
from users_api.exception.user import AlreadyExists
from users_api.exception.country import NotValid

class TestCreateUserUseCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        users_database.delete()
        budget_database.delete()

    def test_create_user_use_case_creates_a_user_properly(self):
        create_user_use_case = CreateUser()
        create_user_use_case.execute(
            'Awesome name',
            'dummy@email.com',
            'dummy-password',
            'publisher',
            'US'
        )

        self.assertEqual(1, len(users_database.select_all()))

    def test_create_user_use_case_fails_when_the_user_already_exists(self):
        users_database.insert({
            'id': str(uuid.uuid4()),
            'name': 'Awesome name',
            'country': 'US',
            'email': 'dummy@email.com',
            'password': 'dummy-password',
            'role': 'publisher'
        })

        with self.assertRaises(AlreadyExists):
            create_user_use_case = CreateUser()
            create_user_use_case.execute(
                'Awesome name',
                'dummy@email.com',
                'dummy-password',
                'publisher',
                'US'
            )

    def test_create_user_use_case_fails_with_an_invalid_country(self):
        with self.assertRaises(NotValid):
            create_user_use_case = CreateUser()
            create_user_use_case.execute(
                'Awesome name',
                'dummy@email.com',
                'dummy-password',
                'publisher',
                'YY'
            )
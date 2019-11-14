import json
import unittest

from users_api.app import users_api
from users_api.database import users_database, budget_database

class TestUsersController(unittest.TestCase):

    def setUp(self):
        users_api.config['TESTING'] = True
        self.client = users_api.test_client()

    def tearDown(self):
        users_database.delete()
        budget_database.delete()

    def test_registration_creates_the_user_properly(self):
        request = self.__create_request('Awesome name', 'dummy@email.com', 'dummy-password', 'publisher', 'US')

        response = self.client.post(
            '/users',
            data=json.dumps(request),
            content_type='application/json'
        )
        self.assertEqual(200, response.status_code)
        self.assertEqual(b"User registered successfully", response.data)

        response = self.client.get('/users')
        response_data = json.loads(response.data.decode())
        self.assertEqual(1, len(response_data))
        self.assertEqual(response_data[0]['email'], request['email'])

    def test_registration_creates_a_budget_if_user_has_advertiser_role(self):
        request = self.__create_request('Awesome name', 'dummy@email.com', 'dummy-password', 'advertiser', 'US')

        response = self.client.post(
            '/users',
            data=json.dumps(request),
            content_type='application/json'
        )

        response = self.client.get('/users')
        user_response_data = json.loads(response.data.decode())

        response = self.client.get('/budgets')
        budget_response_data = json.loads(response.data.decode())
        self.assertEqual(1, len(budget_response_data))
        self.assertEqual(budget_response_data[0]['user_id'], user_response_data[0]['id'])
        self.assertEqual(budget_response_data[0]['amount'], 10000)

    def test_registration_creates_a_budget_with_right_initial_amount_when_advertiser_has_US_as_country(self):
        request = self.__create_request('Awesome name', 'dummy@email.com', 'dummy-password', 'advertiser', 'US')

        response = self.client.post(
            '/users',
            data=json.dumps(request),
            content_type='application/json'
        )

        response = self.client.get('/budgets')
        budget_response_data = json.loads(response.data.decode())
        self.assertEqual(budget_response_data[0]['amount'], 10000)

    def test_registration_creates_a_budget_with_right_initial_amount_when_advertiser_has_a_non_US_country(self):
        request = self.__create_request('Awesome name', 'dummy@email.com', 'dummy-password', 'advertiser', 'ES')

        response = self.client.post(
            '/users',
            data=json.dumps(request),
            content_type='application/json'
        )

        response = self.client.get('/budgets')
        budget_response_data = json.loads(response.data.decode())
        self.assertEqual(budget_response_data[0]['amount'], 1000)

    def test_registration_does_not_create_a_budget_if_user_has_publisher_role(self):
        request = self.__create_request('Awesome name', 'dummy@email.com', 'dummy-password', 'publisher', 'US')

        response = self.client.post(
            '/users',
            data=json.dumps(request),
            content_type='application/json'
        )

        response = self.client.get('/budgets')
        budget_response_data = json.loads(response.data.decode())
        self.assertEqual(0, len(budget_response_data))

    def test_registration_fails_with_a_too_short_name(self):
        request = self.__create_request('A', 'dummy@email.com', 'dummy-password', 'publisher', 'US')

        response = self.client.post(
            '/users',
            data=json.dumps(request),
            content_type='application/json'
        )
        self.assertEqual(400, response.status_code)
        self.assertEqual(b"Name cannot be shorter than 5 characters", response.data)

    def test_registration_fails_with_a_too_short_password(self):
        request = self.__create_request('Awesome name', 'dummy@email.com', 'P', 'publisher', 'US')

        response = self.client.post(
            '/users',
            data=json.dumps(request),
            content_type='application/json'
        )
        self.assertEqual(400, response.status_code)
        self.assertEqual(b"Password cannot be shorter than 8 characters", response.data)

    def test_registration_fails_with_an_invalid_email(self):
        request = self.__create_request('Awesome name', 'invalid-email', 'dummy-password', 'publisher', 'US')

        response = self.client.post(
            '/users',
            data=json.dumps(request),
            content_type='application/json'
        )
        self.assertEqual(400, response.status_code)
        self.assertEqual(b"Email must be valid", response.data)

    def test_registration_fails_with_an_invalid_country(self):
        request = self.__create_request('Awesome name', 'dummy@email.com', 'dummy-password', 'publisher', 'YY')

        response = self.client.post(
            '/users',
            data=json.dumps(request),
            content_type='application/json'
        )
        self.assertEqual(400, response.status_code)
        self.assertEqual(b"Country must be an ISO-3166 valid", response.data)

    def test_registration_fails_with_an_invalid_role(self):
        request = self.__create_request('Awesome name', 'dummy@email.com', 'dummy-password', 'invalid-role', 'US')

        response = self.client.post(
            '/users',
            data=json.dumps(request),
            content_type='application/json'
        )
        self.assertEqual(400, response.status_code)
        self.assertEqual(b"Role must be 'advertiser' or 'publisher'", response.data)

    def test_registration_fails_if_the_user_already_exists(self):
        request = self.__create_request('Awesome name', 'dummy@email.com', 'dummy-password', 'publisher', 'US')

        self.client.post(
            '/users',
            data=json.dumps(request),
            content_type='application/json'
        )

        response = self.client.post(
            '/users',
            data=json.dumps(request),
            content_type='application/json'
        )
        self.assertEqual(400, response.status_code)
        self.assertEqual(b"User already exists", response.data)

    def __create_request(self, name, email, password, role, country):
        return {
            'name': name,
            'email': email,
            'password': password,
            'role': role,
            'country': country
        }
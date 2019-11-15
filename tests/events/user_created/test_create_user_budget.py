import json
import unittest

from users_api.app import users_api
from users_api.database import budget_database
from users_api.events.user_created import create_user_budget
from users_api.model.user import User

class TestCreateUserBudget(unittest.TestCase):

    def tearDown(self):
        budget_database.delete()

    def test_budget_is_not_created_for_publishers(self):        
        user = User('Awesome name', 'dummy@email.com', 'dummy-password', User.ROLE_PUBLISHER, 'US')
        create_user_budget(user)
        self.assertEqual(0, len(budget_database.select_all()))

    def test_budget_is_created_for_advertisers(self):
        user = User('Awesome name', 'dummy@email.com', 'dummy-password', User.ROLE_ADVERTISER, 'US')
        create_user_budget(user)
        inserted_budget = budget_database.select_all()
        self.assertEqual(10000, inserted_budget[0]['amount'])
import json
import unittest

from users_api.model.budget import Budget

class TestBudget(unittest.TestCase):

    def test_user_constructor_creates_a_user_properly(self):
        budget = Budget('dummy-user-id', 1000)
        self.assertEqual('dummy-user-id', budget.user_id)
        self.assertEqual(1000, budget.amount)
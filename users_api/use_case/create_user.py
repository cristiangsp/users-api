import pycountry
import uuid

from users_api.database import users_database, budget_database
from users_api.model.user import User
from users_api.model.budget import Budget
from users_api.exception.user import AlreadyExists
from users_api.exception.country import NotValid

class CreateUser:
    def execute(self, name, email, password, role, country):
        if (users_database.select_by('email', email)):
            raise AlreadyExists()

        if not pycountry.countries.get(alpha_2=country):
            raise NotValid()

        user = User(name, email, password, role, country)
        users_database.insert(user.to_dict())

        if user.has_budget():
            budget = Budget(user.id, user.initial_budget())
            budget_database.insert(budget.to_dict())
from users_api.database import budget_database
from users_api.model.budget import Budget

def create_user_budget(user):
    if user.has_budget():
        budget = Budget(user.id, user.initial_budget())
        budget_database.insert(budget.to_dict())
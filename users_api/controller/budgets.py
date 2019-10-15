from flask import Blueprint, jsonify, request
from users_api.database import budget_database

budgets_blueprint = Blueprint('budgets', __name__, url_prefix='/budgets')

@budgets_blueprint.route('', methods=['GET'])
def get_budget_by_user_id():
    budget = budget_database.select_all()
    return jsonify(budget)
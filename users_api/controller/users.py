import pycountry
import re
import uuid

from flask import Blueprint, jsonify, request
from users_api.model.user import User
from users_api.model.budget import Budget
from users_api.database import users_database, budget_database

users_blueprint = Blueprint('users', __name__, url_prefix='/users')

@users_blueprint.route('', methods=['GET'])
def list_users():
    users = users_database.select_all()
    return jsonify(users)

@users_blueprint.route('', methods=['POST'])
def create_user():
    request_info = request.get_json()

    name = request_info['name']

    if (len(name) < 5):
        return "Name cannot be shorter than 5 characters", 400

    password = request_info['password']

    if (len(password) < 8):
        return "Password cannot be shorter than 8 characters", 400

    email = request_info['email']

    if (users_database.select_by('email', email)):
        return "User already exists", 400

    if not re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
        return "Email must be valid", 400

    country = request_info['country']

    if not pycountry.countries.get(alpha_2=country):
        return "Country must be an ISO-3166 valid", 400

    role = request_info['role']

    if not role in ['advertiser', 'publisher']:
        return "Role must be 'advertiser' or 'publisher'", 400

    user = User()
    user.id = str(uuid.uuid4())
    user.name = name
    user.email = email
    user.password = password
    user.role = role
    user.country = country

    users_database.insert(user.to_dict())

    if user.role == 'advertiser':
        budget = Budget()
        budget.id = str(uuid.uuid4())
        budget.user_id = user.id

        user_country = user.country

        if (user_country == 'US'):
            budget.amount = 10000
        else:
            budget.amount = 1000

        budget_database.insert(budget.to_dict())

    return "User registered successfully", 200
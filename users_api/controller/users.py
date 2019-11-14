import pycountry
import re
import uuid

from flask import Blueprint, jsonify, request
from users_api.model.user import User
from users_api.model.budget import Budget
from users_api.database import users_database, budget_database
from users_api.exception.user import NameTooShort, PasswordTooShort, RoleNotValid, EmailNotValid

users_blueprint = Blueprint('users', __name__, url_prefix='/users')

@users_blueprint.route('', methods=['GET'])
def list_users():
    users = users_database.select_all()
    return jsonify(users)

@users_blueprint.route('', methods=['POST'])
def create_user():
    request_info = request.get_json()

    email = request_info['email']

    if (users_database.select_by('email', email)):
        return "User already exists", 400

    country = request_info['country']

    if not pycountry.countries.get(alpha_2=country):
        return "Country must be an ISO-3166 valid", 400

    try:
        user = User(
            request_info['name'],
            email,
            request_info['password'],
            request_info['role'],
            country
        )
    except NameTooShort as ex:
        return ex.message, 400
    except PasswordTooShort as ex:
        return ex.message, 400
    except EmailNotValid as ex:
        return ex.message, 400
    except RoleNotValid as ex:
        return ex.message, 400

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
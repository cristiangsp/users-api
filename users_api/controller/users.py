import pycountry
import re
import uuid

from flask import Blueprint, jsonify, request
from users_api.model.user import User
from users_api.model.budget import Budget
from users_api.database import users_database, budget_database
from users_api.exception.user import NameTooShort, PasswordTooShort, RoleNotValid, EmailNotValid, AlreadyExists
from users_api.exception.country import NotValid
from users_api.use_case.create_user import CreateUser

users_blueprint = Blueprint('users', __name__, url_prefix='/users')

@users_blueprint.route('', methods=['GET'])
def list_users():
    users = users_database.select_all()
    return jsonify(users)

@users_blueprint.route('', methods=['POST'])
def create_user():
    request_info = request.get_json()

    try:
        create_user_use_case = CreateUser()
        create_user_use_case.execute(
            request_info['name'],
            request_info['email'],
            request_info['password'],
            request_info['role'],
            request_info['country']
        )

    except NameTooShort as ex:
        return ex.message, 400
    except PasswordTooShort as ex:
        return ex.message, 400
    except EmailNotValid as ex:
        return ex.message, 400
    except RoleNotValid as ex:
        return ex.message, 400
    except AlreadyExists as ex:
        return ex.message, 400
    except NotValid as ex:
        return ex.message, 400

    return "User registered successfully", 200
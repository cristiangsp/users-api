from flask import Flask
from pubsub import pub
from users_api.events import register_event_listeners
from users_api.controller.users import users_blueprint
from users_api.controller.budgets import budgets_blueprint

users_api = Flask(__name__)
users_api.register_blueprint(users_blueprint)
users_api.register_blueprint(budgets_blueprint)

register_event_listeners()
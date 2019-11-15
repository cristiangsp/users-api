from pubsub import pub
from users_api.events.user_created import create_user_budget

def register_event_listeners():
    pub.subscribe(create_user_budget, "user.created")
import uuid

class Budget:
    def __init__(self, user_id, amount):
        self.id = str(uuid.uuid4())
        self.user_id = user_id
        self.amount = amount

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'amount': self.amount
        }
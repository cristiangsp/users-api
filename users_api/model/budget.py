class Budget:
    def __init__(self):
        self.id = ''
        self.user_id = ''
        self.amount = 0

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'amount': self.amount
        }
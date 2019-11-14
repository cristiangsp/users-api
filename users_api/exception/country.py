class NotValid(Exception):
    def __init__(self):
        self.message = "Country must be an ISO-3166 valid"
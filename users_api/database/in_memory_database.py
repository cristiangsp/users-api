import uuid

class InMemoryDatabase:
    def __init__(self):
        self._storage = []

    def insert(self, record):
        self._storage.append(record)

    def select_by(self, field, value):
        for record in self._storage:
            if field in record.keys():
                if record[field] == value:
                    return record
        return None

    def select_all(self):
        return self._storage

    def delete(self):
        self._storage =[] 
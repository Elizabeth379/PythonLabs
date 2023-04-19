import json


class Container:
    user = str()
    storage = set()
    file = str()

    def __init__(self, _user):
        self.user = _user
        self.file = "container.json"

    def add(self, element):
        self.storage.add(element)

    def remove(self, element):
        self.storage.remove(element)

    def find(self, element):
        if element in self.storage:
            return element

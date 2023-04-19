import json
import re

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

    def list(self):
        for elem in self.storage:
            print(elem)

    def grep(self, regex):
        found_elements = set()
        for elem in self.storage:
            if re.search(regex, elem):
                found_elements.add(elem)

        if found_elements:
            for el in found_elements:
                print(el)

        else:
            print("Matches not found.")

    

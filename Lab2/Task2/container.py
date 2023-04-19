import json
import re


class Container:
    def __init__(self, _user):
        self.user = _user
        self.file = f"{self.user}.json"
        self.storage = set()

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

    def save(self):
        with open(self.file, "w") as f:
            json.dump(list(self.storage), f)

    def load(self):
        try:
            with open(self.file, "r") as f:
                self.storage = set(json.load(f))
        except FileNotFoundError:
            print("File not found.")

    def switch(self, username):
        self.save()
        self.user = username
        self.file = f"{self.user}.json"
        while True:
            ans = input("Do you want to load data? (y/n)")
            if ans == "y":
                self.load()
                break
            elif ans == "n":
                break

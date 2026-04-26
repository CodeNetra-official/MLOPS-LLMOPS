import json


VARIABLE_NAME = "This is a variable in the read module."

def reading_text(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return text

def reading_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
#!/usr/bin/python3
"""A class that serializes instances to a JSON file and deserializes
    JSON file to instances.
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Serializes and deserializes instances."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key
            <obj class name>.id
        """
        key = "{} {}".format(type(self).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            my_dict = {}
            for key, value in FileStorage.__objects.items():
                my_dict[key] = value.to_dict()
            json.dump(my_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects
            Only if it exists
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                for obj in json.load(f).values():
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            return

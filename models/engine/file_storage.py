#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
<<<<<<< HEAD
        """Serializes __objects to the JSON file"""
        my_dt = FileStorage.__objects
        my_dt = {obj: my_dt[obj].to_dict() for obj in my_dt.keys()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(my_dt, f)
=======
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)
>>>>>>> 55f64c734d64f252d10895dd360693fcca6409f1

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
<<<<<<< HEAD
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                for obj in json.load(f).values():
                    self.new(eval(obj["__class__"])(**obj))
=======
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
>>>>>>> 55f64c734d64f252d10895dd360693fcca6409f1
        except FileNotFoundError:
            return

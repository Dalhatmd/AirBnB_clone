#!/usr/bin/python3
"""file_storage
class FileStorage that serializes instances to a
JSON file and deserializes JSON file to instances
"""
import json


class FileStorage:
    """ serializes/deserializes instances from/to a JSON file"""

    def __init__(self):
        """initialize the Store"""
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """return all stored objs"""
        return self.__objects

    def new(self, obj):
        """store obj"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """store to a file"""
        objs = self.__objects
        for key in objs:
            objs[key] = objs[key].to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(objs, f)

    def reload(self):
        """retrieve the data back to work"""
        try:
            with open(self.__file_path) as f:
                from ..base_model import BaseModel
                objs = json.load(f)
                for key, value in objs.items():
                    if value['__class__'] == "BaseModel":
                        objs[key] = BaseModel(**value)
                self.__objects = objs
        except FileNotFoundError:
            pass

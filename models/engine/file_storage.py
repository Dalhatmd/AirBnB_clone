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
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj.to_dict()

    def save(self):
        """store to a file"""
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """retrieve the data back to work"""
        try:
            with open(self.__file_path) as f:
                self.__objects = json.load(f)
        except:
            pass

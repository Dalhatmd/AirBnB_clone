#!/usr/bin/python3
"""file_storage
class FileStorage that serializes instances to a
JSON file and deserializes JSON file to instances
"""
import json
from datetime import datetime


class FileStorage:
    """ serializes/deserializes instances from/to a JSON file"""

    # __exist_classes = ["BaseModel", "User"]

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

    def save(self, store=None):
        """store to a file"""
        objs = (store.copy() if store else None) or self.__objects.copy()
        for key in objs:
            objs[key] = objs[key].to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(objs, f)

    def reload(self):
        """retrieve the data back to work"""
        try:
            with open(self.__file_path) as f:
                from ..base_model import BaseModel
                from ..user import User
                objs = json.load(f)
                for key, value in objs.items():
                    # TODO: enhancement by using dicts=> dict["Model"]()
                    match value['__class__']:
                        case "BaseModel":
                            objs[key] = BaseModel(**value)
                        case "User":
                            objs[key] = User(**value)
                        case "Amenity":
                            from ..amenity import Amenity
                            objs[key] = Amenity(**value)
                        case "City":
                            from ..city import City
                            objs[key] = City(**value)
                        case "State":
                            from ..state import State
                            objs[key] = State(**value)
                        case "Place":
                            from ..place import Place
                            objs[key] = Place(**value)
                        case "Review":
                            from ..review import Review
                            objs[key] = Review(**value)
                self.__objects = objs
        except FileNotFoundError:
            pass

    def attributes(self):
        """ returns the attributes a class should have. Useful for tests"""
        attributes = {
                "BaseModel" :
                { "id" : str,
                 "created_at" : datetime,
                 "updated_at" : datetime},
                "User" :
                { "email" : str,
                 "password" : str,
                 "first_name" : str,
                 "last_name" : str}
                }
        return attributes


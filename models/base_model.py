#!/usr/bin/python3
""" A module for the base model class """
import uuid
from datetime import datetime
from . import storage


class BaseModel:
    """ Base Model blueprint """

    def __init__(self, *args, **kwargs):
        """ initialiser for BaseModel """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k != '__class__':
                    if k == "created_at" or k == "updated_at":
                        self.__dict__[k] = datetime.strptime(v, tform)
                    else:
                        self.__dict__[k] = v
        else:
            storage.new(self)

    def __str__(self):
        """ Prints a string representation of the class """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ Updates the updated_at value """
        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        """ Returns a dictionary representation of the class """
        dict_repr = self.__dict__.copy()
        dict_repr["created_at"] = self.created_at.isoformat()
        dict_repr["updated_at"] = self.updated_at.isoformat()
        dict_repr["__class__"] = self.__class__.__name__
        return dict_repr

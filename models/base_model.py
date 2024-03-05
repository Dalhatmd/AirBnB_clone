#!/usr/bin/python3
""" A module for the base model class """
import uuid
from datetime import datetime
from . import storage


class BaseModel:
    """ Base Model blueprint """

    def __init__(self, *args, **kwargs):
        """ initialiser for BaseModel """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == 'created_at':
                    self.created_at = datetime.fromisoformat(value)
                elif key == 'updated_at':
                    self.updated_at = datetime.fromisoformat(value)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ Prints a string representation of the class """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ Updates the updated_at value """
        storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Returns a dictionary representation of the class """
        class_dict = self.__dict__.copy()
        class_dict["__class__"] = __class__.__name__
        if hasattr(self, "created_at"):
            class_dict["created_at"] = self.created_at.isoformat()
        if hasattr(self, "updated_at"):
            class_dict["updated_at"] = self.updated_at.isoformat()

        return class_dict

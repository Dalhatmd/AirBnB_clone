#!/usr/bin/python3
""" Unittest for User class """
import unittest
from models.user import User
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
from models import storage


class TestUser(unittest.TestCase):
    """ Unittest class for user class """

    def setUp(self):
        """ sets up test cases """
        pass


    def test_unique(self):
        """ Test all users are unique"""
        u1 = User()
        u2 = User()
        self.assertNotEqual(u1, u2)
        self.assertNotEqual(u1.id, u2.id)

    def test_instant(self):
        """test instantiation is User and subclass of BaseModel"""
        b = User()
        self.assertIsInstance(b, User)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_attributes(self):
        """ Tests for valid attrubutes """
        attributes = storage.attributes()["User"]
        u = User()
        for key, value in attributes.items():
            self.assertTrue(hasattr(u, key))
            self.assertEqual(type(getattr(u, key, None)), value)


if __name__ == "__main__":
    unittest.main()

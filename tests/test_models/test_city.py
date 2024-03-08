#!/usr/bin/python3
""" Test suite for city class"""
import unittest
from models import storage
from datetime import datetime
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """ class for testing city class """

    def setup(self):
        """ set up """
        pass

    def test_instant(self):
        """ Test for instantiation """
        c = City()
        self.assertIsInstance(c, City)
        self.assertTrue(issubclass(type(c), BaseModel))

    def test_attributes(self):
        """ Test all attributes exist and are correct format"""
        attributes = storage.attributes()["City"]
        c = City()
        for key, value in attributes.items():
            self.assertTrue(hasattr(c, key))
            self.assertEqual(type(getattr(c, key, None)), value)


if __name__ == "__main__":
    unittest.main()

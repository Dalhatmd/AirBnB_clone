""" Teat suite for amenity class """
import unittest
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """ Class for testing amenity """

    def test_instant(self):
        """ Test for instantiation """
        a = Amenity()
        self.assertIsInstance(a, Amenity)
        self.assertTrue(issubclass(type(a), BaseModel))

    def test_attributes(self):
        """ Test all attributes exist amd are correct format"""
        attributes = storage.attributes()["Amenity"]
        a = Amenity()
        for key, value in attributes.items():
            self.assertTrue(hasattr(a, key))
            self.assertEqual(type(getattr(a, key, None)), value)

if __name__ == "__main__":
    unittest.main()

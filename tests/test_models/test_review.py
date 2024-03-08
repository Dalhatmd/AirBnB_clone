""" Test suite for review class """
import unittest
from models import storage
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """ Class for testing review """

    def test_instant(self):
        """ Test for instantiation """
        r = Review()
        self.assertIsInstance(r, Review)
        self.assertTrue(issubclass(type(r), BaseModel))

    def test_attributes(self):
        """ Test all attributes exist and are correct format"""
        attributes = storage.attributes()["Review"]
        r = Review()
        for key, value in attributes.items():
            self.assertTrue(hasattr(r, key))
            self.assertEqual(type(getattr(r, key, None)), value)

if __name__ == "__main__":
    unittest.main()

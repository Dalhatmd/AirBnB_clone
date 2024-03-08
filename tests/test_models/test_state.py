""" Unitteat for state Class """
import unittest
from models.state import State
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestState(unittest.TestCase):
    """ Test cases for State"""

    def setup(self):
        """ set up"""
        pass

    def test_instant(self):
        """ Test instantiation """
        s = State()
        self.assertIsInstance(s, State)
        self.assertTrue(issubclass(type(s), BaseModel))

    def test_attributes(self):
        """ Test for valid attributes """
        attributes = storage.attributes()["State"]
        s = State()
        for key, value in attributes.items():
            self.assertTrue(hasattr(s, key))
            self.assertEqual(type(getattr(s, key, None)), value)

if __name__ == "__main__":
    unittest.main()

"""Testing State Module """
import unittest
from models.state import State
from datetime import datetime


class TestState(unittest.TestCase):
    """Test cases for the State class"""

    def setUp(self):
        """Set up a State instance for testing"""
        self.state = State()

    def test_instance_creation(self):
        """Test if a State instance is created successfully"""
        self.assertIsInstance(self.state, State)

    def test_inherited_attributes(self):
        """Test if State inherits required attributes from BaseModel"""
        self.assertTrue(hasattr(self.state, 'id'))
        self.assertTrue(hasattr(self.state, 'created_at'))
        self.assertTrue(hasattr(self.state, 'updated_at'))

    def test_custom_attributes(self):
        """Test if State has custom attributes"""
        attributes = ['name']
        for attribute in attributes:
            self.assertTrue(hasattr(self.state, attribute))

    def test_default_values(self):
        """Test if custom attributes have default values"""
        self.assertEqual(self.state.name, "")

    def test_str_method(self):
        """Test the string representation of the State instance"""
        string_representation = str(self.state)
        self.assertIn("[State]", string_representation)
        self.assertIn("id", string_representation)
        self.assertIn("created_at", string_representation)
        self.assertIn("updated_at", string_representation)

    def test_save_method(self):
        """Test if save method updates the 'updated_at' attribute"""
        original_created_at = self.state.created_at
        self.state.save()
        self.assertNotEqual(original_created_at, self.state.updated_at)

    def test_to_dict_method(self):
        """Test if to_dict method returns a\
        dictionary with the expected keys"""
        dict_representation = self.state.to_dict()
        self.assertIsInstance(dict_representation, dict)
        self.assertIn("__class__", dict_representation)
        self.assertEqual(dict_representation["__class__"], "State")
        self.assertIn("id", dict_representation)
        self.assertIn("created_at", dict_representation)
        self.assertIn("updated_at", dict_representation)

    def test_datetime_attributes(self):
        """Test if 'created_at' and\
            'updated_at' attributes are datetime objects"""
        self.assertIsInstance(self.state.created_at, datetime)
        self.assertIsInstance(self.state.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()

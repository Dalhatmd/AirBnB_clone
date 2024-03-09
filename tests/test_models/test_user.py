"""Testing User Model"""
import unittest
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):
    """Test cases for the User class"""

    def setUp(self):
        """Set up a User instance for testing"""
        self.user = User()

    def test_instance_creation(self):
        """Test if a User instance is created successfully"""
        self.assertIsInstance(self.user, User)

    def test_inherited_attributes(self):
        """Test if User inherits required attributes from BaseModel"""
        self.assertTrue(hasattr(self.user, 'id'))
        self.assertTrue(hasattr(self.user, 'created_at'))
        self.assertTrue(hasattr(self.user, 'updated_at'))

    def test_custom_attributes(self):
        """Test if User has custom attributes"""
        attributes = ['email', 'password', 'first_name', 'last_name']
        for attribute in attributes:
            self.assertTrue(hasattr(self.user, attribute))

    def test_default_values(self):
        """Test if custom attributes have default values"""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_str_method(self):
        """Test the string representation of the User instance"""
        string_representation = str(self.user)
        self.assertIn("[User]", string_representation)
        self.assertIn("id", string_representation)
        self.assertIn("created_at", string_representation)
        self.assertIn("updated_at", string_representation)

    def test_save_method(self):
        """Test if save method updates the 'updated_at' attribute"""
        original_created_at = self.user.created_at
        self.user.save()
        self.assertNotEqual(original_created_at, self.user.updated_at)

    def test_to_dict_method(self):
        """Test if to_dict method returns a\
            dictionary with the expected keys"""
        dict_representation = self.user.to_dict()
        self.assertIsInstance(dict_representation, dict)
        self.assertIn("__class__", dict_representation)
        self.assertEqual(dict_representation["__class__"], "User")
        self.assertIn("id", dict_representation)
        self.assertIn("created_at", dict_representation)
        self.assertIn("updated_at", dict_representation)

    def test_datetime_attributes(self):
        """Test if 'created_at' and 'updated_at'\
            attributes are datetime objects"""
        self.assertIsInstance(self.user.created_at, datetime)
        self.assertIsInstance(self.user.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()

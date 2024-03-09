""" Testing the City Module """
import unittest
from models.city import City
from datetime import datetime


class TestCity(unittest.TestCase):
    """Test cases for the City class"""

    def setUp(self):
        """Set up a City instance for testing"""
        self.city = City()

    def test_instance_creation(self):
        """Test if a City instance is created successfully"""
        self.assertIsInstance(self.city, City)

    def test_inherited_attributes(self):
        """Test if City inherits required attributes from BaseModel"""
        self.assertTrue(hasattr(self.city, 'id'))
        self.assertTrue(hasattr(self.city, 'created_at'))
        self.assertTrue(hasattr(self.city, 'updated_at'))

    def test_custom_attributes(self):
        """Test if City has custom attributes (name, state_id)"""
        self.assertTrue(hasattr(self.city, 'name'))
        self.assertTrue(hasattr(self.city, 'state_id'))

    def test_default_values(self):
        """Test if custom attributes have default values"""
        self.assertEqual(self.city.name, "")
        self.assertEqual(self.city.state_id, "")

    def test_str_method(self):
        """Test the string representation of the City instance"""
        string_representation = str(self.city)
        self.assertIn("[City]", string_representation)
        self.assertIn("id", string_representation)
        self.assertIn("created_at", string_representation)
        self.assertIn("updated_at", string_representation)

    def test_save_method(self):
        """Test if save method updates the 'updated_at' attribute"""
        original_created_at = self.city.created_at
        self.city.save()
        self.assertNotEqual(original_created_at, self.city.updated_at)

    def test_to_dict_method(self):
        """Test if to_dict method returns a\
            dictionary with the expected keys"""
        dict_representation = self.city.to_dict()
        self.assertIsInstance(dict_representation, dict)
        self.assertIn("__class__", dict_representation)
        self.assertEqual(dict_representation["__class__"], "City")
        self.assertIn("id", dict_representation)
        self.assertIn("created_at", dict_representation)
        self.assertIn("updated_at", dict_representation)

    def test_datetime_attributes(self):
        """Test if 'created_at' and 'updated_at'\
            attributes are datetime objects"""
        self.assertIsInstance(self.city.created_at, datetime)
        self.assertIsInstance(self.city.updated_at, datetime)

    def test_attribute_types(self):
        """Test if custom attribute types are as expected"""
        self.assertIsInstance(self.city.name, str)
        self.assertIsInstance(self.city.state_id, str)

    def test_attribute_update(self):
        """Test if custom attributes can be updated and changes are saved"""
        original_name = self.city.name
        self.city.name = "New City Name"
        self.assertNotEqual(original_name, "New City Name")
        self.city.save()
        new_city = City(**self.city.to_dict())
        self.assertEqual(new_city.name, "New City Name")


if __name__ == "__main__":
    unittest.main()

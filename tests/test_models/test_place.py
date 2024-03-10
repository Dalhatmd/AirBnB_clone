"""Testing the place Module """
import unittest
from models.place import Place
from datetime import datetime


class TestPlace(unittest.TestCase):
    """Test cases for the Place class"""

    def setUp(self):
        """Set up a Place instance for testing"""
        self.place = Place()

    def test_instance_creation(self):
        """Test if a Place instance is created successfully"""
        self.assertIsInstance(self.place, Place)

    def test_inherited_attributes(self):
        """Test if Place inherits required attributes from BaseModel"""
        self.assertTrue(hasattr(self.place, 'id'))
        self.assertTrue(hasattr(self.place, 'created_at'))
        self.assertTrue(hasattr(self.place, 'updated_at'))

    def test_custom_attributes(self):
        """Test if Place has custom attributes"""
        attributes = [
            'name', 'amenity_ids', 'longitude', 'latitude',
            'price_by_night', 'max_guest', 'number_bathrooms',
            'number_rooms', 'description', 'city_id', 'user_id'
        ]
        for attribute in attributes:
            self.assertTrue(hasattr(self.place, attribute))

    def test_default_values(self):
        """Test if custom attributes have default values"""
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.amenity_ids, [])
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")

    def test_str_method(self):
        """Test the string representation of the Place instance"""
        string_representation = str(self.place)
        self.assertIn("[Place]", string_representation)
        self.assertIn("id", string_representation)
        self.assertIn("created_at", string_representation)
        self.assertIn("updated_at", string_representation)

    def test_save_method(self):
        """Test if save method updates the 'updated_at' attribute"""
        original_created_at = self.place.created_at
        self.place.save()
        self.assertNotEqual(original_created_at, self.place.updated_at)

    def test_to_dict_method(self):
        """Test if to_dict method returns\
            a dictionary with the expected keys"""
        dict_representation = self.place.to_dict()
        self.assertIsInstance(dict_representation, dict)
        self.assertIn("__class__", dict_representation)
        self.assertEqual(dict_representation["__class__"], "Place")
        self.assertIn("id", dict_representation)
        self.assertIn("created_at", dict_representation)
        self.assertIn("updated_at", dict_representation)

    def test_datetime_attributes(self):
        """Test if 'created_at' and\
            'updated_at' attributes are datetime objects"""
        self.assertIsInstance(self.place.created_at, datetime)
        self.assertIsInstance(self.place.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()

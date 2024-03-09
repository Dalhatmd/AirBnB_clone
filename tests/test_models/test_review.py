"""Testing Review Module"""
import unittest
from models.review import Review
from datetime import datetime


class TestReview(unittest.TestCase):
    """Test cases for the Review class"""

    def setUp(self):
        """Set up a Review instance for testing"""
        self.review = Review()

    def test_instance_creation(self):
        """Test if a Review instance is created successfully"""
        self.assertIsInstance(self.review, Review)

    def test_inherited_attributes(self):
        """Test if Review inherits required attributes from BaseModel"""
        self.assertTrue(hasattr(self.review, 'id'))
        self.assertTrue(hasattr(self.review, 'created_at'))
        self.assertTrue(hasattr(self.review, 'updated_at'))

    def test_custom_attributes(self):
        """Test if Review has custom attributes"""
        attributes = ['place_id', 'user_id', 'text']
        for attribute in attributes:
            self.assertTrue(hasattr(self.review, attribute))

    def test_default_values(self):
        """Test if custom attributes have default values"""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_str_method(self):
        """Test the string representation of the Review instance"""
        string_representation = str(self.review)
        self.assertIn("[Review]", string_representation)
        self.assertIn("id", string_representation)
        self.assertIn("created_at", string_representation)
        self.assertIn("updated_at", string_representation)

    def test_save_method(self):
        """Test if save method updates the 'updated_at' attribute"""
        original_created_at = self.review.created_at
        self.review.save()
        self.assertNotEqual(original_created_at, self.review.updated_at)

    def test_to_dict_method(self):
        """Test if to_dict method returns\
            a dictionary with the expected keys"""
        dict_representation = self.review.to_dict()
        self.assertIsInstance(dict_representation, dict)
        self.assertIn("__class__", dict_representation)
        self.assertEqual(dict_representation["__class__"], "Review")
        self.assertIn("id", dict_representation)
        self.assertIn("created_at", dict_representation)
        self.assertIn("updated_at", dict_representation)

    def test_datetime_attributes(self):
        """Test if 'created_at' and 'updated_at'\
            attributes are datetime objects"""
        self.assertIsInstance(self.review.created_at, datetime)
        self.assertIsInstance(self.review.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()

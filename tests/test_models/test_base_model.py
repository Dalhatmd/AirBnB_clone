#!/usr/bin/python3
'''Module for Base unit tests.'''
from tarfile import data_filter
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test for the Base Clss"""

    def test_not_equal(self):
        b1 = BaseModel()
        b2 = BaseModel()

        self.assertNotEqual(b1, b2)
        self.assertNotEqual(b1.id, b2.id)

    def test_id_string(self):
        b1 = BaseModel()
        self.assertIsInstance(b1.id, str)

    def test_date_string(self):
        b1 = BaseModel()
        self.assertIsInstance(b1.created_at, datetime)
        self.assertIsInstance(b1.updated_at, datetime)

    def test_dict(self):
        b1 = BaseModel()
        b1_dict = b1.to_dict()
        self.assertIsInstance(b1_dict, dict)

    def test_save(self):
        b1 = BaseModel()
        first_time = b1.created_at
        b1.save()
        second_time = b1.updated_at
        self.assertNotEqual(first_time, second_time)

    def test_attr_class(self):
        b1 = BaseModel()
        b1_dict = b1.to_dict()
        self.assertIn("__class__", b1_dict)

    # Testing 4ht Task requirments
    def setUp(self):
        """before each"""
        self.base_model = BaseModel()

    def test_recreate_instance_from_dict_with_attributes(self):
        """recreate_instance_from_dict_with_attributes"""
        original_instance = BaseModel(attr1="value1", attr2="value2")
        dict_representation = original_instance.to_dict()
        recreated_instance = BaseModel(**dict_representation)
        self.assertEqual(original_instance.__dict__, recreated_instance.__dict__)

    def test_recreate_instance_from_dict_with_custom_attributes(self):
        """recreate_instance_from_dict_with_custom_attributes"""
        original_instance = BaseModel(custom_attr="test")
        dict_representation = original_instance.to_dict()
        recreated_instance = BaseModel(**dict_representation)
        self.assertEqual(original_instance.custom_attr, recreated_instance.custom_attr)

    def test_recreate_instance_from_dict_empty_created_at_updated_at(self):
        """recreate_instance_from_dict_empty_created_at_updated_at"""
        original_instance = BaseModel()
        dict_representation = original_instance.to_dict()
        recreated_instance = BaseModel(**dict_representation)
        self.assertEqual(original_instance.id, recreated_instance.id)

    def test_recreate_instance_from_dict_with_additional_attributes(self):
        """instance_from_dict_with_additional_attributes"""
        original_instance = BaseModel(extra_attr="additional_value")
        dict_representation = original_instance.to_dict()
        recreated_instance = BaseModel(**dict_representation)
        self.assertEqual(original_instance.__dict__, recreated_instance.__dict__)


if __name__ == "__main__":
    unittest.main()

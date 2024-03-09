""" Teat suite for amenity class """
import unittest
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """ Class for testing amenity """

    def setUp(self):
        """ Set up a clean environment before each test """
        storage.reload()

    def test_instant(self):
        """ Test for instantiation """
        a = Amenity()
        self.assertIsInstance(a, Amenity)
        self.assertTrue(issubclass(type(a), BaseModel))

    def test_amenity_attributes(self):
        """ Test if Amenity has the required attributes """
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))
        self.assertTrue(hasattr(amenity, 'name'))

    def test_amenity_id_type(self):
        """ Test if the id attribute of Amenity is of type string """
        amenity = Amenity()
        self.assertIsInstance(amenity.id, str)

    def test_amenity_datetime_attributes(self):
        """ Test if created_at and updated_at of Amenity\
            are datetime objects """
        amenity = Amenity()
        self.assertIsInstance(amenity.created_at, datetime)
        self.assertIsInstance(amenity.updated_at, datetime)

    def test_amenity_save_method(self):
        """ Test if the save method updates the updated_at attribute """
        amenity = Amenity()
        first_time = amenity.updated_at
        amenity.save()
        second_time = amenity.updated_at
        self.assertNotEqual(first_time, second_time)

    def test_amenity_to_dict_method(self):
        """ Test if the to_dict method returns a dictionary representation """
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)

    def test_amenity_dict_contains_class_attribute(self):
        """ Test if the to_dict method includes the __class__ attribute """
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertIn('__class__', amenity_dict)

    def test_amenity_reload_method(self):
        """ Test if the reload method retrieves data back from the file """
        amenity = Amenity()
        amenity.save()
        new_storage = storage
        new_storage.reload()
        reloaded_objects = new_storage.all()
        self.assertIn(f"{amenity.__class__.__name__}.{amenity.id}",
                      reloaded_objects)

    def test_amenity_attributes_after_reload(self):
        """ Test if the attributes of Amenity remain the same after reload """
        amenity = Amenity()
        amenity.save()
        new_storage = storage
        new_storage.reload()
        reloaded_objects = new_storage.all()
        reloaded_amenity = reloaded_objects[
            f"{amenity.__class__.__name__}.{amenity.id}"
            ]
        self.assertEqual(amenity.id, reloaded_amenity.id)
        self.assertEqual(amenity.created_at, reloaded_amenity.created_at)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
""" Testing FileStorage Class """
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import json


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """before each
        Create an instance of FileStorage
        """
        self.storage = FileStorage()

    def tearDown(self):
        """after each
        Delete the file created during tests
        """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_default_attributes(self):
        """Test if the default attributes are initialized correctly"""
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")
        self.assertEqual(self.storage._FileStorage__objects, {})

    def test_new_method(self):
        """Test the new method to add an object to the storage"""
        obj = BaseModel()
        self.storage.new(obj)
        self.assertIn(f"{obj.__class__.__name__}.{obj.id}", self.storage.all())

    def test_save_method(self):
        """Test the save method to store objects in the file"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        """Check if the file is created and contains the serialized object"""
        with open("file.json", "r") as f:
            data = json.load(f)
            self.assertIn(f"{obj.__class__.__name__}.{obj.id}", data)

    def test_reload_method(self):
        """Test the reload method to retrieve data back from the file"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        """Create a new instance of FileStorage and reload data"""
        new_storage = FileStorage()
        new_storage.reload()

        """Check if the reloaded data matches the original object"""
        reloaded_objects = new_storage.all()
        self.assertIn(f"{obj.__class__.__name__}.{obj.id}", reloaded_objects)
        reloaded_obj = reloaded_objects[f"{obj.__class__.__name__}.{obj.id}"]
        self.assertIsInstance(reloaded_obj, BaseModel)
        self.assertEqual(obj.id, reloaded_obj.id)
        self.assertEqual(obj.created_at, reloaded_obj.created_at)

    def test_reload_method_with_nonexistent_file(self):
        """Test reload method when the file does not exist"""
        self.storage.reload()
        # It should not raise an exception, and the storage should remain empty
        self.assertEqual(self.storage.all(), {})


if __name__ == "__main__":
    unittest.main()

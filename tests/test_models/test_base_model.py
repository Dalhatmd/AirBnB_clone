import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

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
        self.assertIsInstance(b1.created_at, str)
        self.assertIsInstance(b1.updated_at, str)

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

if __name__ == "__main__":
    unittest.main()

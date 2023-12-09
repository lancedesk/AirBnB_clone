#!/usr/bin/python3
"""
BaseModel tests
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
from uuid import UUID
from unittest.mock import patch


class TestBaseModel(unittest.TestCase):
    """
    Unit tests for the BaseModel class.
    """
    def test_str_representation(self):
        """
        Tests the string representation of the object.
        """
        obj = BaseModel()
        str_representation = str(obj)
        self.assertTrue("[BaseModel]" in str_representation)
        self.assertTrue(obj.id in str_representation)
        self.assertTrue(str(obj.__dict__) in str_representation)

    def test_save_updates_updated_at(self):
        """
        Tests if calling save updates the updated_at attribute.
        """
        obj = BaseModel()
        initial_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(obj.updated_at, initial_updated_at)

    def test_to_dict_method(self):
        """
        Tests the to_dict method of the BaseModel class.
        """
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIn("__class__", obj_dict)
        self.assertEqual(obj_dict["__class__"], "BaseModel")
        self.assertIn("id", obj_dict)
        self.assertEqual(obj_dict["id"], obj.id)
        self.assertIn("created_at", obj_dict)
        self.assertEqual(obj_dict["created_at"], obj.created_at.isoformat())
        self.assertIn("updated_at", obj_dict)
        self.assertEqual(obj_dict["updated_at"], obj.updated_at.isoformat())

    def test_initialization_with_dict(self):
        """
        Tests initializing a new object from a dictionary.
        """
        obj = BaseModel()
        obj_dict = obj.to_dict()
        new_obj = BaseModel(**obj_dict)
        self.assertEqual(obj.id, new_obj.id)
        self.assertEqual(obj.created_at, new_obj.created_at)
        self.assertEqual(obj.updated_at, new_obj.updated_at)

    def test_unique_ids(self):
        """
        Tests that the IDs generated for different objects are unique.
        """
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_created_at_and_updated_at_types(self):
        """
        Tests the types of created_at and updated_at attributes.
        """
        obj = BaseModel()
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_created_at_before_updated_at(self):
        """
        Tests if created_at is before or equal to updated_at.
        """
        obj = BaseModel()
        self.assertLessEqual(obj.created_at, obj.updated_at)

if __name__ == "__main__":
    unittest.main()

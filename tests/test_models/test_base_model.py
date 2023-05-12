#!/usr/bin/python3
"""Defines unittests for models/base_model.py."""
import unittest
from datetime import datetime
from models.base_model import BaseModel
import models
import os
from time import sleep


class TestBaseModel(unittest.TestCase):
    """Unittest Cases for the BaseModel class."""
    def test_instantiation(self):
        """Tests instantiation of BaseModel class."""
        b = BaseModel()
        self.assertIsInstance(b, BaseModel)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_unique_ids(self):
        """Tests for unique user ids."""
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_id_is_str(self):
        """Tests that id generated is a str"""
        b = BaseModel()
        self.assertTrue(type(b.id) is str)

    def test_created_at_is_datetime(self):
        """Tests created_at attribute is a datetime object."""
        b = BaseModel()
        self.assertTrue(type(b.created_at) is datetime)

    def test_updated_at_is_datetime(self):
        """Tests updated_at attribute is a datetime object."""
        b = BaseModel()
        self.assertTrue(type(b.updated_at) is datetime)

    def test_two_different_models_created_at(self):
        """Tests two models created are different."""
        b1 = BaseModel()
        sleep(0.03)
        b2 = BaseModel()
        self.assertLess(b1.created_at, b2.created_at)

    def test_unused_args(self):
        """Tests when the args attribute is not used."""
        b = BaseModel(None)
        self.assertNotIn(None, b.__dict__.values())

    def test_instantiation_with_args_and_kwargs(self):
        """Tests instantiation with kwargs, ignore args."""
        dt = datetime.now()
        dt_iso = dt.isoformat()
        b = BaseModel('1985', id='31', created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(b.id, '31')
        self.assertEqual(b.created_at, dt)
        self.assertEqual(b.updated_at, dt)

    def test_with_None_kwargs(self):
        """Tests when kwargs is None."""
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_str_representation(self):
        """Tests if the string representation is correct."""
        b = BaseModel()
        self.assertEqual(str(b),
                         "[BaseModel] ({}) {}".format(b.id, b.__dict__))


class TestBaseModel_save(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""
    def test_one_save(self):
        """Tests the save() method."""
        b = BaseModel()
        sleep(0.03)
        temp_updated_at = b.updated_at
        b.save()
        self.assertLess(temp_updated_at, b.updated_at)

    def test_two_saves(self):
        """Tests save() twice."""
        b = BaseModel()
        sleep(0.03)
        first_updated_at = b.updated_at
        b.save()
        second_updated_at = b.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.03)
        b.save()
        self.assertLess(second_updated_at, b.updated_at)

    def test_save_with_arg(self):
        """Tests that a TypeError is raised when an argument is passed."""
        b = BaseModel()
        with self.assertRaises(TypeError):
            b.save(None)


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the BaseModel class."""
    def test_to_dict_type(self):
        b = BaseModel()
        self.assertTrue(type(b.to_dict()), dict)

    def test_to_dict_has_correct_keys(self):
        """Tests if to_dict() returns correct keys."""
        b_dict = BaseModel().to_dict()
        keys = ('id', 'created_at', 'updated_at', '__class__')
        for key in keys:
            self.assertIn(key, b_dict)

    def test_to_dict_has_added_attributes(self):
        """Tests if to_dict() returns added attributes."""
        b = BaseModel()
        b.name = "Cynthia"
        b.star = "Aries"
        self.assertIn("name", b.to_dict())
        self.assertIn("star", b.to_dict())

    def test_to_dict_with_arg(self):
        """Tests when an argument is passed."""
        b = BaseModel()
        with self.assertRaises(TypeError):
            b.to_dict(None)

    def test_to_dict_output(self):
        """Tests the output of the to_dict method."""
        dt = datetime.now()
        b = BaseModel()
        b.id = '45678'
        b.created_at = b.updated_at = dt
        my_dict = {
                'id': '45678',
                '__class__': 'BaseModel',
                'created_at': dt.isoformat(),
                'updated_at': dt.isoformat()
        }
        self.assertDictEqual(my_dict, b.to_dict())

    def test_to_dict_datetime_attributes_are_str(self):
        """Tests that the attributes are strings."""
        b = BaseModel()
        b_dict = b.to_dict()
        self.assertEqual(type(b_dict['created_at']), str)
        self.assertEqual(type(b_dict['updated_at']), str)


if __name__ == "__main__":
    unittest.main()

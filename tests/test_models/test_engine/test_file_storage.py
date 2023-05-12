#!/usr/bin/python3
"""Unittests for filestorage file"""
import models
from models import base_model
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def test_init_without_arg(self):
        """Tests initialization without args"""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_init_with_arg(self):
        """Tests initialization with args"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_storage_initialization(self):
        """Tests storage created in __init__.py"""
        self.assertEqual(type(models.storage), FileStorage)

    def test_file_path_is_a_private_class(self):
        """Tests if the file_path is a private class attribute"""
        self.assertFalse(hasattr(FileStorage(), "__file_path"))

    def test_objects_is_a_private_class(self):
        """Tests if the objects attribute is a private class attribute"""
        self.assertFalse(hasattr(FileStorage(), "__objects"))


class TestFileStorage_methods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""
    @classmethod
    def setUp(self):
        """Execute before testing occurs"""
        try:
            os.rename("file.json", "temp.json")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        """Executes after tests are executed"""
        try:
            os.rename("temp.json", "file.json")
        except IOError:
            pass

        FileStorage._FileStorage__objects = {}

    def test_all(self):
        """Tests the all() method"""
        self.assertEqual(type(models.storage.all()), dict)

    def test_all_with_arg(self):
        """Tests the all() method when an argument is passed"""
        with self.assertRaises(TypeError):
            models.storage.all(None)


if __name__ == '__main__':
    unittest.main()

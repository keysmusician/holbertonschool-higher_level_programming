#!/usr/bin/python3
"""
Unit tests for Base class.

"""
import unittest
import pep8
from models.base import Base


class TestBase(unittest.TestCase):
    """Test Base class."""

    def test_id(self):
        """Test Base init"""
        b1 = Base()
        self.assertIsInstance(b1, Base)
        self.assertEqual(b1.id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base().id, 3)
        self.assertEqual(Base(98).id, 98)
        self.assertEqual(Base().id, 4)
        self.assertEqual(Base(None).id, 5)
        self.assertEqual(Base("string").id, "string")

    def test_pep8(self):
        """Test PEP8."""
        files = ["models/base.py", "tests/test_models/test_base.py"]
        style = pep8.StyleGuide(quiet=False)
        errors = style.check_files(files).total_errors
        self.assertEqual(errors, 0, "PEP8")

    def test_init_inval_args(self):
        """Test invalid arguments."""
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_to_json_string(self):
        string = Base.to_json_string([])
        self.assertEqual(string, "[]")

        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_from_json_string(self):
        l = Base.from_json_string("[]")
        self.assertEqual(l, [])

        with self.assertRaises(TypeError):
            Base.from_json_string()

if __name__ == '__main__':
    unittest.main()
    from ...models.base import Base

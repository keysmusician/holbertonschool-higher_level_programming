#!/usr/bin/python3
"""
Unit tests for Rectangle class.

"""
import unittest
import pep8
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test Rectangle class."""

    def test_init(self):
        """Test Rectangle init."""
        Rectangle._Base__nb_objects = 0
        # Expected usage
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 4)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 4)
        self.assertEqual(r3.y, 0)
        self.assertEqual(r3.id, 3)

        r4 = Rectangle(10, 2, 4, 7)
        self.assertEqual(r4.width, 10)
        self.assertEqual(r4.height, 2)
        self.assertEqual(r4.x, 4)
        self.assertEqual(r4.y, 7)
        self.assertEqual(r4.id, 4)

        r5 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r5.width, 10)
        self.assertEqual(r5.height, 2)
        self.assertEqual(r5.x, 0)
        self.assertEqual(r5.y, 0)
        self.assertEqual(r5.id, 12)

        # Bad number of arguments
        with self.assertRaises(TypeError):
            Rectangle()

        with self.assertRaises(TypeError):
            Rectangle(1)

        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

        # Bad argument values
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

        with self.assertRaises(ValueError):
            Rectangle(1, 0)

        with self.assertRaises(ValueError):
            Rectangle(1, -2)

        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

        # Bad argument types
        with self.assertRaises(TypeError):
            Rectangle("", 2)

        with self.assertRaises(TypeError):
            Rectangle(1, "")

        with self.assertRaises(TypeError):
            Rectangle(1, 2, "")

        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "")

    def test_area(self):
        """Test area."""
        area1 = Rectangle(1, 1).area()
        self.assertEqual(area1, 1)

        area2 = Rectangle(5, 6).area()
        self.assertEqual(area2, 30)

        # Bad argument count
        with self.assertRaises(TypeError):
            Rectangle(1, 1).area(1)

    def test_display(self):
        """Test display."""
        r = Rectangle(1, 1)
        self.assertEqual(r.display(), "#\n")

        r = Rectangle(1, 1, 1)
        self.assertEqual(r.display(), " #\n")

        r = Rectangle(1, 1, 1, 1)
        self.assertEqual(r.display(), "\n #\n")

        # Bad argument count
        with self.assertRaises(TypeError):
            area1 = r.display(1)

    def test_str(self):
        """Test __str__."""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.__str__(), "[Rectangle] (5) 3/4 - 1/2")

        # Bad argument count
        with self.assertRaises(TypeError):
            area1 = r.__str__(1)

    def test_update_args(self):
        """Test update args."""
        r = Rectangle(10, 10, 10, 10)

        r.update(89)
        self.assertEqual(r.id, 89)

        r.update(89, 2)
        self.assertEqual(r.width, 2)

        r.update(89, 2, 3)
        self.assertEqual(r.height, 3)

        r.update(89, 2, 3, 4)
        self.assertEqual(r.x, 4)

        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.y, 5)

        with self.assertRaises(IndexError):
            r.update(89, 2, 3, 4, 5, 6)

    def test_update_kwargs(self):
        """Test update kwargs."""
        r = Rectangle(10, 10, 10, 10)

        r.update(id=100)
        self.assertEqual(r.id, 100)

        r.update(width=101)
        self.assertEqual(r.width, 101)

        r.update(height=102)
        self.assertEqual(r.height, 102)

        r.update(x=103)
        self.assertEqual(r.x, 103)

        r.update(y=104)
        self.assertEqual(r.y, 104)

        r.update(new=105)
        with self.assertRaises(AttributeError):
            r.new

    def test_update_args_kwargs(self):
        """Test update args and kwargs."""
        r = Rectangle(10, 10, 10, 10)

        r.update(1, id=100)
        self.assertEqual(r.id, 1)

        r.update(1, 2, width=200)
        self.assertEqual(r.width, 2)

        r.update(1, 2, 3, heigh=300)
        self.assertEqual(r.height, 3)

        r.update(1, 2, 3, 4, x=400)
        self.assertEqual(r.x, 4)

        r.update(1, 2, 3, 4, 5, y=500)
        self.assertEqual(r.y, 5)

    def test_update_val_err(self):
        """Test update with invalid argument values."""
        r = Rectangle(10, 10, 10, 10)

        with self.assertRaises(ValueError):
            r.update(1, -2)

        with self.assertRaises(ValueError):
            r.update(1, 2, -3)

        with self.assertRaises(ValueError):
            r.update(1, 2, 3, -4)

        with self.assertRaises(ValueError):
            r.update(1, 2, 3, 4, -5)

    def test_update_type_err(self):
        """Test update with invalid argument types."""
        r = Rectangle(10, 10, 10, 10)

        with self.assertRaises(TypeError):
            r.update(1, 2.5)

        with self.assertRaises(TypeError):
            r.update(1, 2, 3.5)

        with self.assertRaises(TypeError):
            r.update(1, 2, 3, 4.5)

        with self.assertRaises(TypeError):
            r.update(1, 2, 3, 4, 5.5)

    def test_to_dictionary(self):
        """Test to_dictionary."""
        r = Rectangle(1, 2, 3, 4, 5)

        self.assertIsInstance(r.to_dictionary(), dict)

        d = {'width': 1, 'height': 2, 'x': 3, 'y': 4, 'id': 5}
        self.assertEqual(r.to_dictionary(), d)

        with self.assertRaises(TypeError):
            r.to_dictionary(1)

    def test_to_json_string(self):
        """Test to_json_string."""
        r = Rectangle(10, 7, 2, 8, 1)
        dictionary = r.to_dictionary()
        json_dictionary = Rectangle.to_json_string([dictionary])
        compare = eval('[{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}]')
        self.assertEqual(eval(json_dictionary), compare)

    def test_save_to_file(self):
        """Test JSON string to file for Rectangle."""
        equal = [{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10},
                 {"x": 0, "y": 0, "id": 2, "height": 4, "width": 2}]
        r1 = Rectangle(10, 7, 2, 8, id=1)
        r2 = Rectangle(2, 4, id=2)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            contents = file.read()
            self.assertEqual(eval(contents), equal)

        equal = []
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            contents = file.read()
            self.assertEqual(eval(contents), equal)

    def test_load_empty_json(self):
        """Test empty list to and from JSON."""
        Rectangle.save_to_file([])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(list_rectangles_output, [])

    def test_missing_json_file(self):
        """Test missing JSON file."""
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_create(self):
        d = {'id': 89}
        r = Rectangle.create(**d)
        self.assertEqual(r.id, 89)

        d = {'id': 89, 'width': 1}
        r = Rectangle.create(**d)
        self.assertEqual(r.width, 1)

        d = {'id': 89, 'width': 1, 'height': 2}
        r = Rectangle.create(**d)
        self.assertEqual(r.height, 2)

        d = {'id': 89, 'width': 1, 'height': 2, 'x': 3}
        r = Rectangle.create(**d)
        self.assertEqual(r.x, 3)

        d = {'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        r = Rectangle.create(**d)
        self.assertEqual(r.y, 4)

    def test_pep8(self):
        """Test PEP8."""
        files = ["models/rectangle.py", "tests/test_models/test_rectangle.py"]
        style = pep8.StyleGuide(quiet=False)
        errors = style.check_files(files).total_errors
        self.assertEqual(errors, 0, "PEP8")

if __name__ == '__main__':
    unittest.main()
    from ...models.rectangle import Rectangle

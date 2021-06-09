#!/usr/bin/python3
"""
Unit tests for Square class.

"""
import unittest
import pep8
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test Square class."""

    def test_init(self):
        """Test Square init."""
        Square._Base__nb_objects = 0
        # Expected usage
        s1 = Square(1)
        self.assertEqual(s1.width, 1)
        self.assertEqual(s1.height, 1)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 1)

        s2 = Square(1)
        self.assertEqual(s2.id, 2)

        s3 = Square(10, 2)
        self.assertEqual(s3.width, 10)
        self.assertEqual(s3.height, 10)
        self.assertEqual(s3.size, 10)
        self.assertEqual(s3.x, 2)
        self.assertEqual(s3.y, 0)
        self.assertEqual(s3.id, 3)

        s4 = Square(10, 2, 3)
        self.assertEqual(s4.width, 10)
        self.assertEqual(s4.height, 10)
        self.assertEqual(s4.size, 10)
        self.assertEqual(s4.x, 2)
        self.assertEqual(s4.y, 3)
        self.assertEqual(s4.id, 4)

        s5 = Square(10, 2, 3, 400)
        self.assertEqual(s5.width, 10)
        self.assertEqual(s5.height, 10)
        self.assertEqual(s5.size, 10)
        self.assertEqual(s5.x, 2)
        self.assertEqual(s5.y, 3)
        self.assertEqual(s5.id, 400)

        s6 = Square(1, 2, 3, '')
        self.assertEqual(s6.id, '')

        # Bad number of arguments
        with self.assertRaises(TypeError):
            Square()

        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

        # Bad argument values
        with self.assertRaises(ValueError):
            Square(0)

        with self.assertRaises(ValueError):
            Square(-1)

        with self.assertRaises(ValueError):
            Square(1, -2)

        with self.assertRaises(ValueError):
            Square(1, 2, -3)

        # Bad argument types
        with self.assertRaises(TypeError):
            Square("", 2)

        with self.assertRaises(TypeError):
            Square(1, "")

        with self.assertRaises(TypeError):
            Square(1, 2, "")

    def test_area(self):
        """Test area."""
        area1 = Square(1).area()
        self.assertEqual(area1, 1)

        area2 = Square(5).area()
        self.assertEqual(area2, 25)

        # Bad argument count
        with self.assertRaises(TypeError):
            Square().area(1)

    def test_display(self):
        """Test display."""
        s = Square(1)
        self.assertEqual(s.display(), "#\n")

        s = Square(1, 1)
        self.assertEqual(s.display(), " #\n")

        s = Square(1, 1, 1)
        self.assertEqual(s.display(), "\n #\n")

        # Bad argument count
        with self.assertRaises(TypeError):
            area1 = s.display(1)

    def test_str(self):
        """Test __str__."""
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.__str__(), "[Square] (4) 2/3 - 1")

        # Bad argument count
        with self.assertRaises(TypeError):
            area1 = s.__str__(1)

    def test_update_args(self):
        """Test update args."""
        s = Square(10, 10, 10, 10)

        s.update(89)
        self.assertEqual(s.id, 89)

        s.update(89, 2)
        self.assertEqual(s.size, 2)

        s.update(89, 2, 3)
        self.assertEqual(s.x, 3)

        s.update(89, 2, 3, 4)
        self.assertEqual(s.y, 4)

        with self.assertRaises(IndexError):
            s.update(1, 2, 3, 4, 5)

    def test_update_kwargs(self):
        """Test update kwargs."""
        s = Square(10, 10, 10, 10)

        s.update(id=100)
        self.assertEqual(s.id, 100)

        s.update(width=101)
        self.assertEqual(s.width, 101)
        self.assertEqual(s.size, 101)

        s.update(height=102)
        self.assertEqual(s.height, 102)
        self.assertEqual(s.size, 102)

        s.update(size=103)
        self.assertEqual(s.size, 103)
        self.assertEqual(s.width, 103)
        self.assertEqual(s.height, 103)

        s.update(x=104)
        self.assertEqual(s.x, 104)

        s.update(y=105)
        self.assertEqual(s.y, 105)

    def test_update_args_kwargs(self):
        """Test update args and kwargs."""
        s = Square(10, 10, 10, 10)

        s.update(1, id=100)
        self.assertEqual(s.id, 1)

        s.update(1, 2, size=200)
        self.assertEqual(s.size, 2)

        s.update(1, 2, 3, x=300)
        self.assertEqual(s.x, 3)

        s.update(1, 2, 3, 4, y=400)
        self.assertEqual(s.y, 4)

        s.update(new=101)
        with self.assertRaises(AttributeError):
            s.new

    def test_update_val_err(self):
        """Test update with invalid argument values."""
        s = Square(10, 10, 10, 10)

        with self.assertRaises(ValueError):
            s.update(1, -2)

        with self.assertRaises(ValueError):
            s.update(1, 2, -3)

        with self.assertRaises(ValueError):
            s.update(1, 2, 3, -4)

    def test_update_type_err(self):
        """Test update with invalid argument types."""
        r = Square(10, 10, 10, 10)

        with self.assertRaises(TypeError):
            r.update(1, 2.5)

        with self.assertRaises(TypeError):
            r.update(1, 2, 3.5)

        with self.assertRaises(TypeError):
            r.update(1, 2, 3, 4.5)

    def test_to_dictionary(self):
        """Test to_dictionary."""
        s = Square(1, 2, 3, 4)

        self.assertIsInstance(s.to_dictionary(), dict)

        d = {'size': 1, 'x': 2, 'y': 3, 'id': 4}
        self.assertEqual(s.to_dictionary(), d)

        with self.assertRaises(TypeError):
            s.to_dictionary(1)

    def test_to_json_string(self):
        """Test to_json_string."""
        s = Square(10, 2, 8, 1)
        dictionary = s.to_dictionary()
        json_dictionary = Square.to_json_string([dictionary])
        compare = eval('[{"x": 2, "y": 8, "id": 1, "size": 10}]')
        self.assertEqual(eval(json_dictionary), compare)

    def test_save_to_json(self):
        """Test JSON string to file for Square."""
        equal = [{"x": 2, "y": 8, "id": 1, "size": 10},
                 {"x": 0, "y": 0, "id": 2, "size": 2}]
        s1 = Square(10, 2, 8, id=1)
        s2 = Square(2, id=2)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as file:
            contents = file.read()
            self.assertEqual(eval(contents), equal)

        equal = []
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            contents = file.read()
            self.assertEqual(eval(contents), equal)

    def test_load_empty_json(self):
        """Test empty list to and from JSON."""
        Square.save_to_file([])
        list_squares_output = Square.load_from_file()
        self.assertEqual(list_squares_output, [])

    def test_missing_json_file(self):
        """Test missing JSON file."""
        self.assertEqual(Square.load_from_file(), [])

    def test_create(self):
        d = {'id': 89}
        s = Square.create(**d)
        self.assertEqual(s.id, 89)

        d = {'id': 89, 'size': 1}
        s = Square.create(**d)
        self.assertEqual(s.size, 1)

        d = {'id': 89, 'size': 1, 'x': 2}
        s = Square.create(**d)
        self.assertEqual(s.x, 2)

        d = {'id': 89, 'size': 1, 'x': 2, 'y': 3}
        s = Square.create(**d)
        self.assertEqual(s.y, 3)

    def test_pep8(self):
        """Test PEP8."""
        files = ["models/square.py", "tests/test_models/test_square.py"]
        style = pep8.StyleGuide(quiet=False)
        errors = style.check_files(files).total_errors
        self.assertEqual(errors, 0, "PEP8")

if __name__ == '__main__':
    unittest.main()
    from ...models.square import Square

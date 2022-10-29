#!/usr/bin/python3
from unittest import TestCase
from contextlib import redirect_stdout
import inspect
import io
import os
from models.base import Base
from models.rectangle import Rectangle
import json
from io import StringIO
import sys

"""Module to test the rectangle class"""


class test_rectangle(TestCase):
    """To test the rectangle class"""
    def setUp(self):
        """Set up for the test case"""
        self.rec = Rectangle(2, 5)

    def tearDown(self):
        """ tear down after the test case"""
        del self.rec

    def test_rect_width(self):
        """test the width of the rectangle"""
        self.assertEqual(2, self.rec.width)

    def test_rect_height(self):
        """test the height of the rectangle"""
        self.assertEqual(5, self.rec.height)

    def test_x(self):
        """test x default value"""
        self.assertEqual(0, self.rec.x)

    def test_y(self):
        """test y default value"""
        self.assertEqual(0, self.rec.y)

    def test_x_with_str(self):
        """test x with string"""
        with self.assertRaises(TypeError):
            rec = Rectangle(4, 5, "hello")

    def test_y_with_str(self):
        """test y with string"""
        with self.assertRaises(TypeError):
            rec = Rectangle(4, 5, 5, "hello")

    def test_width_with_str(self):
        """test width with string"""
        with self.assertRaises(TypeError):
            rec = Rectangle("width")

    def test_height_with_str(self):
        """test height with str"""
        with self.assertRaises(TypeError):
            rec = Rectangle(4, "height")

    def test_x_with_bool(self):
        """test x with bool"""
        with self.assertRaises(TypeError):
            rec = Rectangle(4, 5, True)

    def test_y_with_bool(self):
        """test y with bool"""
        with self.assertRaises(TypeError):
            rec = Rectangle(4, 5, 5, False)

    def test_width_with_bool(self):
        """test width with bool"""
        with self.assertRaises(TypeError):
            rec = Rectangle(True)

    def test_height_with_bool(self):
        """test height with bool"""
        with self.assertRaises(TypeError):
            rec = Rectangle(4, False)

    def test_width_with_list(self):
        """test width with list"""
        with self.assertRaises(TypeError):
            rec = Rectangle([4, 5])

    def test_height_with_list(self):
        """test height with list"""
        with self.assertRaises(TypeError):
            rec = Rectangle(5, [4, 5])

    def test_x_with_list(self):
        """test x with list"""
        with self.assertRaises(TypeError):
            rec = Rectangle(5, 6, [4, 5])

    def test_y_with_list(self):
        """test y with list"""
        with self.assertRaises(TypeError):
            rec = Rectangle(5, 6, 7, [4, 5])

    def test_width_with_float(self):
        """test width with float"""
        with self.assertRaises(TypeError):
            rec = Rectangle(4.0)

    def test_height_with_float(self):
        """test height with float"""
        with self.assertRaises(TypeError):
            rec = Rectangle(1, 4.0)

    def test_x_with_float(self):
        """test x with float"""
        with self.assertRaises(TypeError):
            rec = Rectangle(1, 2, 4.0)

    def test_y_with_float(self):
        """test y with float"""
        with self.assertRaises(TypeError):
            rec = Rectangle(1, 2, 3, 4.0)

    def test_width_with_tuple(self):
        """test width with tuple"""
        with self.assertRaises(TypeError):
            rec = Rectangle((4, 5))

    def test_height_with_tuple(self):
        """test height with tuple"""
        with self.assertRaises(TypeError):
            rec = Rectangle(5, (4, 5))

    def test_x_with_tuple(self):
        """test x with tuple"""
        with self.assertRaises(TypeError):
            rec = Rectangle(5, 6, (4, 5))

    def test_y_with_tuple(self):
        """test y with tuple"""
        with self.assertRaises(TypeError):
            rec = Rectangle(5, 6, 7, (4, 5))

    def test_width_with_dict(self):
        """test width with dict"""
        with self.assertRaises(TypeError):
            rec = Rectangle({"h": 4, "w": 5})

    def test_height_with_dict(self):
        """test height with dict"""
        with self.assertRaises(TypeError):
            rec = Rectangle(4, {"h": 4, "w": 5})

    def test_x_with_dict(self):
        """test x with dict"""
        with self.assertRaises(TypeError):
            rec = Rectangle(5, 6, {"h": 4, "w": 5})

    def test_y_with_dict(self):
        """test y with dict"""
        with self.assertRaises(TypeError):
            rec = Rectangle(5, 6, 7, {"h": 4, "w": 5})

    def test_width_with_zero(self):
        """test width with zero"""
        with self.assertRaises(ValueError):
            rec = Rectangle(0, 4)

    def test_height_with_zero(self):
        """test height with zero"""
        with self.assertRaises(ValueError):
            rec = Rectangle(5, 0)

    def test_width_with_negative(self):
        """test width with negative"""
        with self.assertRaises(ValueError):
            rec = Rectangle(-6, 4)

    def test_height_with_negative(self):
        """test height with negative"""
        with self.assertRaises(ValueError):
            rec = Rectangle(5, -5)

    def test_x_with_negative(self):
        """test x with negative"""
        with self.assertRaises(ValueError):
            rec = Rectangle(5, 5, -2)

    def test_y_with_negative(self):
        """test y with negative"""
        with self.assertRaises(ValueError):
            rec = Rectangle(5, 5, 7, -2)

    def test_area(self):
        """test area"""
        self.assertEqual(self.rec.area(), 10)

    def test_str_overide(self):
        """test the str overide method"""
        rec = Rectangle(5, 2, 3, 4, 50)
        self.assertEqual(rec.__str__(), "[Rectangle] (50) 3/4 - 5/2")

    def test_update_for_id(self):
        """test update for id"""
        self.rec.update(10)
        self.assertEqual(10, self.rec.id)

    def test_update_for_width(self):
        """test for upate for width"""
        self.rec.update(10, 8)
        self.assertEqual(8, self.rec.width)

    def test_update_for_height(self):
        """test for update for height"""
        self.rec.update(10, 8, 6)
        self.assertEqual(6, self.rec.height)

    def test_update_for_x(self):
        """test for update for x"""
        self.rec.update(10, 8, 6, 4)
        self.assertEqual(4, self.rec.x)

    def test_update_for_y(self):
        """test for update for y"""
        self.rec.update(10, 8, 6, 4, 2)
        self.assertEqual(2, self.rec.y)

    def test_update_with_kwargs(self):
        """test update with kwargs"""
        self.rec.update(id=25, x=15, y=10, width=5, height=13)
        self.assertEqual(5, self.rec.width)
        self.assertEqual(13, self.rec.height)
        self.assertEqual(15, self.rec.x)
        self.assertEqual(25, self.rec.id)
        self.assertEqual(10, self.rec.y)

    def test_to_dictionary(self):
        """test to dictionary"""
        rec = Rectangle(5, 6, 1, 3, 4)
        rec_dict = rec.to_dictionary()
        self.assertEqual(rec_dict,
                         {'height': 6, 'id': 4, 'width': 5, 'x': 1, 'y': 3})

    def test_to_dict_return_type(self):
        rec = Rectangle(5, 6, 1, 3, 4)
        rec_dict = rec.to_dictionary()
        self.assertEqual(type(rec_dict), dict)

    def test_missing_width(self):
        """test for missing width"""
        with self.assertRaises(TypeError):
            rec = Rectangle()

    def test_missing_height(self):
        """test for missing height"""
        with self.assertRaises(TypeError):
            rec = Rectangle(4)

    def test_documentation(self):
        """Test documentation"""
        self.assertTrue(len(Rectangle.__doc__) >= 1)

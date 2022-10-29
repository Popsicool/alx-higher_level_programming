#!/usr/bin/python3
from unittest import TestCase
from models.base import Base
from models.rectangle import Rectangle
import inspect


class test_base(TestCase):
    """Class test to test the  base class in  the model"""

    def test_none_id(self):
        """Test with no id input"""

        case = Base()
        self.assertEqual(1, case.id)

    def test_with_id(self):
        """test base with  id"""
        case = Base(67)
        self.assertEqual(67, case.id)

    def test_with_negative(self):
        """test with negativve"""
        case = Base(-5)
        self.assertEqual(-5, case.id)

    def test_with_string(self):
        """test with string"""
        case = Base("Hello")
        self.assertEqual("Hello", case.id)

    def test_with_zero(self):
        """Test with zero"""
        case = Base(0)
        self.assertEqual(0, case.id)

    def test_with_bool(self):
        """Test wih boolean"""
        case = Base(True)
        self.assertEqual(1, case.id)

    def test_with_tuple(self):
        """testb with tuple"""
        case = Base((2, 3, 4))
        self.assertEqual((2, 3, 4), case.id)

    def test_with_dict(self):
        """test with dictionary"""
        case = Base({"hello": "world"})
        self.assertEqual({"hello": "world"}, case.id)

    def test_with_list(self):
        """test with list"""
        case = Base([1, 2, 3, 4, 5])
        self.assertEqual([1, 2, 3, 4, 5], case.id)

    def test_to_json_string(self):
        """test to_json_string"""
        case = Rectangle(3, 6)
        json_dic = case.to_dictionary()
        json_dic = Base.to_json_string(json_dic)
        self.assertEqual(
                '{"id": 2, "width": 3, "height": 6, "x": 0, "y": 0}', json_dic)

    @classmethod
    def setUpClass(cls):
        """set up method"""
        cls.setup = inspect.getmembers(Base, inspect.isfunction)

    def test_documentation(self):
        """Test documentation"""
        self.assertTrue(len(Base.__doc__) >= 1)

        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)

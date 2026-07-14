import unittest
from src.calculator import add, divide

class TestMathOperations(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)


    def test_divide(self):
        self.assertEqual(divide(6, 2), 3)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError, "Деление на ноль невозможно"):
            divide(10, 0)

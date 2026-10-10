import unittest
from calculator import add, sub, mul

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3),5)
    def test_sub(self):
        self.assertEqual(sub(5,3),2)
    def test_mul(self):
        self.assertEqual(mul(2,3),6)
    def test_zero_input(self):
        with self.assertRaises(ValueError):
            add(0,3)
    def test_negative_input(self):
        with self.assertRaises(ValueError):
            sub(-1,3)
    def test_non_integer_input(self):
        with self.assertRaises(ValueError):
            mul(2.5,3)
if __name__ == '__main__':
    unittest.main()
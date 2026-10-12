import unittest
from calculator import add,mul,sub

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3,5),8)
    def test_sub(self):
        self.assertEqual(sub(5,2),3)
    def test_mul(self):
        self.assertEqual(mul(5,10),50)
    def test_zero(self):
        with self.assertRaises(ValueError):
            add(0,3)
    def test_negative(self):
        with self.assertRaises(ValueError):
            add(-1,3)
    def test_non_int(self):
        with self.assertRaises(ValueError):
            mul(2.5,3)
if __name__ == "__main__":
    unittest.main()
import unittest
from app.modulo2 import producto, division

class TestCalculadora(unittest.TestCase):

    def test_producto(self):
        self.assertEqual(producto(2, 3), 6)

    def test_resta(self):
        self.assertEqual(division(4, 2), 2)

if __name__ == '__main__':
    unittest.main()

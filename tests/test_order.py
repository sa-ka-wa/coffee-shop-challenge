import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from order import Order

# Minimal dummy classes if needed:
class Customer:
    pass

class Coffee:
    pass

from order import Order  # adjust if needed

class TestOrder(unittest.TestCase):

    def setUp(self):
        self.customer = Customer()
        self.coffee = Coffee()

    def test_valid_order_creation(self):
        order = Order(self.customer, self.coffee, 5.5)
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.coffee, self.coffee)
        self.assertEqual(order.price, 5.5)

    def test_price_type_validation(self):
        with self.assertRaises(TypeError):
            Order(self.customer, self.coffee, "not a number")

    def test_price_range_validation(self):
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 0.5)  # too low
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 15)   # too high

    def test_price_immutable(self):
        order = Order(self.customer, self.coffee, 6)
        with self.assertRaises(AttributeError):
            order.price = 7

if __name__ == "__main__":
    unittest.main()

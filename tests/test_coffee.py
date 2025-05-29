import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from coffee import Coffee
 # assuming your Coffee class is in coffee.py
# We'll include Order here for simplicity
class Order:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

class TestCoffee(unittest.TestCase):

    def setUp(self):
        self.coffee = Coffee("Espresso", 3.5)

    def test_name_property(self):
        self.assertEqual(self.coffee.name, "Espresso")

    def test_no_orders_initially(self):
        self.assertEqual(self.coffee.num_orders(), 0)
        self.assertEqual(self.coffee.orders(), [])
        self.assertEqual(self.coffee.customers(), [])
        self.assertEqual(self.coffee.average_price(), 0)

    def test_add_order_and_orders(self):
        order1 = Order("Alice", 3.5)
        order2 = Order("Bob", 4.0)
        self.coffee.add_order(order1)
        self.coffee.add_order(order2)

        self.assertEqual(self.coffee.num_orders(), 2)
        self.assertCountEqual(self.coffee.orders(), [order1, order2])
        self.assertCountEqual(self.coffee.customers(), ["Alice", "Bob"])
        expected_avg = (3.5 + 4.0) / 2
        self.assertAlmostEqual(self.coffee.average_price(), expected_avg)

    def test_customers_unique(self):
        order1 = Order("Alice", 3.5)
        order2 = Order("Alice", 4.0)
        self.coffee.add_order(order1)
        self.coffee.add_order(order2)

        self.assertEqual(len(self.coffee.customers()), 1)
        self.assertEqual(self.coffee.customers()[0], "Alice")

if __name__ == "__main__":
    unittest.main()

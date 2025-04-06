import unittest
from shopping_cart import ShoppingCart

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.cart = ShoppingCart()

    def test_add_item(self):
        self.cart.add_item("Laptop", 999.99, 1)
        self.assertEqual(len(self.cart.get_items()), 1)
        self.assertEqual(self.cart.get_items()[0]["name"], "Laptop")
        self.assertEqual(self.cart.get_items()[0]["price"], 999.99)
        self.assertEqual(self.cart.get_items()[0]["quantity"], 1)

    def test_remove_item(self):
        self.cart.add_item("Headphones", 150.75, 2)
        self.cart.remove_item("Headphones")
        self.assertEqual(len(self.cart.get_items()), 0)

    def test_remove_item_not_found(self):
        with self.assertRaises(ValueError):
            self.cart.remove_item("Smartwatch")

    def test_get_total_price(self):
        self.cart.add_item("Laptop", 999.99, 1)
        self.cart.add_item("Keyboard", 50.5, 3)
        self.assertEqual(self.cart.get_total_price(), 1151.49)

    def test_clear_cart(self):
        self.cart.add_item("Tablet", 450.99, 1)
        self.cart.add_item("Mouse", 25.5, 2)
        self.cart.clear_cart()
        self.assertEqual(len(self.cart.get_items()), 0)

    def test_get_items(self):
        self.cart.add_item("Tablet", 450.99, 1)
        self.cart.add_item("Mouse", 25.5, 2)
        items = self.cart.get_items()
        self.assertEqual(len(items), 2)
        self.assertEqual(items[0]["name"], "Tablet")
        self.assertEqual(items[1]["name"], "Mouse")

    def test_add_item_with_negative_price(self):
        with self.assertRaises(ValueError):
            self.cart.add_item("Laptop", -1000, 1)

    def test_add_item_with_negative_quantity(self):
        with self.assertRaises(ValueError):
            self.cart.add_item("Laptop", 1000, -1)

    def test_add_item_with_zero_quantity(self):
        with self.assertRaises(ValueError):
            self.cart.add_item("Laptop", 1000, 0)

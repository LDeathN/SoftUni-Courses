from project.shopping_cart import ShoppingCart
from unittest import TestCase


class TestShoppingCart(TestCase):
    def test_constructor(self):
        Cart = ShoppingCart("Super", 300.0)
        self.assertEqual(Cart.shop_name, "Super")
        self.assertEqual(Cart.budget, 300.0)
        self.assertEqual(Cart.products, {})
        with self.assertRaises(ValueError) as ve:
            ShoppingCart("Super2", 400.0)
        self.assertEqual(str(ve.exception), "Shop must contain only letters and must start with capital letter!")
        with self.assertRaises(ValueError) as ve2:
            ShoppingCart("super", 500.0)
        self.assertEqual(str(ve2.exception), "Shop must contain only letters and must start with capital letter!")

    def test_add_to_cart_case1(self):
        Cart = ShoppingCart("Super", 300.0)
        message = Cart.add_to_cart("Naruto", 50.0)
        self.assertEqual(message, "Naruto product was successfully added to the cart!")
        self.assertEqual(Cart.products, {"Naruto": 50.0})
        Cart.add_to_cart("Nami", 45.0)
        self.assertEqual(Cart.products, {"Naruto": 50.0, "Nami": 45.0})

    def test_add_to_cart_case2(self):
        Cart = ShoppingCart("Super", 300.0)
        with self.assertRaises(ValueError) as ve:
            Cart.add_to_cart("RTX 3060", 2399.0)
        self.assertEqual(str(ve.exception), "Product RTX 3060 cost too much!")

    def test_remove_from_cart_case1(self):
        Cart = ShoppingCart("Super", 600.0)
        Cart.add_to_cart("Nami", 45.0)
        Cart.add_to_cart("Naruto", 50.0)
        message = Cart.remove_from_cart("Nami")
        self.assertEqual(message, "Product Nami was successfully removed from the cart!")
        self.assertEqual(Cart.products, {"Naruto": 50.0})
        Cart.remove_from_cart("Naruto")
        self.assertEqual(Cart.products, {})

    def test_remove_from_cart_case2(self):
        Cart = ShoppingCart("Super", 600.0)
        Cart.add_to_cart("Nami", 45.0)
        Cart.add_to_cart("Naruto", 50.0)
        with self.assertRaises(ValueError) as ve:
            Cart.remove_from_cart("RTX 3060")
        self.assertEqual(str(ve.exception), "No product with name RTX 3060 in the cart!")

    def test_add_method_case1(self):
        Cart = ShoppingCart("Super", 600.0)
        Cart2 = ShoppingCart("Cool", 400.0)
        Cart.add_to_cart("Nami", 45.0)
        Cart.add_to_cart("Naruto", 50.0)
        Cart2.add_to_cart("Goku", 90.0)
        Cart2.add_to_cart("Sunglasses", 60.0)
        Cart3 = Cart.__add__(Cart2)
        self.assertEqual(Cart3.shop_name, "SuperCool")
        self.assertEqual(Cart3.budget, 1000.0)
        self.assertEqual(Cart3.products, {"Nami": 45.0, "Naruto": 50.0, "Goku": 90.0, "Sunglasses": 60.0})
        Cart4 = ShoppingCart("Bro", 500.0)
        Cart4.add_to_cart("Mouse", 75.0)
        Cart5 = Cart3.__add__(Cart4)
        self.assertEqual(Cart5.shop_name, "SuperCoolBro")
        self.assertEqual(Cart5.budget, 1500.0)
        self.assertEqual(Cart5.products, {"Nami": 45.0, "Naruto": 50.0, "Goku": 90.0, "Sunglasses": 60.0, "Mouse": 75.0})

    def test_buy_products_case1(self):
        Cart = ShoppingCart("Super", 500.0)
        Cart.add_to_cart("Nami", 45.0)
        Cart.add_to_cart("Naruto", 50.0)
        message = Cart.buy_products()
        self.assertEqual(message, "Products were successfully bought! Total cost: 95.00lv.")

    def test_buy_products_case2(self):
        Cart = ShoppingCart("Super", 100.0)
        Cart.add_to_cart("Nami", 65.0)
        Cart.add_to_cart("Naruto", 50.0)
        with self.assertRaises(ValueError) as ve:
            Cart.buy_products()
        self.assertEqual(str(ve.exception), "Not enough money to buy the products! Over budget with 15.00lv!")


from project.pet_shop import PetShop
from unittest import TestCase


class TestPetShop(TestCase):
    def test_constructor(self):
        shop = PetShop("Devin")
        self.assertEqual(shop.name, "Devin")
        self.assertEqual(shop.food, {})
        self.assertEqual(shop.pets, [])
        shop2 = PetShop("")
        self.assertEqual(shop2.name, "")
        self.assertEqual(shop2.food, {})
        self.assertEqual(shop2.pets, [])

    def test_add_food_case1(self):
        shop = PetShop("Devin")
        message = shop.add_food("Salam", 200)
        self.assertEqual(message, "Successfully added 200.00 grams of Salam.")
        self.assertEqual(shop.food, {"Salam": 200})
        shop.add_food("Salam", 300)
        self.assertEqual(shop.food, {"Salam": 500})
        shop.add_food("Meat", 200)
        self.assertEqual(shop.food, {"Salam": 500, "Meat": 200})
        with self.assertRaises(ValueError) as ve:
            shop.add_food("Meat", -200)
        self.assertEqual(str(ve.exception), 'Quantity cannot be equal to or less than 0')
        with self.assertRaises(ValueError) as ve2:
            shop.add_food("Salam", 0)
        self.assertEqual(str(ve2.exception), 'Quantity cannot be equal to or less than 0')

    def test_add_pet_case1(self):
        shop = PetShop("Devin")
        message = shop.add_pet("Aik")
        self.assertEqual(message, "Successfully added Aik.")
        self.assertEqual(shop.pets, ["Aik"])
        shop.add_pet("Murat")
        self.assertEqual(shop.pets, ["Aik", "Murat"])
        with self.assertRaises(Exception) as ve:
            shop.add_pet("Aik")
        self.assertEqual(str(ve.exception), "Cannot add a pet with the same name")
        self.assertEqual(shop.pets, ["Aik", "Murat"])

    def test_feed_pet_case1(self):
        shop = PetShop("Devin")
        shop.add_food("Salam", 300)
        shop.add_food("Salam", 200)
        shop.add_food("Meat", 200)
        shop.add_pet("Aik")
        shop.add_pet("Murat")
        message = shop.feed_pet("Meat", "Aik")
        self.assertEqual(message, "Aik was successfully fed")
        self.assertEqual(shop.food, {"Salam": 500, "Meat": 100})
        shop.feed_pet("Meat", "Aik")
        self.assertEqual(shop.food, {"Salam": 500, "Meat": 0})
        message = shop.feed_pet("Meat", "Murat")
        self.assertEqual(message, "Adding food...")
        self.assertEqual(shop.food, {"Salam": 500, "Meat": 1000})
        message = shop.feed_pet("Meso", "Aik")
        self.assertEqual(message, "You do not have Meso")

    def test_feed_pet_case2(self):
        shop = PetShop("Devin")
        shop.add_food("Salam", 300)
        shop.add_food("Salam", 200)
        shop.add_food("Meat", 200)
        shop.add_pet("Aik")
        shop.add_pet("Murat")
        with self.assertRaises(Exception) as e:
            shop.feed_pet("Tiger", "Salam")
        self.assertEqual(str(e.exception), "Please insert a valid pet name")

    def test_repr_method(self):
        shop = PetShop("Devin")
        shop.add_food("Salam", 300)
        shop.add_food("Salam", 200)
        shop.add_food("Meat", 200)
        shop.add_pet("Aik")
        shop.add_pet("Murat")
        result = shop.__repr__()
        actual = f'Shop Devin:\nPets: Aik, Murat'
        self.assertEqual(result, actual)
        shop2 = PetShop("Nastan")
        self.assertEqual(shop2.__repr__(), "Shop Nastan:\nPets: ")
        shop3 = PetShop("")
        self.assertEqual(shop3.__repr__(), "Shop :\nPets: ")

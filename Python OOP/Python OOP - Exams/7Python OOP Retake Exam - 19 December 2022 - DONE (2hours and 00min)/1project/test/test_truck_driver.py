from project.truck_driver import TruckDriver
from unittest import TestCase


class TestTruckDriver(TestCase):
    def test_constructor(self):
        driver1 = TruckDriver("Dani", 5.5)
        self.assertEqual(driver1.name, "Dani")
        self.assertEqual(driver1.money_per_mile, 5.5)
        self.assertEqual(driver1.available_cargos, {})
        self.assertEqual(driver1.earned_money, 0)
        self.assertEqual(driver1.miles, 0)

    def test_add_cargo_case1(self):
        driver1 = TruckDriver("Dani", 5.5)
        message = driver1.add_cargo_offer("Finland", 2500)
        self.assertEqual(message, "Cargo for 2500 to Finland was added as an offer.")
        self.assertEqual(driver1.available_cargos, {"Finland": 2500})

    def test_add_cargo_case2(self):
        driver1 = TruckDriver("Dani", 5.5)
        driver1.add_cargo_offer("Finland", 2500)
        driver1.add_cargo_offer("Moscow", 3000)
        driver1.add_cargo_offer("France", 1800)
        self.assertEqual(driver1.available_cargos, {"Finland": 2500, "Moscow": 3000, "France": 1800})

    def test_add_cargo_case3(self):
        driver1 = TruckDriver("Dani", 5.5)
        driver1.add_cargo_offer("Finland", 2500)
        driver1.add_cargo_offer("Moscow", 3000)
        with self.assertRaises(Exception) as ve:
            driver1.add_cargo_offer("Finland", 2300)
        self.assertEqual(str(ve.exception), "Cargo offer is already added.")

    def test_best_offer_case1(self):
        driver1 = TruckDriver("Dani", 5)
        driver1.add_cargo_offer("Finland", 250)
        message = driver1.drive_best_cargo_offer()
        self.assertEqual(message, "Dani is driving 250 to Finland.")
        self.assertEqual(driver1.miles, 250)
        self.assertEqual(driver1.earned_money, 1230)
        self.assertEqual(driver1.available_cargos, {"Finland": 250})
        driver1.add_cargo_offer("Moscow", 1000)
        message = driver1.drive_best_cargo_offer()
        self.assertEqual(message, "Dani is driving 1000 to Moscow.")
        self.assertEqual(driver1.miles, 1250)
        self.assertEqual(driver1.earned_money, 6105)
        self.assertEqual(driver1.available_cargos, {"Finland": 250, "Moscow": 1000})
        driver1.add_cargo_offer("France", 1500)
        message = driver1.drive_best_cargo_offer()
        self.assertEqual(message, "Dani is driving 1500 to France.")
        self.assertEqual(driver1.miles, 2750)
        self.assertEqual(driver1.earned_money, 12940)
        self.assertEqual(driver1.available_cargos, {"Finland": 250, "Moscow": 1000, "France": 1500})
        driver1.add_cargo_offer("Italy", 10000)
        message = driver1.drive_best_cargo_offer()
        self.assertEqual(message, "Dani is driving 10000 to Italy.")
        self.assertEqual(driver1.miles, 12750)
        self.assertEqual(driver1.earned_money, 51190)
        self.assertEqual(driver1.available_cargos, {"Finland": 250, "Moscow": 1000, "France": 1500, "Italy": 10000})


    def test_best_offer_case2(self):
        driver1 = TruckDriver("Dani", 5)
        message = driver1.drive_best_cargo_offer()
        self.assertEqual(message, "There are no offers available.")

    def test_best_offer_case3(self):
        driver1 = TruckDriver("Dani", 1)
        driver1.add_cargo_offer("Finland", 250)
        driver1.add_cargo_offer("Moscow", 1000)
        driver1.add_cargo_offer("Italy", 10000)
        driver1.add_cargo_offer("France", 1500)
        with self.assertRaises(ValueError) as ve:
            driver1.drive_best_cargo_offer()
        self.assertEqual(str(ve.exception), "Dani went bankrupt.")

    def test_repr_method(self):
        driver2 = TruckDriver("Dani", 1)
        driver1 = TruckDriver("Peter", 5)
        driver1.add_cargo_offer("Finland", 2500)
        driver1.drive_best_cargo_offer()
        driver1.add_cargo_offer("Moscow", 3000)
        driver1.add_cargo_offer("France", 1800)
        driver1.drive_best_cargo_offer()
        message1 = driver1.__repr__()
        message2 = driver2.__repr__()
        self.assertEqual(message1, "Peter has 5500 miles behind his back.")
        self.assertEqual(message2, "Dani has 0 miles behind his back.")
        

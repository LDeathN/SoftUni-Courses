from project.second_hand_car import SecondHandCar
from unittest import TestCase, main


class TestSecondHandCar(TestCase):
    def test_constructor(self):
        car1 = SecondHandCar("Audi A4", "Sedan", 150000, 10000)
        car2 = SecondHandCar("", "", 1000, 1000)
        with self.assertRaises(ValueError) as ve:
            SecondHandCar("Audi A4", "Sedan", 0, 10000)
        self.assertEqual(str(ve.exception), "Please, second-hand cars only! Mileage must be greater than 100!")
        with self.assertRaises(ValueError) as ve:
            SecondHandCar("Audi A4", "Sedan", 150000, 0)
        self.assertEqual(str(ve.exception), "Price should be greater than 1.0!")
        with self.assertRaises(ValueError) as ve:
            SecondHandCar("Audi A4", "Sedan", -100, 5000)
        self.assertEqual(str(ve.exception), "Please, second-hand cars only! Mileage must be greater than 100!")
        with self.assertRaises(ValueError) as ve:
            SecondHandCar("Audi A4", "Sedan", 150000, -5000)
        self.assertEqual(str(ve.exception), "Price should be greater than 1.0!")
        with self.assertRaises(ValueError) as ve:
            SecondHandCar("Audi A4", "Sedan", 100, 5000)
        self.assertEqual(str(ve.exception), "Please, second-hand cars only! Mileage must be greater than 100!")
        with self.assertRaises(ValueError) as ve:
            SecondHandCar("Audi A4", "Sedan", 150000, 1)
        self.assertEqual(str(ve.exception), "Price should be greater than 1.0!")
        self.assertEqual(car1.model, "Audi A4")
        self.assertEqual(car1.car_type, "Sedan")
        self.assertEqual(car1.mileage, 150000)
        self.assertEqual(car1.price, 10000)
        self.assertEqual(car2.car_type, "")
        self.assertEqual(car2.model, "")
        self.assertEqual(car2.price, 1000)
        self.assertEqual(car2.mileage, 1000)

    def test_promotional_price(self):
        car1 = SecondHandCar("Audi A4", "Sedan", 150000, 10000)
        message = car1.set_promotional_price(9000)
        self.assertEqual(message, "The promotional price has been successfully set.")
        self.assertEqual(car1.price, 9000)

    def test_promotional_price_failed(self):
        car1 = SecondHandCar("Audi A4", "Sedan", 150000, 10000)
        with self.assertRaises(ValueError) as ve:
            car1.set_promotional_price(15000)
        self.assertEqual(str(ve.exception), "You are supposed to decrease the price!")

    def test_promotional_price_double(self):
        car1 = SecondHandCar("Audi A4", "Sedan", 150000, 10000)
        message = car1.set_promotional_price(9000)
        self.assertEqual(message, "The promotional price has been successfully set.")
        self.assertEqual(car1.price, 9000)
        message1 = car1.set_promotional_price(8000)
        self.assertEqual(message, "The promotional price has been successfully set.")
        self.assertEqual(car1.price, 8000)

    def test_repair_case_1(self):
        car1 = SecondHandCar("Audi A4", "Sedan", 150000, 10000)
        car2 = SecondHandCar("Audi A4", "Sedan", 150000, 8000)
        message = car1.need_repair(1000, "New Battery")
        message2 = car2.need_repair(4000, "Tuning")
        self.assertEqual(message, "Price has been increased due to repair charges.")
        self.assertEqual(car1.price, 11000)
        self.assertEqual(car1.repairs, ["New Battery"])
        self.assertEqual(message2, "Price has been increased due to repair charges.")
        self.assertEqual(car2.price, 12000)
        self.assertEqual(car2.repairs, ["Tuning"])

    def test_repair_case_2(self):
        car1 = SecondHandCar("Audi A4", "Sedan", 150000, 10000)
        message = car1.need_repair(5500, "LS Swap")
        self.assertEqual(message, "Repair is impossible!")

    def test_repair_case_3(self):
        car1 = SecondHandCar("Audi A4", "Sedan", 150000, 10000)
        car1.need_repair(1000, "New Battery")
        car1.need_repair(5500, "LS Swap")
        self.assertEqual(car1.price, 16500)
        self.assertEqual(car1.repairs, ["New Battery", "LS Swap"])

    def test_gt_method_failed(self):
        car1 = SecondHandCar("Audi A4", "Sedan", 150000, 10000)
        car2 = SecondHandCar("BMW X5", "SUV", 150000, 10000)
        message = car1.__gt__(car2)
        self.assertEqual(message, "Cars cannot be compared. Type mismatch!")

    def test_gt_method_success(self):
        car1 = SecondHandCar("Audi A4", "Sedan", 350000, 10000)
        car2 = SecondHandCar("BMW E90", "Sedan", 250000, 12000)
        self.assertEqual(car1.__gt__(car2), False)
        self.assertEqual(car2.__gt__(car1), True)

    def test_str_method(self):
        car1 = SecondHandCar("Audi A4", "Sedan", 150000, 10000)
        car2 = SecondHandCar("", "", 1000, 1000)
        self.assertEqual(car1.__str__(), f"""Model Audi A4 | Type Sedan | Milage 150000km
Current price: 10000.00 | Number of Repairs: 0""")
        self.assertEqual(car2.__str__(), f"""Model  | Type  | Milage 1000km
Current price: 1000.00 | Number of Repairs: 0""")
        car1.set_promotional_price(9000)
        car1.need_repair(1500, "Chain Change")
        car1.need_repair(600, "New Battery")
        car1.need_repair(900, "New Winter Tires")
        self.assertEqual(car1.__str__(), f"""Model Audi A4 | Type Sedan | Milage 150000km
Current price: 12000.00 | Number of Repairs: 3""")

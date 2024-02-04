class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


car = Car("a", "b", 1, 4)
car.make = ""
print(car)


import unittest


class CarTests(unittest.TestCase):

    def test_constructor(self):
        car1 = Car("Toyota", "Camry", 10, 50)
        self.assertEqual(car1.make, "Toyota")
        self.assertEqual(car1.model, "Camry")
        self.assertEqual(car1.fuel_consumption, 10)
        self.assertEqual(car1.fuel_capacity, 50)
        self.assertEqual(car1.fuel_amount, 0)

    def test_property(self):
        pass

    def test_make_setter(self):
        car2 = Car("Toyota", "Camry", 10, 50)
        with self.assertRaises(Exception) as context:
            car2.make = ""
        self.assertEqual(str(context.exception), "Make cannot be null or empty!")

    def test_model_setter(self):
        car3 = Car("Toyota", "Camry", 10, 50)
        with self.assertRaises(Exception) as context:
            car3.model = ""
        self.assertEqual(str(context.exception), "Model cannot be null or empty!")

    def test_consumption_setter(self):
        car4 = Car("Toyota", "Camry", 10, 50)
        with self.assertRaises(Exception) as context:
            car4.fuel_consumption = 0
        self.assertEqual(str(context.exception), "Fuel consumption cannot be zero or negative!")

    def test_capacity_fuel_setter(self):
        car5 = Car("Toyota", "Camry", 10, 50)
        with self.assertRaises(Exception) as context:
            car5.fuel_capacity = 0
        self.assertEqual(str(context.exception), "Fuel capacity cannot be zero or negative!")

    def test_amount_fuel_setter(self):
        car6 = Car("Toyota", "Camry", 10, 50)
        with self.assertRaises(Exception) as context:
            car6.fuel_amount = -5
        self.assertEqual(str(context.exception), "Fuel amount cannot be negative!")

    def test_refuel_method_positive(self):
        car7 = Car("Toyota", "Camry", 10, 50)
        car7.refuel(20)
        self.assertEqual(car7.fuel_amount, 20)

    def test_refuel_method_negative(self):
        car8 = Car("Toyota", "Camry", 10, 50)
        with self.assertRaises(Exception) as context:
            car8.refuel(-10)
        self.assertEqual(str(context.exception), "Fuel amount cannot be zero or negative!")

    def test_drive_method_positive(self):
        car9 = Car("Toyota", "Camry", 10, 50)
        car9.refuel(20)
        car9.drive(100)
        self.assertEqual(car9.fuel_amount, 10.0)

    def test_drive_method_negative(self):
        car10 = Car("Toyota", "Camry", 10, 50)
        with self.assertRaises(Exception) as context:
            car10.drive(100)
        self.assertEqual(str(context.exception), "You don't have enough fuel to drive!")


if __name__ == '__main__':
    unittest.main()




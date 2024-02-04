from project.vehicle import Vehicle
from unittest import TestCase, main


class TestVehicle(TestCase):

    def test_class_instances(self):
        car = Vehicle(50.0, 190.0)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, 1.25)
        self.assertEqual(type(car.fuel), float)
        self.assertEqual(type(car.horse_power), float)

    def test_constructor(self):
        car = Vehicle(50.0, 190.0)
        self.assertEqual(car.fuel, 50.0)
        self.assertEqual(car.capacity, 50.0)
        self.assertEqual(car.horse_power, 190.0)
        self.assertEqual(car.fuel_consumption, 1.25)

    def test_drive_method_positive(self):
        car = Vehicle(50.0, 190.0)
        car.drive(20)
        self.assertEqual(car.fuel, 25)

    def test_drive_method_negative(self):
        car = Vehicle(50.0, 190.0)
        with self.assertRaises(Exception) as context:
            car.drive(50)
        self.assertEqual(str(context.exception), "Not enough fuel")

    def test_refuel_method_positive(self):
        car = Vehicle(50.0, 190.0)
        car.drive(20)
        car.refuel(20)
        self.assertEqual(car.fuel, 45)

    def test_refuel_method_negative(self):
        car = Vehicle(50.0, 190.0)
        car.drive(20)
        with self.assertRaises(Exception) as context:
            car.refuel(30)
        self.assertEqual(str(context.exception), "Too much fuel")

    def test_str_method(self):
        car = Vehicle(50.0, 190.0)
        message = car.__str__()
        expected_message = "The vehicle has 190.0 horse power with 50.0 fuel left and 1.25 fuel consumption"
        self.assertEqual(message, expected_message)


if __name__ == '__main__':
    main()



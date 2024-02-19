from project.train.train import Train
from unittest import TestCase


class TestTrain(TestCase):
    def test_constructor(self):
        train = Train("North", 100)
        self.assertEqual(train.name, "North")
        self.assertEqual(train.capacity, 100)
        self.assertEqual(train.passengers, [])
        self.assertEqual(train.TRAIN_FULL, "Train is full")
        self.assertEqual(train.PASSENGER_ADD, "Added passenger {}")
        self.assertEqual(train.PASSENGER_EXISTS, "Passenger {} Exists")
        self.assertEqual(train.PASSENGER_NOT_FOUND, "Passenger Not Found")
        self.assertEqual(train.PASSENGER_REMOVED, "Removed {}")
        self.assertEqual(train.ZERO_CAPACITY, 0)

    def test_add_case1(self):
        train = Train("North", 3)
        message = train.add("Martin")
        self.assertEqual(message, "Added passenger Martin")
        self.assertEqual(train.passengers, ["Martin"])
        train.add("Dani")
        self.assertEqual(train.passengers, ["Martin", "Dani"])
        with self.assertRaises(ValueError) as ve:
            train.add("Martin")
        self.assertEqual(str(ve.exception), "Passenger Martin Exists")
        self.assertEqual(train.passengers, ["Martin", "Dani"])
        train.add("Gosho")
        self.assertEqual(train.passengers, ["Martin", "Dani", "Gosho"])
        with self.assertRaises(ValueError) as ve2:
            train.add("Maria")
        self.assertEqual(str(ve2.exception), "Train is full")

    def test_remove_case1(self):
        train = Train("North", 3)
        train.add("Martin")
        train.add("Dani")
        train.add("Gosho")
        message = train.remove("Gosho")
        self.assertEqual(message, "Removed Gosho")
        self.assertEqual(train.passengers, ["Martin", "Dani"])
        train.remove("Dani")
        self.assertEqual(train.passengers, ["Martin"])
        with self.assertRaises(ValueError) as ve:
            train.remove("Dani")
        self.assertEqual(str(ve.exception), "Passenger Not Found")
        self.assertEqual(train.passengers, ["Martin"])


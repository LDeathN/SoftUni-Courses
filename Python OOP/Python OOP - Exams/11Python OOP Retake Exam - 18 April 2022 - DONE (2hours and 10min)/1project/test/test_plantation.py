from project.plantation import Plantation
from unittest import TestCase


class TestPlantation(TestCase):
    def test_constructor(self):
        Place = Plantation(3000)
        self.assertEqual(Place.size, 3000)
        self.assertEqual(Place.plants, {})
        self.assertEqual(Place.workers, [])
        self.assertEqual(len(Place), 0)
        with self.assertRaises(ValueError) as ve:
            Plantation(-2000)
        self.assertEqual(str(ve.exception), "Size must be positive number!")

    def test_hire_worker_case1(self):
        Place = Plantation(3000)
        result = Place.hire_worker("Dani")
        self.assertEqual(result, "Dani successfully hired.")
        self.assertEqual(Place.workers, ["Dani"])
        Place.hire_worker("Bobi")
        self.assertEqual(Place.workers, ["Dani", "Bobi"])
        with self.assertRaises(ValueError) as ve:
            Place.hire_worker("Dani")
        self.assertEqual(str(ve.exception), "Worker already hired!")

    def test_planting_case1(self):
        Place = Plantation(3)
        Place.hire_worker("Bobi")
        Place.hire_worker("Dani")
        message = Place.planting("Dani", "Tulips")
        self.assertEqual(message, "Dani planted it's first Tulips.")
        self.assertEqual(Place.plants, {"Dani": ["Tulips"]})
        self.assertEqual(len(Place), 1)
        message = Place.planting("Dani", "Poppy")
        self.assertEqual(message, "Dani planted Poppy.")
        self.assertEqual(Place.plants, {"Dani": ["Tulips", "Poppy"]})
        self.assertEqual(len(Place), 2)
        Place.planting("Bobi", "Poppy")
        self.assertEqual(len(Place), 3)
        self.assertEqual(Place.plants, {"Dani": ["Tulips", "Poppy"], "Bobi": ["Poppy"]})
        with self.assertRaises(ValueError) as ve:
            Place.planting("Ivan", "Rose")
        self.assertEqual(str(ve.exception), "Worker with name Ivan is not hired!")
        with self.assertRaises(ValueError) as ve2:
            Place.planting("Dani", "Tulips")
        self.assertEqual(str(ve2.exception), "The plantation is full!")

    def test_str_method(self):
        Place = Plantation(3)
        Place.hire_worker("Bobi")
        Place.hire_worker("Dani")
        Place.planting("Dani", "Tulips")
        Place.planting("Dani", "Poppy")
        Place.planting("Bobi", "Poppy")
        result = Place.__str__()
        actual = ["Plantation size: 3"]
        actual.append("Bobi, Dani")
        actual.append("Dani planted: Tulips, Poppy")
        actual.append("Bobi planted: Poppy")
        actual = "\n".join(actual)
        self.assertEqual(result, actual)
        Place2 = Plantation(0)
        result2 = Place2.__str__()
        actual2 = "Plantation size: 0\n"
        self.assertEqual(result2, actual2)

    def test_repr_method(self):
        Place = Plantation(3)
        Place.hire_worker("Bobi")
        Place.hire_worker("Dani")
        result = Place.__repr__()
        actual = "Size: 3\nWorkers: Bobi, Dani"
        self.assertEqual(result, actual)
        Place2 = Plantation(0)
        resul2 = Place2.__repr__()
        actual2 = "Size: 0\nWorkers: "
        self.assertEqual(resul2, actual2)


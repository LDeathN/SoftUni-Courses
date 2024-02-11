from project.toy_store import ToyStore
from unittest import TestCase


class TestToyStore(TestCase):
    def test_constructor(self):
        Store1 = ToyStore()
        self.assertEqual(Store1.toy_shelf, {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })

    def test_add_toy_case1(self):
        Store1 = ToyStore()
        message = Store1.add_toy("A", "Naruto")
        self.assertEqual(message, "Toy:Naruto placed successfully!")
        self.assertEqual(Store1.toy_shelf, {
            "A": "Naruto",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })
        Store1.add_toy("B", "Luffy")
        Store1.add_toy("C", "Nami")
        Store1.add_toy("D", "Franky")
        Store1.add_toy("E", "Chopper")
        Store1.add_toy("F", "Robin")
        Store1.add_toy("G", "Zoro")
        self.assertEqual(Store1.toy_shelf, {
            "A": "Naruto",
            "B": "Luffy",
            "C": "Nami",
            "D": "Franky",
            "E": "Chopper",
            "F": "Robin",
            "G": "Zoro",
        })

    def test_add_toy_case2(self):
        Store1 = ToyStore()
        with self.assertRaises(Exception) as e:
            Store1.add_toy("O", "Kizaru")
        self.assertEqual(str(e.exception), "Shelf doesn't exist!")

    def test_add_toy_case3(self):
        Store1 = ToyStore()
        Store1.add_toy("A", "Kizaru")
        with self.assertRaises(Exception) as e:
            Store1.add_toy("A", "Kizaru")
        self.assertEqual(str(e.exception), "Toy is already in shelf!")

    def test_add_toy_case4(self):
        Store1 = ToyStore()
        Store1.add_toy("A", "Shanks")
        with self.assertRaises(Exception) as e:
            Store1.add_toy("A", "Kizaru")
        self.assertEqual(str(e.exception), "Shelf is already taken!")

    def test_remove_toy_case1(self):
        Store1 = ToyStore()
        Store1.add_toy("B", "Luffy")
        Store1.add_toy("C", "Nami")
        Store1.add_toy("D", "Franky")
        message = Store1.remove_toy("B", "Luffy")
        self.assertEqual(message, "Remove toy:Luffy successfully!")
        self.assertEqual(Store1.toy_shelf, {
            "A": None,
            "B": None,
            "C": "Nami",
            "D": "Franky",
            "E": None,
            "F": None,
            "G": None,
        })
        Store1.remove_toy("C", "Nami")
        Store1.remove_toy("D", "Franky")
        self.assertEqual(Store1.toy_shelf, {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })

    def test_remove_toy_case2(self):
        Store1 = ToyStore()
        Store1.add_toy("B", "Luffy")
        Store1.add_toy("C", "Nami")
        Store1.add_toy("D", "Franky")
        with self.assertRaises(Exception) as e:
            Store1.remove_toy("Q", "Luffy")
        self.assertEqual(str(e.exception), "Shelf doesn't exist!")

    def test_remove_toy_case3(self):
        Store1 = ToyStore()
        Store1.add_toy("B", "Luffy")
        Store1.add_toy("C", "Nami")
        Store1.add_toy("D", "Franky")
        with self.assertRaises(Exception) as e:
            Store1.remove_toy("D", "Luffy")
        self.assertEqual(str(e.exception), "Toy in that shelf doesn't exists!")


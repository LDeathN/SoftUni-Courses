from mammal.project.mammal import Mammal
import unittest


class TestMammal(unittest.TestCase):

    def test_constructor(self):
        dog = Mammal("Aik", "Dog", "Woof!")
        self.assertEqual(dog.name, "Aik")
        self.assertEqual(dog.type, "Dog")
        self.assertEqual(dog.sound, "Woof!")
        self.assertEqual(dog.get_kingdom(), "animals")

    def test_make_sound(self):
        dog = Mammal("Aik", "Dog", "Woof!")
        message = dog.make_sound()
        self.assertEqual(message, "Aik makes Woof!")

    def test_get_kingdom(self):
        dog = Mammal("Aik", "Dog", "Woof!")
        message = dog.get_kingdom()
        self.assertEqual(message, "animals")

    def test_info(self):
        dog = Mammal("Aik", "Dog", "Woof!")
        message = dog.info()
        self.assertEqual(message, "Aik is of type Dog")


if __name__ == '__main__':
    unittest.main()

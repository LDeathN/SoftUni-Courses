class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception("Already fed.")

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception("Cannot sleep while hungry")

        self.sleepy = False


import unittest


class CatTests(unittest.TestCase):

    def test_increase_size_after_eating(self):
        cat = Cat("Tom")
        cat.eat()
        self.assertEqual(cat.size, 1)

    def test_cat_is_fed_after_eating(self):
        cat = Cat("Jerry")
        cat.eat()
        self.assertEqual(cat.fed, True)

    def test_cat_cannot_eat_if_already_fed(self):
        cat = Cat("Tom")
        cat.eat()
        with self.assertRaises(Exception) as context:
            cat.eat()
        expected_message = "Already fed."
        self.assertEqual(str(context.exception), expected_message)

    def test_cat_cannot_sleep_if_not_fed(self):
        cat = Cat("Jerry")
        with self.assertRaises(Exception) as context:
            cat.sleep()
        expected_message = "Cannot sleep while hungry"
        self.assertEqual(str(context.exception), expected_message)

    def test_cat_not_sleepy_after_sleep(self):
        cat = Cat("Tom")
        cat.eat()
        cat.sleep()
        self.assertEqual(cat.sleepy, False)


if __name__ == '__main__':
    unittest.main()



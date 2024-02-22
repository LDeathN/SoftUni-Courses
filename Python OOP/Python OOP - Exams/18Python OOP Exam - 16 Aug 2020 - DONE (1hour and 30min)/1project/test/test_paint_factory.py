from project.factory.paint_factory import PaintFactory
from unittest import TestCase


class TestPaintFactory(TestCase):
    def test_constructor(self):
        factory = PaintFactory("Pain", 10)
        self.assertEqual(factory.name, "Pain")
        self.assertEqual(factory.capacity, 10)
        self.assertEqual(factory.ingredients, {})
        self.assertEqual(factory.valid_ingredients, ["white", "yellow", "blue", "green", "red"])
        factory2 = PaintFactory('', 20)
        self.assertEqual(factory2.name, "")
        self.assertEqual(factory2.capacity, 20)
        self.assertEqual(factory2.ingredients, {})
        self.assertEqual(factory2.valid_ingredients, ["white", "yellow", "blue", "green", "red"])

    def test_add_ingredient_case1(self):
        factory = PaintFactory("Pain", 10)
        self.assertEqual(factory.products, {})
        factory.add_ingredient("white", 3)
        self.assertEqual(factory.ingredients, {"white": 3})
        factory.add_ingredient("white", 2)
        self.assertEqual(factory.ingredients, {"white": 5})
        factory.add_ingredient("blue", 2)
        self.assertEqual(factory.ingredients, {"white": 5, "blue": 2})
        self.assertEqual(factory.products, {"white": 5, "blue": 2})
        with self.assertRaises(ValueError) as ve:
            factory.add_ingredient("red", 4)
        self.assertEqual(str(ve.exception), "Not enough space in factory")
        with self.assertRaises(TypeError) as ve2:
            factory.add_ingredient("purple", 2)
        self.assertEqual(str(ve2.exception), "Ingredient of type purple not allowed in PaintFactory")

    def test_remove_ingredient_case1(self):
        factory = PaintFactory("Pain", 10)
        factory.add_ingredient("white", 3)
        factory.add_ingredient("red", 2)
        factory.add_ingredient("blue", 2)
        factory.remove_ingredient("white", 2)
        self.assertEqual(factory.ingredients, {"white": 1, "red": 2, "blue": 2})
        factory.remove_ingredient("white", 1)
        self.assertEqual(factory.ingredients, {"white": 0, "red": 2, "blue": 2})
        with self.assertRaises(ValueError) as ve:
            factory.remove_ingredient("blue", 4)
        self.assertEqual(str(ve.exception), "Ingredients quantity cannot be less than zero")
        with self.assertRaises(KeyError) as ke:
            factory.remove_ingredient("lime", 2)
        self.assertEqual(str(ke.exception), "'No such ingredient in the factory'")

    def test_repr_method(self):
        factory = PaintFactory("Pain", 10)
        factory.add_ingredient("white", 3)
        factory.add_ingredient("red", 2)
        factory2 = PaintFactory("", 20)
        result = factory.__repr__()
        result2 = factory2.__repr__()
        actual = ["Factory name: Pain with capacity 10."]
        actual.append(f"white: 3\nred: 2\n")
        actual = "\n".join(actual)
        actual2 = "Factory name:  with capacity 20.\n"
        self.assertEqual(result, actual)
        self.assertEqual(result2, actual2)

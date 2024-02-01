from project.animals.animal import Mammal
from project.food import Vegetable, Meat, Fruit


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region, food_eaten=0)

    def make_sound(self):
        return f"Squeak"

    def feed(self, food):
        if isinstance(food, Vegetable) or isinstance(food, Fruit):
            self.weight += 0.10 * food.quantity
            self.food_eaten += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {type(food).__name__}!"


class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region, food_eaten=0)

    def make_sound(self):
        return f"Woof!"

    def feed(self, food):
        if isinstance(food, Meat):
            self.weight += 0.40 * food.quantity
            self.food_eaten += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {type(food).__name__}!"


class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region, food_eaten=0)

    def make_sound(self):
        return f"Meow"

    def feed(self, food):
        if isinstance(food, Vegetable) or isinstance(food, Meat):
            self.weight += 0.30 * food.quantity
            self.food_eaten += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {type(food).__name__}!"


class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region, food_eaten=0)

    def make_sound(self):
        return f"ROAR!!!"

    def feed(self, food):
        if isinstance(food, Meat):
            self.weight += 1.00 * food.quantity
            self.food_eaten += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {type(food).__name__}!"

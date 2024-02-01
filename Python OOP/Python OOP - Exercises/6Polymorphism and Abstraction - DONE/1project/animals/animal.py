from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, weight: float, food_eaten=0):
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self, food):
        pass

    @abstractmethod
    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.food_eaten}]"


class Bird(Animal):
    def __init__(self, name: str, weight: float, wing_size: float, food_eaten=0):
        super().__init__(name, weight, food_eaten)
        self.wing_size = wing_size

    @abstractmethod
    def make_sound(self):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal):
    def __init__(self, name: str, weight: float, living_region: str, food_eaten=0):
        super().__init__(name, weight, food_eaten)
        self.living_region = living_region

    @abstractmethod
    def make_sound(self):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"

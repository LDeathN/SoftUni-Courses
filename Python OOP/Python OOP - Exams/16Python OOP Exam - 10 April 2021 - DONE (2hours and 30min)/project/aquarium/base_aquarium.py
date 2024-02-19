from abc import ABC


class BaseAquarium(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip() or not value:
            raise ValueError(f"Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum([decoration.comfort for decoration in self.decorations])

    def add_fish(self, fish):
        if fish.fish_type in ["SaltwaterFish", "FreshwaterFish"]:
            if len(self.fish) < self.capacity:
                self.fish.append(fish)
                return f"Successfully added {type(fish).__name__} to {self.name}."
            else:
                return f"Not enough capacity."

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        fish_names = ' '.join([fish.name for fish in self.fish]) if self.fish else 'none'
        return f"{self.name}:\nFish: {fish_names}\nDecorations: {len(self.decorations)}\nComfort: {self.calculate_comfort()}"


from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.plant import Plant
from project.decoration.ornament import Ornament
from project.decoration.decoration_repository import DecorationRepository


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in ["FreshwaterAquarium", "SaltwaterAquarium"]:
            return f"Invalid aquarium type."
        elif aquarium_type == "FreshwaterAquarium":
            new_aquarium = FreshwaterAquarium(aquarium_name)
        elif aquarium_type == "SaltwaterAquarium":
            new_aquarium = SaltwaterAquarium(aquarium_name)
        self.aquariums.append(new_aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type not in ["Ornament", "Plant"]:
            return f"Invalid decoration type."
        elif decoration_type == "Ornament":
            new_decoration = Ornament()
        elif decoration_type == "Plant":
            new_decoration = Plant()
        self.decorations_repository.add(new_decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        aquarium = next((a for a in self.aquariums if a.name == aquarium_name), None)
        decoration = self.decorations_repository.find_by_type(decoration_type)
        if aquarium and decoration:
            aquarium.add_decoration(decoration)
            result = self.decorations_repository.remove(decoration)
            if result:
                return f"Successfully added {decoration_type} to {aquarium_name}."
        elif not decoration:
            return f"There isn't a decoration of type {decoration_type}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type not in ["FreshwaterFish", "SaltwaterFish"]:
            return f"There isn't a fish of type {fish_type}."
        elif fish_type == "FreshwaterFish":
            new_fish = FreshwaterFish(fish_name, fish_species, price)
        elif fish_type == "SaltwaterFish":
            new_fish = SaltwaterFish(fish_name, fish_species, price)
        aquarium = next((a for a in self.aquariums if a.name == aquarium_name), None)
        if aquarium:
            if new_fish.lives == type(aquarium).__name__:
                result = aquarium.add_fish(new_fish)
                return result
            else:
                return f"Water not suitable."

    def feed_fish(self, aquarium_name: str):
        aquarium = next((a for a in self.aquariums if a.name == aquarium_name), None)
        if aquarium:
            aquarium.feed()
            fed_count = len(aquarium.fish)
            return f"Fish fed: {fed_count}"

    def calculate_value(self, aquarium_name: str):
        aquarium = next((a for a in self.aquariums if a.name == aquarium_name), None)

        if aquarium:
            value = sum(fish.price for fish in aquarium.fish) + sum(
                decoration.price for decoration in aquarium.decorations)
            return f"The value of Aquarium {aquarium_name} is {value:.2f}."
        else:
            return f"There isn't an aquarium with the name {aquarium_name}."

    def report(self):
        result = []
        for aquarium in self.aquariums:
            result.append(aquarium.__str__())
        return "\n".join(result)



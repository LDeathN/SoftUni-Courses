from project.planet.planet_repository import PlanetRepository
from project.planet.planet import Planet
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.astronaut.astronaut_repository import AstronautRepository


class SpaceStation:
    astronaut_types = ["Biologist", "Geodesist", "Meteorologist"]
    completed_missions = 0
    failed_missions = 0

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type: str, name: str):
        astronaut = [a for a in self.astronaut_repository.astronauts if a.name == name]
        if astronaut:
            return f"{name} is already added."
        if astronaut_type not in self.astronaut_types:
            raise Exception(f"Astronaut type is not valid!")
        if astronaut_type == "Biologist":
            new_astronaut = Biologist(name)
        elif astronaut_type == "Geodesist":
            new_astronaut = Geodesist(name)
        elif astronaut_type == "Meteorologist":
            new_astronaut = Meteorologist(name)
        self.astronaut_repository.add(new_astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        planet = [p for p in self.planet_repository.planets if p.name == name]
        if planet:
            return f"{name} is already added."
        list_items = items.split(", ")
        new_planet = Planet(name)
        new_planet.items.extend(list_items)
        self.planet_repository.add(new_planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if not astronaut:
            raise Exception(f"Astronaut {name} doesn't exist!")
        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)
        if not planet:
            raise Exception(f"Invalid planet name!")
        astronauts = [a for a in self.astronaut_repository.astronauts if a.oxygen > 30]
        sorted_astronauts = sorted(astronauts, key=lambda a: -a.oxygen)
        if not sorted_astronauts:
            raise Exception(f"You need at least one astronaut to explore the planet!")
        going_astronauts = []
        for i in range(len(sorted_astronauts)):
            going_astronauts.append(sorted_astronauts[i])
            if len(going_astronauts) == 5:
                break
        mission_completed = False
        searched = 0
        for i in range(len(going_astronauts)):
            if mission_completed:
                break
            astronaut = going_astronauts[i]
            searched += 1
            while astronaut.oxygen > 0:
                astronaut.breathe()
                astronaut.backpack.append(planet.items.pop())
                if not planet.items:
                    mission_completed = True
                    break
        if mission_completed:
            self.planet_repository.remove(planet)
            self.completed_missions += 1
            return f"Planet: {planet_name} was explored. {searched} astronauts participated in collecting items."
        else:
            self.failed_missions += 1
            return f"Mission is not completed."

    def report(self):
        result = [f"{self.completed_missions} successful missions!"]
        result.append(f"{self.failed_missions} missions were not completed!")
        result.append(f"Astronauts' info:")
        for astronaut in self.astronaut_repository.astronauts:
            result.append(f"Name: {astronaut.name}")
            result.append(f"Oxygen: {astronaut.oxygen}")
            if astronaut.backpack:
                result.append(f"Backpack items: {', '.join(astronaut.backpack)}")
            else:
                result.append(f"Backpack items: none")
        return "\n".join(result)


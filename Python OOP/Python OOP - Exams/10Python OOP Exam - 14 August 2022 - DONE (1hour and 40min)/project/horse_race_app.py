from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey
from project.horse_race import HorseRace


class HorseRaceApp:
    valid_horse_types = ["Appaloosa", "Thoroughbred"]

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        horse = [h for h in self.horses if h.name == horse_name]
        if horse:
            raise Exception(f"Horse {horse_name} has been already added!")
        if horse_type not in self.valid_horse_types:
            return
        if horse_type == self.valid_horse_types[0]:
            new_horse = Appaloosa(horse_name, horse_speed)
        elif horse_type == self.valid_horse_types[1]:
            new_horse = Thoroughbred(horse_name, horse_speed)
        self.horses.append(new_horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        jockey = [j for j in self.jockeys if j.name == jockey_name]
        if jockey:
            raise Exception(f"Jockey {jockey_name} has been already added!")
        new_jockey = Jockey(jockey_name, age)
        self.jockeys.append(new_jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type_: str):
        race = [r for r in self.horse_races if r.race_type == race_type_]
        if race:
            raise Exception(f"Race {race_type_} has been already created!")
        new_race = HorseRace(race_type_)
        self.horse_races.append(new_race)
        return f"Race {race_type_} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = [j for j in self.jockeys if j.name == jockey_name]
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        jockey = jockey[0]
        horse = [h for h in self.horses if type(h).__name__ == horse_type and not h.is_taken]
        if not horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")
        if horse and jockey.horse:
            return f"Jockey {jockey_name} already has a horse."
        horse = horse.pop()
        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type_: str, jockey_name: str):
        race = [r for r in self.horse_races if r.race_type == race_type_]
        if not race:
            raise Exception(f"Race {race_type_} could not be found!")
        race = race[0]
        jockey = [j for j in self.jockeys if j.name == jockey_name]
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        jockey = jockey[0]
        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type_} race."
        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type_} race."

    def start_horse_race(self, race_type_: str):
        race = [r for r in self.horse_races if r.race_type == race_type_]
        if not race:
            raise Exception(f"Race {race_type_} could not be found!")
        race = race[0]
        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type_} needs at least two participants!")
        ordered = sorted(race.jockeys, key=lambda j: -j.horse.speed)
        winner = ordered[0]
        return f"The winner of the {race_type_} race, with a speed of {winner.horse.speed}km/h is {winner.name}! Winner's horse: {winner.horse.name}."




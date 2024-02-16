from project.race import Race
from project.driver import Driver
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type, model: str, speed_limit: int):
        car = [c for c in self.cars if c.model == model]
        if car:
            raise Exception(f"Car {model} is already created!")
        if car_type == "MuscleCar" or car_type == "SportsCar":
            if car_type == "MuscleCar":
                new_car = MuscleCar(model, speed_limit)
            elif car_type == "SportsCar":
                new_car = SportsCar(model, speed_limit)
            self.cars.append(new_car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        driver = [d for d in self.drivers if d.name == driver_name]
        if driver:
            raise Exception(f"Driver {driver_name} is already created!")
        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        race = [r for r in self.races if r.name == race_name]
        if race:
            raise Exception(f"Race {race_name} is already created!")
        new_race = Race(race_name)
        self.races.append(new_race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = [d for d in self.drivers if d.name == driver_name]
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")
        driver = driver[0]
        car = [c for c in self.cars if type(c).__name__ == car_type and not c.is_taken]
        if not car:
            raise Exception(f"Car {car_type} could not be found!")
        car = car.pop()
        if driver.car:
            old_one = driver.car
            old_one.is_taken = False
            driver.car = car
            car.is_taken = True
            return f"Driver {driver_name} changed his car from {old_one.model} to {car.model}."
        else:
            driver.car = car
            car.is_taken = True
            return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, drive_name: str):
        race = [r for r in self.races if r.name == race_name]
        if not race:
            raise Exception(f"Race {race_name} could not be found!")
        race = race[0]
        driver = [d for d in self.drivers if d.name == drive_name]
        if not driver:
            raise Exception(f"Driver {drive_name} could not be found!")
        driver = driver[0]
        if not driver.car:
            raise Exception(f"Driver {drive_name} could not participate in the race!")
        if driver in race.drivers:
            return f"Driver {drive_name} is already added in {race_name} race."
        race.drivers.append(driver)
        return f"Driver {drive_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = [r for r in self.races if r.name == race_name]
        if not race:
            raise Exception(f"Race {race_name} could not be found!")
        race = race[0]
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")
        order = sorted(race.drivers, key=lambda d: -d.car.speed_limit)
        first = order.pop(0)
        second = order.pop(0)
        third = order.pop(0)
        first.number_of_wins += 1
        second.number_of_wins += 1
        third.number_of_wins += 1
        result = [f"Driver {first.name} wins the {race_name} race with a speed of {first.car.speed_limit}."]
        result.append(f"Driver {second.name} wins the {race_name} race with a speed of {second.car.speed_limit}.")
        result.append(f"Driver {third.name} wins the {race_name} race with a speed of {third.car.speed_limit}.")
        return "\n".join(result)

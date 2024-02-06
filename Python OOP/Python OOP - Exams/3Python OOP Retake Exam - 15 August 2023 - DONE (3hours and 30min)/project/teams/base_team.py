from abc import ABC, abstractmethod


class BaseTeam(ABC):
    def __init__(self, name: str, country: str, advantage: int, budget: float):
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins = 0
        self.equipment = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError(f"Team name cannot be empty!")
        self.__name = value

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        if len(value.strip()) < 2:
            raise ValueError(f"Team country should be at least 2 symbols long!")
        self.__country = value

    @property
    def advantage(self):
        return self.__advantage

    @advantage.setter
    def advantage(self, value):
        if value <= 0:
            raise ValueError(f"Advantage must be greater than zero!")
        self.__advantage = value

    @abstractmethod
    def win(self):
        pass

    def get_statistics(self):
        result = []
        total_equipment_price = sum(equipment.price for equipment in self.equipment)
        avg_team_protection = sum(equipment.protection for equipment in self.equipment) / len(self.equipment) if self.equipment else 0
        result.append(f"Name: {self.name}")
        result.append(f"Country: {self.country}")
        result.append(f"Advantage: {self.advantage} points")
        result.append(f"Budget: {self.budget:.2f}EUR")
        result.append(f"Wins: {self.wins}")
        result.append(f"Total Equipment Price: {total_equipment_price:.2f}")
        result.append(f"Average Protection: {int(avg_team_protection)}")
        return "\n".join(result)

    def sum_points(self):
        return self.advantage + sum([eq.protection for eq in self.equipment])
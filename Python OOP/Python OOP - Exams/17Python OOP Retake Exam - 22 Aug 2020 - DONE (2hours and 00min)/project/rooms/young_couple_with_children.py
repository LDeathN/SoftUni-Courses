from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        super().__init__(family_name, budget=salary_one + salary_two, members_count=2 + len(children))
        self.room_cost = 30
        self.appliances = [TV(), Fridge(), Laptop()] * (2 + len(children))
        self.children.extend(children)
        self.calculate_expenses(self.appliances, self.children)



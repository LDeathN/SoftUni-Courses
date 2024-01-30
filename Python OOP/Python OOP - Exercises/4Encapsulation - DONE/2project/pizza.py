from project.dough import Dough
from project.topping import Topping


class Pizza:
    def __init__(self, name: str, dough: Dough, max_number_of_toppings: int):

        self.name = name
        self.dough = dough
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings = {}

        if self.name == "":
            raise ValueError("The name cannot be an empty string")

        if self.dough is None:
            raise ValueError("You should add dough to the pizza")

        if self.max_number_of_toppings <= 0:
            raise ValueError("The maximum number of toppings cannot be less or equal to zero")

    def add_topping(self, topping: Topping):
        if len(self.toppings) >= self.max_number_of_toppings:
            raise ValueError("Not enough space for another topping")

        if topping.get_topping_type() in self.toppings:
            self.toppings[topping.get_topping_type()] += topping.get_weight()
        else:
            self.toppings[topping.get_topping_type()] = topping.get_weight()

    def calculate_total_weight(self):
        total_weight = self.dough.get_weight() + sum(self.toppings.values())
        return total_weight

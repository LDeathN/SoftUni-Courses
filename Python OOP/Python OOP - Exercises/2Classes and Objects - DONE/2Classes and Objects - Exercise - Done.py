# First Problem

class Vet:
    animals = []
    space = 5
    def __init__(self, name):
        self.name = name
        self.animals = []

    def register_animal(self, animal_name):
        if len(Vet.animals) < Vet.space:
            Vet.animals.append(animal_name)
            self.animals.append(animal_name)
            return f"{animal_name} registered in the clinic"
        else:
            return f"Not enough space"

    def unregister_animal(self, animal_name):

        if animal_name in Vet.animals:
            Vet.animals.remove(animal_name)
            self.animals.remove(animal_name)
            return f"{animal_name} unregistered successfully"
        else:
            return f"{animal_name} not in the clinic"

    def info(self):
        return f"{self.name} has {len(self.animals)} animals. {Vet.space} space left in clinic"



# Second Problem

class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        if self.hours < 10 and self.minutes < 10 and self.seconds < 10:
            return f"0{self.hours}:0{self.minutes}:0{self.seconds}"
        elif self.hours < 10 and self.minutes < 10:
            return f"0{self.hours}:0{self.minutes}:{self.seconds}"
        elif self.hours < 10 and self.seconds < 10:
            return f"0{self.hours}:{self.minutes}:0{self.seconds}"
        elif self.minutes < 10 and self.seconds < 10:
            return f"{self.hours}:0{self.minutes}:0{self.seconds}"
        elif self.hours < 10:
            return f"0{self.hours}:{self.minutes}:{self.seconds}"
        elif self.minutes < 10:
            return f"{self.hours}:0{self.minutes}:{self.seconds}"
        elif self.seconds < 10:
            return f"{self.hours}:{self.minutes}:0{self.seconds}"
        else:
            return f"{self.hours}:{self.minutes}:{self.seconds}"

    def next_second(self):
        self.seconds += 1
        if self.seconds > self.max_seconds:
            self.seconds = 0
            self.minutes += 1
            if self.minutes > self.max_minutes:
                self.minutes = 0
                self.hours += 1
                if self.hours > self.max_hours:
                    self.hours = 0
        return self.get_time()



# Third Problem

class Account:
    def __init__(self, id, name, balance=0):
        self.id = id
        self.name = name
        self.balance = balance

    def credit(self, amount):
        self.balance += amount
        return self.balance

    def debit(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return f"Amount exceeded balance"

    def info(self):
        return f"User {self.name} with account {self.id} has {self.balance} balance"



# Fourth Problem

class PizzaDelivery:
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float):
        if not self.ordered:
            if ingredient in self.ingredients:
                self.ingredients[ingredient] += quantity
                self.price += price_per_quantity * quantity
            else:
                self.ingredients[ingredient] = quantity
                self.price += price_per_quantity * quantity
        else:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float):
        if not self.ordered:
            if ingredient not in self.ingredients:
                return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
            elif ingredient in self.ingredients and quantity > self.ingredients[ingredient]:
                return f"Please check again the desired quantity of {ingredient}!"
            else:
                self.ingredients[ingredient] -= quantity
                self.price -= price_per_quantity * quantity
        else:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

    def make_order(self):
        self.ordered = True
        return f"You've ordered pizza {self.name} prepared with {', '.join(f'{x}: {y}' for x, y in self.ingredients.items())} and the price will be {self.price}lv."






























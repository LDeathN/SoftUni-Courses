# First Problem

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        if self.fuel_quantity - distance * (self.fuel_consumption + 0.9) >= 0:
            self.fuel_quantity -= distance * (self.fuel_consumption + 0.9)

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        if self.fuel_quantity - distance * (self.fuel_consumption + 1.6) >= 0:
            self.fuel_quantity -= distance * (self.fuel_consumption + 1.6)

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95


# Second Problem

class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        return Person(self.name, other.surname)


class Group:
    def __init__(self, name: str, people: list):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        combined_name = f"{self.name} {other.name}"
        combined_people = self.people + other.people
        return Group(combined_name, combined_people)

    def __repr__(self):
        members_str = ", ".join(map(str, self.people))
        return f"Group {self.name} with members {members_str}"

    def __iter__(self):
        for index, person in enumerate(self.people, 0):
            yield f"Person {index}: {person}"

    def __getitem__(self, index):
        return f"Person {index}: {self.people[index]}"


# Third Problem

class Account:
    def __init__(self, owner: str, amount=0):
        self.begin_amount = amount
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def handle_transaction(self, transaction_amount):
        if self.amount + transaction_amount < 0:
            raise ValueError(f"sorry cannot go in debt!")
        else:
            self.amount += transaction_amount
            self._transactions.append(transaction_amount)
            return f"New balance: {self.amount}"

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError(f"please use int for amount")
        self.handle_transaction(amount)

    @property
    def balance(self):
        return self.amount

    def __repr__(self):
        return f"Account({self.owner}, {self.begin_amount})"

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.begin_amount}"

    def __len__(self):
        return len(self._transactions)

    def __iter__(self):
        for transaction in self._transactions:
            yield transaction

    def __reversed__(self):
        return reversed(self._transactions)

    def __add__(self, other):
        owner = f"{self.owner}&{other.owner}"
        amount = self.begin_amount + other.begin_amount
        new_account = Account(owner, amount)
        new_account._transactions = self._transactions + other._transactions
        return new_account

    def __le__(self, other):
        return self.amount <= other.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __ne__(self, other):
        return self.amount != other.amount

    def __ge__(self, other):
        return self.amount >= other.amount

    def __lt__(self, other):
        return self.amount < other.amount

    def __gt__(self, other):
        return self.amount > other.amount

    def __getitem__(self, index):
        return self._transactions[index]
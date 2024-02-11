from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.stolen import Stolen
from project.delicacies.gingerbread import Gingerbread


class ChristmasPastryShopApp:
    types_of_delicacies = ["Gingerbread", "Stolen"]
    types_of_booths = ["Open Booth", "Private Booth"]

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        delicacy = [d for d in self.delicacies if d.name == name]
        if delicacy:
            raise Exception(f"{name} already exists!")
        if type_delicacy not in self.types_of_delicacies:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")
        if type_delicacy == "Gingerbread":
            new_delicacy = Gingerbread(name, price)
        elif type_delicacy == "Stolen":
            new_delicacy = Stolen(name, price)
        self.delicacies.append(new_delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth, booth_number: int, capacity: int):
        booth = [b for b in self.booths if b.booth_number == booth_number]
        if booth:
            raise Exception(f"Booth number {booth_number} already exists!")
        if type_booth not in self.types_of_booths:
            raise Exception(f"{type_booth} is not a valid booth!")
        if type_booth == "Open Booth":
            new_booth = OpenBooth(booth_number, capacity)
        elif type_booth == "Private Booth":
            new_booth = PrivateBooth(booth_number, capacity)
        self.booths.append(new_booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        booth = [b for b in self.booths if not b.is_reserved and b.capacity >= number_of_people]
        if not booth:
            raise Exception(f"No available booth for {number_of_people} people!")
        booth = booth[0]
        booth.reserve(number_of_people)
        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = [b for b in self.booths if b.booth_number == booth_number]
        if not booth:
            raise Exception(f"Could not find booth {booth_number}!")
        booth = booth[0]
        delicacy = [d for d in self.delicacies if d.name == delicacy_name]
        if not delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")
        delicacy = delicacy[0]
        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = [b for b in self.booths if b.booth_number == booth_number][0]
        bill = booth.price_for_reservation + sum([d.price for d in booth.delicacy_orders])
        self.income += bill
        booth.delicacy_orders = []
        booth.is_reserved = False
        booth.price_for_reservation = 0
        return f"Booth {booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."



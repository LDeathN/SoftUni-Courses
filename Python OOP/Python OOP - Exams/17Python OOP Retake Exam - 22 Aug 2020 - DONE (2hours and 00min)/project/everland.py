from project.rooms.young_couple_with_children import YoungCoupleWithChildren
from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = sum(room.expenses + room.room_cost for room in self.rooms)
        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        result = []
        for room in self.rooms:
            cost = room.room_cost + room.expenses
            if room.budget >= cost:
                room.budget -= cost
                result.append(f"{room.family_name} paid {cost:.2f}$ and have {room.budget:.2f}$ left.")
            else:
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                self.rooms.remove(room)
        return "\n".join(result)

    def status(self):
        result = []
        all_people_in_the_hotel = sum(room.members_count for room in self.rooms)
        result.append(f"Total population: {all_people_in_the_hotel}")

        for room in self.rooms:
            if isinstance(room, YoungCoupleWithChildren):
                result.append(
                    f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$"
                )

                for child in room.children:
                    result.append(
                        f"--- Child {room.children.index(child) + 1} monthly cost: {child.get_monthly_expense():.2f}$"
                    )

                result.append(
                    f"--- Appliances monthly cost: {sum(appliance.get_monthly_expense() for appliance in room.appliances):.2f}$"
                )
            else:
                result.append(
                    f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$"
                )

                result.append(
                    f"--- Appliances monthly cost: {sum(appliance.get_monthly_expense() for appliance in room.appliances):.2f}$"
                )

        return "\n".join(result)


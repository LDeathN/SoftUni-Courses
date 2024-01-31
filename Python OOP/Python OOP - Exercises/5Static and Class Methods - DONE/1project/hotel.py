from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number and not room.is_taken:
                room.take_room(people)
                self.guests += room.guests

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number and room.is_taken:
                self.guests -= room.guests
                room.free_room()

    def status(self):
        result = f"Hotel {self.name} has {self.guests} total guests\n"
        free_rooms = [str(room.number) for room in self.rooms if not room.is_taken]
        taken_rooms = [str(room.number) for room in self.rooms if room.is_taken]
        result += f"Free rooms: {', '.join(free_rooms)}" + "\n"
        result += f"Taken rooms: {', '.join(taken_rooms)}"
        return result

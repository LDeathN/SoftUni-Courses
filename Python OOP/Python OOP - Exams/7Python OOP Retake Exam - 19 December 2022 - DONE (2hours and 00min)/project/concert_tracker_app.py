from project.band_members.singer import Singer
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band import Band
from project.concert import Concert


class ConcertTrackerApp:
    musician_types = ["Guitarist", "Drummer", "Singer"]

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type, name: str, age: int):
        if musician_type not in self.musician_types:
            raise ValueError("Invalid musician type!")
        musician = [m for m in self.musicians if m.name == name]
        if musician:
            raise Exception(f"{name} is already a musician!")
        if musician_type == "Guitarist":
            new_musician = Guitarist(name, age)
        elif musician_type == "Drummer":
            new_musician = Drummer(name, age)
        elif musician_type == "Singer":
            new_musician = Singer(name, age)
        self.musicians.append(new_musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        band = [b for b in self.bands if b.name == name]
        if band:
            raise Exception(f"{name} band is already created!")
        new_band = Band(name)
        self.bands.append(new_band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert = [c for c in self.concerts if c.place == place]
        if concert:
            concert = concert[0]
            raise Exception(f"{place} is already registered for {concert.genre} concert!")
        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = [m for m in self.musicians if m.name == musician_name]
        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")
        musician = musician[0]
        band = [b for b in self.bands if b.name == band_name]
        if not band:
            raise Exception(f"{band_name} isn't a band!")
        band = band[0]
        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = [b for b in self.bands if b.name == band_name]
        if not band:
            raise Exception(f"{band_name} isn't a band!")
        band = band[0]
        musician = [m for m in band.members if m.name == musician_name]
        if not musician:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")
        musician = musician[0]
        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = [b for b in self.bands if b.name == band_name][0]
        concert = [c for c in self.concerts if c.place == concert_place][0]
        guitarists = [g for g in band.members if type(g).__name__ == "Guitarist"]
        drummers = [d for d in band.members if type(d).__name__ == "Drummer"]
        singers = [s for s in band.members if type(s).__name__ == "Singer"]
        if not len(guitarists) >= 1 or not len(drummers) >= 1 or not len(singers) >= 1:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")
        band_ready = True
        if concert.genre == "Rock":
            for musician in guitarists:
                if "play rock" not in musician.skills:
                    band_ready = False
            for musician in drummers:
                if "play the drums with drumsticks" not in musician.skills:
                    band_ready = False
            for musician in singers:
                if "sing high pitch notes" not in musician.skills:
                    band_ready = False
        elif concert.genre == "Metal":
            for musician in guitarists:
                if "play metal" not in musician.skills:
                    band_ready = False
            for musician in drummers:
                if "play the drums with drumsticks" not in musician.skills:
                    band_ready = False
            for musician in singers:
                if "sing low pitch notes" not in musician.skills:
                    band_ready = False
        elif concert.genre == "Jazz":
            for musician in guitarists:
                if "play jazz" not in musician.skills:
                    band_ready = False
            for musician in drummers:
                if "play the drums with drum brushes" not in musician.skills:
                    band_ready = False
            for musician in singers:
                if "sing high pitch notes" not in musician.skills or "sing low pitch notes" not in musician.skills:
                    band_ready = False
        if not band_ready:
            raise Exception(f"The {band_name} band is not ready to play at the concert!")
        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."

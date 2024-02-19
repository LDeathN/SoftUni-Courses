from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    lives = "FreshwaterAquarium"
    fish_type = "FreshwaterFish"

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, size=3, price=price)

    def eat(self):
        self.size += 3

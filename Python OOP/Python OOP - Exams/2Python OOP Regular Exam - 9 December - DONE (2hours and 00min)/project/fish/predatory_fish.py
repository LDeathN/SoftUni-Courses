from project.fish.base_fish import BaseFish


class PredatoryFish(BaseFish):
    type_ = "PredatoryFish"
    predatory_time_to_catch = 90

    def __init__(self, name: str, points: float):
        super().__init__(name, points, self.predatory_time_to_catch)

    def fish_details(self):
        return f"{self.type_}: {self.name} [Points: {self.points}, Time to Catch: {self.predatory_time_to_catch} seconds]"

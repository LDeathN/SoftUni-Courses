from project.fish.base_fish import BaseFish


class DeepSeaFish(BaseFish):
    type_ = "DeepSeaFish"
    predatory_time_to_catch = 180

    def __init__(self, name: str, points: float):
        super().__init__(name, points, self.predatory_time_to_catch)

    def fish_details(self):
        return f"{self.type_}: {self.name} [Points: {self.points}, Time to Catch: {self.predatory_time_to_catch} seconds]"

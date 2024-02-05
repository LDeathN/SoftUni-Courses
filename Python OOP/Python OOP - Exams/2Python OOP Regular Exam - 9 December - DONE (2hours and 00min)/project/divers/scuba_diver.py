from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    type_ = "ScubaDiver"
    diver_oxygen_level = 540

    def __init__(self, name: str):
        super().__init__(name, self.diver_oxygen_level)

    def miss(self, time_to_catch: int):
        if self.oxygen_level < round(time_to_catch * 0.3):
            self.oxygen_level = 0
        else:
            self.oxygen_level -= round(time_to_catch * 0.3)

    def renew_oxy(self):
        self.oxygen_level = self.diver_oxygen_level


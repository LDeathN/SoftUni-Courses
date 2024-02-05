from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    type_ = "FreeDiver"
    diver_oxygen_level = 120

    def __init__(self, name: str):
        super().__init__(name, self.diver_oxygen_level)

    def miss(self, time_to_catch: int):
        if self.oxygen_level < round(time_to_catch * 0.6):
            self.oxygen_level = 0
        else:
            self.oxygen_level -= round(time_to_catch * 0.6)

    def renew_oxy(self):
        self.oxygen_level = self.diver_oxygen_level


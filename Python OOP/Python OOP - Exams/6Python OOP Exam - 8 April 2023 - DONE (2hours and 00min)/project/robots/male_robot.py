from project.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):
    type_ = "MaleRobot"
    weight = 9

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, weight=self.weight)

    def eating(self):
        self.weight += 3

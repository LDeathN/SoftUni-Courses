from project.car.car import Car


class MuscleCar(Car):
    SPEED_LIMIT_MIN = 250
    SPEED_LIMIT_MAX = 450

    def __init__(self, model: str, speed_limit: int):
        super().__init__(model, speed_limit)

from project.car.car import Car


class SportsCar(Car):
    SPEED_LIMIT_MIN = 400
    SPEED_LIMIT_MAX = 600

    def __init__(self, model: str, speed_limit: int):
        super().__init__(model, speed_limit)

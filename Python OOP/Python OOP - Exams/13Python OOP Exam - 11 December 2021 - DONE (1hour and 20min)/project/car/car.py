from abc import ABC


class Car(ABC):
    SPEED_LIMIT_MIN = None
    SPEED_LIMIT_MAX = None

    def __init__(self, model: str, speed_limit: int):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if len(value) < 4:
            raise ValueError(f"Model {value} is less than 4 symbols!")
        self.__model = value

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        if not self.SPEED_LIMIT_MIN <= value <= self.SPEED_LIMIT_MAX:
            raise ValueError(f"Invalid speed limit! Must be between {self.SPEED_LIMIT_MIN} and {self.SPEED_LIMIT_MAX}!")
        self.__speed_limit = value


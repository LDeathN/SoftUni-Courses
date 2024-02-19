from abc import ABC


class BaseDecoration(ABC):
    def __init__(self, comfort: int, price: float):
        self.comfort = comfort
        self.price = price

    @property
    def comfort(self):
        return self.__comfort

    @comfort.setter
    def comfort(self, value):
        self.__comfort = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value


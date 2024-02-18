from project.drink.drink import Drink


class Tea(Drink):
    type_price = 2.50

    def __init__(self, name: str, portion: float, brand: str):
        super().__init__(name, portion, self.type_price, brand)


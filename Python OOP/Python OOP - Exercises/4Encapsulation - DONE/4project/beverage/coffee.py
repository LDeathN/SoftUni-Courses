from project.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    MILLILITERS = 50
    PRICE = 3.50

    def __init__(self, name: str, caffeine: float):
        super().__init__(name, Coffee.PRICE, Coffee.MILLILITERS)
        self._Coffee__caffeine = caffeine

    @property
    def caffeine(self):
        return self._Coffee__caffeine

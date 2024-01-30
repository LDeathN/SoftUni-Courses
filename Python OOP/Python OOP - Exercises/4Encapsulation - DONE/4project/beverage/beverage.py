from project.product import Product


class Beverage(Product):
    def __init__(self, name: str, price: float, milliliters: float):
        super().__init__(name, price)
        self._Beverage__milliliters = milliliters

    @property
    def milliliters(self):
        return self._Beverage__milliliters

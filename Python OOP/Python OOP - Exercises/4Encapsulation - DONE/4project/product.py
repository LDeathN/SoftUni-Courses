class Product:
    def __init__(self, name: str, price: float):
        self._Product__name = name
        self._Product__price = price

    @property
    def name(self):
        return self._Product__name

    @property
    def price(self):
        return self._Product__price

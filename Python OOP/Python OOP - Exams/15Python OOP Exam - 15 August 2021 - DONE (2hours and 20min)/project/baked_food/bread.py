from project.baked_food.baked_food import BakedFood


class Bread(BakedFood):
    bread_portion = 200

    def __init__(self, name: str, price: float):
        super().__init__(name, self.bread_portion, price)


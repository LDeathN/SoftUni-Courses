from project.delicacies.delicacy import Delicacy


class Stolen(Delicacy):
    type_portion = 250

    def __init__(self, name: str, price: float):
        super().__init__(name, self.type_portion, price)

    def details(self):
        return f"Stolen {self.name}: 250g - {self.price:.2f}lv."

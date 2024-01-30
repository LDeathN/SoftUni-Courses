class Topping:
    def __init__(self, topping_type: str, weight: float):

        self.__topping_type = topping_type
        self.__weight = weight

        if not self.__topping_type:
            raise ValueError("The topping type cannot be an empty string")

        if self.__weight <= 0:
            raise ValueError("The weight cannot be less or equal to zero")

    def get_topping_type(self):
        return self.__topping_type

    def get_weight(self):
        return self.__weight

class Dough:
    def __init__(self, flour_type: str, baking_technique: str, weight: float):

        self.__flour_type = flour_type
        self.__baking_technique = baking_technique
        self.__weight = weight

        if not self.__flour_type:
            raise ValueError("The flour type cannot be an empty string")

        if not self.__baking_technique:
            raise ValueError("The baking technique cannot be an empty string")

        if self.__weight <= 0:
            raise ValueError("The weight cannot be less or equal to zero")

    def get_flour_type(self):
        return self.__flour_type

    def get_baking_technique(self):
        return self.__baking_technique

    def get_weight(self):
        return self.__weight
    
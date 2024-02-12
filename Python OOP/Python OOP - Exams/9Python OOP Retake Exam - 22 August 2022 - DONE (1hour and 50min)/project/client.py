class Client:

    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart = []
        self.bill = 0.0
        self.ordered_meals = {}

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        error = False
        for symbol in value:
            if symbol.isalpha():
                error = True
        if value[0] != "0" or len(value) != 10 or error:
            raise ValueError("Invalid phone number!")
        self.__phone_number = value


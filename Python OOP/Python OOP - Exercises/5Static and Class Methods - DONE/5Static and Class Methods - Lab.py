# First Problem

class Calculator:

    @staticmethod
    def add(self, *args):
        result = sum(int(x) for x in args)
        return result

    @staticmethod
    def multiply(self, *args):
        result = 1
        for x in args:
            result *= int(x)
        return result

    @staticmethod
    def divide(self, *args):
        result = int(args[0])
        for i in range(1, len(args)):
            result /= int(args[i])
        return result

    @staticmethod
    def subtract(self, *args):
        result = int(args[0])
        for i in range(1, len(args)):
            result -= int(args[i])
        return result


# Second Problem

class Shop:
    def __init__(self, name: str, type: str, capacity: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}

    @staticmethod
    def small_shop(name: str, type: str):
        return Shop(name, type, 10)

    def add_item(self, item_name: str):
        if sum(self.items.values()) >= self.capacity:
            return f"Not enough capacity in the shop"
        if item_name not in self.items:
            self.items[item_name] = 0
        self.items[item_name] += 1
        return f"{item_name} added to the shop"

    def remove_item(self, item_name: str, amount: int):
        if item_name in self.items:
            if self.items[item_name] >= amount:
                self.items[item_name] -= amount

                if self.items[item_name] == 0:
                    del self.items[item_name]
                return f"{amount} {item_name} removed from the shop"
        return f"Cannot remove {amount} {item_name}"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"


# Third Problem

class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if type(float_value) == float:
            return cls(int(float_value))
        else:
            return f"value is not a float"

    @classmethod
    def from_roman(cls, value):
        answer = 0
        i = 0
        roman_numbers = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50, "XC": 90, "C":100, "CD":400, "D": 500, "CM": 900, "M": 1000}
        while (i < len(value)):
            for letter, number in roman_numbers.items():
                if letter == value[i]:
                    s1 = number
                    break
            if (i + 1 < len(value)):
                for letter, number in roman_numbers.items():
                    if letter == value[i + 1]:
                        s2 = number
                        if s1 >= s2:
                            answer = answer + s1
                            i = i + 1
                            break
                        else:
                            answer = answer + s2 - s1
                            i = i + 2
                            break
            else:
                answer = answer + s1
                i = i + 1
        return cls(answer)


    @classmethod
    def from_string(cls, value):
        if value == str(value):
            return cls(int(value))
        else:
            return "wrong type"


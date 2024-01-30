from project.animal import Animal


class Lion(Animal):
    def __init__(self, name, age, gender, money_for_care=50):
        Animal.__init__(self, name, age, gender, money_for_care)

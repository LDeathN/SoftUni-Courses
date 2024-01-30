from project.animal import Animal


class Cheetah(Animal):
    def __init__(self, name, age, gender, money_for_care=60):
        Animal.__init__(self, name, age, gender, money_for_care)

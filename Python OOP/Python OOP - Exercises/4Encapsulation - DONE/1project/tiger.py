from project.animal import Animal


class Tiger(Animal):
    def __init__(self, name, age, gender, money_for_care=45):
        Animal.__init__(self, name, age, gender, money_for_care)

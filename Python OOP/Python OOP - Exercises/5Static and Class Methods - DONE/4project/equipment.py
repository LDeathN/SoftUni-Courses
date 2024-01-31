class Equipment:
    id = 1

    def __init__(self, name: str):
        self.name = name
        self.equipment_id = Equipment.next_id()
        self.id = self.equipment_id

    @classmethod
    def next_id(cls):
        next_id = cls.id
        cls.id += 1
        return next_id

    def __repr__(self):
        return f"Equipment <{self.equipment_id}> {self.name}"

    @staticmethod
    def get_next_id():
        return Equipment.id

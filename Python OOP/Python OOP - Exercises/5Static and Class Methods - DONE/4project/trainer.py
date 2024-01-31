class Trainer:
    id = 1

    def __init__(self, name: str):
        self.name = name
        self.trainer_id = Trainer.next_id()
        self.id = self.trainer_id

    @classmethod
    def next_id(cls):
        next_id = cls.id
        cls.id += 1
        return next_id

    @staticmethod
    def get_next_id():
        return Trainer.id

    def __repr__(self):
        return f"Trainer <{self.trainer_id}> {self.name}"

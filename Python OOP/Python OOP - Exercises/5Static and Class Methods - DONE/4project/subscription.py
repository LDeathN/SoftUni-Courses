class Subscription:
    id = 1

    def __init__(self, date: str, customer_id: int, trainer_id: int, exercise_id: int):
        self.date = date
        self.customer_id = customer_id
        self. trainer_id = trainer_id
        self.exercise_id = exercise_id
        self.subscription_id = Subscription.next_id()
        self.id = self.subscription_id

    @classmethod
    def next_id(cls):
        next_id = cls.id
        cls.id += 1
        return next_id

    @staticmethod
    def get_next_id():
        return Subscription.id

    def __repr__(self):
        return f"Subscription <{self.subscription_id}> on {self.date}"

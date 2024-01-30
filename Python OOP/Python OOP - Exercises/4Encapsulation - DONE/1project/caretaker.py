from project.worker import Worker


class Caretaker(Worker):
    def __init__(self, name, age, salary):
        Worker.__init__(self, name, age, salary)
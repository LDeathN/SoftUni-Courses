from project.worker import Worker


class Vet(Worker):
    def __init__(self, name, age, salary):
        Worker.__init__(self, name, age, salary)
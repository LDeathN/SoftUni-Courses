from project.worker import Worker
from project.animal import Animal
class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self._Zoo__budget = budget
        self._Zoo__animal_capacity = animal_capacity
        self._Zoo__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self._Zoo__budget - price >= 0 and len(self.animals) < self._Zoo__animal_capacity:
            self.animals.append(animal)
            self._Zoo__budget -= price
            return f"{animal.name} the {type(animal).__name__} added to the zoo"
        elif self._Zoo__budget - price >= 0:
            return f"Not enough space for animal"
        elif len(self.animals) < self._Zoo__animal_capacity:
            return f"Not enough budget"

    def hire_worker(self, worker):
        if len(self.workers) < self._Zoo__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        else:
            return f"Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries = 0
        for worker in self.workers:
            salaries += worker.salary
        if self._Zoo__budget >= salaries:
            self._Zoo__budget -= salaries
            return f"You payed your workers. They are happy. Budget left: {self._Zoo__budget}"
        else:
            return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        cost = 0
        for animal in self.animals:
            cost += animal.money_for_care
        if self._Zoo__budget >= cost:
            self._Zoo__budget -= cost
            return f"You tended all the animals. They are happy. Budget left: {self._Zoo__budget}"
        else:
            return f"You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self._Zoo__budget += amount

    def animals_status(self):
        amount_of_lions = sum(1 for animal in self.animals if type(animal).__name__ == "Lion")
        amount_of_tigers = sum(1 for animal in self.animals if type(animal).__name__ == "Tiger")
        amount_of_cheetahs = sum(1 for animal in self.animals if type(animal).__name__ == "Cheetah")
        lions = '\n'.join(Animal.__repr__(animal) for animal in self.animals if type(animal).__name__ == 'Lion')
        tigers = ('\n'.join(Animal.__repr__(animal) for animal in self.animals if type(animal).__name__ == 'Tiger'))
        cheetahs = ('\n'.join(Animal.__repr__(animal) for animal in self.animals if type(animal).__name__ == 'Cheetah'))
        return f"You have {len(self.animals)} animals\n" \
               f"----- {amount_of_lions} Lions:\n" \
               f"{lions}\n" \
               f"----- {amount_of_tigers} Tigers:\n" \
               f"{tigers}\n" \
               f"----- {amount_of_cheetahs} Cheetahs:\n" \
               f"{cheetahs}"

    def workers_status(self):
        amount_of_keepers = sum(1 for worker in self.workers if type(worker).__name__ == "Keeper")
        amount_of_caretakers = sum(1 for worker in self.workers if type(worker).__name__ == "Caretaker")
        amount_of_vets = sum(1 for worker in self.workers if type(worker).__name__ == "Vet")
        keepers = ('\n'.join(Worker.__repr__(worker) for worker in self.workers if type(worker).__name__ == 'Keeper'))
        caretakers = ('\n'.join(Worker.__repr__(worker) for worker in self.workers if type(worker).__name__ == 'Caretaker'))
        vets = ('\n'.join(Worker.__repr__(worker) for worker in self.workers if type(worker).__name__ == 'Vet'))
        return f"You have {len(self.workers)} workers\n" \
               f"----- {amount_of_keepers} Keepers:\n" \
               f"{keepers}\n" \
               f"----- {amount_of_caretakers} Caretakers:\n" \
               f"{caretakers}\n" \
               f"----- {amount_of_vets} Vets:\n" \
               f"{vets}"

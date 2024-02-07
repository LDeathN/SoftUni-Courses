from project.clients.base_client import BaseClient


class Student(BaseClient):
    interest = 2.0
    type_ = "Student"

    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, self.interest)

    def increase_clients_interest(self):
        self.interest += 1.0

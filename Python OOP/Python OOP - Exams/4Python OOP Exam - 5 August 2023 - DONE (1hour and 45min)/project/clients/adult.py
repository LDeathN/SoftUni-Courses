from project.clients.base_client import BaseClient


class Adult(BaseClient):
    interest = 4.0
    type_ = "Adult"

    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, self.interest)

    def increase_clients_interest(self):
        self.interest += 2.0

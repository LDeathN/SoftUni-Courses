from project.clients.student import Student
from project.clients.adult import Adult
from project.loans.student_loan import StudentLoan
from project.loans.mortgage_loan import MortgageLoan


class BankApp:
    granted_loans = 0
    granted_sum = 0

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type: str):
        if loan_type == StudentLoan.type_:
            new_loan = StudentLoan()
            self.loans.append(new_loan)
            return f"{loan_type} was successfully added."
        elif loan_type == MortgageLoan.type_:
            new_loan = MortgageLoan()
            self.loans.append(new_loan)
            return f"{loan_type} was successfully added."
        else:
            raise Exception("Invalid loan type!")

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type == Student.type_:
            if len(self.clients) < self.capacity:
                new_client = Student(client_name, client_id, income)
                self.clients.append(new_client)
                return f"{client_type} was successfully added."
            else:
                return "Not enough bank capacity."
        elif client_type == Adult.type_:
            if len(self.clients) < self.capacity:
                new_client = Adult(client_name, client_id, income)
                self.clients.append(new_client)
                return f"{client_type} was successfully added."
            else:
                return "Not enough bank capacity."
        else:
            raise Exception("Invalid client type!")

    def grant_loan(self, loan_type, client_id: str):
        loan = self.get_loan_by_loan_type(loan_type)
        client = self.get_client_by_client_id(client_id)
        if loan.type_ == "StudentLoan" and client.type_ == "Student":
            self.granted_loans += 1
            self.granted_sum += loan.amount
            client.loans.append(loan)
            self.loans.remove(loan)
            return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."
        elif loan.type_ == "MortgageLoan" and client.type_ == "Adult":
            self.granted_loans += 1
            self.granted_sum += loan.amount
            client.loans.append(loan)
            self.loans.remove(loan)
            return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."
        else:
            raise Exception("Inappropriate loan type!")

    def remove_client(self, client_id: str):
        client = self.get_client_by_client_id(client_id)
        if client:
            if client.loans:
                raise Exception("The client has loans! Removal is impossible!")
            else:
                self.clients.remove(client)
                return f"Successfully removed {client.name} with ID {client_id}."
        else:
            raise Exception("No such client!")

    def increase_loan_interest(self, loan_type: str):
        changed_loans = len([loan.increase_interest_rate() for loan in self.loans if loan.type_ == loan_type])
        return f"Successfully changed {changed_loans} loans."

    def increase_clients_interest(self, min_rate: float):
        changed_clients_rates = len([c.increase_clients_interest() for c in self.clients if c.interest < min_rate])
        return f"Number of clients affected: {changed_clients_rates}."

    def get_statistics(self):
        result = []
        avg_client_rate = sum([client.interest for client in self.clients]) / len(self.clients) if self.clients else 0
        result.append(f"Active Clients: {len(self.clients)}")
        result.append(f"Total Income: {sum([c.income for c in self.clients]):.2f}")
        result.append(f"Granted Loans: {self.granted_loans}, Total Sum: {self.granted_sum:.2f}")
        result.append(f"Available Loans: {len(self.loans)}, Total Sum: {sum([l.amount for l in self.loans]):.2f}")
        result.append(f"Average Client Interest Rate: {avg_client_rate:.2f}")
        return "\n".join(result)

    def get_loan_by_loan_type(self, loan_type):
        collection = [loan for loan in self.loans if loan.type_ == loan_type]
        return collection[0] if collection else None

    def get_client_by_client_id(self, client_id):
        collection = [c for c in self.clients if c.client_id == client_id]
        return collection[0] if collection else None



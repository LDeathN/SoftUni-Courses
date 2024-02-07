from project.loans.base_loan import BaseLoan


class MortgageLoan(BaseLoan):
    interest_rate = 3.5
    amount = 50000.0
    type_ = "MortgageLoan"

    def __init__(self):
        super().__init__(self.interest_rate, self.amount)

    def increase_interest_rate(self):
        self.interest_rate += 0.5

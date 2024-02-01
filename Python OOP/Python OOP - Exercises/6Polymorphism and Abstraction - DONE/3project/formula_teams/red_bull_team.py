from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    def __init__(self, budget: int):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int):
        oracle_sponsor = {1: 1500000, 2: 800000}
        honda_sponsor = {8: 20000, 10: 10000}
        expenses = 250000

        revenue1 = 0
        revenue2 = 0
        for position, price in oracle_sponsor.items():
            if race_pos == position or race_pos < position:
                if revenue1 < price:
                    revenue1 = price
        for position, price in honda_sponsor.items():
            if race_pos == position or race_pos < position:
                if revenue2 < price:
                    revenue2 = price

        revenue = (revenue1 + revenue2) - expenses
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"

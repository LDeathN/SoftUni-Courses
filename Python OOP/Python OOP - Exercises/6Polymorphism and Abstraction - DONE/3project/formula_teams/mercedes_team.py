from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    def __init__(self, budget: int):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int):
        petronas_sponsor = {1: 1000000, 3: 500000}
        teamviewer_sponsor = {5: 100000, 7: 50000}
        expenses = 200000

        revenue1 = 0
        revenue2 = 0
        for position, price in petronas_sponsor.items():
            if race_pos == position or race_pos < position:
                if revenue1 < price:
                    revenue1 = price
        for position, price in teamviewer_sponsor.items():
            if race_pos == position or race_pos < position:
                if revenue2 < price:
                    revenue2 = price

        revenue = (revenue1 + revenue2) - expenses
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"

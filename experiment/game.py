class Payoff:
    def __init__(self, row_payoff, column_payoff):
        self.row_payoff = row_payoff
        self.column_payoff = column_payoff


class Row:
    def __init__(self, column_a: Payoff, column_b: Payoff):
        self.column_a = column_a
        self.column_b = column_b


class Game:
    def __init__(self, row_a, row_b):
        self.row_a = row_a
        self.row_b = row_b






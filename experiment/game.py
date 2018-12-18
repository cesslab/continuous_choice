from otree.api import Currency as c
from typing import List


class Payoff:
    def __init__(self, row_payoff, column_payoff):
        self.row_payoff = c(row_payoff)
        self.column_payoff = c(column_payoff)


class Game:
    A = 1
    B = 2
    NONE = 0

    def __init__(self, game: List[List[Payoff]]):
        self.game = game

    @property
    def row_aa(self):
        return self.game[0][0].row_payoff

    @property
    def row_ab(self):
        return self.game[0][1].row_payoff

    @property
    def row_ba(self):
        return self.game[1][0].row_payoff

    @property
    def row_bb(self):
        return self.game[1][1].row_payoff

    @property
    def column_aa(self):
        return self.game[0][0].column_payoff

    @property
    def column_ab(self):
        return self.game[0][1].column_payoff

    @property
    def column_ba(self):
        return self.game[1][0].column_payoff

    @property
    def column_bb(self):
        return self.game[1][1].column_payoff

    def row_payoff(self, row_move, column_move):
        if row_move == Game.NONE or column_move == Game.NONE:
            return c(0)
        return self.game[row_move - 1][column_move - 1].row_payoff

    def column_payoff(self, row_move, column_move):
        if row_move == Game.NONE or column_move == Game.NONE:
            return c(0)
        return self.game[row_move - 1][column_move - 1].column_payoff








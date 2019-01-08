from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from experiment.game import Game, Payoff

author = 'Anwar A. Ruff '

doc = """
Practice Stage
"""


class Constants(BaseConstants):
    name_in_url = 'practice'
    players_per_group = None
    num_rounds = 1
    column_moves = [Game.B]
    games = [
        Game([[Payoff(5, 8), Payoff(7, 3)], [Payoff(8, 0), Payoff(6, 4)]]),
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    strategies = models.LongStringField()
    row_move = models.IntegerField(choices=[0, 1, 2])
    random_time = models.IntegerField(min=0, max=60)

    def set_payoff(self):
        game = Constants.games[self.round_number - 1]
        column_move = Constants.column_moves[self.round_number - 1]
        self.payoff = game.row_payoff(self.row_move, column_move)


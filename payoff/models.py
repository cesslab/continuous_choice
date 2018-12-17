from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from experiment.game import Game, Row, Payoff

author = 'Anwar A. RUff'

doc = """
Payoff Phase
"""


class Constants(BaseConstants):
    name_in_url = 'payoff'
    players_per_group = None
    num_rounds = 4


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass

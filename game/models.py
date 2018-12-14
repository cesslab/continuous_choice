from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from experiment.game import Game, Row, Payoff

author = 'Anwar A. Ruff'

doc = """
Game Play Stage
"""


class Constants(BaseConstants):
    name_in_url = 'game'
    players_per_group = None
    num_rounds = 20
    games = [
        # PC800, 100
        Game(Row(Payoff(800, 800), Payoff(100, 100)), Row(Payoff(100, 100), Payoff(500, 500))),
        # BOS 800, 100
        Game(Row(Payoff(800, 500), Payoff(100, 100)), Row(Payoff(100, 100), Payoff(500, 800))),
        # PD 300
        Game(Row(Payoff(300, 300), Payoff(100, 400)), Row(Payoff(400, 100), Payoff(200, 200))),
        # CS 400
        Game(Row(Payoff(400, 100), Payoff(100, 400)), Row(Payoff(100, 400), Payoff(400, 100))),
        # It Dom
        Game(Row(Payoff(300, 100), Payoff(200, 200)), Row(Payoff(100, 400), Payoff(400, 300))),
        # Strict Dom 300
        Game(Row(Payoff(300, 300), Payoff(400, 400)), Row(Payoff(200, 100), Payoff(200, 300))),
        # CH1
        Game(Row(Payoff(800, 800), Payoff(500, 1000)), Row(Payoff(1000, 500), Payoff(400, 400))),
        # CH2
        Game(Row(Payoff(800, 800), Payoff(500, 1000)), Row(Payoff(1000, 500), Payoff(0, 0))),
        # PD 800
        Game(Row(Payoff(800, 800), Payoff(100, 1000)), Row(Payoff(1000, 100), Payoff(500, 500))),
        # Strict Dom 800
        Game(Row(Payoff(800, 800), Payoff(900, 900)), Row(Payoff(700, 600), Payoff(700, 800))),
        # BOS 800
        Game(Row(Payoff(800, 500), Payoff(0, 0)), Row(Payoff(0, 0), Payoff(500, 800))),
        # PC 0
        Game(Row(Payoff(800, 800), Payoff(0, 0)), Row(Payoff(0, 0), Payoff(500, 500))),
        # Strict Dom 500
        Game(Row(Payoff(800, 800), Payoff(900, 900)), Row(Payoff(700, 600), Payoff(700, 800))),
        # Weak Dom Trust 0, 600
        Game(Row(Payoff(0, 600), Payoff(900, 600)), Row(Payoff(400, 500), Payoff(400, 500))),
        # Strict Dom 700
        Game(Row(Payoff(700, 800), Payoff(500, 500)), Row(Payoff(600, 200), Payoff(400, 500))),
        # Anything Goes
        Game(Row(Payoff(500, 500), Payoff(500, 500)), Row(Payoff(500, 500), Payoff(500, 500))),
        # Mixed Strat Not CS
        Game(Row(Payoff(400, 500), Payoff(400, 400)), Row(Payoff(600, 600), Payoff(500, 500))),
        # CS 300
        Game(Row(Payoff(300, 600), Payoff(600, 300)), Row(Payoff(600, 300), Payoff(300, 600))),
        # Equity Concern Practice Games
        Game(Row(Payoff(200, 0), Payoff(200, 0)), Row(Payoff(200, 400), Payoff(199, 900))),
        # Weak Dom Trust 0, 300
        Game(Row(Payoff(0, 300), Payoff(600, 300)), Row(Payoff(100, 200), Payoff(100, 200))),
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    strategies = models.LongStringField()
    strategy = models.StringField()
    start = models.StringField()
    end = models.StringField()

import json
import random
import numpy as np

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
    num_rounds = 3
    games = [
        # PC800, 100
        Game(Row(Payoff(800, 800), Payoff(100, 100)), Row(Payoff(100, 100), Payoff(500, 500)), Game.A),
        # BOS 800, 100
        Game(Row(Payoff(800, 500), Payoff(100, 100)), Row(Payoff(100, 100), Payoff(500, 800)), Game.B),
        # PD 300
        Game(Row(Payoff(300, 300), Payoff(100, 400)), Row(Payoff(400, 100), Payoff(200, 200)), Game.A),
        # # CS 400
        # Game(Row(Payoff(400, 100), Payoff(100, 400)), Row(Payoff(100, 400), Payoff(400, 100)), Game.B),
        # # It Dom
        # Game(Row(Payoff(300, 100), Payoff(200, 200)), Row(Payoff(100, 400), Payoff(400, 300)), Game.A),
        # # Strict Dom 300
        # Game(Row(Payoff(300, 300), Payoff(400, 400)), Row(Payoff(200, 100), Payoff(200, 300)), Game.B),
        # # CH1
        # Game(Row(Payoff(800, 800), Payoff(500, 1000)), Row(Payoff(1000, 500), Payoff(400, 400)), Game.A),
        # # CH2
        # Game(Row(Payoff(800, 800), Payoff(500, 1000)), Row(Payoff(1000, 500), Payoff(0, 0)), Game.B),
        # # PD 800
        # Game(Row(Payoff(800, 800), Payoff(100, 1000)), Row(Payoff(1000, 100), Payoff(500, 500)), Game.A),
        # # Strict Dom 800
        # Game(Row(Payoff(800, 800), Payoff(900, 900)), Row(Payoff(700, 600), Payoff(700, 800)), Game.B),
        # # BOS 800
        # Game(Row(Payoff(800, 500), Payoff(0, 0)), Row(Payoff(0, 0), Payoff(500, 800)), Game.A),
        # # PC 0
        # Game(Row(Payoff(800, 800), Payoff(0, 0)), Row(Payoff(0, 0), Payoff(500, 500)), Game.B),
        # # Strict Dom 500
        # Game(Row(Payoff(800, 800), Payoff(900, 900)), Row(Payoff(700, 600), Payoff(700, 800)), Game.A),
        # # Weak Dom Trust 0, 600
        # Game(Row(Payoff(0, 600), Payoff(900, 600)), Row(Payoff(400, 500), Payoff(400, 500)), Game.B),
        # # Strict Dom 700
        # Game(Row(Payoff(700, 800), Payoff(500, 500)), Row(Payoff(600, 200), Payoff(400, 500)), Game.A),
        # # Anything Goes
        # Game(Row(Payoff(500, 500), Payoff(500, 500)), Row(Payoff(500, 500), Payoff(500, 500)), Game.B),
        # # Mixed Strat Not CS
        # Game(Row(Payoff(400, 500), Payoff(400, 400)), Row(Payoff(600, 600), Payoff(500, 500)), Game.B),
        # # CS 300
        # Game(Row(Payoff(300, 600), Payoff(600, 300)), Row(Payoff(600, 300), Payoff(300, 600)), Game.B),
        # # Equity Concern Practice Games
        # Game(Row(Payoff(200, 0), Payoff(200, 0)), Row(Payoff(200, 400), Payoff(199, 900)), Game.A),
        # # Weak Dom Trust 0, 300
        # Game(Row(Payoff(0, 300), Payoff(600, 300)), Row(Payoff(100, 200), Payoff(100, 200)), Game.A),
    ]


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for player in self.get_players():
                player.participant.vars['payment_rounds'] = np.random.choice(3, 2)
                player.participant.vars['payment_games'] = []


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    strategies = models.LongStringField()
    final_strategy = models.StringField()
    random_strategy = models.StringField()

    def set_payoff(self):
        game = Constants.games[self.round_number - 1]
        # Column Player Move: A
        if self.random_strategy == Game.A:
            # Row Player Move: A
            if self.final_strategy == "A":
                self.payoff = c(game.row_a.column_a.row_payoff)
            elif self.final_strategy == "B":
                self.payoff = c(game.row_b.column_a.row_payoff)
            else:
                self.payoff = 0
        else:
            if self.final_strategy == "A":
                self.payoff = c(game.row_a.column_b.row_payoff)
            elif self.final_strategy == "B":
                self.payoff = c(game.row_b.column_b.row_payoff)
            else:
                self.payoff = 0

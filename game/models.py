import json
import random
import numpy as np

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from experiment.game import Game, Payoff


author = 'Anwar A. Ruff'

doc = """
Game Play Stage
"""


class Constants(BaseConstants):
    name_in_url = 'game'
    players_per_group = None
    num_rounds = 20
    payment_rounds = 4
    column_moves = [Game.A, Game.B, Game.A, Game.B]
    games = [
        # PC800, 100
        Game([[Payoff(800, 800), Payoff(100, 100)], [Payoff(100, 100), Payoff(500, 500)]]),
        # BOS 800, 100
        Game([[Payoff(800, 500), Payoff(100, 100)], [Payoff(100, 100), Payoff(500, 800)]]),
        # PD 300
        Game([[Payoff(300, 300), Payoff(100, 400)], [Payoff(400, 100), Payoff(200, 200)]]),
        # CS 400
        Game([[Payoff(400, 100), Payoff(100, 400)], [Payoff(100, 400), Payoff(400, 100)]]),
        # It Dom
        Game([[Payoff(300, 100), Payoff(200, 200)], [Payoff(100, 400), Payoff(400, 300)]]),
        # Strict Dom 300
        Game([[Payoff(300, 300), Payoff(400, 400)], [Payoff(200, 100), Payoff(200, 300)]]),
        # CH1
        Game([[Payoff(800, 800), Payoff(500, 1000)], [Payoff(1000, 500), Payoff(400, 400)]]),
        # CH2
        Game([[Payoff(800, 800), Payoff(500, 1000)], [Payoff(1000, 500), Payoff(0, 0)]]),
        # PD 800
        Game([[Payoff(800, 800), Payoff(100, 1000)], [Payoff(1000, 100), Payoff(500, 500)]]),
        # Strict Dom 800
        Game([[Payoff(800, 800), Payoff(900, 900)], [Payoff(700, 600), Payoff(700, 800)]]),
        # BOS 800
        Game([[Payoff(800, 500), Payoff(0, 0)], [Payoff(0, 0), Payoff(500, 800)]]),
        # PC 0
        Game([[Payoff(800, 800), Payoff(0, 0)], [Payoff(0, 0), Payoff(500, 500)]]),
        # Strict Dom 500
        Game([[Payoff(800, 800), Payoff(900, 900)], [Payoff(700, 600), Payoff(700, 800)]]),
        # Weak Dom Trust 0, 600
        Game([[Payoff(0, 600), Payoff(900, 600)], [Payoff(400, 500), Payoff(400, 500)]]),
        # St[Dom 700
        Game([[Payoff(700, 800), Payoff(500, 500)], [Payoff(600, 200), Payoff(400, 500)]]),
        # An[g Goes
        Game([[Payoff(500, 500), Payoff(500, 500)], [Payoff(500, 500), Payoff(500, 500)]]),
        # Mi[trat Not CS
        Game([[Payoff(400, 500), Payoff(400, 400)], [Payoff(600, 600), Payoff(500, 500)]]),
        # CS[
        Game([[Payoff(300, 600), Payoff(600, 300)], [Payoff(600, 300), Payoff(300, 600)]]),
        # Eq[Concern Practice Games
        Game([[Payoff(200, 0), Payoff(200, 0)], [Payoff(200, 400), Payoff(199, 900)]]),
        # We[m Trust 0, 300
        Game([[Payoff(0, 300), Payoff(600, 300)], [Payoff(100, 200), Payoff(100, 200)]]),
    ]


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for player in self.get_players():
                player.participant.vars['payment_rounds'] = np.random.choice(len(Constants.games), Constants.payment_rounds, False)
                player.participant.vars['payment_games'] = []


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    strategies = models.LongStringField()
    row_move = models.IntegerField(choices=[0, 1, 2])

    def set_payoff(self):
        game = Constants.games[self.round_number - 1]
        column_move = Constants.column_moves[self.round_number - 1]
        self.payoff = game.row_payoff(self.row_move, column_move)

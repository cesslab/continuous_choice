import random

from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class GameInfo(Page):

    def is_displayed(self):
        return self.round_number == 1


class Game(Page):
    form_model = 'player'
    form_fields = ['strategies', 'row_move', 'random_time']

    def vars_for_template(self):
        return {
            'game': Constants.games[self.round_number-1],
            'num_rounds': Constants.num_rounds,
            'round': self.round_number,
        }

    def before_next_page(self):
        if (self.round_number - 1) in self.participant.vars['payment_rounds']:
            self.player.set_payoff()
            self.participant.vars['payment_games'].append({
                'round': self.round_number,
                'game': Constants.games[self.round_number-1],
                'payoff': self.player.payoff,
                'random_time': self.player.random_time,
                'row_move': self.player.row_move,
                'column_move': Constants.column_moves[self.round_number - 1]
            })


page_sequence = [
    GameInfo,
    Game
]
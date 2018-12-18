import random

from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Game(Page):
    form_model = 'player'
    form_fields = ['strategies', 'row_move']

    def vars_for_template(self):
        return {
            'game': Constants.games[self.round_number-1],
            'round': self.round_number,
        }

    def before_next_page(self):
        if (self.round_number - 1) in self.participant.vars['payment_rounds']:
            self.player.set_payoff()
            self.participant.vars['payment_games'].append({
                'round': self.round_number,
                'game': Constants.games[self.round_number-1],
                'payoff': self.player.payoff,
                'row_move': self.player.row_move,
                'column_move': Constants.column_moves[self.round_number - 1]
            })


page_sequence = [
    Game
]
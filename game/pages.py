import random

from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Game(Page):
    form_model = 'player'
    form_fields = ['strategies', 'final_strategy', 'random_strategy']

    def vars_for_template(self):
        return {
            'game': Constants.games[self.round_number-1],
            'round': self.round_number,
        }

    def before_next_page(self):
        if (self.round_number - 1) in self.participant.vars['payment_rounds']:
            self.player.set_payoff()







class Results(Page):
    pass


page_sequence = [
    Game
]
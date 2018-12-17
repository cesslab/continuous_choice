from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Game(Page):
    def vars_for_template(self):
        obj = self.participant.vars['payment_games'][self.round_number - 1]
        return {
            'round': obj['round'],
            'game': obj['game'],
            'payoff': obj['payoff'],
            'move': obj['move']
        }


class FinalPayoff(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds


page_sequence = [
    Game,
    FinalPayoff,
]

from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class GameOutcome(Page):
    def vars_for_template(self):
        move_label = {0: 'None', 1: 'A', 2: 'B'}
        obj = self.participant.vars['payment_games'][self.round_number - 1]
        return {
            'round': obj['round'],
            'game': obj['game'],
            'payoff': obj['payoff'],
            'row_move': move_label[obj['row_move']],
            'column_move': move_label[obj['column_move']],
        }


class FinalPayoff(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        return {'final_payoff': self.participant.payoff.to_real_world_currency(self.session)}


class Message(Page):
    def is_displayed(self):
        return self.round_number == 1


page_sequence = [
    Message,
    GameOutcome,
    FinalPayoff,
]

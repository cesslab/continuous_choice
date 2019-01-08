from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class PracticeGame(Page):
    form_model = 'player'
    form_fields = ['strategies', 'row_move', 'random_time']

    def vars_for_template(self):
        return {
            'game': Constants.games[0],
            'round': self.round_number,
        }

    def before_next_page(self):
            self.player.set_payoff()
            self.participant.vars['payment_games'].append({
                'round': self.round_number,
                'game': Constants.games[0],
                'payoff': self.player.payoff,
                'row_move': self.player.row_move,
                'column_move': Constants.column_moves[0]
            })


class PracticeGameOutcome(Page):
    def vars_for_template(self):
        move_label = {0: 'None', 1: 'A', 2: 'B'}
        return {
            'round': self.round_number,
            'game': Constants.games[0],
            'payoff': self.player.payoff,
            'payoff_dollars': self.player.payoff.to_real_world_currency(self.session),
            'row_move': move_label[self.player.row_move],
            'random_time': self.player.random_time,
            'column_move': move_label[Constants.column_moves[0]],
        }


page_sequence = [
    PracticeGame,
    PracticeGameOutcome
]

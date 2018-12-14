from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Game(Page):
    form_model = 'player'
    form_fields = ['strategies', 'strategy', 'start', 'end']

    def vars_for_template(self):
        return {
            'game': Constants.games[self.round_number-1],
        }

    def strategies_error_message(self, strategies):
        print(strategies)


class Results(Page):
    pass


page_sequence = [
    Game
]
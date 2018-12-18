from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        strategies = '[{"strategies":"A", "time": 4.2}, {"strategies":"B", "time": 55.807}, {"strategies": "A", "time": 58.013}]'
        yield (pages.Game, {
            'strategies': strategies,
            'final_strategy': 'A',
            'row_move': 'B'
        })

        assert (self.player.strategies == strategies)
        assert (self.player.final_strategy == 'A')
        assert (self.player.random_strategy == 'B')

        if self.round_number == 3:
            assert (len(self.participant.vars['payment_games']) == 2)

from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Game(Page):
    pass


class Results(Page):
    pass


page_sequence = [
    Game,
    Results
]

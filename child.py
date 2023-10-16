import typing

from forest import Forest
from mobile import Mobile
from sprite import Sprite


class Child(Mobile):

    def __init__(self, inhabitant: typing.Any, forest: Forest):
        super().__init__(inhabitant, forest, Sprite("🤓"))

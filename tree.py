from sprite import Sprite
from square import Square


class Tree(Square):

    def __init__(self):
        super().__init__(False, Sprite("🌳"))

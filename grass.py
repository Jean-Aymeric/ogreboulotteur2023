from sprite import Sprite
from square import Square


class Grass(Square):

    def __init__(self):
        super().__init__(True, Sprite("🕷️"))

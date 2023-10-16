from sprite import Sprite


class Square:
    __passable: bool
    __sprite: Sprite

    def __init__(self, passable: bool, sprite: Sprite):
        self.__passable = passable
        self.__sprite = sprite

    def isPassable(self) -> bool:
        return self.__passable

    def getSprite(self) -> Sprite:
        return self.__sprite

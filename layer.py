import abc

from sprite import Sprite


class Layer :
    @abc.abstractmethod
    def getSpriteXY(self, x: int, y: int) -> Sprite | None:
        ...


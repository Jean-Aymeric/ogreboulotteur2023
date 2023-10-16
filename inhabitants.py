from child import Child
from forest import Forest
from layer import Layer
from mobile import Mobile
from ogre import Ogre
from sprite import Sprite


class Inhabitants(Layer):
    __mobiles: [Mobile]

    def __init__(self, nbChildren: int, forest: Forest):
        super().__init__()
        self.__mobiles = []
        for i in range(nbChildren):
            self.__mobiles.append(Child(self, forest))
        self.__mobiles.append(Ogre(self, forest))

    def moveAll(self):
        for mobile in self.__mobiles:
            mobile.move()

    def getSpriteXY(self, x: int, y: int) -> Sprite | None:
        for mobile in self.__mobiles:
            if mobile.getX() == x and mobile.getY() == y:
                return mobile.getSprite()
        return None

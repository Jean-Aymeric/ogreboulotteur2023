import random
import typing

from forest import Forest
from sprite import Sprite
from square import Square


class Mobile(Square):
    __x: int
    __y: int
    __inhabitant: typing.Any
    __forest: Forest

    def __init__(self,inhabitant: typing.Any, forest: Forest, sprite: Sprite):
        super().__init__(True, sprite)
        self.__forest = forest
        self.__x = 0
        self.__y = 0
        self.__inhabitant = inhabitant
        while not self.__forest.isPassableAtXY(self.__x, self.__y):
            self.__x = random.randint(1, self.__forest.getWidth() - 2)
            self.__y = random.randint(1, self.__forest.getHeight() - 2)

    def getX(self) -> int:
        return self.__x

    def getY(self) -> int:
        return self.__y

    def move(self):
        newX = self.__x
        newY = self.__y
        match random.randint(0,3):
            case 0:
                newY = self.__y -1

            case 1:
                newX = self.__x + 1

            case 2:
                newY = self.__y + 1

            case 3:
                newX = self.__x - 1

        if self.__forest.isPassableAtXY(newX,newY):
            self.__x = newX
            self.__y = newY



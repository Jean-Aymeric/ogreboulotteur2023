import random

from grass import Grass
from layer import Layer
from sprite import Sprite
from square import Square
from tree import Tree


class Forest(Layer):
    __squares: [[Square]]
    __width: int
    __height: int

    def __init__(self, width: int, height: int, nbTrees: int):
        self.__width = width
        self.__height = height
        tree = Tree()
        grass = Grass()
        self.__squares = []
        for i in range(self.__height):
            self.__squares.append([grass] * self.__width)

        for i in range(self.__height):
            for j in range(self.__width):
                if (i == 0) or (j == 0) or (i == self.__height - 1) or (j == self.__width - 1):
                    self.__squares[i][j] = tree

        for i in range(nbTrees):
            self.__squares[random.randint(0,self.__height-1)][random.randint(0,self.__width-1)] = tree

    def getWidth(self) -> int:
        return self.__width

    def getHeight(self) -> int:
        return self.__height

    def getSpriteXY(self, x: int, y: int) -> Sprite:
        return self.__squares[y][x].getSprite()

    def isPassableAtXY(self, x: int, y: int) -> bool:
        return self.__squares[y][x].isPassable()

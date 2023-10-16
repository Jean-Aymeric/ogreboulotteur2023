from forest import Forest
from layer import Layer


class Screen:
    __layers: [Layer]

    def __init__(self):
        self.__layers = []

    def addLayer(self,layer:Layer):
        self.__layers.append(layer)

    def show(self):
        for i in range(self.__layers[0].getHeight()):
            for j in range(self.__layers[0].getWidth()):
                num = -1
                while self.__layers[num].getSpriteXY(j, i) is None:
                    num -= 1
                print(self.__layers[num].getSpriteXY(j, i).getCharacter(), end="")

            print()

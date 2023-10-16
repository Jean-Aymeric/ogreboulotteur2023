import time

from forest import Forest
from inhabitants import Inhabitants
from screen import Screen

forest = Forest(80, 40, 500)

inhabitants = Inhabitants(100, forest)
screen = Screen()
screen.addLayer(forest)
screen.addLayer(inhabitants)
screen.show()
while True:
    inhabitants.moveAll()
    screen.show()
    time.sleep(0.4)

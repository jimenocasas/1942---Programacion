import random
import pyxel

isles = []
isles1 = []

class Portaaviones:
    def __init__(self, y: int):
        self.y = y
        isles.append(self)
        self.counter = 0
        self.is_alive = True
    def mover(self):
        self.y += 1.5
        if self.y > pyxel.height - 1:
            self.is_alive = False

class Mapa:

    def __init__(self, y: int):
        self.y = y
        self.rposi = 200
        self.u = 0
        self.v = 0
        self.w = 0
        self.h = 0
        self.counter = 0
        self.is_alive = True
        isles1.append(self)
        self.numr = 0
    def mover(self):

        self.y += 2.5

        if self.y > pyxel.height - 1:
            self.is_alive = False
            self.y = -250
            self.rposi = random.randint(-25, 275)
            self.numr = random.randint(0, 2)

        if self.numr == 0:
            self.x = self.rposi
            self.u = 120
            self.v = 8
            self.w = 219
            self.h = 98

        elif self.numr == 1:
            self.x = self.rposi
            self.u = 104
            self.v = 112
            self.w = 81
            self.h = 60
        elif self.numr == 2:
            self.x = self.rposi
            self.u = 113
            self.v = 178
            self.w = 232
            self.h = 236

    def draw(self):

        pyxel.blt(self.x, self.y, 1, self.u, self.v, self.w
                  , self.h, colkey=1)
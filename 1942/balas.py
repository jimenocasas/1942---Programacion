import constantes

#Definimos la clase bala que se va a utilizar en el avión.

class Balas:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.sprite = constantes.BALAS_SPRITE
        self.balasAvionIs_alive = True

    def moverbala(self):
        self.y -= 8


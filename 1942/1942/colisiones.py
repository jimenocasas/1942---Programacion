import pyxel
import constantes

listacolisones = []
listaExplosionSuperBombardero = []
listaExplosionBombardero =[]

#Definimos la clase colisiones que se ejecutará en el tablero. Esta hará que
# exploten tanto los enemigos "regulares" como los "rojos".

class Colisiones:

    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
        listacolisones.append(self)

#Esta hará que explote el bombardero"

class ExplosionBombardero:

    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
        listaExplosionBombardero.append(self)

#Esta hará que explote el Superbombardero"

class ExplosionSuperBombardero:

    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
        listaExplosionSuperBombardero.append(self)



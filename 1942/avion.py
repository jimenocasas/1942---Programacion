import pyxel
import balas
from balas import Balas
import constantes

#En esta clase se almacena lo relacionado con el avión

class Avion:

    def __init__(self, x: int, y: int):

        self.x = x
        self.y = y

        self.vidas = 3
        self.vidasloop = 3
        self.sprite = (0, 5, 2, 24, 24)
        self.avionisalive = True
        self.loopalive = False
        self.contador = 0
        self.contadorloop = 0
        self.elices = 0
        self.aumentocontador = 0.3
        self.listabalas = []
        self.balasalive = True

    #Creamos el movimiento del avión.

    def mover(self, direccion: str, tamaño: int):

        tamaño_avion_x = self.sprite[3]
        tamaño_avion_y = self.sprite[4]

        if (direccion.lower() == "derecha" and
                self.x < tamaño - tamaño_avion_x):
            self.x += 3
        elif (direccion.lower() == "izquierda" and self.x > 0):
            self.x -= 3
        elif (direccion.lower() == "arriba" and self.y > 0):
            self.y -= 3
        elif (direccion.lower()== "abajo" and self.y < tamaño- tamaño_avion_y):
            self.y += 3

    def pintarAvion(self):

        pyxel.blt(self.x, self.y, *self.sprite, colkey=0)

    #Con esta función conseguimos que el avikón gire cuando mantenemos
    # alguna de las teclas de movimiento y que vuelva a su posición original
    # cuando toca los bordes del tablero o se dejan de presionar las teclas.

    def giroAvion(self, tamaño: int, tamaño_avion_x: int):

        #Para que al chocar contra la pared vuelva a su posición inicial
        # (derecha)

        if pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT):
           if self.contador >= 0:
                if self.x <= (tamaño - tamaño_avion_x):
                    self.contador += self.aumentocontador
                else:
                   self.contador -= self.aumentocontador
           else:
               self.contador = 0

        #Para que al chocar contra la pared vuelva a su posición inicial
        # (izquierda)

        elif pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT):
            self.elices += 1
            if self.contador <= 0:
                if self.x > 0:
                    self.contador -= self.aumentocontador
                else:
                   self.contador += self.aumentocontador
            else:
                self.contador = 0

        #Para que al ir alante o atras vuelva a su posición inicila

        elif pyxel.btn(pyxel.KEY_W) or pyxel.btn(pyxel.KEY_UP) or pyxel.btn(\
                pyxel.KEY_S) or pyxel.btn(pyxel.KEY_DOWN):
           self.elices += 1
           if self.contador != 0:
                if self.contador > 0:
                    self.contador -= self.aumentocontador
                elif self.contador < 0:
                    self.contador += self.aumentocontador

        else:
            if self.contador != 0:
                if self.contador > 0:
                    self.contador -= self.aumentocontador
                elif self.contador < 0:
                    self.contador += self.aumentocontador
            self.elices += 1

        if (self.contador >= -2) and (self.contador < 2):
            if self.elices % 2 == 0:
                self.sprite = constantes.SPRITE_AVION[0]
            elif self.elices % 2 != 0:
                self.sprite = constantes.SPRITE_AVION[1]

        elif (self.contador >= 2) and (self.contador < 4):
            self.sprite = constantes.SPRITES_GIRO_AVION[0]

        elif (self.contador >= 4) and (self.contador < 6):
            self.sprite = constantes.SPRITES_GIRO_AVION[1]

        elif (self.contador >= 6):
            self.sprite = constantes.SPRITES_GIRO_AVION[2]
            self.contador = 6

        elif (self.contador <= -2) and (self.contador > -4):
            self.sprite = constantes.SPRITES_GIRO_AVION[3]

        elif (self.contador <= -4) and (self.contador > -6):
            self.sprite = constantes.SPRITES_GIRO_AVION[4]

        elif (self.contador <= -6) :
            self.sprite = constantes.SPRITES_GIRO_AVION[5]
            self.contador = -6

    #Con las funciones de antes creamos una nueva que las ejecute en el
    # tablero al presionar ciertas teclas

    def updateMovimineto(self):

        if self.avionisalive == True:

            if pyxel.btnp(pyxel.KEY_ESCAPE):
                pyxel.quit()

            elif pyxel.btn(pyxel.KEY_D):
                self.mover('derecha', constantes.ANCHO)
                self.giroAvion(255, self.sprite[3])

            elif pyxel.btn(pyxel.KEY_RIGHT):
                self.mover('derecha', constantes.ANCHO)
                self.giroAvion(255, self.sprite[3])

            elif pyxel.btn(pyxel.KEY_A):
                self.mover('izquierda', constantes.ANCHO)
                self.giroAvion(255, self.sprite[3])

            elif pyxel.btn(pyxel.KEY_LEFT):
                self.mover('izquierda', constantes.ANCHO)
                self.giroAvion(255, self.sprite[3])

            elif pyxel.btn(pyxel.KEY_W):
                self.mover('arriba', constantes.ALTO)
                self.giroAvion(255, self.sprite[3])

            elif pyxel.btn(pyxel.KEY_UP):
                self.mover('arriba', constantes.ALTO)
                self.giroAvion(255, self.sprite[3])

            elif pyxel.btn(pyxel.KEY_DOWN):
                self.mover('abajo', constantes.ALTO)
                self.giroAvion(255, self.sprite[3])

            elif pyxel.btn(pyxel.KEY_S):
                self.mover('abajo', constantes.ALTO)
                self.giroAvion(255, self.sprite[3])

            else:
                self.giroAvion(255, self.sprite[3])

            if pyxel.btnr(pyxel.KEY_Z):
                if self.vidasloop > 0:
                    self.loopalive = True
                    self.vidasloop -= 1

    #Creamos el loop del avión, que esquivará las balas y las colisiones con
    # los enemigos.

    def loopAvion(self):

        if self.vidasloop >= 0:

            if self.loopalive == True:

                self.balasalive = False
                self.contadorloop += 0.3
                if self.contadorloop <= 1:
                    self.sprite = constantes.SPRITS_LOOP[0]
                elif self.contadorloop <= 2:
                    self.sprite = constantes.SPRITS_LOOP[1]
                elif self.contadorloop <= 3:
                    self.sprite = constantes.SPRITS_LOOP[2]
                elif self.contadorloop <= 4:
                    self.sprite = constantes.SPRITS_LOOP[3]
                elif self.contadorloop <= 5:
                    self.sprite = constantes.SPRITS_LOOP[4]
                elif self.contadorloop <= 6:
                    self.sprite = constantes.SPRITS_LOOP[5]
                elif self.contadorloop <= 7:
                    self.sprite = constantes.SPRITS_LOOP[6]
                elif self.contadorloop <= 8:
                    self.sprite = constantes.SPRITS_LOOP[7]
                elif self.contadorloop <= 9:
                    self.sprite = constantes.SPRITS_LOOP[8]
                elif self.contadorloop <= 10:
                    self.sprite = constantes.SPRITS_LOOP[9]
                elif self.contadorloop <= 11:
                    self.sprite = constantes.SPRITS_LOOP[10]
                elif self.contadorloop <= 12:
                    self.sprite = constantes.SPRITS_LOOP[11]
                elif self.contadorloop <= 13:
                    self.sprite = constantes.SPRITS_LOOP[12]
                elif self.contadorloop <= 14:
                    self.sprite = constantes.SPRITS_LOOP[13]
                elif self.contadorloop <= 15:
                    self.sprite = constantes.SPRITS_LOOP[14]
                elif self.contadorloop > 15:
                    self.balasalive = True
                    self.loopalive = False
                    self.contadorloop = 0

    # Añadimos las balas creadas en la clase balas a una lista

    def updatebalas(self):

        if self.balasalive == True:
            if pyxel.btnr(pyxel.KEY_SPACE):
                self.listabalas.append(Balas(self.x - 1, self.y))

    #Pintamos las balas de la listabalas

    def pintarBalas(self):

        if self.balasalive == True:

            for element in self.listabalas:
                element.moverbala()
                pyxel.blt(element.x, element.y-2, *element.sprite, colkey=0)

    #Eliminamos las balas cuando no son necesarias o se han estrellado
    # contra un eneimgo

    def borrarBalas(self):

        for elem in self.listabalas:

            if elem.y < 0 or self.balasalive == False:
                self.listabalas.remove(elem)



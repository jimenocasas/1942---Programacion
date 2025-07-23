import random

import pyxel

import constantes


balax1 = [5, 4, 3, 2, 1]
balay1 = [1, 2, 3, 4, 5]
balasE = []

class Enemigo:

    def __init__(self, x: float, y: float, tipo: str, limite: int, cont: int,
                 direcc: str, aspecto: tuple, vidas: int, bala : int):
        self.x = x
        self.y = y
        self.tipo = tipo
        self.limite = limite
        self.cont = cont
        self.direcc = direcc
        self.aspecto = aspecto
        self.vidas = vidas
        self.bala = bala
        self.is_alive = True

    def MoverEnemigo(lista: list):
        for elem in lista:
            if elem.tipo == "REGULAR":
                numbala = random.randint(1, 5)
                if numbala == 1:
                    if elem.bala == 0:
                        if elem.y in range(58, 62):
                            balasE.append(BalaEnem(elem.x, elem.y, 0,
                                                   "REGULAR", 0))
                            elem.bala = 1
                elif numbala == 2:
                    if elem.bala == 0:
                        if elem.y in range(100, 104):
                            balasE.append(BalaEnem(elem.x, elem.y, 0,
                                                   "REGULAR", 0))
                            elem.bala = 1
                elif numbala == 3:
                    if elem.bala == 0:
                        if elem.y in range(150, 154):
                            balasE.append(BalaEnem(elem.x, elem.y, 0,
                                                   "REGULAR", 0))
                            elem.bala = 1
                if elem.y == 0-constantes.REGULAR_SPRITE[4] and elem.x < 255/2:
                    elem.direcc = 'abd'
                    elem.aspecto = constantes.REGULAR_ABD
                elif elem.y == 0-constantes.REGULAR_SPRITE[4] and elem.x > 255/2:
                    elem.direcc = 'abi'
                    elem.aspecto = constantes.REGULAR_ABI
                elif elem.y >= elem.limite and elem.direcc == 'abi':
                    elem.direcc = 'ai'
                    elem.aspecto = constantes.REGULAR_AI
                elif elem.y >= elem.limite and elem.direcc == 'abd':
                    elem.direcc = 'ad'
                    elem.aspecto = constantes.REGULAR_AD
                if elem.direcc == 'abd':
                    elem.x += 1
                    elem.y += 3
                elif elem.direcc == 'abi':
                    elem.x -= 1
                    elem.y += 3
                elif elem.direcc == 'ad':
                    elem.x += 1
                    elem.y -= 3
                    if elem.y == 0-constantes.REGULAR_SPRITE[4]:
                        lista.remove(elem)
                elif elem.direcc == 'ai':
                    elem.x -= 1
                    elem.y -= 3
                    if elem.y == 0-constantes.REGULAR_SPRITE[4]:
                        lista.remove(elem)
            if elem.tipo == "ROJO":
                if elem.cont == 0:
                    if elem.x < 100 and elem.y == 40:
                        elem.x += 4
                        elem.aspecto = constantes.ROJO_SPRITE[2]
                    elif elem.x >= 100 and elem.y < 120:
                        elem.y += 4
                        elem.aspecto = constantes.ROJO_SPRITE[0]
                    elif elem.y >= 120 and elem.x > 20:
                        elem.x -= 4
                        elem.aspecto = constantes.ROJO_SPRITE[3]
                    elif elem.y >= 120 and elem.x <= 20:
                        elem.cont = 1
                elif elem.cont == 1:
                    if elem.y > 40:
                        elem.y -= 4
                        elem.aspecto = constantes.ROJO_SPRITE[1]
                    elif elem.y <= 40:
                        elem.cont = 2

                elif elem.cont == 2:
                    if elem.x < 210 and elem.y <= 40:
                        elem.x += 4
                        elem.aspecto = constantes.ROJO_SPRITE[2]
                    elif elem.x >= 210 and elem.y < 120:
                        elem.y += 4
                        elem.aspecto = constantes.ROJO_SPRITE[0]
                    elif elem.y >= 120 and elem.x > 135:
                        elem.x -= 4
                        elem.aspecto = constantes.ROJO_SPRITE[3]
                    elif elem.y >= 120 and elem.x <= 135 and elem.cont == 2:
                        elem.cont = 3
                elif elem.cont == 3:
                    if elem.y > 40:
                        elem.y -= 4
                        elem.aspecto = constantes.ROJO_SPRITE[1]
                    elif elem.y <= 40:
                        elem.cont = 4
                elif elem.cont == 4:
                    elem.x += 4
                    elem.aspecto = constantes.ROJO_SPRITE[2]
                    if elem.x > 257:
                        lista.remove(elem)
            if elem.tipo == "BOMBARDERO":
                if pyxel.frame_count % 60 == 0:
                    balasE.append(BalaEnem(elem.x, elem.y, 0, 'BOMBARDERO', 0))
                numr = random.randint(1, 2)
                if elem.direcc == 'ai':
                    elem.y -= 1
                    elem.x -= 2
                    elem.aspecto = constantes.BOMBARDERO_SPRITE
                elif elem.direcc == 'ad':
                    elem.y -= 1
                    elem.x += 2
                    elem.aspecto = constantes.BOMBARDERO_SPRITE
                elif elem.direcc == 'abd':
                    elem.y += 1
                    elem.x += 2
                    elem.aspecto = constantes.BOMBARDERO_SPRITE2
                elif elem.direcc == 'abi':
                    elem.y += 1
                    elem.x -= 2
                    elem.aspecto = constantes.BOMBARDERO_SPRITE2
                if elem.cont == 0:
                    if numr == 1:
                        elem.x = 190
                        elem.cont = 2
                        elem.direcc = 'ai'
                    else:
                        elem.x = 63
                        elem.cont = 1
                        elem.direcc = 'ad'
                elif elem.cont == 1:
                    if elem.x > 127:
                        elem.direcc = 'ai'
                    elif elem.x < 1:
                        elem.direcc = 'ad'
                    if elem.y < 1:
                        elem.cont = 3
                        elem.direcc = 'abd'
                elif elem.cont == 2:
                    if elem.x < 127:
                        elem.direcc = 'ad'
                    elif elem.x > 230:
                        elem.direcc = 'ai'
                    if elem.y < 1:
                        elem.cont = 4
                        elem.direcc = 'abd'
                elif elem.cont == 3:
                    if elem.x > 127:
                        elem.direcc = 'abi'
                    elif elem.x < 1:
                        elem.direcc = 'abd'
                    if elem.y > 260:
                        lista.remove(elem)
                elif elem.cont == 4:
                    if elem.x < 127:
                        elem.direcc = 'abd'
                    elif elem.x > 230:
                        elem.direcc = 'abi'
                    if elem.y > 260:
                        lista.remove(elem)
            elif elem.tipo == 'SUPERBOMBARDERO':
                if elem.cont == 0:
                    elem.y -= 1
                    if elem.y < elem.limite:
                        elem.cont = 1
                elif elem.cont == 1:
                    if pyxel.frame_count % 120 == 0:
                        balasE.append(BalaEnem(elem.x + 32, elem.y + 49, 0,
                                               'SUPERBOMBARDERO', 1))
                        balasE.append(BalaEnem(elem.x + 32, elem.y + 49, 0,
                                               'SUPERBOMBARDERO', 2))
                        balasE.append(BalaEnem(elem.x + 32, elem.y + 49, 0,
                                               'SUPERBOMBARDERO', 3))



    def DrawEnem(lista1: list):
        for elemm in lista1:
            pyxel.blt(elemm.x, elemm.y, *elemm.aspecto, colkey=0)


class BalaEnem:
    def __init__(self, x: int, y : int, cont : int, tipo : str, z : int):
        self.x = x
        self.y = y
        self.cont = cont
        self.tipo = tipo
        self.z = z
    def moverbalaenem(lista : list):
        for bala in lista:
            if bala.tipo == 'REGULAR':
                numr = random.randint(0, 4)
                bala.y += 5
                if bala.cont == 0:
                    if bala.x < 127:
                        bala.cont = 1
                    elif bala.x >= 127:
                        bala.cont = 2
                elif bala.cont == 1:
                    bala.x += balax1[numr]

                elif bala.cont == 2:
                    bala.x -= balax1[numr]
                if bala.x not in range(-4, 256) or bala.y not in range(0, 256):
                    lista.remove(bala)
            elif bala.tipo == 'BOMBARDERO':
                if bala.cont == 0:
                    if bala.y in range(0, 42):
                        bala.cont = 5
                    elif bala.y in range(42, 84):
                        bala.cont = 4
                    elif bala.y in range(84, 125):
                        bala.cont = 3
                    elif bala.y in range(125, 168):
                        bala.cont = 2
                    elif bala.y in range(168, 209):
                        bala.cont = 1
                    else:
                        bala.y += 5
                    if bala.x < 127:
                        bala.z = 1
                    else:
                        bala.z = 2
                else:
                    bala.y += balay1[bala.cont-1]
                    if bala.z == 1:
                        bala.x += balax1[bala.cont-1]
                    elif bala.z == 2:
                        bala.x -= balax1[bala.cont-1]
                if bala.x not in range(-4, 256) or bala.y not in range(0, 256):
                    lista.remove(bala)
            elif bala.tipo == 'SUPERBOMBARDERO':
                if bala.z == 1:
                    bala.x -= balax1[random.randint(2, 4)]
                    bala.y += balay1[random.randint(2, 4)]
                elif bala.z == 2:
                    bala.y += 5
                elif bala.z == 3:
                    bala.x += balax1[random.randint(2, 4)]
                    bala.y += balay1[random.randint(2, 4)]
                if bala.x not in range(-4, 256) or bala.y not in range(0, 256):
                    lista.remove(bala)


    def drawBala(lista2 : list):
        for eleme in lista2:
            pyxel.blt(eleme.x, eleme.y, *constantes.SPRITE_BALA_ENEMIGO, colkey=0)
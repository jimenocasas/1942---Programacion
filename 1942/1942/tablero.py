import random
from avion import Avion
import enemigo
from enemigo import Enemigo
from enemigo import BalaEnem
import pyxel
import constantes
import mapa
from mapa import Portaaviones
from mapa import Mapa
import colisiones
from colisiones import Colisiones
from colisiones import ExplosionSuperBombardero
from colisiones import ExplosionBombardero

islas = mapa.isles
islas1 = mapa.isles1
enemies = []

def update_list(list):
    for elem in list:
        elem.update()

def cleanup_list(list):
    i = 0
    while i < len(list):
        elem = list[i]
        if not elem.is_alive:
            list.pop(i)
        else:
            i += 1

#Creamos la clase tablero que es la que se va a encargar de ejecutar todas
# las funciones del programa

class Tablero:

    def __init__(self):

        self.ancho = constantes.ANCHO
        self.alto = constantes.ALTO
        #Creamos el tablero donde vamos a hacer el juego
        pyxel.init(self.ancho, self.alto, title="1942")
        # Cargamos el fichero pyxres que vamos a usar
        pyxel.load("assets/example.pyxres")

        self.pantalla = "INICIO"
        self.contadorInicio = 0
        self.contadorFin = 0
        self.avion = Avion(constantes.ANCHO/2, 200)
        self.contadorExplosionAvion = 0
        self.contadorExplosionBombardero = 0
        self.contadorExplosionSuperBombardero = 0
        self.contadorcolisiones = 0
        self.enemigo = Enemigo
        self.balaenem = BalaEnem
        self.spritecolison = constantes.SPRITES_COLISIONES[0]
        self.spriteExplosionSuperBombardero = \
            constantes.SPRITES_EXPLOSIONES_SUPER[0]
        self.spriteExplosionBombardero = \
            constantes.SPRITES_EXPLOSION_BOMBARDERO[0]
        self.map = Mapa(-150)
        self.porte2 = Portaaviones(150)
        self.puntos = 0
        # Ejecutamos el juego
        pyxel.run(self.update, self.draw)

    #Esta función ejecutará cada frame todas las funciones que se encuentren
    # dentro dependiendo de la pantalla del juego en la que te encuentres

    def update(self):
        self.cambiarPantalla()

        if self.pantalla == "INICIO":
            self.contadorInicio += 1

        if self.pantalla == "JUEGO":
            self.avion.updateMovimineto()
            self.avion.updatebalas()
            self.avion.loopAvion()
            self.porte2.mover()
            self.map.mover()
            self.crearListaEnem()
            self.enemigo.MoverEnemigo(enemies)
            self.balaenem.moverbalaenem(enemigo.balasE)
            self.ColisionEnemigos()
            self.SpritesColisionesEnemigos()
            self.SpritesExplosionSuper()
            self.spritesExplosionAvion()
            self.spritesExplosionBombardero()
            self.ExplosionAvion()
            self.avion.borrarBalas()
            self.borrarEnemigos()
            self.borrarBalasEnemigos()

    #Creamos la lista que va a almacenar todos los enemigos del juego

    def crearListaEnem(self):

        if pyxel.frame_count % 60 == 0 and pyxel.frame_count > 59:
            enemies.append(
            Enemigo(random.randint(0,self.ancho - constantes.REGULAR_SPRITE[3]),
            0 - constantes.REGULAR_SPRITE[4], "REGULAR",random.randint(180, 255),
                    0, "", (0, 0, 0, 0, 0), 1,0))

        if pyxel.frame_count % 400 == 0 and pyxel.frame_count > 399:
            enemies.append(
                (Enemigo(0, 40, "ROJO", 0, 0, "", (0, 178, 241, 16, 16), 1,0)))
            enemies.append(
                (Enemigo(-25, 40, "ROJO", 0, 0, "", (0, 178, 241, 16, 16),1,
                 0)))
            enemies.append(
                (Enemigo(-50, 40, "ROJO", 0, 0, "", (0, 178, 241, 16, 16),
                         1, 0)))
            enemies.append(
                (Enemigo(-75, 40, "ROJO", 0, 0, "", (0, 178, 241, 16, 16),
                         1, 0)))
            enemies.append(
                (Enemigo(-100, 40, "ROJO", 0, 0, "", (0, 178, 241, 16, 16),
                         1, 0)))

        if pyxel.frame_count % 600 == 0 and pyxel.frame_count > 599:
            enemies.append(Enemigo(random.randint(0,
                            self.ancho - constantes.BOMBARDERO_SPRITE[3]),
                            self.alto + constantes.BOMBARDERO_SPRITE[4],
                            "BOMBARDERO", 0, 0, "",
                                   constantes.BOMBARDERO_SPRITE, 6, 0))

        if pyxel.frame_count % 1500 == 0 and pyxel.frame_count > 1499:
            enemies.append(Enemigo(random.randint(60,
                            160),
                            self.alto + constantes.SUPERBOMBARDERO_SPRITE[4],
                            "SUPERBOMBARDERO", random.randint(30, 90),0, "",
                            constantes.SUPERBOMBARDERO_SPRITE, 12, 0))

    #En esta función definimos las distintas formas de colisión entre las
    # balas y los enemigos.

    def ColisionEnemigos(self):

        for enemigos in enemies:
            for balas in self.avion.listabalas:

                 if (enemigos.x + enemigos.aspecto[3] > balas.x and
                    balas.x + balas.sprite[3] > enemigos.x and
                    enemigos.y + enemigos.aspecto[4] > balas.y and
                    balas.y + balas.sprite[4] > enemigos.y):

                    self.avion.listabalas.remove(balas)
                    enemigos.vidas -= 1

                    #Colisión para los enemigos "regulares" y "rojos"

                    if enemigos.tipo == "ROJO" or enemigos.tipo == "REGULAR":
                        colisiones.listacolisones.append(Colisiones(enemigos.x,
                        enemigos.y))
                        self.puntos += 20

                        if enemigos.vidas == 0:
                            enemies.remove(enemigos)

                    # Colisión para los bombarderos"

                    if enemigos.tipo == "BOMBARDERO":
                        self.puntos += 100

                        if enemigos.vidas == 0:
                            enemies.remove(enemigos)
                            colisiones.listaExplosionBombardero.append(
                                ExplosionBombardero(enemigos.x, enemigos.y))

                    # Colisión para los Superbombarderos"

                    if enemigos.tipo == "SUPERBOMBARDERO":
                        self.puntos += 200

                        if enemigos.vidas == 0:
                            enemies.remove(enemigos)
                            colisiones.listaExplosionSuperBombardero.append(
                                ExplosionSuperBombardero(enemigos.x,
                                                         enemigos.y))

    #Función que crea la explosion del avión cuando choca contra una bala de
    # un enemigo o con uno de ellos

    def ExplosionAvion(self):

        for enemigos in enemies:
            if (self.avion.x + self.avion.sprite[3] > enemigos.x and
                enemigos.x + enemigos.aspecto[3] > self.avion.x and
                self.avion.y + self.avion.sprite[4] > enemigos.y and
                enemigos.y + enemigos.aspecto[4] > self.avion.y) and \
                    self.avion.loopalive == False:

                self.avion.avionisalive = False
                enemies.remove(enemigos)
                self.avion.vidas -= 1

                if enemigos.tipo == "ROJO" or enemigos.tipo == "REGULAR":
                    colisiones.listacolisones.append(Colisiones(enemigos.x,
                                                            enemigos.y))

                elif enemigos.tipo == "SUPERBOMBARDERO":
                    colisiones.listaExplosionSuperBombardero.append(
                        ExplosionSuperBombardero(enemigos.x,enemigos.y))

                elif enemigos.tipo == "BOMBARDERO":
                    colisiones.listaExplosionBombardero.append(
                        ExplosionBombardero(enemigos.x, enemigos.y))

        for bala in enemigo.balasE:

            if (self.avion.x + self.avion.sprite[3] > bala.x and
                bala.x + constantes.SPRITE_BALA_ENEMIGO[3] > self.avion.x and
                self.avion.y + self.avion.sprite[4] > bala.y and
                bala.y + constantes.SPRITE_BALA_ENEMIGO[4] > self.avion.y) and \
                    self.avion.loopalive == False:

                self.avion.avionisalive = False
                enemigo.balasE.remove(bala)
                self.avion.vidas -= 1

#Las siguientes funciones definen el cambio de sprites cuando suceden las
# colisiones con los enemigos o la explosión del avion

    def SpritesColisionesEnemigos(self):

        for colision in colisiones.listacolisones:
            self.contadorcolisiones += 1
            if self.contadorcolisiones < 2:
                self.spritecolison = constantes.SPRITES_COLISIONES[0]
            elif self.contadorcolisiones < 4:
                self.spritecolison = constantes.SPRITES_COLISIONES[1]
            elif self.contadorcolisiones < 6:
                self.spritecolison = constantes.SPRITES_COLISIONES[2]
            elif self.contadorcolisiones < 8:
                self.spritecolison = constantes.SPRITES_COLISIONES[3]
            elif self.contadorcolisiones < 10:
                colisiones.listacolisones.remove(colision)
            elif self.contadorcolisiones == 10:
                self.contadorcolisiones = 0

    def SpritesExplosionSuper(self):

        for explosion in colisiones.listaExplosionSuperBombardero:
            self.contadorExplosionSuperBombardero += 0.1
            if self.contadorExplosionSuperBombardero < 2:
                self.spriteExplosionSuperBombardero = \
                    constantes.SPRITES_EXPLOSIONES_SUPER[0]
            elif self.contadorExplosionSuperBombardero < 4:
                self.spriteExplosionSuperBombardero = \
                    constantes.SPRITES_EXPLOSIONES_SUPER[1]
            elif self.contadorExplosionSuperBombardero < 6:
                self.spriteExplosionSuperBombardero = \
                    constantes.SPRITES_EXPLOSIONES_SUPER[2]
            elif self.contadorExplosionSuperBombardero < 8:
                self.spriteExplosionSuperBombardero = \
                    constantes.SPRITES_EXPLOSIONES_SUPER[3]
            elif self.contadorExplosionSuperBombardero < 10:
                self.spriteExplosionSuperBombardero = \
                    constantes.SPRITES_EXPLOSIONES_SUPER[4]
            elif self.contadorExplosionSuperBombardero < 12:
                self.spriteExplosionSuperBombardero = \
                    constantes.SPRITES_EXPLOSIONES_SUPER[5]
            elif self.contadorExplosionSuperBombardero < 14:
                self.spriteExplosionSuperBombardero = \
                    constantes.SPRITES_EXPLOSIONES_SUPER[6]
            elif self.contadorExplosionSuperBombardero < 15:
                colisiones.listaExplosionSuperBombardero.remove(explosion)
            if self.spriteExplosionSuperBombardero == 15:
                self.contadorExplosionSuperBombardero = 0

    def spritesExplosionBombardero(self):

        for explosion in colisiones.listaExplosionBombardero:
            self.contadorExplosionBombardero += 0.4
            if self.contadorExplosionBombardero < 2:
                self.spriteExplosionBombardero = \
                    constantes.SPRITES_EXPLOSION_BOMBARDERO[0]
            elif self.contadorExplosionBombardero < 4:
                self.spriteExplosionBombardero = \
                    constantes.SPRITES_EXPLOSION_BOMBARDERO[1]
            elif self.contadorExplosionBombardero < 6:
                self.spriteExplosionBombardero = \
                    constantes.SPRITES_EXPLOSION_BOMBARDERO[2]
            elif self.contadorExplosionBombardero > 6:
                self.contadorExplosionBombardero = 0
                colisiones.listaExplosionBombardero.remove(explosion)


    def spritesExplosionAvion(self):
        if self.avion.avionisalive == False:
            self.avion.balasalive = False
            self.contadorExplosionAvion += 0.2
            if self.contadorExplosionAvion <= 1:
                self.avion.sprite = constantes.SPRITES_EXPLOSION_AVION[0]
            elif self.contadorExplosionAvion <= 2:
                self.avion.sprite = constantes.SPRITES_EXPLOSION_AVION[1]
            elif self.contadorExplosionAvion <= 3:
                self.avion.sprite = constantes.SPRITES_EXPLOSION_AVION[2]
            elif self.contadorExplosionAvion <= 4:
                self.avion.sprite = constantes.SPRITES_EXPLOSION_AVION[3]
            elif self.contadorExplosionAvion <= 5:
                self.avion.sprite = constantes.SPRITES_EXPLOSION_AVION[4]
            elif self.contadorExplosionAvion <= 6:
                self.avion.sprite = constantes.SPRITES_EXPLOSION_AVION[5]
            elif self.contadorExplosionAvion > 6:
                self.avion.x = constantes.ANCHO/2
                self.avion.y = 200
                self.contadorExplosionAvion = 0
                self.avion.balasalive = True
                self.avion.avionisalive = True

#Para pintar en el tablero:

    update_list(islas)
    cleanup_list(islas)
    update_list(islas1)
    cleanup_list(islas1)

    #Para pintar el portaaviones
    def pintarPorte(self):
        pyxel.blt(100, self.porte2.y, 1, 0, 0, 84, 245,
                  colkey=1)
    def pintarIsla(self):
        for elem in islas1:
            pyxel.blt(elem.x, elem.y, 1, elem.u, elem.v, elem.w
                  , elem.h, colkey=1)

    def pintarColisiones(self):
        for colision in colisiones.listacolisones:
            pyxel.blt(colision.x, colision.y, *self.spritecolison,
                        colkey=0)

    def pintarExplosionSuperBombardero(self):
        for explosion in colisiones.listaExplosionSuperBombardero:
            pyxel.blt(explosion.x, explosion.y,
                      *self.spriteExplosionSuperBombardero, colkey=0)

    def pintarExplosionBombardero(self):
        for explosion in colisiones.listaExplosionBombardero:
            pyxel.blt(explosion.x, explosion.y,
                      *self.spriteExplosionBombardero, colkey=0)

    def pintarPuntos(self):
        pyxel.text(5,5,"PUNTOS:%i"%self.puntos,col=0)

    def pintarVidasLoop(self):
        if self.avion.vidasloop >= 0:
            pyxel.text(220,5,"LOOPS:%i"%self.avion.vidasloop,col=0)
        else:
            pyxel.text(220, 5, "LOOPS:0", col=0)

    def PintarVidasAvion(self):
        if self.avion.vidas >= 0:
            pyxel.text(110, 5, "VIDAS:%i" % self.avion.vidas, col=0)
        else:
            pyxel.text(110, 5, "VIDAS:0", col=0)

#Esta función pinta en el tablero cada frame lo que corresponda a su pantalla

    def draw(self):
        pyxel.cls(1)  # esto es el fondo

        if self.pantalla == "JUEGO":
            self.pintarPorte()
            self.pintarIsla()
            self.avion.pintarAvion()
            self.avion.pintarBalas()
            self.pintarColisiones()
            self.pintarExplosionSuperBombardero()
            self.pintarExplosionBombardero()
            self.enemigo.DrawEnem(enemies)
            self.balaenem.drawBala(enemigo.balasE)
            self.pintarPuntos()
            self.pintarVidasLoop()
            self.PintarVidasAvion()

        elif self.pantalla == "INICIO":
            pyxel.text(20, 20, "PUNTUACION MAXIMA: 40000\n\nTU PUNTUACION: "
                               "0",col=0)
            if self.contadorInicio % 4 != 0:
                pyxel.text(80, constantes.ALTO / 2,
                        "PULSA TAB PARA EMPEZAR", col=0)

        elif self.pantalla == "FIN":
            pyxel.text(70, constantes.ALTO / 2,
                       "PULSA ESC PARA CERRAR EL JUEGO", col=0)

            if self.puntos > 40000:
                pyxel.text(20, 20, "FELICIDADES HAS SUPERADO LA "
                                   "PUNTUACION MAXIMA\n\nTU PUNTUACION: "
                                   "%i"%self.puntos,col=0)

            elif self.puntos == 40000:
                pyxel.text(20, 20, "FELICIDADES HAS ALCANZADO LA "
                                   "PUNTUACION MAXIMA\n\nTU PUNTUACION: "
                                   "%i" % self.puntos, col=0)

            else:
                pyxel.text(20, 20,
                "PUNTUACION MAXIMA: 40000\n\nTU PUNTUACION: %i"%self.puntos,col=0)

#Para eliminar:

    def borrarEnemigos(self):
        for enemigos in enemies:
            if self.avion.avionisalive == False:
                enemies.remove(enemigos)

    def borrarBalasEnemigos(self):
        for balas in enemigo.balasE:
            if self.avion.avionisalive == False:
                enemigo.balasE.remove(balas)

#Para cambiar la pantalla

    def cambiarPantalla(self):
        if pyxel.btn(pyxel.KEY_TAB):
            self.pantalla = "JUEGO"
        elif self.avion.vidas < 0:
            self.contadorFin += 0.1
            if self.contadorFin > 3:
                self.pantalla = "FIN"

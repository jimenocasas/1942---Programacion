# 1942 — Videojuego estilo arcade con Pyxel

Proyecto desarrollado por Miguel Jimeno y Fernando López de Olmedo  
Universidad · Asignatura de Programación.  
Basado en el clásico de aviones de la Segunda Guerra Mundial

## Descripción

1942 es un videojuego de disparos en 2D desarrollado con Python y la librería [Pyxel](https://github.com/kitao/pyxel). Inspirado en títulos clásicos como Space Invaders, el objetivo es esquivar enemigos y proyectiles mientras destruyes aeronaves enemigas para lograr la mayor puntuación posible.

Se trata de un proyecto académico cuyo desarrollo ha supuesto un reto técnico y creativo, especialmente en la implementación de movimientos personalizados, colisiones y animaciones con recursos limitados.

## Características

- Control mediante flechas o teclas WASD
- Disparo con barra espaciadora
- Loop evasivo con la tecla Z (limitado a 3 usos)
- Pantallas de inicio, juego y fin
- Diferentes tipos de enemigos con vidas y puntuaciones únicas
- Detección de colisiones y efectos visuales
- Escenario dinámico con scroll vertical continuo
- Gestión modular del código mediante clases separadas

## Estructura del Proyecto

- `main.py`: punto de entrada del juego
- `tablero.py`: lógica principal y ciclo de juego
- `avion.py`: control y comportamiento del avión
- `enemigos.py`: definición y movimiento de enemigos
- `balas.py`: gestión de proyectiles
- `mapa.py`: generación y movimiento del fondo
- `colisiones.py`: detección e implementación de impactos
- `constantes.py`: configuración y parámetros globales
- `assets/`: sprites y recursos gráficos creados con Pyxel Edit

## Requisitos

- Python 3.7 o superior
- Librería Pyxel

Instalación:

```bash
pip install pyxel


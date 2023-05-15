import pygame
from pygame.locals import *

# Cargamos las bibliotecas de OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *

#se inicializa Pygame
pygame.init()
#se define el tamaño del canvas
screen_width = 900
screen_height = 600
#se define el modo de la pantalla, estableciendo su ancho y alto en pixeles y el modo de trabajo de la ventana
#el cual será de doble buffer y responderá a Opengl
screen = pygame.display.set_mode(
    (screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption("OpenGL en Python")

# https://docs.microsoft.com/es-es/windows/win32/opengl/glmatrixmode
# Se establece el modo de la matriz a Proyección, de manera que las siguientes operaciones se considerarán
# como proyecciones en el plano 2D
glMatrixMode(GL_PROJECTION)
# https://docs.microsoft.com/es-es/windows/win32/opengl/glloadidentity
glLoadIdentity()
# Carga la matriz identidad, es una buena práctica siempre hacerlo cuando se establece un modo de matriz
# https://docs.microsoft.com/es-es/windows/win32/opengl/gluortho2d
# Establece que la proyección será ortográfica en 2 dimensiones comenzando en el pixel (0,0) y terminando en el
# pixel (600,400)
gluOrtho2D(600, 0, 400, 0)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # https://docs.microsoft.com/es-es/windows/win32/opengl/glclear
    # Se reinicia el buffer de color y el de profundidad en cada iteración del ciclo.
    # Se establece el modo de matriz a ModelView, de manera que las siguientes operaciones se considerarán
    # como vértices del modelo
    # Se inicializa a la matriz identidad (recomendable)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # https://docs.microsoft.com/es-es/windows/win32/opengl/glpointsize
    # Establece el radio de un punto a 10 pixeles
    glPointSize(10)
    # https://docs.microsoft.com/es-es/windows/win32/opengl/glbegin
    # Inicializa la construcción de primitivas, en este caso puntos
    glBegin(GL_POINTS)
    # https://docs.microsoft.com/es-es/windows/win32/opengl/glvertex2i
    # Cada punto está definido como un vértice de dos coordenadas enteras (¿Por qué?)
    # dado que son puntos, se pintarán solo dos puntos.
    glVertex2i(50, 50)
    glVertex2i(590, 390)
    # https://docs.microsoft.com/es-es/windows/win32/opengl/glend
    # termina el bloque de primitivas
    glEnd()

    # Realiza el cambio de buffers, es decir, pasa el contenido a la pantalla
    # hace una pausa de 100 ms (a nivel de proceso) (es más exacto usar delay)
    pygame.display.flip()
    pygame.time.wait(100)

pygame.quit()

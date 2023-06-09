from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
import numpy as np

# Definir espejo de cada vertice
coordenadas=[(0,0),(-10,10),(-15,0),(-30,10),(-40,0),(-60,0),(-150,0),(-15,30),(-40,20),(-10,40),
            (-70,40),(-115,40),(-140,30),(-190,20),(-10,60),(-40,60),(-80,80),(-120,80),(-170,90),(-190,80),           
            (-20,70),(-35,75),(-60,80),(-100,100),(0,90),(-10,100),(-30,90),(-40,95),(-60,110),(-110,110),
            (-170,110),(0,130),(-50,130),(-60,130),(-130,140),(-170,130),(-40,150),(0,150),(-30,170),(-70,180),
            (-150,180),(-20,190),(-80,200),(-150,200),(0,210),(-50,220),(-120,230),(-20,230),(-70,250),(-90,240),
            (0,50),(-20,-10),(-10,-15),(-60,-20),(-110,-20),(-5,-25),(-15,-25),(-5,-30),(-5,-40),(-20,-50),
            (-40,-55),(-45,-50),(-50,-40),(-60,-35),(-50,-60),(0,-80),(-30,-80),(-50,-80),(-100,-80),(-150,-50),
            (-30,-100),(-55,-110),(-80,-120),(-60,-140),(-30,-150),(-60,-170),(0,-240)]
#Uniones

f1=[41,44, 47, 48,49,45,41];f2=[41,45, 46, 43,42,38,41];f3=[37,38,41,44,37]
f4=[38,42,39,36,31,38]#Figura rellena
f5=[31,38,37,31];f6=[39,42,40,39];f7=[32,36,39,40,32];f8=[32,34,35,40,32];f9=[31,36,32,26,31];f10=[33,34,30,19,18,29,33];f11=[28,32,33,29,28]
f12=[16,28,29,16]#Figura rellena
f13=[23,29,18,13,23];f14=[22,16,32,26,27,22];f15=[20,21,22,27,26,20];f16=[14,20,26,25,14]
f17=[15,20,21,22,15]#Figura rellena
f18=[10,15,22,16,10]
f19=[10,11,16,10]#Figura rellena
f20=[6,12,17,23,16,11,6];f21=[13,12,17,13];f22=[8,14,15,10,8];f23=[14,15,20,14];f24=[8,9,14,8];f25=[9,50,24,25,14,9];f26=[8,7,50,9,8];f27=[2,1,7,3,4,51,2];f28=[6,11,10,54,69,6]
f29=[68,10,8,5,53,63,68]#Figura rellena
f30=[56,5,8,7,3,4,51,56];f31=[68,10,54,68];f32=[51,52,55,57,56,51];f33=[5,56,57,53,5];f34=[57,53,63,62,57];f35=[57,58,59,60,61,62,57]
f36=[63,62,61,64,67,63] #Figura rellena
f37=[63,68,72,63]
f38=[71,67,64,66,71]#Figura rellena
f39=[63,67,71,73,72,63]
f40=[65,66,71,70,65]#Figura rellena
f41=[65,70,75,74,65];f42=[70,71,73,75,70];f43=[65,74,76,65]

# Coordenadas espejo
espejo=[(0,0),(10,10),(15,0),(30,10),(40,0),(60,0),(150,0),(15,30),(40,20),(10,40),
            (70,40),(115,40),(140,30),(190,20),(10,60),(40,60),(80,80),(120,80),(170,90),(190,80),           
            (20,70),(35,75),(60,80),(100,100),(0,90),(10,100),(30,90),(40,95),(60,110),(110,110),
            (170,110),(0,130),(50,130),(60,130),(130,140),(170,130),(40,150),(0,150),(30,170),(70,180),
            (150,180),(20,190),(80,200),(150,200),(0,210),(50,220),(120,230),(20,230),(70,250),(90,240),
            (0,50),(20,-10),(10,-15),(60,-20),(110,-20),(5,-25),(15,-25),(5,-30),(5,-40),(20,-50),
            (40,-55),(45,-50),(50,-40),(60,-35),(50,-60),(0,-80),(30,-80),(50,-80),(100,-80),(150,-50),
            (30,-100),(55,-110),(80,-120),(60,-140),(30,-150),(60,-170),(0,-240)]

#Coordenadas absolutas (en ambos lados de los cuadrantes 1 y 2 o 3 y 4)
abs1=[(0,0),(-10,10),(-15,30),(0,50),(15,30),(10,10),(0,0)]
abs2=[(-15,0),(0,-10),(15,0)]
abs3=[(0,-10),(-15,0),(-20,-10),(-10,-15),(-5,-25),(-5,-30),(0,-30),(5,-30),(5,-25),(10,-15),(20,-10),(15,0)]

#Definicion de funciones para cada tipo de trazado (lineas, poligonos o poligonos rellenos de color)
def draw_poligono(puntos,uniones):
    glBegin(GL_LINE_LOOP)
    for uniones in uniones:
        glVertex2fv(puntos[uniones])
    glEnd()

def draw_relleno(puntos,uniones):
    glBegin(GL_POLYGON)
    for uniones in uniones:
        glVertex2fv(puntos[uniones])
    glEnd()

def draw_recta(puntos,uniones):
    glBegin(GL_LINES)
    for t in range(len(uniones) - 1):
        glVertex2fv(puntos[uniones[t]])
        glVertex2fv(puntos[uniones[t + 1]])
    glEnd()

# Inicializar Pygame y OpenGL
pygame.init()
display = (800, 800)
pygame.display.set_mode(display, pygame.DOUBLEBUF|pygame.OPENGL)
#Establecemos en el centro el origen de coordenadas
gluOrtho2D(-250, 250, -300, 300)

# Dibujar las figuras de los cuadrantes 2 y 3 (izquierda)
glClear(GL_COLOR_BUFFER_BIT)
draw_poligono(coordenadas, f1);draw_poligono(coordenadas, f2);draw_poligono(coordenadas, f3)
draw_relleno(coordenadas, f4);draw_poligono(coordenadas, f5);draw_poligono(coordenadas, f6)
draw_poligono(coordenadas, f7);draw_poligono(coordenadas, f8);draw_poligono(coordenadas, f9)
draw_poligono(coordenadas, f10);draw_poligono(coordenadas, f11);draw_relleno(coordenadas, f12)
draw_poligono(coordenadas, f13);draw_poligono(coordenadas, f14);draw_poligono(coordenadas, f15)
draw_poligono(coordenadas, f16);draw_relleno(coordenadas, f17);draw_poligono(coordenadas, f18)
draw_relleno(coordenadas, f19);draw_poligono(coordenadas, f20);draw_poligono(coordenadas, f21)
draw_poligono(coordenadas, f22);draw_poligono(coordenadas, f23);draw_poligono(coordenadas, f24)
draw_poligono(coordenadas, f25);draw_poligono(coordenadas, f26);draw_poligono(coordenadas, f27)
draw_poligono(coordenadas, f28);draw_relleno(coordenadas, f29);draw_poligono(coordenadas, f30)
draw_poligono(coordenadas, f31);draw_poligono(coordenadas, f32);draw_poligono(coordenadas, f33)
draw_poligono(coordenadas, f34);draw_poligono(coordenadas, f35);draw_relleno(coordenadas, f36)
draw_poligono(coordenadas, f37);draw_relleno(coordenadas, f38);draw_poligono(coordenadas, f39)
draw_relleno(coordenadas, f40);draw_poligono(coordenadas, f41);draw_poligono(coordenadas, f42)
draw_poligono(coordenadas, f43)
#Espejo derecho (Cuadrantes 1 y 4)
draw_poligono(espejo, f1);draw_poligono(espejo, f2);draw_poligono(espejo, f3)
draw_relleno(espejo, f4);draw_poligono(espejo, f5);draw_poligono(espejo, f6)
draw_poligono(espejo, f7);draw_poligono(espejo, f8);draw_poligono(espejo, f9)
draw_poligono(espejo, f10);draw_poligono(espejo, f11);draw_relleno(espejo, f12)
draw_poligono(espejo, f13);draw_poligono(espejo, f14);draw_poligono(espejo, f15)
draw_poligono(espejo, f16);draw_relleno(espejo, f17);draw_poligono(espejo, f18)
draw_relleno(espejo, f19);draw_poligono(espejo, f20);draw_poligono(espejo, f21)
draw_poligono(espejo, f22);draw_poligono(espejo, f23);draw_poligono(espejo, f24)
draw_poligono(espejo, f25);draw_poligono(espejo, f26);draw_poligono(espejo, f27)
draw_poligono(espejo, f28);draw_relleno(espejo, f29);draw_poligono(espejo, f30)
draw_poligono(espejo, f31);draw_poligono(espejo, f32);draw_poligono(espejo, f33)
draw_poligono(espejo, f34);draw_poligono(espejo, f35);draw_relleno(espejo, f36)
draw_poligono(espejo, f37);draw_relleno(espejo, f38);draw_poligono(espejo, f39)
draw_relleno(espejo, f40);draw_poligono(espejo, f41);draw_poligono(espejo, f42)
draw_poligono(espejo, f43)

draw_recta(abs1,[0,1,2,3,4,5,6,0])
draw_recta(abs2,[0,1,2])
draw_relleno(abs3,[0,1,2,3,4,5,6,7,8,9,10,11,0])
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

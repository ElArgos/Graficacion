from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
import numpy as np

# Definir las espejo de los trapecios
coordenadas=[(0,0),(-10,10),(-15,0),(-30,10),(-40,0),(-60,0),(-150,0),(-15,30),(-40,20),(-10,40),
            (-70,40),(-115,40),(-140,30),(-190,20),(-10,60),(-40,60),(-80,80),(-120,80),(-170,90),(-190,80),           
            (-20,70),(-35,75),(-60,80),(-100,100),(0,90),(-10,100),(-30,90),(-50,100),(-60,110),(-110,110),
            (-170,110),(0,130),(-50,130),(-60,130),(-130,140),(-170,130),(-40,150),(0,150),(-30,170),(-70,180),
            (-150,180),(-20,190),(-80,200),(-150,200),(0,210),(-50,220),(-120,230),(-20,230),(-70,250),(-90,240),
            (0,50),(-20,-10),(-10,-15),(-60,-20),(-110,-20),(-5,-25),(-15,-25),(-5,-30),(-5,-40),(-20,-50),
            (-40,-55),(-45,-50),(-50,-40),(-60,-35),(-50,-60),(0,-80),(-30,-80),(-50,-80),(-100,-80),(-150,-50),
            (-30,-100),(-55,-110),(-80,-120),(-60,-140),(-30,-150),(-60,-170),(0,-240)]

f1=[41,44, 47, 48,49,45,41];f2=[41,45, 46, 43,42,38,41];f3=[37,38,41,44,37]
f4=[38,42,39,36,31,38]#Rellenar
f5=[31,38,37,31];f6=[39,42,40,39];f7=[32,36,39,40,32];f8=[32,34,35,40,32];f9=[31,36,32,26,31];f10=[33,34,30,19,18,29,33];f11=[28,32,33,29,28]
f12=[16,28,29,16]#Rellenar
f13=[23,29,18,13,23];f14=[22,16,32,26,27,22];f15=[20,21,22,27,26,20];f16=[14,20,26,25,14]
f17=[15,20,21,22,15]#Rellenar
f18=[10,15,22,16,10]
f19=[10,11,16,10]#Rellenar
f20=[6,12,17,23,16,11,6];f21=[13,12,17,13];f22=[8,14,15,10,8];f23=[14,15,20,14];f24=[8,9,14,8];f25=[9,50,24,25,14,9];f26=[8,7,50,9,8];f27=[2,1,7,3,4,51,2];f28=[6,11,10,54,69,6]
f29=[68,10,8,5,53,63,68]#Rellenar
f30=[56,5,8,7,3,4,51,56];f31=[68,10,54,68];f32=[51,52,55,57,56,51];f33=[5,56,57,53,5];f34=[57,53,63,62,57];f35=[57,58,59,60,61,62,57]
f36=[63,62,61,64,67,63] #Rellenar
f37=[63,68,72,63];f38=[71,67,64,66,71];f39=[63,67,71,73,72,63];f40=[65,66,71,70,65];f41=[65,70,75,74,65];f42=[70,71,73,75,70];f43=[65,74,76,65]

espejo=[(0,0),(10,10),(15,0),(30,10),(40,0),(60,0),(150,0),(15,30),(40,20),(10,40),
            (70,40),(115,40),(140,30),(190,20),(10,60),(40,60),(80,80),(120,80),(170,90),(190,80),           
            (20,70),(35,75),(60,80),(100,100),(0,90),(10,100),(30,90),(50,100),(60,110),(110,110),
            (170,110),(0,130),(50,130),(60,130),(130,140),(170,130),(40,150),(0,150),(30,170),(70,180),
            (150,180),(20,190),(80,200),(150,200),(0,210),(50,220),(120,230),(20,230),(70,250),(90,240),
            (0,50),(20,-10),(10,-15),(60,-20),(110,-20),(5,-25),(15,-25),(5,-30),(5,-40),(20,-50),
            (40,-55),(45,-50),(50,-40),(60,-35),(50,-60),(0,-80),(30,-80),(50,-80),(100,-80),(150,-50),
            (30,-100),(55,-110),(80,-120),(60,-140),(30,-150),(60,-170),(0,-240)]

f44=[41,44, 47, 48,49,45,41];f45=[41,45, 46, 43,42,38,41];f46=[37,38,41,44,37]
f47=[38,42,39,36,31,38]#Rellenar
f48=[31,38,37,31];f49=[39,42,40,39];f50=[32,36,39,40,32];f51=[32,34,35,40,32];f52=[31,36,32,26,31];f53=[33,34,30,19,18,29,33];f54=[28,32,33,29,28]
f55=[16,28,29,16]#Rellenar
f56=[23,29,18,13,23];f57=[22,16,32,26,27,22];f58=[20,21,22,27,26,20];f59=[14,20,26,25,14]
f60=[15,20,21,22,15]#Rellenar
f61=[10,15,22,16,10]
f62=[10,11,16,10]#Rellenar
f63=[6,12,17,23,16,11,6];f64=[13,12,17,13];f65=[8,14,15,10,8];f66=[14,15,20,14];f67=[8,9,14,8];f68=[9,50,24,25,14,9];f69=[8,7,50,9,8];f70=[2,1,7,3,4,51,2];f71=[6,11,10,54,69,6]
f72=[68,10,8,5,53,63,68]#Rellenar
f73=[56,5,8,7,3,4,51,56];f74=[68,10,54,68];f75=[51,52,55,57,56,51];f76=[5,56,57,53,5];f77=[57,53,63,62,57];f78=[57,58,59,60,61,62,57]
f79=[63,62,61,64,67,63] #Rellenar
f80=[63,68,72,63];f81=[71,67,64,66,71];f82=[63,67,71,73,72,63];f83=[65,66,71,70,65];f84=[65,70,75,74,65];f85=[70,71,73,75,70];f86=[65,74,76,65]



def draw_figure(puntos,uniones):
    glBegin(GL_LINE_LOOP)
    for uniones in uniones:
        glVertex2fv(puntos[uniones])
    glEnd()

# Inicializar Pygame y OpenGL
pygame.init()
display = (800, 800)
pygame.display.set_mode(display, pygame.DOUBLEBUF|pygame.OPENGL)

gluOrtho2D(-250, 250, -300, 300)

# Dibujar los trapecios
glClear(GL_COLOR_BUFFER_BIT)
draw_figure(coordenadas, f1);draw_figure(coordenadas, f2);draw_figure(coordenadas, f3)
draw_figure(coordenadas, f4);draw_figure(coordenadas, f5);draw_figure(coordenadas, f6)
draw_figure(coordenadas, f7);draw_figure(coordenadas, f8);draw_figure(coordenadas, f9)
draw_figure(coordenadas, f10);draw_figure(coordenadas, f11);draw_figure(coordenadas, f12)
draw_figure(coordenadas, f13);draw_figure(coordenadas, f14);draw_figure(coordenadas, f15)
draw_figure(coordenadas, f16);draw_figure(coordenadas, f17);draw_figure(coordenadas, f18)
draw_figure(coordenadas, f19);draw_figure(coordenadas, f20);draw_figure(coordenadas, f21)
draw_figure(coordenadas, f22);draw_figure(coordenadas, f23);draw_figure(coordenadas, f24)
draw_figure(coordenadas, f25);draw_figure(coordenadas, f26);draw_figure(coordenadas, f27)
draw_figure(coordenadas, f28);draw_figure(coordenadas, f29);draw_figure(coordenadas, f30)
draw_figure(coordenadas, f31);draw_figure(coordenadas, f32);draw_figure(coordenadas, f33)
draw_figure(coordenadas, f34);draw_figure(coordenadas, f35);draw_figure(coordenadas, f36)
draw_figure(coordenadas, f37);draw_figure(coordenadas, f38);draw_figure(coordenadas, f39)
draw_figure(coordenadas, f40);draw_figure(coordenadas, f41);draw_figure(coordenadas, f42)
draw_figure(coordenadas, f43)
#Espejo derecho
draw_figure(espejo, f44);draw_figure(espejo, f45);draw_figure(espejo, f46)
draw_figure(espejo, f47);draw_figure(espejo, f48);draw_figure(espejo, f49)
draw_figure(espejo, f50);draw_figure(espejo, f51);draw_figure(espejo, f52)
draw_figure(espejo, f53);draw_figure(espejo, f54);draw_figure(espejo, f55)
draw_figure(espejo, f56);draw_figure(espejo, f57);draw_figure(espejo, f58)
draw_figure(espejo, f59);draw_figure(espejo, f60);draw_figure(espejo, f61)
draw_figure(espejo, f62);draw_figure(espejo, f63);draw_figure(espejo, f64)
draw_figure(espejo, f65);draw_figure(espejo, f66);draw_figure(espejo, f67)
draw_figure(espejo, f68);draw_figure(espejo, f69);draw_figure(espejo, f70)
draw_figure(espejo, f71);draw_figure(espejo, f72);draw_figure(espejo, f73)
draw_figure(espejo, f74);draw_figure(espejo, f75);draw_figure(espejo, f76)
draw_figure(espejo, f77);draw_figure(espejo, f78);draw_figure(espejo, f79)
draw_figure(espejo, f80);draw_figure(espejo, f81);draw_figure(espejo, f82)
draw_figure(espejo, f83);draw_figure(espejo, f84);draw_figure(espejo, f85)
draw_figure(espejo, f86)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

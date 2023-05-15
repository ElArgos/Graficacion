import math
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *


class GLUtils:

    @staticmethod
    def initOrtho(left, right, top, bottom):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(left, right, top, bottom)
        
    #dibuja a la función que se le pase por parametro (String) regla
    @staticmethod
    def drawGraphPoints(regla, minx, maxx):
        glPointSize(5)
        glBegin(GL_POINTS)
        for x in np.arange(minx, maxx, 0.015):
            glColor3f(0.5, 0.3, 0.8)
            glVertex2f(x, eval(regla))
        glEnd()

    #Dibuja el eje de las x e y
    @staticmethod
    def drawAxis(minx, maxx, miny, maxy):
        glPointSize(5)
        glColor3f(0, 0, 0)
        glBegin(GL_LINES)
        glVertex2f(minx, 0)
        glVertex2f(maxx, 0)
        glVertex2f(0, miny)
        glVertex2f(0, maxy)
        glEnd()

    #Función añadida para dbujar una linea entre 2 puntos    
    @staticmethod
    def drawLine(x1,y1,x2,y2):
        glPointSize(5)
        glColor3f(0, 0, 0)
        glBegin(GL_LINES)
        glVertex2f(x1, y1)
        glVertex2f(x2, y2)
        glEnd()

    @staticmethod
    def drawLines(vertices,uniones):
        glColor3f(0, 0, 0)
        for t in range(len(uniones) - 1):
            glBegin(GL_LINES)
            glVertex2fv(vertices[uniones[t]])
            glVertex2fv(vertices[uniones[t + 1]])
            glEnd()
            print(t)

            
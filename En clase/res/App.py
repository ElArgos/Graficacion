import sys
import pygame as pg
from pygame.locals import *


class App:
    def __init__(self, title, width, height, maxFps):
        pg.init()
        self.title, self.maxFps = title, maxFps
        self.screenWidth, self.screenHeight = width, height
        self.display = pg.display.set_mode((width, height), DOUBLEBUF | OPENGL)
        self.clock = pg.time.Clock()

    def Run(self):

        self.Init()   # initial members
        self.Setup()  # initial configs

        while 1:
            self.events = pg.event.get()
            # Añadido para saber la posicion del mouse
            if self.events == pg.MOUSEMOTION:
                print(pg.mouse.get_pos())
            for event in self.events:
                if event.type == pg.QUIT:
                    sys.exit()

            self.deltaTime = self.clock.tick(self.maxFps) / 1000

            self.Inputs()  # frame inputs
            self.Update()  # frame logic
            self.Render()  # frame drawing

            pg.display.flip()
            pg.display.set_caption(
                f"{self.title} ({self.clock.get_fps():.2f} fps)")

    def Init(self):
        pass

    def Setup(self):
        pass

    def Inputs(self):
        pass

    def Update(self):
        pass

    def Render(self):
        pass

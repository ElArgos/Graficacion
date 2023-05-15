import pygame
class Input(object):
    def __init__(self):
        # has the user quit the application?
        self.quit = False

    def update(self):
        # iterate over all user input events (such as keyboard or mouse)
        for event in pygame.event.get():
        # that occurred since the last time events were checked
            if event.type == pygame.QUIT:
                self.quit = True
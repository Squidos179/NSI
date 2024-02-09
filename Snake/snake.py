import pygame
from random import randint
from anneau import Anneau

class Serpent:
    head = Anneau()

    vec2D = [0, 0]

    def keyHandling(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.vec2D[0] != 1:
            self.vec2D[0] = -1
            self.vec2D[1] = 0
        if keys[pygame.K_RIGHT] and self.vec2D[0] != -1:
            self.vec2D[0] = 1
            self.vec2D[1] = 0
        if keys[pygame.K_UP] and self.vec2D[1] != 1:
            self.vec2D[0] = 0
            self.vec2D[1] = -1
        if keys[pygame.K_DOWN] and self.vec2D[1] != -1:
            self.vec2D[0] = 0
            self.vec2D[1] = 1

    def update(self):
        self.keyHandling()
        self.head.update(self.vec2D)
        self.head.render()
from snake import Serpent
import pygame

class Serpent2(Serpent):

    def __init__(self) -> None:
        super().__init__()

    def keyHandling(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q] and self.vec2D[0] != 1:
            self.vec2D[0] = -1
            self.vec2D[1] = 0
        if keys[pygame.K_d] and self.vec2D[0] != -1:
            self.vec2D[0] = 1
            self.vec2D[1] = 0
        if keys[pygame.K_z] and self.vec2D[1] != 1:
            self.vec2D[0] = 0
            self.vec2D[1] = -1
        if keys[pygame.K_s] and self.vec2D[1] != -1:
            self.vec2D[0] = 0
            self.vec2D[1] = 1

    def render(self, surf, scoreFont):
        self.head.render(surf)
        pygame.draw.rect(surf, (0, 0, 255), (self.px, self.py, 20, 20))

        scoreText = scoreFont.render(str(self.score), True, (255, 255, 255))
        surf.blit(scoreText, (780, 20))
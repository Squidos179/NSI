from snake import Serpent
import pygame

class Serpent2(Serpent):

    def __init__(self) -> None:
        """
        Initialise un objet Serpent2 en utlisant comme base la classe Serpent avec de l'héritage.
        Returns:
            None : on crée un objet Serpent2.
        """
        super().__init__()

    def keyHandling(self):
        """
        Gère les touches du clavier pour contrôler le serpent
        Returns:
            None : on modifie directement les attributs du serpent.
        """
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
        """
        Dessine le serpent sur la surface donnée.
        Args:
            surf (pygame.Surface): La surface sur laquelle on dessine.
            scoreFont (pygame.font.Font): La police pour afficher le score.
        Returns:
            None : on modifie directement la surface.
        """
        self.head.render(surf, (0x7B, 0x50, 0x6F))

        scoreText = scoreFont.render(str(self.score), True, (255, 255, 255))
        surf.blit(scoreText, (640, 20))
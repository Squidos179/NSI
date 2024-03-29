import pygame
from anneau import Anneau
from constants import MULTIPLE, LARG, HAUT

class Serpent:

    class Snake:
        def __init__(self) -> None:
            """
            Initialise un objet Snake.
            Returns:
                None : on crée un objet Snake.
            """
            self.head = Anneau()
            self.vec2D = [0, 0]
            self.score = 0

    def keyHandling(self):
            """
            Gère les touches du clavier pour contrôler le serpent
            Returns:
                None : on modifie directement les attributs du serpent.
            """
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

    def gameOver(self):
        """
        Réinitialise les attributs du jeu lorsque la partie est terminée.
        """
        self.score = 0
        self.head.x, self.head.y = (LARG * MULTIPLE) / 2, (HAUT * MULTIPLE) / 2
        self.vec2D = [0, 0]
        self.head.suivant = None
        print("feur")

    def collision(self):
        """
        Vérifie s'il y a une collision entre la tête du serpent et ses segments du corps ou les limites du plateau de jeu.
        Si une collision est détectée, le jeu est terminé.
        Retuns:
            None : on modifie directement les attributs du serpent.
        """
        suivant = self.head.suivant

        while suivant != None:
            if self.head.x == suivant.x and self.head.y == suivant.y:
                self.gameOver()
                suivant = suivant.suivant

            if self.head.x > (LARG * MULTIPLE) - 20 or self.head.x < 0 or self.head.y > (HAUT * MULTIPLE) - 20 or self.head.y < 0:
                self.gameOver()

    def update(self):
            """
            Met à jour la position des anneaux du serpent en fonction de la direction actuelle.
            Returns:
                None : on modifie directement les attributs du serpent.
            """
            suivant = self.head.suivant
            self.keyHandling()
            self.collision()
            self.head.fx = self.head.x + 20 * self.vec2D[0]
            self.head.fy = self.head.y + 20 * self.vec2D[1]


            while suivant != None:

                suivant.fx = suivant.avant.x
                suivant.fy = suivant.avant.y

                suivant = suivant.suivant

            self.head.update()

            suivant = self.head.suivant

            while suivant != None:

                suivant.update()

                suivant = suivant.suivant

    def render(self, surf, scoreFont):
        """
        Dessine le serpent sur la surface donnée.
        Args:
            surf (pygame.Surface): La surface sur laquelle on dessine.
            scoreFont (pygame.font.Font): La police pour afficher le score.
        Returns:
            None : on modifie directement la surface.
        """
        self.head.render(surf, (255, 255, 255))

        scoreText = scoreFont.render(str(self.score), True, (255, 255, 255))
        surf.blit(scoreText, (20, 20))
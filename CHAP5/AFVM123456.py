class Voiture:
    """
    Permet de modéliser une voiture
    """
    matière="acier"
    nombre_de_places=5
    longueur=4.5
    def __init__(self, couleur_utilisateur, nombre_de_km=0, a_charger=[ ]):
        """
        Constructeur
        Un arg. pos. – chaine de caractères pour la couleur de la voiture
        Deux arguments nommés :
            * nombre_de_km : Entier pour le nombre de km du véhicule
            * a_charger : Liste pour tous les objets à mettre dans le coffre
        """
        self.couleur = couleur_utilisateur
        self.km=nombre_de_km
        self.coffre= a_charger[ :]

    def avance(self, distance) :
        """
        Incrémente la variable km par une distance
        Args:
            distance : Un entier, le nombre de kilomètres qu'on ajoute
        """
        self.km+=distance

    def charge(self, a_charger=[ ]) :
        """
        Ajoute des éléments au coffre
        Args:
            a_charger: Une liste, les éléments qu'on ajoute au coffre
        """
        self.coffre+= a_charger

    def estNeuve(self):
        """
        Retourne si la voiture à déjà avancé
        """
        return self.km == 0
            
        
    def videLeCoffre(self):
        """
        Retourne si coffre est vide
        """
        self.coffre = []

    def __repr__(self):
        return f"Jaaj {self.coffre}"

feur = Voiture('bleu', 0, ['poulet', 'jambon'])

print(feur.__repr__)
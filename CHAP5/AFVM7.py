class Wagon:
    def __init__(self, contenu):
        "Constructeur"
        self.contenu = contenu
        self.suivant = None
    def __repr__(self):
        "Affichage dans la console"
        return f'Wagon de {self.contenu}'
    def __str__(self):
        "Conversion en string"
        return self.__repr__()

wagon1 = Wagon('Une bouteille de champagne')
print(wagon1.__repr__())
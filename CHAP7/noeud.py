from __future__ import annotations

class Noeud:
    def __init__(self, etiquette:str, enfants:list) -> None:
        self.etiquette = etiquette
        self.enfants = enfants

    def ajoute_fils(self, noeud:Noeud) -> None:
        self.enfants.append(noeud)

    def __str__(self) -> str:
        if self.enfants == []:
            return f"({self.etiquette})"
        else:
            result = f"({self.etiquette} ( "
            for i in self.enfants:
                result += f"{i.__str__()}"
                result += ' '
            result += ')'
            return result
        
c = Noeud("jifghso", [])
f = Noeud("feur", [c])
p = Noeud("jaaj", [f, c])
print(p)
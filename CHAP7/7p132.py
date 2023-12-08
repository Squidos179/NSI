from __future__ import annotations

class BinTree:
    def __init__(self, data, left=None, right=None) -> None:
        self._data = data
        self._left = left
        self._right = right

    def set_left(self, left=None):
        self._left = left

    def left(self):
        return self._left
    
    def set_right(self, right = None):
        self._right = right
    
    def right(self):
        return self.right
    
    def set_data(self, data):
        self._data = data

    def data(self):
        return self._data
    
    def __str__(self):
        if self._right == None and self._left == None:
            return '(' + self._data + ')'
        elif self._right == None:
            return '(' + self._data + ')' + self._left.__str__()
        elif self._left == None:
            return '(' + self._data + ')' + self._right.__str__()
    
def size(arbre:BinTree)->int:
    if arbre == None:
        return 0
    return 1 + size(arbre.left) + size(arbre.right)

def hauteur(arbre:BinTree):
    if arbre._left == None and arbre._right == None:
        return 0
    elif arbre._left == None:
        return 1 + hauteur(arbre._right)
    elif arbre._right == None:
        return 1 + hauteur(arbre._left)
    else:
        return max(1 + hauteur(arbre._left), 1 + hauteur(arbre._right))
    
def feuilles(arbre:BinTree)->int:
    if arbre._left == None and arbre._right == None:
        return 1
    elif arbre._left == None:
        return feuilles(arbre._right)
    elif arbre._right == None:
        return feuilles(arbre._left)
    else:
        return feuilles(arbre.left) + feuilles(arbre.right)

def noeud(arbre:BinTree)->int:
    return size(arbre) - feuilles(arbre)

feur  = BinTree("A", BinTree("B", BinTree("D"), BinTree("E", BinTree("H"), BinTree("I", BinTree("N"), BinTree("O")))), BinTree("C", BinTree("F", BinTree("J"), BinTree("K")), BinTree("G", BinTree("L"), BinTree("M", BinTree("P"), BinTree("Q")))))
a = BinTree("A")

print(feur)
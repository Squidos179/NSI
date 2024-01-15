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
            return self._data
        else:
            return self._data + self._left.__str__() + self._right.__str__()
        
    
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

jaaj  = BinTree("A", BinTree("B", BinTree("D"), BinTree("E", BinTree("H"), BinTree("I", BinTree("N"), BinTree("O")))), BinTree("C", BinTree("F", BinTree("J"), BinTree("K")), BinTree("G", BinTree("L"), BinTree("M", BinTree("P"), BinTree("Q")))))

def prefixe(arbre:BinTree)-> None:
    print(arbre._data)
    if (arbre._left != None) :
        prefixe(arbre._left)
    if (arbre._right != None) :
        prefixe(arbre._right) 

def infixe(arbre:BinTree)-> None:
    global feur
    if (arbre._left != None) :
        infixe(arbre._left)
    feur.append(arbre._data)
    if (arbre._right != None) :
        infixe(arbre._right)

def postfixe(arbre:BinTree)-> None:
    if (arbre._left != None) :
        infixe(arbre._left)
    if (arbre._right != None) :
        infixe(arbre._right)
    print(arbre._data)

def insertion(arbre:BinTree, key:str) :
    if arbre._data == None :
        return BinTree(key, None, None)
    else :
        e = arbre._data
        if e < key :
            return BinTree(e, insertion(arbre._left, key), arbre._right)
        else :
            return BinTree(e, arbre._left, insertion(arbre._right, key))

def recherche(arbre:list) :
    if arbre == None:
        return False
    for i in range(len(arbre) - 1):
        if arbre[i] > arbre[i + 1]:
            return False
    return True

def max(arbre:list):
    if recherche(arbre):
        return arbre[len(arbre) - 1]
    return False

def min(arbre:list):
    if recherche(arbre):
        return arbre[0]
    return False

def e(arbre:list, key):
    for i in arbre:
        if i == key:
            return True
    return False

feur = []
jaaj = BinTree(13, BinTree(11, BinTree(4), BinTree(12)), BinTree(16))

infixe(jaaj)
print(feur)
print(min(feur))
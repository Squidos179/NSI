import string
import random

def numero_lettre():
    dic = {}
    p = 0
    for i in string.ascii_uppercase:
        dic[i] = p
        p += 1
    return dic

def numero_lettrei():
    dic = {}
    p = 0
    for i in string.ascii_uppercase:
        dic[p] = i
        p += 1
    return dic

def codage_cesar(string, dec):
    ref = numero_lettre()
    refi = numero_lettrei()
    num = ""
    res = ""
    for i in string:
        num = ref[i] + dec
        res += refi[num % 26]
    return res

def decodage_cesar(string, dec):
    ref = numero_lettre()
    refi = numero_lettrei()
    num = ""
    res = ""
    for i in string:
        num = ref[i] - dec
        res += refi[num % 26]
    return res

def codage_inverse(string):
    ref = numero_lettre()
    refi = numero_lettrei()
    res = ""
    for i in string:
        res += str(refi[25 - ref[i]])
    return res

def genere_table()->dict:
    liste = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    liste2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    random.shuffle(liste)
    table = {}
    for i in range(len(liste)):
        table[liste2[i]] = liste[i]
    return table

def codage(string, table=genere_table()):
    res = ""
    for i in string:
        res += table[i]
    return res, table

def decodage(string, table=genere_table()):
    res = ""
    inv = {}
    for (key, value) in table:
        inv[value] = key
    for i in string:
        res += inv[i]
    return res

print(decodage("ZOOZ", {'A': 'O', 'B': 'J', 'C': 'Q', 'D': 'D', 'E': 'T', 'F': 'R', 'G': 'S', 'H': 'B', 'I': 'Y', 'J': 'Z', 'K': 'K', 'L': 'C', 'M': 'H', 'N': 'X', 'O': 'A', 'P': 'M', 'Q': 'I', 'R': 'G', 'S': 'N', 'T': 'P', 'U': 'E', 'V': 'V', 'W': 'L', 'X': 'F', 'Y': 'U', 'Z': 'W'}))
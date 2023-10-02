import csv

def import_csv(fichier):
    file = open(fichier, 'r')
    read_File = csv.DictReader(file)
    list = []
    for ligne in read_File:
        nLigne = dict(ligne)
        list.append(nLigne)
    return list

def export_to_csv(dico, att):
    with open(dico + '.csv', 'w') as fic:
        dic = csv.DictWriter(fic, fieldnames=att)
        table = eval(dico)
        print(table)
        dic.writeheader()
        for ligne in table:
            dic.writerow(ligne)
    return None

def select(table, critere):
    def test(ligne):
        return eval(critere)
    return [ligne for ligne in table if test(ligne)]

def projection(table, liste_attributs):
    ma_liste = []
    for ligne in table:
        mon_dico = {}
        for cle in ligne:
            if cle in liste_attributs:
                mon_dico[cle] = ligne[cle]
        ma_liste.append(mon_dico)
    return ma_liste

def tri(table, attribut, decroit=False):
    def critere(ligne):
        return ligne[attribut]
    return sorted(table, key=critere, reverse=decroit)

jaajjaaj = [{'Nom': 'feur', 'E': True}, {'Nom': 'Axel', 'E': False}, {'Nom': 'jaaj', 'E': False}]

print(import_csv('base.csv'))
print(export_to_csv('jaajjaaj', ['Nom', 'E']))
print(select(import_csv('base.csv'), 'ligne["Nom"]=="Joe"'))
print(projection(jaajjaaj, ['Nom']))
print(tri(jaajjaaj, 'Nom', False))

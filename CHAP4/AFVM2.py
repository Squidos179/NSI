# -*- coding: utf-8 -*-

import csv
from copy import deepcopy

def import_csv(fichier):
    file = open(fichier, 'r')
    read_File = csv.DictReader(file)
    list = []
    for ligne in read_File:
        nLigne = dict(ligne)
        list.append(nLigne)
    return list

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

def jointure(table1, table2, cle1, cle2=None):
    if cle2 is None:
        cle2 = cle1
    new_table = []
    for ligne1 in table1:
        for ligne2 in table2:
            if ligne1[cle1] == ligne2[cle2]:
                new_line = deepcopy(ligne1)
                for cle in ligne2:
                    if cle != cle2:
                        new_line[cle] = ligne2[cle]
                    new_table.append(new_line)
    return new_table

print(select(import_csv('localisation_colleges_cotes_d_armor.csv'), 'ligne["Commune"]=="DINAN"'))
print(projection(import_csv('localisation_colleges_cotes_d_armor.csv'), ['Communesrelevantdusecteurderecrutement', 'Detailsecteurscolaire', 'Commune', 'college']))
print(tri(import_csv('localisation_colleges_cotes_d_armor.csv'), 'Commune', False))
print(jointure(import_csv('base.csv'), import_csv('base2.csv'), 'Nom', 'Name'))
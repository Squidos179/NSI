# -*- coding: utf-8 -*-

import csv

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

print(select(import_csv('localisation_colleges_cotes_d_armor.csv'), 'ligne["Commune"]=="DINAN"'))
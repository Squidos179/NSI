import pandas
info_villes=pandas.read_csv("villes_virgule.csv")
nom_alt=info_villes.loc[(info_villes["alt_min"]>1500) & (info_villes["nb_hab_2010"]>600),["nom", "nb_hab_2010", "alt_min"]]
print(nom_alt)
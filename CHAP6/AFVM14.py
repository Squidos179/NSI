from timeit import timeit

def fusion(lst1:list, lst2:list)->list:
    t= []
    while lst1 and lst2:
        if lst1[0] > lst2[0]:
            t.append(lst2[0])
            lst2.pop(0)
        else:
            t.append(lst1[0])
            lst1.pop(0)
    t += lst1
    t += lst2
    return t

def triFusion(lst:list)->list:
    if 1 < len(lst):
        return fusion(triFusion(lst[0:len(lst)//2]), triFusion(lst[len(lst)//2:len(lst)]))
    return lst

def tri_insertion(liste):
    j = 1
    while j<len(liste):
        i = j-1
        k = liste[j]
        while i>=0 and liste[i]>k:
            liste[i+1] = liste[i]
            i = i-1
        liste[i+1] = k
        j = j+1
    return liste

def tri_selection(liste):
    i = 0
    while i<len(liste):
        j = i+1
        min = i
        while j<len(liste):
            if liste[j]<liste[min]:
                min = j
            j = j+1
        if min != i :
            liste[i], liste[min] = liste[min], liste[i]
        i = i+1
    return liste

def tri_a_bulle(liste):
    for j in range(len(liste)-1):
        for i in range(len(liste)-1):
            if liste[i] > liste[i+1]:
                liste[i], liste[i+1] = liste[i+1], liste[i]
    return liste

tps = timeit("triFusion([0, 2, 3, 47, 56, 5, 78, 56, 67, 2, 4.5, 3, 2])", number = 1000000, globals=globals())
print(f"Temps écoulé pour 1 000 000 exécution de la fonction tri fusion : {tps} ")
tps2 = timeit("tri_insertion([0, 2, 3, 47, 56, 5, 78, 56, 67, 2, 4.5, 3, 2])", number = 1000000, globals=globals())
print(f"Temps écoulé pour 1 000 000 exécution de la fonction tri insertion : {tps2} ")
tps3 = timeit("tri_selection([0, 2, 3, 47, 56, 5, 78, 56, 67, 2, 4.5, 3, 2])", number = 1000000, globals=globals())
print(f"Temps écoulé pour 1 000 000 exécution de la fonction tri selection : {tps3} ")
tps4 = timeit("tri_a_bulle([0, 2, 3, 47, 56, 5, 78, 56, 67, 2, 4.5, 3, 2])", number = 1000000, globals=globals())
print(f"Temps écoulé pour 1 000 000 exécution de la fonction tri à bulles : {tps4} ")
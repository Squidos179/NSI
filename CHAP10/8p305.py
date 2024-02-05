from functools import wraps
from time import perf_counter_ns as feur

def decorateur_magique(fonction_a_decorer):

    @wraps(fonction_a_decorer)
    def wrapper_autour_de_la_fonction_originale():

        print("Avant que la fonction_originale")

        fonction_a_decorer()

        print("Après que la fonction se soit exécutée.")

    return wrapper_autour_de_la_fonction_originale

def chrono(func):
    def chronom(n):
        p = feur()

        func(n)

        s = feur()

        return s - p
    return chronom

@chrono
def boucle(n):
    for _ in range(n):
        pass

@decorateur_magique
def une_fonction_intouchable():
    "Ceci est une docstring de test"
    print("Je suis une fonction, intouchable, ne me modifiez pas !")

def chrono2(f):
    @wraps(f)
    def my_f(*args, **kwargs):
        t0 = feur()
        v = f(*args, **kwargs)
        t1 = feur()
        print(t1-t0, "ns")
        return v
    return my_f

@chrono2
def boucle2(n, autre=100):
    for _ in range(n*autre):
        pass

boucle2(1000000, autre=50)
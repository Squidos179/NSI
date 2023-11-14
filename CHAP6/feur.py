def pgcd(a, b):
    if b == 0:
        return a
    else:
        return pgcd(b, a %b)
    
def irr(a, b):
    feur = pgcd(a, b)
    return [a/feur, b/feur]

def lst(n):
    if n == 0:
        return [0]
    else:
        return [n] + lst(n-1)

print(lst(5))
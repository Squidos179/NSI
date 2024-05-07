import string

def numero_lettrei():
    dic = {}
    p = 0
    for i in string.ascii_uppercase:
        if p + 1 < 10:
            dic[i] = "0" +  str(p + 1)
        else:
            dic[i] = str(p + 1)
        p += 1
    return dic

def numero_lettre():
    dic = {}
    p = 0
    for i in string.ascii_uppercase:
        if p + 1 < 10:
            dic[ "0" + str(p + 1)] =str(i)
        else:
            dic[str(p + 1)] = str(i)
        p += 1
    return dic

def car_to_fig(string):
    ref = numero_lettrei()
    res = ""
    for i in string:
        res += ref[i]
    return res

def chiffrement_RSA(string, cle):
    e = 7
    ref = car_to_fig(string)
    res = []
    mods = []
    if len(ref) % 3 != 0:
        ref = "0" + ref
    for i in range(0, len(ref), 3):
        res.append(ref[i:i+3])
    for i in res:
        mods.append(str(int(i)**e % cle))
    return mods

def dechiffrement_RSA(l, p, q):
    n = p * q
    jaaj = (p - 1) * (q - 1)
    d = 0
    while (d * 7) % jaaj != 1:
        d += 1
    res = []
    for i in l:
        a = (int(i) ** d) % n
        if len(str(a)) % 3:
            while len(str(a)) % 3 != 0:
                a = "0" + str(a)
        res.append(str(a))
    return res

def fig_to_car(l):
    c =  ""
    ref = numero_lettre()
    res = ""
    for i in l:
        c += i
    if c[0] == '0':
        c = c[1:]
    for i in range(0, len(c), 2):
        res += ref[c[i:i+2]]
    return res

feur = chiffrement_RSA("FEUR", 5141)
#print(feur)
jaaj = dechiffrement_RSA(feur, 53, 97)
#print(jaaj)
juuj = fig_to_car(jaaj)
print(juuj)

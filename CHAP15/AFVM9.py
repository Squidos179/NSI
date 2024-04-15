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

def car_to_fig(string):
    ref = numero_lettrei()
    res = ""
    for i in string:
        res += ref[i]
    return res

def chiffrement(string, cle):
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

def dechiffrement(l, p, q):
    print("002151410152118")

print(chiffrement("BONJOUR", 5141))
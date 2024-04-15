def codage_binaire(a, b):
    t = None
    res = ""
    for i in range(len(a)):
        t = ord(a[i]) ^ ord(b[i % len(b)])
        print(t)
        res += chr(t)
    return res

print(codage_binaire("lul", "jaaj"))
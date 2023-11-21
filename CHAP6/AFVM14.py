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

print(triFusion([0, 2, 3, 47, 56, 5, 78, 56]))
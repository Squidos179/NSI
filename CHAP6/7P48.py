def div_egypt(a,b):
    if a == 0:
        return 0
    elif a%2 == 0:
        return div_egypt(a//2, b*2)
    elif a%2 == 1:
        return b+div_egypt(a-1, b)
    
print(div_egypt(13,61))
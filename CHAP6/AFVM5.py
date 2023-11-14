def factorielRecursive(n) :
    if n > 0 :
        return n*factorielRecursive(n-1)
    else :
        return 1
    
print(factorielRecursive(5))
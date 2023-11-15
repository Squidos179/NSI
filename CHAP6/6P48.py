import timeit

def pui(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return pui(a*a, n / 2)
    else:
        return a * pui(a*a, (n-1)/2)
    
def puiC(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return (a* a)**(n/2)
    else:
        return a*(a* a)**((n-1)/2)

    
print(puiC(2, 3))
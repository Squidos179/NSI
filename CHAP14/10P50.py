def recur_tribonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return recur_tribonacci(n-1) + recur_tribonacci(n-2) + recur_tribonacci(n-3)    
    
def pgcd(a, b):
    c = a % b
def integral(f, a, b, n):
    """Calcul de l' intégrale d' une fonction sur un intervalle
    @params :
    - f : fonction python
    - a : borne inférieure de l' intervalle
    - b : borne supérieure de l' intervalle
    - n : nombre de sous-intervalles
    @returns :
    - Une valeur approchée de l' intégrale
    """
    h = (b-a)/n
    integrale = 0
    for i in range(n):
        integrale += (f(a)+f(a+h))/2
    return integrale
from math import factorial

def calcular_fatorial(numero):
    if type(numero) == int and numero > 0:
        print(factorial(numero))

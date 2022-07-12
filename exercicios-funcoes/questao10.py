def calcular_sequencia(n):
    if type(n) == int and n > 0:
        s = 0
        for i in range(1,n+1):
            s += 1/i
        print(s)

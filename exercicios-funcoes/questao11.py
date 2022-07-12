def calcular_sequencia(n):
    if type(n) == int and n > 0:
        s = 0
        qtd = 0
        for i in range(1,n+1):
            s += (n**2) / (n+3)
            qtd += 1
        print(s, qtd)

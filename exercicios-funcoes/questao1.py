def somar_numeros(numero):
    soma = 0
    if numero > 0:
        for i in range(1,numero+1):
            soma += i
    print(soma)

def somar_divisores(numero):
    if type(numero) == int and numero > 0:
        soma = 0
        for i in range(1, numero+1):
            if numero % i == 0:
                soma += i
        return soma

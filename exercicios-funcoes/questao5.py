def analisar_numero(numero):
    if type(numero) == int:
        if numero > 0:
            print('numero positivo')
        else:
            print('numero negativo')
    else:
        print('não é um numero inteiro')


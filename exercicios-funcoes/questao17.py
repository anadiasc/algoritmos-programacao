def calcular_mdc(num1, num2):
    maior = 0
    divisores = []
    mdc = 0
    if num1 > num2:
        maior = num1
    elif num1 < num2:
        maior = num2
    else:
        maior = num1
    
    for i in range(1,maior):
        if num1 % i == 0 and num2 % i == 0:
            divisores.append(i)
    
    for i in range(len(divisores)):
        if i == 0:
            mdc = divisores[i]
        elif mdc < divisores[i]:
            mdc = divisores[i]

    print(f'O MDC entre {num1} e {num2} é: {mdc}')

calcular_mdc(24,60)
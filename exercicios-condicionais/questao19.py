altura = float(input())
sexo = str(input())

if sexo == 'feminino':
    peso_ideal = (62.1 * altura) - 44.7
    print(f'O peso ideal é {peso_ideal}')
elif sexo == 'masculino':
    peso_ideal = (72.7 * altura) - 58
    print(f'O peso ideal é {peso_ideal}')
else:
    print('Escolha inválida.\nInforme se o sexo é masculino ou feminino')
while True:
    print('Menu de opções:\n1. Novo salario\n2. Férias\n3. Décimo terceiro\n4. sair')
    escolha = int(input('Digite a opção desejada: '))
    
    if escolha == 1:
        salario = float(input())
        if salario < 210:
            novo_salario = salario + (salario * 0.15)
            print(novo_salario)
        elif salario >= 210 and salario >= 600:
            novo_salario = salario + (salario * 0.1)
            print(novo_salario)
        elif salario > 600:
            novo_salario = salario + (salario * 0.05)
            print(novo_salario)
    elif escolha == 2:
        salario = float(input())
        ferias = salario + (salario * 1/3)
        print(ferias)
    elif escolha == 3:
        salario = float(input())
        meses_trabalhados = int(input())
        decimo = salario * meses_trabalhados
        print(decimo)
    else:
        break

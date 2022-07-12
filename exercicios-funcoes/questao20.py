def analisar_dados():
    salario = []
    qtd_pessoas = 0
    soma_salario = 0
    soma_filhos = 0
    maior_salario = 0
    inferior_380 = 0

    while True:
        print('Menu: \n1. Inserir novos dados\n2. Exibir pequisa\n0. Sair\n')

        escolha = int(input('Insira a opção: '))

        if escolha == 1:
            salario.append(float(input('Informe o salario: ')))
            soma_filhos += int(input('Informe o nº de filhos: '))
            qtd_pessoas += 1

        for y in range(len(salario)):
            soma_salario += salario[y]
                
        if qtd_pessoas > 0:
            for i in range(len(salario)):
                if salario [i] < 380:
                    inferior_380 += 1
                if i == 0:
                    maior_salario = salario[i]
                elif maior_salario < salario[i]:
                    maior_salario = salario[i]

        if escolha == 2:
            if qtd_pessoas > 0:
                print(f'Média salarial: {soma_salario / qtd_pessoas}')
                print(f'Média do nº de filhos: {soma_filhos / qtd_pessoas}')
                print(f'Maior salario: {maior_salario}')
                print(f'Percentual de pessoas que recebem menos que R$ 380,00: {inferior_380 / qtd_pessoas}')
            else:
                print('Não há dados disponiveis')

analisar_dados()
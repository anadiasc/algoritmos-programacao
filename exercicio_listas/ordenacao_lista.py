lista = []
maior = 0

while True:
    print('menu opções:\n1. inserir elemento na lista\n2. deletar um elemento da lista\n3. exibir lista\n4. verificar qual é o maior\n5. ordenar de forma crescente\n')

    escolha = int(input('Escolha uma ação: '))

    if escolha == 1:
        lista.append(int(input('Insira o elemento: ')))
    elif escolha == 2:
        deletar = int(input('insira o elemento qur irá deletar: '))
        for i in range(len(lista)):
            if deletar == lista[i]:
                del(lista[i])
    elif escolha == 3:
        print(f'Lista: {lista}')
    elif escolha == 4:
        for i in range(len(lista)):
            if i == 0:
                maior = lista[i]
            elif maior < lista[i]:
                maior = lista[i]
        print(maior)
    elif escolha == 5:
        for k in range(len(lista)):
            for l in range(len(lista)-1):
                if lista[l] < lista[l + 1]:
                    aux = lista[l]
                    lista[l] = lista[l + 1]
                    lista[l + 1] = aux
